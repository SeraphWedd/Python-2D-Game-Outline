'''
ImageHandler Module

Contains the class for handling all Image related matters of the game.
'''
import os
import pygame as pg

class ImageHander():
    def __init__(self):
        #Holds image and image properties for current scene
        self.current_images = {}
        self.current_parameters = {}
        #Holds the image and image properties for next scene
        self.to_load = {}
        self.to_load_parameters = {}

    def get_image_to_load(self, list_items):
        #For images, we need name, path, rotation, scale, crop rect
        for name, path, rot, scale, crect in list_items:
            #Load image and apply rotation
            try:
                self.to_load[name] =  pg.transform.rotate(pg.image.load(path), rot)
            except:
                #If image is not found, create a 32px rect as placeholder
                self.to_load[name] =  pg.surface.Surface((0, 0, 32, 32)).convert_alpha()
                self.to_load[name].fill((200, 20, 20))
                crect = None
                
            if crect is not None:
                #Crop image based on crop rect crect
                self.to_load[name] = pg.transform.crop(self.to_load[name], crect)
            
            w, h = self.to_load[image].get_size()
            #Resize image based on scale
            self.to_load[name] = pg.transform.scale(self.to_load[name], w*scale, h*scale)
            #Converts alpha channels
            self.to_load[name] = self.to_load[name].convert_alpha()
            #Save current properties of the image
            self.to_load_parameters[name] = {'rotation':rot, 'scale':scale, 'width':w, 'height':h}
        
    def switch_loaded_images(self):
        #Set to_load into current_images
        self.current_images = self.to_load.copy()
        self.current_parameters = self.to_load_parameters.copy()
        #Reset to_load
        self.to_load = {}
        self.to_load_parameters = {}

    def get_rotated_image(self, name, new_rot, persistent=False):
        #get change in rotation and return image rotated delta degrees
        delta = new_rot - self.current_parameters[name]['rotation']
        new_image = pg.transform.rotate(self.current_images[name], delta)
        #If persistent, we will update current
        if persistent:
            self.current_images[name] = new_image
            self.current_parameters[name]['rotation'] = new_rot
        return new_image

    def get_rescaled_image(self, name, new_scale, persistent=False):
        #Get properties
        try:
            delta = new_scale / self.current_parameters[name]['scale']
        #Filter out possible ZeroDivisionError
        except ZeroDivisionError:
            return self.current_images[name]

        w = self.current_parameters[name]['width']
        h = self.current_parameters[name]['height']
        new_image = pg.transform.scale(self.current_images[name], w*delta, h*delta)
        #If persistent, we will update current
        if persistent:
            self.current_images[name] = new_image
            self.current_parameters[name]['scale'] = new_scale
            w, h = new_image.get_size()
            self.current_parameters[name]['width'] = w
            self.current_parameters[name]['height'] = h
        return new_image
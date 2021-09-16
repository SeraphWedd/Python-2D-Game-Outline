'''
GameEngine Module

Contains the class for handling the main game engine.
Backbone of the game.

Control succession of screens, keypresses, and pygame events.
'''

import pygame as pg

class Engine():
    def __init__(self, width, height, flags, AH, IH, PE, SM):
        #Inherent properties
        self.width = width
        self.height = height
        self.flags = flags
        self.window = pg.display.set_mode((self.width, self.height), self.flags)
        self.clock = pg.time.Clock()
        #Links to other Modules
        self.audio = AH
        self.image = IH
        self.physics = PE
        self.state_machine = SM
        #Options
        self.options = {}
        self.get_options()
        #Object holder for the current scene
        self.scene_objects = {}

    def get_options(self):
        with open('./options.ini', 'r') as f:
            all_lines = f.readlines()

        for line in all_lines:
            key, value = line.split('=')
            key = key.strip(' ')
            value = value.strip(' ')
            self.options[key] = int(value)

    def game_loop(self):
        self.pressed_keys = {}
        self.game_is_running = True

        while self.game_is_running:
            #Check for system events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_is_running = False
                    break
                #Check for keypress
                elif event.type == pg.KEYDOWN:
                    self.pressed_keys[event.key] = 1
                #Check for key release
                elif event.type == pg.KEYUP:
                    self.pressed_keys[event.key] = 0
            dt = self.clock(self.options['fps'])
            #Update then draw items to window
            self.window.fill((120, 120, 120))
            for key in self.scene_objects.keys():
                self.scene_objects[key].update(dt)
                self.scene_objects[key].draw(self.window)
            pg.display.flip()

        #If game is not running, quit
        pg.quit()
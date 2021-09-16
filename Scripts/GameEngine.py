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
        self.all_events = [pg.QUIT, pg.KEYDOWN, pg.KEYUP, pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP, pg.MOUSEMOTION]
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
            for event in pg.event.get(self.all_events):
                if event.type == pg.QUIT:
                    self.game_is_running = False
                    break
                #Check for keypress
                elif event.type == pg.KEYDOWN:
                    self.pressed_keys[event.key] = 1
                #Check for key release
                elif event.type == pg.KEYUP:
                    self.pressed_keys[event.key] = 0
                #Ckeck for mouse click
                elif (event.type == pg.MOUSEBUTTONDOWN) or (
                    event.type == pg.MOUSEBUTTONUP):
                    self.pressed_keys['mouse_buttons'] = pg.mouse.get_pressed()
                #Check for mouse motion
                elif event.type == pg.MOUSEMOTION:
                    self.pressed_keys['mouse_pos'] = pg.mouse.get_pos()

            dt = self.clock.tick_busy_loop(self.options['max_fps'])
            #Update then draw items to window
            self.window.fill((120, 120, 120))
            for key in self.scene_objects.keys():
                self.scene_objects[key].update(dt)
                self.scene_objects[key].draw(self.window)
            pg.display.flip()

        #If game is not running, quit
        pg.quit()
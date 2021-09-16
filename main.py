'''
Main Module

Handles the main game loop and Setup.
'''

import os
import sys
import pygame as pg
from Scripts.GameEngine import Engine
from Scripts.PhysicsEngine import PhysicsEngine
from Scripts.StateMachine import StateMachine
from Scripts.AudioHandler import AudioHander
from Scripts.ImageHandler import ImageHander
from Scripts.GameObjects import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

pg.init()
pg.mixer.init(44100, -16, 8, 256)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_FLAGS = pg.HWSURFACE|pg.DOUBLEBUF

AH = AudioHander()
IH = ImageHander()
PE = PhysicsEngine()
SM = StateMachine()
GE = Engine(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_FLAGS, AH, IH, PE, SM)
GE.game_loop()

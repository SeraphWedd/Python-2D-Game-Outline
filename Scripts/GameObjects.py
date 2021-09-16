'''
GameObjects Module

Contains all classes pertaining to game objects.
Contains:
- StaticObject
- AnimatedObject
- PlayerObject
- InvisibleObject
'''
import pygame as pg

class GameObject(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

    def draw(self, screen):
        pass

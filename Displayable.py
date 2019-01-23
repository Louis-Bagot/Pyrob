import numpy as np;
import pygame;

class Displayable():
    """Any object that can be displayed onscreen.
    Has a position and a sprite."""
    def __init__(self,pos,spriteName, halfsize):
        self.pos = np.array(pos);
        self.sprite = pygame.image.load(spriteName);
        self.halfsize = halfsize;

    def display(self,screen):
        screen.blit(self.sprite, tuple(self.pos - self.halfsize));

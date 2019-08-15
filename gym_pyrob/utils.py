import numpy as np;
import pygame;

class Displayable():
    """ Any object that can be displayed onscreen.
    Has a position and a sprite."""
    def __init__(self, pos, sprite_name, halfsize):
        self.pos = np.array(pos);
        self.sprite = pygame.image.load(sprite_name);
        self.halfsize = halfsize;

    def display(self,screen):
        screen.blit(self.sprite, tuple(self.pos - self.halfsize));


def hitboxes_touch(position1, position2, radius1, radius2):
    """ Returns whether the two ROUND hitboxes touch.
        """
    return (np.linalg.norm(position1 - position2) < radius1 + radius2)

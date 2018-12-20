import numpy as np;

class Displayable():
    """Any object that can be displayed onscreen.
    Has a position and a sprite."""
    def __init__(self,pos, sprite):
        self.pos = pos;
        self.sprite = sprite;

    def display(self):
        pass

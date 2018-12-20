import numpy as np;

class Displayable():
    """Any object that can be displayed onscreen.
    Has a position and a sprite."""
    def __init__(self,pos, spriteName):
        self.pos = pos;
        self.sprite = spriteFromName(spriteName);

    def display(self):
        pass

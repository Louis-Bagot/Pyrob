import numpy as np;
from Displayable import Displayable

class Foe(Displayable):
    """Foe is the bullet that goes straight and may touch Starob or its Shield
    Angle and a speed give the 2D speed vector."""
    def __init__(self, pos,angle,spriteName='sprites/foe.png', speed=10, damage=1):
        self.radius = 128/8;
        super().__init__(pos, spriteName, self.radius)
        self.speedVec = speed*np.array([np.cos(angle), np.sin(angle)]);
        self.damage = damage;

    def nextFrame(self):
        """Computes the next frame, ie computes next position of Foe"""
        self.pos += self.speedVec;

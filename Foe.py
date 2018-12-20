import numpy as np;

class Foe(Displayable):
    """Foe is the bullet that goes straight and may touch Starob or its Shield
    Angle and a speed give the 2D speed vector."""
    def __init__(self, pos, spriteName='res/foe.png', angle, speed=10, damage=1):
        super().__init__(pos)
        self.speedVec = speed*np.array([np.cos(angle), np.sin(angle)]);
        self.radius = radius;
        self.damage = damage;

    def nextFrame():
        """Computes the next frame, ie computes next position of Foe"""
        self.pos += self.speedVec;

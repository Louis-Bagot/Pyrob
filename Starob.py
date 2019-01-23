import numpy as np;
from Foe import Foe;
from Displayable import Displayable;

class Starob(Displayable):
    """Starob is the spaceship. It can move around, has a shield, a radius
    (which defines its hitbox), a life that dwindles when the hitbox is touched.
    Angle and a speed give the 2D speed vector."""
    def __init__(self, pos, spriteName='sprites/starob.png'):
        # init values for Starob
        self.radius = 128/2;
        super().__init__(pos, spriteName, self.radius);
        self.life = 10;
        self.angle = 0;
        self.speed = 0;
        self.brain = 0;
#        self.brain = QZSDMoves();

    def touched(self,foe):
        """Returns whether the Foe is within distance of harming Starob"""
        assert isinstance(foe, Foe), "input of function touched isn't a Foe!"
        return (np.linalg.norm(foe.pos-self.pos) < foe.radius + self.radius);

    def decreaseLifeBy(self,damage):
        """takes out the damage from the life of Starob"""
        assert (damage>0), "Damage isn't positive !"
        self.life -= damage;

    def dead(self):
        """Returns whether Starob's life has run out"""
        return self.life <= 0;

    def nextFrame(self,game):
        """Computes the next frame, ie calculates next position of Starob"""
        self.angle = 0; #self.brain.chooseAngle(game)
        self.pos += self.speed*np.array([np.cos(self.angle), np.sin(self.angle)]);

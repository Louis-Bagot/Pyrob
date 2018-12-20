import numpy as np;
from foe import Foe;

class Starob(Displayable):
    """Starob is the spaceship. It can move around, has a shield, a radius
    (which defines its hitbox), a life that dwindles when the hitbox is touched.
    Angle and a speed give the 2D speed vector."""
    def __init__(self, pos, spriteName='res/starob.png'):
        # init values for Starob
        super().__init__(pos, sprite);
        self.life = 10;
        self.radius = 10;
        self.angle = 0;
        self.speed = 5;

    def touched(foe):
        """Returns whether the Foe is within distance of harming Starob"""
        assert isinstance(foe, Foe), "input of function touched isn't a Foe!"
        return (np.linalg.norm(foe.pos-self.pos) < foe.radius + self.radius);

    def decreaseLifeBy(damage):
        """takes out the damage from the life of Starob"""
        assert (damage<0), "Damage isn't negative !"
        self.life -= damage;

    def dead():
        """Returns whether Starob's life has run out"""
        return self.life <= 0;

    def nextFrame(game):
        """Computes the next frame, ie calculates next position of Starob"""
        self.angle = StarobBrain.chooseAngle(game)
        self.pos += speed*np.array([np.cos(angle), np.sin(angle)]);

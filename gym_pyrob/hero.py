import numpy as np;
from .utils import Displayable;
from .enemy import Bullet;

class Shield(Displayable):
    """ Starob's shield; destroys any bullet it touches.
    Can turn around Starob clockwise or counter clockwise at a constant speed
    TODO """
    def __init__(self, starob):
        self.starob = starob
        self.radius = self.starob.radius
        self.ang_pos = np.pi
        self.pos = self._compute_pos()
        sprite_name = './gym_pyrob/sprites/shield.png'
        super(Shield, self).__init__(self.pos,sprite_name, self.radius)
        self.speed = np.pi/8    # the amount the shield moves per action
        self.momentum = 0.5     # much lower than Starob: need more reactivity

    def _compute_pos(self):
        """ Computes the shield position from the angular position """
        return self.starob.pos + np.array([np.cos(self.ang_pos),
                                           np.sin(self.ang_pos)])

    def next_frame(self, action:int):
        """ Computes the next position of the shield given the move in (0,1,2)
        Resulting in pushes respectively of (-1 0 1) """
        action -= 1
        assert action in (-1,0,+1)
        speed_ang = self.speed*action
        self.ang_pos = self.momentum*self.ang_pos + (1-self.momentum)*speed_ang
        self.ang_pos %= 2*np.pi # prevent overflow
        self.pos = self._compute_pos()


class Starob(Displayable):
    """ Starob is the spaceship. It can move around, has a shield, a radius
    (which defines its hitbox), a life that dwindles when the hitbox is touched.
    Angle and a speed give the 2D speed vector."""
    def __init__(self, pos, radius, n_directions):
        # init values for Starob
        self.radius = radius
        self.pos = pos
        sprite_name = './gym_pyrob/sprites/starob.png'
        super().__init__(self.pos,sprite_name, self.radius);
        self.life = 10;
        self.speed = 3
        self.angle = 0;
        self.momentum = 0.9
        assert n_directions in (4,8), "n_directions = {} not in (4,8)".format(n_directions)
        self.n_directions = n_directions # 8 means possibility of diagonals
        self.shield = Shield(self)

    def touched(self,foe):
        """ Returns whether the Foe is within distance of harming Starob"""
        assert isinstance(foe, Foe), "input of function touched isn't a Foe!"
        return (np.linalg.norm(foe.pos-self.pos) < foe.radius + self.radius);

    def take_damage(self, damage:int):
        """ Takes out the damage from the life of Starob.
        The damage should be a positive integer (since life is an int too)"""
        assert (damage>0), "Damage isn't positive !"
        self.life -= damage;

    def is_dead(self):
        """ Returns whether Starob's life has run out"""
        return self.life <= 0;

    def next_frame(self, action):
        """ Computes the next frame, ie calculates next position of Starob
        based on the action = (SEWN, shield rotation)"""
        # S corresponds to angle 0; E: pi/2, N:pi, w:3pi/2
        move, shield_action = action
        self.angle = move*np.pi*2/self.n_directions; # pi/2 if 4moves, pi/4 if 8
        speed_v = self.speed*np.array([np.cos(self.angle), np.sin(self.angle)])
        self.pos = self.momentum*self.pos + (1-self.momentum)*speed_v
        self.shield.next_frame(shield_action)

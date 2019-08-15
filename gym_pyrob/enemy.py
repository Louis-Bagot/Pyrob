import numpy as np;
from .utils import Displayable
from .generating_functions import *;

class Bullet(Displayable):
    """ Bullet is the ball that goes straight and may touch Starob or its Shield
    Angle and a speed give the 2D speed vector."""
    def __init__(self, pos, angle, radius):
        self.radius = radius;
        self.pos = pos
        super().__init__(pos, './gym_pyrob/sprites/bullet.png', self.radius)
        self.speed = 10
        self.damage = 1
        self.speed_vec = self.speed*np.array([np.cos(angle), np.sin(angle)])

    def next_frame(self):
        """Computes the next frame, ie computes next position of Bullet"""
        print("speed: {}, pos: {}".format(self.speed_vec, self.pos))
        self.pos += self.speed_vec
"""
class Bullet_Swarm(object):
    Swarm of Bullets. Manages their appearances, positions, angles.
    def __init__(self, game, fGen):
        self.bullet_array = [];
        self.fGen = fGen; # method f gives the probability to spawn a Bullet at t
        self.new_bullet(game);

    def new_bullet(self, game):
        Creates a new Bullet where the angle is chosen by the Brain
        r = np.random.rand(1); # controls the fixed side bullet pops on
        fixed =

        if (r<.5): # pops up or down
            if (r<.25): # pops up
                bulletPos =

        self.bullet_array.append(Bullet(bulletPos,
            angle = self.brain.chooseAngle(bulletPos, game)));

    def generateBullet(self, frame, game):
        Spawns a Bullet under probability fGen(frame), every 4th frame
        if (frame%20 == 0) and (np.random.rand(1) < self.fGen.f(frame)):
            self.new_bullet(game);

    def nextFrame(self, frame, game):
        May generate a Bullet; also computes next frames for every bullet
        self.generateBullet(frame, game);
        for bullet in self.bullet_array:
            bullet.nextFrame();
            if any(coord<0 for coord in bullet.pos) or \
               any(coord>game.dim for coord in bullet.pos):
                self.delete(bullet);

    def delete(self, bullet):
        self.bullet_array.remove(bullet);
"""

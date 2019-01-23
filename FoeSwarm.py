import numpy as np;
from Foe import Foe;
from generatingFunctions import *;

class FoeSwarm(object):
    """Swarm of Foes. Manages their appearance, positions, angles."""
    def __init__(self, game, fGen, foeBrain):
        self.foeArray = [];
        self.fGen = fGen; # method f gives the probability to spawn a Foe at t
        self.brain = foeBrain;
        self.newFoe(game);

    def newFoe(self, game):
        """Creates a new Foe where the angle is chosen by the Brain"""
        r = np.random.rand(1); # controls the fixed side foe pops on
        fixed =

        if (r<.5): # pops up or down
            if (r<.25): # pops up
                foePos =

        self.foeArray.append(Foe(foePos,
            angle = self.brain.chooseAngle(foePos, game)));

    def generateFoe(self, frame, game):
        """Spawns a Foe under probability fGen(frame), every 4th frame"""
        if (frame%20 == 0) and (np.random.rand(1) < self.fGen.f(frame)):
            self.newFoe(game);

    def nextFrame(self, frame, game):
        """May generate a Foe; also computes next frames for every foe"""
        self.generateFoe(frame, game);
        for foe in self.foeArray:
            foe.nextFrame();
            if any(coord<0 for coord in foe.pos) or any(coord>game.dim for coord in foe.pos):
                self.delete(foe);

    def delete(self, foe):
        self.foeArray.remove(foe);

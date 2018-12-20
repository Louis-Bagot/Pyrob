import numpy as np;
from foe import Foe;
from generatingFunctions import *;

class FoeSwarm(object):
    """Swarm of Foes. Manages their appearance, positions, angles."""
    def __init__(self, starob, fGen, foeBrain):
        self.foeArray = [];
        self.fGen = fGen; # method f gives the probability to spawn a Foe at t
        self.brain = foeBrain;
        newFoe(starob);

    def generateFoe(frame, starob):
        """Spawns a Foe under probability fGen(frame), every 4th frame"""
        if (frame%4 == 0)&&(np.random.rand(1) < self.fGen.f(frame)):
            newFoe(starob)

    def nextFrame(frame, starob):
        """May generate a Foe; also computes next frames for every foe"""
        generateFoe(frame);
        for foe in self.foeArray:
            foe.nextFrame();

    def newFoe(game):
        """Creates a new Foe where the angle is chosen by the Brain"""
        if (np.random.rand(1)<.5):
            foePos = TODO;
        else foePos = TODO;
        self.foeArray.append(Foe(foePos,
            angle = self.foeBrain.chooseAngle(foePos, game)));

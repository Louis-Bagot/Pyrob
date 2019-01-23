import pygame;
import numpy as np;
from Starob import Starob;
from FoeSwarm import FoeSwarm;
from generatingFunctions import FlatSigmoid;
from NaiveFoeBrain import NaiveFoeBrain;

class Game():
    """Class that manages the frames and loops"""
    def __init__(self, dim=1024, nbStar=1, displayed=True, maxframes=1000):
        self.dim = dim;
        self.displayed = displayed;
        self.maxframes = maxframes;
        starRadius = dim/8/2;
        foeRadius = dim/8/8;
        # Create starobs and their foes
        initPos = np.array([dim/2, dim/2]);
        self.starray = [Starob(initPos) for i in range(nbStar)];
        # create FoeSwarm aiming at a random Starob
        self.foeSwarm = FoeSwarm(self,FlatSigmoid(self.maxframes),
            NaiveFoeBrain());
        # pygame init if needed
        if self.displayed:
            self.background = pygame.image.load('sprites/background.jpg')
            pygame.init();
            self.screen = pygame.display.set_mode((dim,dim));

    def gameLoop(self, frame):
        alive=[];
        self.foeSwarm.nextFrame(frame, self);
        for starob in self.starray:
            starob.nextFrame(self);
            if starob.dead():
                self.starray.remove(starob);
                alive.append(False);
            else : alive.append(True);
            for foe in self.foeSwarm.foeArray:
                if starob.touched(foe):
                    starob.decreaseLifeBy(foe.damage);
                    self.foeSwarm.delete(foe);

        if self.displayed:
            self.screen.fill((0, 0, 0));
            self.screen.blit(self.background, (0,0));
            for starob in self.starray:
                starob.display(self.screen);
                # TODO starob.shield.display(self.screen)
            for foe in self.foeSwarm.foeArray:
                foe.display(self.screen);
            pygame.display.flip();

        return not any(alive);

    def launchGame(self):
        exit = False;
        over = False;
        for frame in range(self.maxframes):
            over = self.gameLoop(frame);
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit=True;
            if exit:
                print("exited via window cross")
                break
            if over:
                print("game ended at frame ", frame, "/", self.maxframes)
                break

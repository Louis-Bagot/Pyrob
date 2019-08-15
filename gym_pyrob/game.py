import pygame;
import numpy as np;
from hero import Starob;
from enemy import FoeSwarm;
from generating_functions import FlatSigmoid;

class Game():
    """Class that manages the frames and loops"""
    def __init__(self, dim=1024, displayed=True, maxframes=1000):
        self.dim = dim;
        self.displayed = displayed;
        self.maxframes = maxframes;
        star_radius = dim/8/2;
        foe_radius = dim/8/8;
        # Create starobs and their foes
        initPos = np.ones(2)*dim/2;
        self.starob = Starob(initPos)
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

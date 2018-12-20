class Game():
    """Class that manages the frames and loops"""
    def __init__(self, dimx, dimy, nbStar):
        self.dimx = dimx;
        self.dimy = dimy;
        # Create starobs and their foes
        initPos = np.array([dimx/2, dimy/2]);
        self.starray = [Starob(initPos) for i in range(nbStar)];
        # create FoeSwarm aiming at a random Starob
        self.foeSwarm = FoeSwarm(np.random.choice(self.starray));

    def gameLoop():
        pass

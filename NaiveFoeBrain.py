import numpy as np;

class NaiveFoeBrain():
    """Fires straight at the ship"""
    def __init__(self):
        pass

    def chooseAngle(self,foePos, game):
        """we want to shoot down starob, choosing an angle for the last foe"""
        # random target's position
        vec = np.random.choice(game.starray).pos - foePos;
        return np.angle(vec[0]+1j*vec[1])

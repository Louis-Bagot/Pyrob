class NaiveFoeBrain():
    """Fires straight at the ship"""
    def __init__(self):
        pass

    def chooseAngle(foePos, game):
        """we want to shoot down starob, choosing an angle for the last foe"""
        # random target's position
        vec = np.random.choice(self.starray).pos - foePos;
        return np.angle(vec[1]+1j*vec[2])

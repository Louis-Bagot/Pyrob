import gym
from gym import spaces
import numpy as np
import pygame
from .hero import Starob
from .enemy import Bullet;
from .utils import Displayable, hitboxes_touch
from .generating_functions import FlatSigmoid

class PyrobEnv(gym.Env):
    """ Environment for the Starob game in Python as a Gym environment.
    The hero player controls a spaceship that can move in 2D; also has a shield
    around him: its goal is to dodge or block the bullets for as long as possible
    The enemy player controls 4 cannons on the 4 corners of the map.
    The bullet popping is random (but accelerating), the player can select a
    cannon and an angle at which to send the bullet.
    Action is a (hero, enemy) tuple where the controls are:
        hero: (move, shield rotation) where the move is in (0:3) = (S,E,N,W)
            the move can also be in (0:7)  (with diagonals) : (S,SE,E,NE,...)
            the shield rotation is -1,0 or +1 where 1 is a counter clockwise push
        enemy: (cannon, angle) tuple where the cannon is in (0,1,2,3), counter
            clockwise starting from upper left, and the angle is normalized
            in [0,1] counter clockwise.
    The state is 2 frames of 3 arrays of size 32x32 with booleans for the
        positions of the hero, shield and bullets.
        Or, an array of [posx, posy, speedx, speedy] for all actors.
        Probem: what to do with 'unborn' bullets ?
    Rewards: the hero is rewarded +1 for a survived frame, 0 overwise,
        substract total damage taken in the frame.
        The enemy is rewarded with the total damage taken in the frame
        """

    def __init__(self):
        self.dim = 1024
        self.starob_radius = self.dim/8/2    # Starob spreads 1/8th of the screen
        self.bullet_radius = self.starob_radius/4 # Bullets are 1/4th of Starob
        self.max_bullets = 10
        self.n_directions = 4 # number of directions allowed for Starob
        self._starob = Starob(np.ones(2, dtype=np.float32)*self.dim/2,
                              self.starob_radius, self.n_directions)
        self._bullet_swarm = []
        self.gen_function = FlatSigmoid(1000)
        self._max_bullet_freq = 1/5 # one every 5 frames
        self.t = 0
        # Hero action space: 8 (E,NE, N,...) for directions,
        # -1,0,+1 for shield rotation
        self.action_space_hero = spaces.Tuple((spaces.Discrete(8),
                                               spaces.Discrete(3)))
        # Enemy action space: 4 cannons at borders; angle in [0,1]
        self.action_space_enemy = spaces.Tuple((spaces.Discrete(4), # 4 cannons
                                                spaces.Box(low=np.array([0]),
                                                           high=np.array([1]),
                                                           dtype=np.float32)))
        self.action_space = spaces.Tuple((self.action_space_hero,
                                         self.action_space_enemy))
        n_scalars = 4*(self.max_bullets + 1) + 2    # number of pos and speeds
        self.observation_space = spaces.Box(low=np.ones(n_scalars)*-10,
                                            high=np.ones(n_scalars)*10)

    def reset(self):
        """ Resets the environemnt according to the Gym.Env definition """
        self._starob = Starob(np.ones(2, dtype=np.float32)*self.dim/2,
                              self.starob_radius, self.n_directions)
        self._bullet_swarm = []
        self.t = 0


    def step(self, actions):
        """ Single game step generated usig the actions from the hero and enemy.
        Starob moves in the required direction, as well as its shield;
        If a new Bullet should be created, it follows action_enemy directives.
        """
        self.t += 1
        action_hero, action_enemy = actions
        # update starob
        self._starob.next_frame(action_hero)
        # update bullets
        for bullet in self._bullet_swarm:
            bullet.next_frame()
        # generate bullets
        if np.random.randn() < self._proba_generate_bullet():
            pos, angle = self._action_enemy2pos_angle(action_enemy)
            self._bullet_swarm.append(Bullet(pos, angle, self.bullet_radius))
        # update collisions
        del_bullets = []
        n_shielded = 0
        total_damage = 0
        for i, bullet in enumerate(self._bullet_swarm):
            if hitboxes_touch(self._starob.shield.pos,    bullet.pos,
                              self._starob.shield.radius, bullet.radius):
                del_bullets.append(i)
                n_shielded += 1
            elif hitboxes_touch(self._starob.pos,    bullet.pos,
                                self._starob.radius, bullet.radius):
                self._starob.take_damage(bullet.damage)
                del_bullets.append(i)
                total_damage += bullet.damage
        # output
        obs = self._state_to_vector()
        done = self._starob.is_dead()    # the done flag doesn't use time
        rewards = [1-int(done)-total_damage, total_damage]
        return obs, rewards, done, ""

    def _proba_generate_bullet(self):
        """ Outputs the probability to generate a new bullet.
        Uses the frame number, generating_function, and number of bullets
        """
        if len(self._bullet_swarm) >= self.max_bullets:
            return 0
        else:
            return self._max_bullet_freq * self.gen_function(self.t)

    def _action_enemy2pos_angle(self, action):
        """ Converts the action into an intelligible position and action
        as input to the Bullet's constructor.
        # Arguments:
            action : a (cannon number, normalized angle) tuple where the cannon
                number ranges from 0 to 3, corresponding to counter clockwise
                corners starting from upper left. The normalized angle covers
                the counter clockwise possible angles from 0 to 1
                e.g. for cannon 0 (upper left): angle 0 is down, 1 is right"""
        cannon_n, normd_angle = action
        assert cannon_n in range(4), "Invalid cannon entry: {}".format(cannon_n)
        assert 0 <= normd_angle <= 1, "Invalid angle entry: {}".format(normd_angle)
        # position
        cannon_positions = {0:[0,0], 1:[1,0], 2:[1,1], 3:[0,1]}
        position = np.array(cannon_positions[cannon_n], dtype=np.float32)
        position *= (self.dim - 2*self.bullet_radius) # 2* to cancel once next step:
        position += self.bullet_radius  # spawn fully in the field
        # angle
        angle = (cannon_n + normd_angle)*np.pi/2
        print(angle, position)
        return position, angle

    def _state_to_vector(self):
        """ Returns the state according to the class doc """
        return None
        raise NotImplementedError("Oy")

    def render(self):
        """ Displays the environment using pygame
            """
        return NotImplementedError("Render not written yet")

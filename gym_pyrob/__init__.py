""" Game Starob adapted for Python.

The game is formulated as a gym environment and cna be used as such.
"""

from gym.envs.registration import register

register(
    id='Pyrob-v0',
    entry_point='gym_pyrob.core:PyrobEnv'
)

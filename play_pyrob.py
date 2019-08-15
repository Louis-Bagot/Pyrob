import gym
import gym_pyrob

env = gym.make('Pyrob-v0')

n_episodes = 1
n_steps = 1000

for ep in range(n_episodes):
    obs = env.reset()
    for step in range(n_steps):
        env.render()
        action_hero  = env.action_space_hero.sample() # agent_hero .act(obs)
        action_enemy = env.action_space_enemy.sample() # agent_enemy.act(obs)
        obs, rewards, done, info = env.step([action_hero, action_enemy])
        reward_hero, reward_enemy = rewards
        if done:
            print("Episode finished after {} timesteps"
                  .format(step+1))
            env.render()
            break
env.close()

import gym
import gym_raas
import numpy as np
import time

freq = 2.0
start_time = time.time()


env = gym.make('raaspendulum-v0')
env.reset()
obs = []


N_steps = 400

try:
    for i in range(N_steps):

        dt = time.time() - start_time

        torque = np.sin(2*np.pi*f*dt)

        observation, reward, done, info = env.step([2])
        time.sleep(0.01)
        obs.append(observation)

except:
    print('Stopped!')



env.reset()

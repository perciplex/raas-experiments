import gym
import gym_raas
import numpy as np
import time

freq = 0.7
phase_0 = np.pi/2
start_time = time.time()


env = gym.make('raaspendulum-v0')
env.reset()
obs = []


N_steps = 400

try:
    for i in range(N_steps):

        dt = time.time() - start_time

        torque = 5*np.sin(2*np.pi*freq*dt + phase_0)
        torque = np.clip(torque, -2, 2)
        observation, reward, done, info = env.step([torque])
        time.sleep(0.01)
        obs.append(observation)

except:
    print('Stopped!')



env.reset()

import gym
import gym_raas
import numpy as np
import time
import traceback as tb



env = gym.make('raaspendulum-v0')
env.reset()
obs = []

pause_time = 2.0
reset_time = 2.0

torques = np.linspace(-2, 2, 24).tolist() + np.linspace(2, -2, 24).tolist()

xs = []
ys = []

try:

    for t in np.linspace(0, -2, 10):

        start_time = time.time()
        while True:
            time.sleep(0.15)
            x, y, thetadot = env._get_obs()

            if (time.time() - start_time) >= 0.5:
                break

        print(f'\nApplying torque = {t:.2f}')
        _, _, _, _ = env.step([t])


    for t in torques:

        t = np.clip(t, -2, 2)

        print(f'\nApplying torque = {t:.2f}')
        _, _, _, _ = env.step([t])

        start_time = time.time()
        while True:
            time.sleep(0.15)
            x, y, thetadot = env._get_obs()

            if (time.time() - start_time) >= pause_time:
                break

        xs.append(x)
        ys.append(y)

        print('\nFinal:\n\n x = {:.3f},\t y = {:.3f},\t thetadot = {:.3f}'.format(x, y, thetadot))



except:
    print('\n\nStopped!\n')
    print(tb.format_exc())
    print('\n\n')

print('\n\n')
print('torques = ', torques)
print('xs = ', xs)
print('ys = ', ys)





env.reset()

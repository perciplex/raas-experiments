import numpy as np
import matplotlib.pyplot as plt


torques =  [-2.0, -1.8260869565217392, -1.6521739130434783, -1.4782608695652173, -1.3043478260869565, -1.1304347826086958, -0.9565217391304348, -0.7826086956521738, -0.6086956521739131, -0.43478260869565233, -0.26086956521739135, -0.08695652173913038, 0.08695652173913038, 0.26086956521739113, 0.43478260869565233, 0.6086956521739131, 0.7826086956521738, 0.9565217391304346, 1.1304347826086953, 1.3043478260869565, 1.4782608695652173, 1.652173913043478, 1.8260869565217392, 2.0]
xs =  [0.6190939493098341, 0.9692309097067544, 0.9692309097067544, 0.9692309097067544, 0.9692309097067544, 0.9692309097067544, 0.9996573249755573, 0.9996573249755573, 0.9996573249755573, 0.9996573249755573, 0.9996573249755573, 0.9996573249755573, 0.9996573249755573, 0.9996573249755573, 0.9996573249755573, 0.9996573249755573, 0.9996573249755573, 0.9996573249755573, 0.9510565162951535, 0.9510565162951535, 0.9510565162951535, 0.9510565162951535, 0.9510565162951535, 0.8241261886220156]
ys =  [-0.7853169308807448, -0.24615329302899303, -0.24615329302899303, -0.24615329302899303, -0.24615329302899303, -0.24615329302899303, 0.02617694830787315, 0.02617694830787315, 0.02617694830787315, 0.02617694830787315, 0.02617694830787315, 0.02617694830787315, 0.02617694830787315, 0.02617694830787315, 0.02617694830787315, 0.02617694830787315, 0.02617694830787315, 0.02617694830787315, 0.3090169943749474, 0.3090169943749474, 0.3090169943749474, 0.3090169943749474, 0.3090169943749474, 0.5664062369248328]

xs = np.array(xs)
ys = np.array(ys)

torques = np.array(torques)
angs = np.arctan2(ys, xs)

pair = list(zip(torques, angs))

sorted_pairs = list(zip(*sorted(pair, key=lambda x: x[0])))

print(sorted_pairs)
#exit()

plt.plot(*sorted_pairs, 'o-', color='dodgerblue')

plt.xlabel('Applied torque')
plt.ylabel('Angle')

plt.savefig('torque_ang_curve.png')

plt.show()





















#
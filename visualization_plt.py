import matplotlib.pyplot as plt
import numpy as np

name = 'star/star_rotation'
voxels = np.load('./data/' + name + '_voxel_entire_carved.npy')
voxels_interior = np.load('./data/' + name + '_voxel_interior_carved.npy')

resolution = 64


fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
ax1.voxels(voxels, edgecolor='k')
ax2.voxels(voxels_interior, edgecolor='k')
plt.show()

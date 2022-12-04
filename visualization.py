import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d


# import carving

def barycenter(voxels_np):
    """
    Input: A numpy array (full) with the information whether the voxel is contained
    Output: The grid coordinates of the center of mass
    """
    grid_shape = voxels_np.shape
    counter = 0
    center = np.array([0., 0., 0.])
    for id_x in range(grid_shape[0]):
        for id_y in range(grid_shape[1]):
            for id_z in range(grid_shape[2]):
                # check whether we hit a a voxel in the mesh
                if (voxels_np[id_x, id_y, id_z] == 1):
                    counter += 1
                    center = (1 / float(counter)) * np.array([float(id_x), float(id_y), float(id_z)]) + (
                            float(counter - 1) / float(counter)) * center

    return ([int(center[0]), int(center[1]), int(center[2])])


name = 'star/star_rotation'
# name = 'bunny_final'
# name = "bunny_flipped_3"

voxels = o3d.io.read_voxel_grid("./data/" + name + "_voxelized.ply")
o3d.visualization.draw_geometries([voxels], point_show_normal=True, mesh_show_wireframe=True)

import open3d as o3d
import numpy as np
import os

name = "star/star"

mesh_path = "./data/" + name + ".obj"
mesh = o3d.io.read_triangle_mesh(mesh_path)
output_mesh_filename = os.path.abspath("./data/" + name + "_rotation.obj")
camera_path = os.path.abspath("./data/sphere.ply")

R = mesh.get_rotation_matrix_from_xyz((np.pi / 3, 0, 0))
o3d.visualization.draw_geometries([mesh])
mesh.rotate(R, center=(0, 0, 0))

print('saving rotation file')
o3d.visualization.draw_geometries([mesh])
o3d.io.write_triangle_mesh(output_mesh_filename, mesh)
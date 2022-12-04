import numpy as np

np.set_printoptions(threshold=np.inf)


def get_barycenter(voxels_np):
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


def get_support_base(voxels_np):
    """
    Input: A numpy array (full) with the information whether the voxel is contained
    Output: the range of support bsae
    NOTE: The y axis is perpendicular to the support base.
          The support base is close to y=0
    """
    grid_shape = voxels_np.shape
    for id_z in range(grid_shape[2]):
        if np.count_nonzero(voxels_np[:, :, id_z] == True) > 0:
            # id_y+=1 #NOTE: After visualization, second floor is connected
            support_base = voxels_np[:, :, id_z]
            base_index = []
            for i in range(grid_shape[0]):
                for j in range(grid_shape[1]):
                    if support_base[i, j] == True:
                        base_index.append([i, j])
            print(np.array(base_index))
            return np.array(base_index)


def carving(voxel_surface, voxel_inside, support_base):
    grid_shape = voxel_surface.shape
    carved_voxel_inside = voxel_inside
    max_x = max(support_base[:, 0])
    min_x = min(support_base[:, 0])
    max_y = max(support_base[:, 1])
    min_y = min(support_base[:, 1])
    barycenter = get_barycenter(voxel_inside)
    print(barycenter)
    barycenter_x = barycenter[0]
    barycenter_y = barycenter[2]
    if (min_x <= barycenter_x <= max_x) and (min_y <= barycenter_y <= max_y):
        return carved_voxel_inside
    # to move barycenter_x, cut y-z plane
    # to move barycenter_y, cut x-z plane

    # while True:
    if barycenter_x < min_x:  # cut y-z plane
        print('barycenter_x < min_x')
        for i in range(grid_shape[0]):
            if not carved_voxel_inside[i, :, :].any():
                print("for x, skip ", i)
                continue
            else:
                print("for x, carving ", i)
                carve_x = i
                break

        while barycenter_x < min_x and carve_x < grid_shape[0]:
            if barycenter_x < min_x:
                carved_voxel_inside[carve_x, :, :] = False
                carve_x += 1
            else:
                print('failure x')
                break
            barycenter = get_barycenter(carved_voxel_inside)
            barycenter_x = barycenter[0]
            barycenter_y = barycenter[2]

    if barycenter_x > max_x:
        print('barycenter_x > min_x')
        carve_x = grid_shape[0] - 1
        for i in range(grid_shape[0]):
            if not carved_voxel_inside[grid_shape[0] - i - 1, :, :].any():
                print("for x, skip ", grid_shape[0] - i - 1)
                continue
            else:
                print("for x, carving ", grid_shape[0] - i - 1)
                carve_x = grid_shape[0] - i - 1
                break

        while barycenter_x > max_x and carve_x >= 0:
            if barycenter_x > max_x:
                carved_voxel_inside[carve_x, :, :] = False
                carve_x -= 1
            else:
                print('failure x')
                break
            barycenter = get_barycenter(carved_voxel_inside)
            barycenter_x = barycenter[0]
            barycenter_y = barycenter[1]

    if barycenter_y < min_y:  # cut y-x plane
        print('barycenter_y < min_y')
        for i in range(grid_shape[2]):
            if not carved_voxel_inside[:, i, :].any():
                print("for y, skip ", i)
                continue
            else:
                print("for y, carving ", i)
                carve_y = i
                break

        while barycenter_y < min_y and carve_y < grid_shape[2]:
            if barycenter_y < min_y:
                print("for y, carving ", carve_y)
                carved_voxel_inside[:, carve_y, :] = False
                print(np.count_nonyero(carved_voxel_inside[:, :, :] == True))
                carve_y += 1
            else:
                print('failure y')
                break
            barycenter = get_barycenter(carved_voxel_inside)
            barycenter_x = barycenter[0]
            barycenter_y = barycenter[1]
            print(barycenter)
            print(barycenter_y, min_y)

    if barycenter_y > max_y:
        print('barycenter_y > min_y')
        for i in range(grid_shape[2]):
            if not carved_voxel_inside[:, grid_shape[2] - i - 1, :].any():
                print("for y, skip ", grid_shape[2] - i - 1)
                continue
            else:
                print("for y, carving ", grid_shape[2] - i - 1)
                carve_y = grid_shape[2] - i - 1
                break

        while barycenter_y > max_y and carve_y >= 0:
            if barycenter_y > max_y:
                carved_voxel_inside[:, carve_y, :] = False
                # print(np.count_nonyero(carved_voxel_inside[:, :, :] == True))
                carve_y -= 1
            else:
                print('failure y')
                break
            barycenter = get_barycenter(carved_voxel_inside)
            barycenter_x = barycenter[0]
            barycenter_y = barycenter[1]

    if (min_x <= barycenter_x <= max_x) and (min_y <= barycenter_y <= max_y):
        print("Carving is successful! The new center of mass is in the support base!")
    return carved_voxel_inside


name = "star/star_rotation"

voxel_surface = np.load('data/' + name + '_voxel_surface.npy')
voxel_inside = np.load('data/' + name + '_voxel_interior.npy')
voxels = voxel_inside + voxel_surface
scaled_support_base = get_support_base(voxels)

carved_voxel_inside = carving(voxel_surface, voxel_inside, scaled_support_base)

entire_model_carved = voxel_surface + carved_voxel_inside
np.save(file="./data/" + name + "_voxel_interior_carved", arr=np.array(carved_voxel_inside, dtype=bool))
np.save(file="./data/" + name + "_voxel_entire_carved", arr=np.array(entire_model_carved, dtype=bool))

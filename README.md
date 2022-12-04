# INF574_Project 
***By Zhaoyang Chen and Ribal Teeny***
## General introduction
An python implementation for the paper ```Make It Stand: Balancing Shapes for 3D Fabrication``` published in 2013.
## How it works
1. (If the model is stored as ```.off``` file) Run ```off2obj.py``` to generate the corresponding ```.obj``` file.
2. (If the model object is in a stable status) Run ```Rotation.py``` to rotate the model object.
3. Run ```voxelize.py``` to voxelize the model and generate the corresponding ```.npy``` files.
4. Run ```Carve.py``` to carve the interior of the model to make it balance while keeping the surface intact.
5. (If you want)Run ```Visualization_plt.py``` to visualize the results.

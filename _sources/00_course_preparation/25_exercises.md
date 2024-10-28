## Suggested exercises

1.  Install dependencies, download the data, and run the notebooks to test whether dependencies were installed correctly. 

2.  Run ```10_label_augment_train\03_napari_layers``` and practice interacting with Napari Layers in a notebook. 

3.  Run the notebooks in ```10_label_augment_train``` on one of your own images.  Label a single ROI and try to train a model to detect object in the rest of the image.   

4.  Run the notebooks in ```15_sparse_labeling```, add additional labels and try to improve the clustered ladybug detection. 

5.  Run the notebook in ```20_scale\20_cell_pose_diameter.ipynb```, and try tweaking the test image (for example make the spheres closer together or even overlapping)

6.  Run the notebooks 30 through 50 in ```20_scale``` and try to train a cellpose model to detect ladybugs at different scales. 

7.  Run notebook ```20_scale\80_protrusions``` on one of your own tough images, and try to get perfect results self-predicting a single image. 

8.  Run notebook ```20_mobile_sam``` or ```30_filter_labels``` and try to find a filterset that finds ladybugs and discards other objects.
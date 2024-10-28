## Sparse Labeling 

In the previous example we had to label every object within a rectangular ROI.  It is also possible to label only a subset of objects if the deep learning trainer supports 'sparse labels'.

This means the deep learning training algorithm has reprentations for 

1. Background pixels
2. Object pixels
3. 'Not labeled' pixels. 

As of Stardist release 0.9, stardist supports training with label images for which background is 0, objects are assigned an integer index, and 'Not labeled' pixels 

In the below image background and several (but not all) objects have been labeled. 

![not found](sparse_labels.jpg)
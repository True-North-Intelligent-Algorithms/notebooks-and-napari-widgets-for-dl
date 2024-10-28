## Labeling and Augmentation

### In this section:

1.  Use Napari ROIs to divide single image into training and testing sets
2.  Use data augmentation to train Stardist or Cellpose with a small number of labels
3.  Compare deep learning results from different frameworks in the same viewer.  

### Napari-easy-augment-batch-dl tool

The napari-easy-augment-batch-dl tool can be used to label a directory containing an image sequence.  To start it from a notebook use the following code. 

```
viewer = napari.Viewer()

batch_dl = easy_augment_batch_dl.NapariEasyAugmentBatchDL(viewer, label_only = True)

viewer.window.add_dock_widget(
    batch_dl
)

data_path = r'username\data'

batch_dl.load_image_directory(data_path)
```

Then label data using the built in Napari labelling tools.  

1.  Use the ```Label Box``` layer to draw ROIs that indicate the areas that will become 'labels'.  Even if annotated, areas outside ```Label Box``` rois will not be used for training. 

2.  If mobile SAM is installed you can optionally use the ```Object Box``` layer to draw ROIs around individual objects and these will be autosegmented.  

![Not found](napari-easy-augment-batch-dl.jpg)
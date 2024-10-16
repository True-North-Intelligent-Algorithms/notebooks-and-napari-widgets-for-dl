## Todo: Dependences


Install latest development version of napari-easy-augment-batch-dl and tnia-python

```
    pip install git+https://github.com/bnorthan/napari-easy-augment-batch-dl.git
    pip install git+https://github.com/True-North-Intelligent-Algorithms/tnia-python.git
```

You will need to install napari and for augmentation you will need albumentations library.  Also explicitly install numpy 1.26.  (We have not tested with numpy 2.0 so it is a good idea to explicitly install numpy 1.26 to avoid another dependency installing numpy 2.x)

```
    pip install numpy==1.26
    pip install napari[all]
    pip install albumentations
    pip install matplotlib
```

You will also need one or more of stardist, cellpose, segment-everything or Yolo

### Stardist

#### Windows

```
    conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
    pip install "tensorflow<2.11"
    pip install stardist==0.8.5
    pip install gputools
    pip install edt
```

#### Linux

```
    pip install tensorflow[and-cuda]
    pip install stardist
    pip install gputools
    pip install edt
```

### Pytorch (for unet segmentation)

```
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    pip install pytorch-lightning
    pip install monai
    pip install scipy
    pip install tifffile
```

### Cellpose

```
    pip install cellpose
```

### SAM (Segment Anything)

```
    pip install segment-everything
```
## Dependencies

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
    conda install -c conda-forge cudatoolkit=11.8 cudnn=8.1.0
    pip install "tensorflow<2.11"
```

#### Linux

```
    pip install tensorflow[and-cuda]
```

#### Windows and Linux

```
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

Install ```segment-everything``` which will install SAM as a dependency and also has a vendored copy of [MobileSAMv2](https://github.com/ChaoningZhang/MobileSAM)

```
    pip install segment-everything
```

### Napari-easy-augment-batch-dl and tnia-python

Install latest development version of napari-easy-augment-batch-dl, tnia-python and napari-segment-everything.

```
    pip install git+https://github.com/bnorthan/napari-easy-augment-batch-dl.git
    pip install git+https://github.com/True-North-Intelligent-Algorithms/tnia-python.git 
    pip install git+https://github.com/True-North-Intelligent-Algorithms/napari-segment-everything.git
```

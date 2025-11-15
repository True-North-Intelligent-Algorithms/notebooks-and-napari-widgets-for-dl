# Dependencies

You will need to install napari and for augmentation you will need albumentations library.  Also explicitly install numpy 1.26.  (We have not tested with numpy 2.0 so it is a good idea to explicitly install numpy 1.26 to avoid another dependency installing numpy 2.x)

You will also need stardist, cellpose, segment-everything and Yolo.  On Windows you will likely need to create separate environments for Stardist and the Pytorch dependencies (Cellpose, SAM and YOLO).

In addition to the popular deep learning toolkits these tutorials use 4 helper and widget libraries.  (Note that Yolo is installed via the vendored version of [MobileSam](https://github.com/ChaoningZhang/MobileSAM) installed through ```segment-everything```)

**tnia-python:** General image processing and deep learning helpers.  
**napari-easy-augment-batch-dl:**  Napari widgets for labelling and running deep learning workflows on image series.  
**segment-everything:**  Helper to run YOLO and SAM variations and work with lists representing (possibly overlapping) labels.  
**napari-segment-everything:**  Napari GUI for segment-everything. 


## Linux

```
    conda create -n I2k2024_env python=3.11
    conda activate I2k2024_env
    conda install pip
    pip install "napari[all]" # requires quotation marks to parse the square brackets on Linux, not sure if generalizes
    pip install albumentations matplotlib scipy tifffile 
    pip install "tensorflow[and-cuda]" # as above, requires quotation marks (only needed for stardist)
    pip install stardist 
    pip install gputools #==0.2.15 may no longer needed if we are happy with np 2
    pip install edt # pip throws: numba v0.60.0, tensorflow v2.18.0 require lower versions of numpy. Should still work but iffy.
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    pip install pytorch-lightning
    pip install git+https://github.com/Project-MONAI/MONAI # as of early spring 2025 need to get the github version of monai if using numpy 2.x 
    pip install cellpose
    pip install git+https://github.com/True-North-Intelligent-Algorithms/tnia-python.git 
    pip install git+https://github.com/True-North-Intelligent-Algorithms/segment-everything.git
    pip install git+https://github.com/True-North-Intelligent-Algorithms/napari-easy-augment-batch-dl.git
    pip install git+https://github.com/True-North-Intelligent-Algorithms/napari-segment-everything.git
```

## Mac M1

```
    conda create -n I2k2024_env python=3.11
    conda activate I2k2024_env
    pip install "napari[all]" # also requires quotes on Mac
    pip install albumentations matplotlib scipy tifffile 
    pip install "tensorflow[and-cuda]" # as above, requires quotation marks. Pip throws a bunch of conflicts, but whatever. (only needed for stardist)
    pip install stardist
    pip install gputools # version may no longer be needed if going with numpy 2.x ==0.2.15 # pip dependency incompatibilities
    pip install edt 
    pip install torch torchvision torchaudio # remove the index flag url
    pip install pytorch-lightning
    pip install git+https://github.com/Project-MONAI/MONAI # as of early spring 2025 need to get the github version of monai if using numpy 2.x 
    pip install cellpose
    pip install git+https://github.com/True-North-Intelligent-Algorithms/segment-everything.git
    pip install git+https://github.com/True-North-Intelligent-Algorithms/napari-easy-augment-batch-dl.git
    pip install git+https://github.com/True-North-Intelligent-Algorithms/tnia-python.git 
    pip install git+https://github.com/True-North-Intelligent-Algorithms/napari-segment-everything.git
```

## Windows 

Note that to use GPU with Stardist in Windows we need two different environments because Windows needs an older version of tensorflow, which is not compatible wither newer version of pytorch based toolkits.   This has led to increasingly convoluted installation instructions for stardist-GPU-windows (as transitive dependencies become an issue).  See this [thread](https://forum.image.sc/t/difficulty-installing-stardist-tensorflow-gputools-with-anaconda/104305/15).  Please add to it if you run into issues. 

I've also archived a windows gpu stardist environment.yml [here](https://github.com/True-North-Intelligent-Algorithms/notebooks-and-napari-widgets-for-dl/tree/main/dependencies/windows_stardist).  You will need both the ```environment.yml``` and ```requirements.txt```.  

### Current Windows stardist GPU environment instructions ()

```
    conda create -n I2k2024_stardist_env python=3.11
    conda activate I2k2024_stardist_env
    pip install numpy==1.26.4 # start with numpy 1.26 and hope nothing upgrades it...
    pip install "napari[all]"
    pip install albumentations matplotlib scipy tifffile 
    conda install -c conda-forge cudatoolkit=11.8 cudnn=8.1.0
    pip install "tensorflow<2.11"
    pip install stardist==0.8.5
    pip install gputools==0.2.15
    pip install edt
    pip install reikna==0.8.0 
    pip install numpy==1.26.4 # in case numpy got upgraded go back (hacky yes, but this is what people are reporting works)
    pip install numba==0.59.1
    pip install git+https://github.com/True-North-Intelligent-Algorithms/tnia-python.git 
    pip install git+https://github.com/True-North-Intelligent-Algorithms/napari-easy-augment-batch-dl.git
```

### Windows pytorch environment

```
    conda create -n I2k2024_pytorch_env python=3.11
    conda activate I2k2024_pytorch_env
    pip install "napari[all]"
    pip install albumentations matplotlib scipy tifffile 
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    pip install pytorch-lightning
    pip install git+https://github.com/Project-MONAI/MONAI # as of early spring 2025 need to get the github version of monai if using numpy 2.x 
    pip install cellpose
    pip install git+https://github.com/True-North-Intelligent-Algorithms/segment-everything.git
    pip install git+https://github.com/True-North-Intelligent-Algorithms/napari-easy-augment-batch-dl.git
    pip install git+https://github.com/True-North-Intelligent-Algorithms/tnia-python.git 
    pip install git+https://github.com/True-North-Intelligent-Algorithms/napari-segment-everything.git
```

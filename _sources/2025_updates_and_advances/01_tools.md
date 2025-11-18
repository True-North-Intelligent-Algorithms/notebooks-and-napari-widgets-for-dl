# 2025 Updates and Advances 

This workshop is an update to the 2024 workshop.  

###  Question:  Does the 2024 workshop still work?

**Answer**:  I don't know.  I haven't gone back yet and tried to re-run sections 10 to 30.  I will eventually, and try to integrate the new examples toward a more organized flow.  First step is to introduce technologies that will allow the old examples to be more robust to age. 

### New technologies we will learn today

And how they will help make the entire workshop (including last year's sections) more robust:

#### Pixi

Pixi solves the "it worked last year but breaks today" problem. Unlike conda environments that can drift over time or break because ambiguous dependencies change, Pixi creates locked, reproducible environments from a single `pixi.toml` file. 

The key is `pixi.lock` file. Even if someone writes a sloppy `pixi.toml` with loose version constraints, the lock file captures the exact versions that actually worked. This lock file is what makes true reproduction possible.

This means:
- Examples from 2024 will still run in 2030
- No more "conda environment not found" errors
- Faster setup - one `pixi install` command gets everything
- Cross-platform consistency
- Exact reproducibility thanks to locked dependency versions

Pixi makes our deep learning workflows future-proof by eliminating the dependency hell that often breaks older tutorials.

#### Appose

Appose lets us run conflicting deep learning models in the same notebook without environment clashes. Instead of choosing between Cellpose v3 vs v4, or SAM vs MicroSAM, we can use them all.

This means:
- Compare multiple models side-by-side easily
- No more "this breaks that" dependency conflicts
- Future models can be added without breaking existing ones
- Notebooks become model comparison laboratories

Appose makes our examples resilient to the fast-changing deep learning landscape by isolating each model in its own environment while keeping them accessible from one place.

### Code

Code for the entire workshop can be found [here](https://github.com/True-North-Intelligent-Algorithms/notebooks-and-napari-widgets-for-dl). Please clone this repository before the course. Today we will focus on the notebooks in this [section](https://github.com/True-North-Intelligent-Algorithms/notebooks-and-napari-widgets-for-dl/tree/main/docs/2025_updates_and_advances).

### Jupyter book view

The Jupyter book view of the workshop can be found [here](https://true-north-intelligent-algorithms.github.io/notebooks-and-napari-widgets-for-dl/intro.html)

### Data

Data can be found on Dropbox [here](https://www.dropbox.com/scl/fo/4lvuwq8pbdx0ubba9ey85/AMz_dint2PkRASM1oFWx6uA?rlkey=4ibypc0u40ub702trdipzokir&st=g70qjhe6&dl=0). Download all the data and place it at the top level of the repository in the ```data``` directory. 

The 2025 update to the workshop uses Jupyter Notebooks, Napari, Cellpose, Stardist and Microsam among other tools.  In addition the following other projects are used.  We will be using Pixi to get these projects. 

[tnia-python](https://github.com/True-North-Intelligent-Algorithms/tnia-python) - This is a general utility project for image processing including deep learning utilities.

[easy-augment-batch-dl](https://github.com/True-North-Intelligent-Algorithms/napari-easy-augment-batch-dl) - A plugin to perform deep learning on small to medium-sized image sets with UNETs, Cellpose, Stardist, SAM and friends. This plugin is particularly useful for performing deep learning with a small number of labels and augmentation, and for experimenting with different deep learning frameworks.  

[napari-ai-lab](https://github.com/True-North-Intelligent-Algorithms/napari-ai-lab) - A collection of plugins and utilities for ND segmentation with Cellpose, StarDist, SAM and more. The motivation for this newer project is to construct a better foundation for handling ND datasets and complicated dependency management (via Appose and Pixi).

## Some examples may be 'under construction' 

![not found](under_construction.jpg)
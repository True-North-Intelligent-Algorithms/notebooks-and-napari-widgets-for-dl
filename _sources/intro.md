# Introduction

This workshop shows several Jupyter Notebooks and Napari widgets that can be used to run and compare different Deep Learning frameworks such as Stardist, Cellpose, Instanseg, SAM (Segment Anything Model), YOLO, and PyTorch Semantic Segmentation – within the same project. Examples include: comparing results from different frameworks in the same viewer, training and evaluating models on images with structure at different scales, using Napari to visualize overlapping labels generated by SAM, using Napari ROIs to divide a single image into training and validation sets, applying data augmentation to train Stardist and/or Cellpose with a small number of labels, visualizing the receptive field of a neural network, training Stardist using partial (sparse) labels, and filtering the (potentially) hundreds or thousands of labels produced by SAM.

## License

[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed by Brian Northan and Ian Coccimiglio 
[Creative Commons Attribution 4.0 International License][cc-by].

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

This repository is maintained using [Jupyter lab](https://jupyterlab.readthedocs.io/en/stable/) and build using [Jupyter book](https://jupyterbook.org/intro.html).

## Acknowledgements

[Image SC](https://forum.image.sc/) discussions are the inspiration for most of the material in this tutorial.  

[Cellpose](https://www.nature.com/articles/s41592-020-01018-x)  Carsen Stringer, Tim Wang, Michalis Michaelos, Marius Pachitariu and [Cellpose 2.0](https://www.nature.com/articles/s41592-022-01663-4)

[Stardist](https://arxiv.org/abs/1806.03535) Uwe Schmidt, Martin Weigert, Coleman Broaddus, Gene Myers.

[Mobile SAM](https://arxiv.org/abs/2312.09579) Chaoning Zhang
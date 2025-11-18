# napari-easy-augment-batch-dl

## What is it?

A [napari plugin](https://github.com/True-North-Intelligent-Algorithms/napari-easy-augment-batch-dl) for deep learning on small to medium-sized image datasets. Useful for experimenting with different deep learning frameworks when you have limited labeled data.

## Features

- **Multiple frameworks**: UNETs, Cellpose, Stardist, SAM
- **Augmentation options**: Generate additional training data from existing labels
- **Model comparison**: Test different approaches on the same dataset
- **Flexible dependencies**: Works with whatever frameworks you have installed

## Use Cases

- Small datasets (dozens to hundreds of images)
- Comparing segmentation models
- Limited labeled data scenarios

## Dependencies

This plugin works with different combinations of frameworks - you don't need to install everything. Install what you want to use (PyTorch, Cellpose, SAM, Stardist, etc.) and the plugin adapts accordingly.

## Getting Started

See the [full documentation](https://true-north-intelligent-algorithms.github.io/napari-easy-augment-batch-dl/) for installation instructions and tutorials.

**Dependency Note:** This plugin intentionally doesn't force you to install every possible deep learning framework. Install what you want to use (PyTorch, Cellpose, SAM, Stardist, etc.) and the plugin will work with your chosen combination.

For questions about dependencies, please post on the [Image.sc](https://image.sc) forum.
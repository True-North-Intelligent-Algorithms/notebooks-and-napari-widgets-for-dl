from qtpy import QtCore, QtWidgets
from napari_easy_augment_batch_dl import easy_augment_batch_dl

print("Startup running...")

import napari
print("Napari version:", napari.__version__)

import torch

# Print PyTorch version
print("PyTorch version:", torch.__version__)

# Check if CUDA (GPU) is available
print("CUDA available:", torch.cuda.is_available())

# If available, print the name of the GPU
if torch.cuda.is_available():
    print("GPU name:", torch.cuda.get_device_name(0))
    print("Current device:", torch.cuda.current_device())
else:
    print("Running on CPU")

import cellpose
print("Cellpose version:", cellpose.version)

viewer = napari.Viewer()

batch_dl = easy_augment_batch_dl.NapariEasyAugmentBatchDL(viewer)

class WideScroll(QtWidgets.QScrollArea):
    def sizeHint(self):
        return QtCore.QSize(500, 300)  # width=900, height arbitrary

scroll = WideScroll()
scroll.setWidgetResizable(True)
scroll.setWidget(batch_dl)

viewer.window.add_dock_widget(
    scroll
)

napari.run()

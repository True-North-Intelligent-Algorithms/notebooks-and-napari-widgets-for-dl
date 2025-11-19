import numpy
import tensorflow as tf 
import napari
import stardist
import sys
from napari_easy_augment_batch_dl import easy_augment_batch_dl
from qtpy import QtCore, QtWidgets

print('Python:', sys.version)
print('numpy is', numpy.__version__)
print('Tensorflow:', tf.__version__, '| GPU:', tf.test.is_gpu_available(), '| Name:', tf.test.gpu_device_name() if tf.test.is_gpu_available() else 'None')
print('napari:', napari.__version__)
print('stardist:', stardist.__version__)

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
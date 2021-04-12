
from .coco import CocoDataset
from .registry import DATASETS
from .xml_style import XMLDataset
### IMPORT YOUR DATASET FORMAT AND PASS IT IN MYDATASET FUNC

@DATASETS.register_module
class MyDataset(XMLDataset):

    CLASSES = ('table') ## ADD ALL YOUR CLASSES

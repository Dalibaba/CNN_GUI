class Window:
    TITLE_LABEL = "IMAGE CLASSIFICATION - Train and Classify"
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    CLASSIFY_SCREEN_INDEX = 1
    TRAIN_SCREEN_INDEX = 0


class Menubar:
    EXIT_LABEL = '&Exit'
    TRAIN_LABEL = '&Train CNN'
    CLASSIFY_LABEL = '&Classify with CNN'
    SCREEN_LABEL = '&Classify with CNN'


class ClassifyWidget:
    CHOOSE_IMAGE_LABEL = "Choose Image"
    CHOOSE_MODEL_LABEL = "Choose Model"
    CLASSIFICATION_LABEL = "Classify Images with Model"
    CLASSIFY_LABEL = "Classify Images with Model"


class TrainWidget:
    TRAIN_LABEL = "Choose Image"
    CLASSIFY_IMAGE_LABEL = "Classify Images with Model"
    RESNET_LABEL = "ResNet-50"
    VGG16_LABEL = "VGG16"
    MODEL_TYPE = "Type of Model"

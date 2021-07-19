from tensorflow import keras

"""class for the cnn model"""


class Model:
    input_shape = ()
    output_shape = ()

    """load model file"""

    def load(self, model_path):
        model = keras.models.load_model(model_path)
        self.input_shape = model.layers[0].output_shape
        self.output_shape = model.layers[len(model.layers) - 1].output_shape
        return model

    """preprocess image"""

    """classify image with model"""

    def classify(self, image_path):
        print("classify")
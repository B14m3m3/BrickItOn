from brain.helpers import *
import tensorflow as tf
import numpy as np
import input as inp

class Detector:
    def __init__(self):
        self.classifier = getEstimator()

    def guessFromFile(self, filename):
        (predict_data, labels) = loadDataset(filename)

        return self.guess(predict_data[0])

    def guess(self, imagepixels):

        imagepixels = np.asarray([imagepixels], dtype=np.float32)

        # Predict input
        predict_input_fn = tf.estimator.inputs.numpy_input_fn(
            x={"x": imagepixels},
            num_epochs=1,
            shuffle=False)

        prediction = self.classifier.predict(input_fn=predict_input_fn)
        predicted_classes = [p["classes"] for p in prediction]

        # Print all:
        print("All predictions: ", predicted_classes)
        return inp.Input(predicted_classes[0])



#runner = Detector()
#print("Guess is: ", runner.guessFromFile("dataset/sign_mnist_predict.csv"))
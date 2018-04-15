from brain.helpers import *
import tensorflow as tf
import numpy as np
import input as inp

tf.logging.set_verbosity(tf.logging.ERROR)

class Detector:
    def __init__(self):
        self.classifier = getEstimator()

    def guessFromFile(self, filename):
        (predict_data, labels) = loadDataset(filename)

        for set in predict_data:
            print(self.guess(set))

    def guess(self, imagepixels):
        imagepixels = np.asarray([imagepixels], dtype=np.float32)

        # Predict input
        predict_input_fn = tf.estimator.inputs.numpy_input_fn(
            x={"x": imagepixels},
            num_epochs=1,
            shuffle=False)

        prediction = self.classifier.predict(input_fn=predict_input_fn)

        for p in prediction:

            char = p["classes"]
            print("Prediction: ", inp.Input(char))
            #for key, prob in np.array(p["probabilities"]):
            #    print(key, ": ", prob, "%")
            print("A: {0:.2f}".format(p["probabilities"][0]))
            print("B: {0:.2f}".format(p["probabilities"][1]))
            print("C: {0:.2f}".format(p["probabilities"][2]))
            print("D: {0:.2f}".format(p["probabilities"][3]))
            print(p)
            print("")

            return inp.Input(char)


        # Print all:
        #print("All predictions: ", predicted_classes)
        #return inp.Input(predicted_classes[0])
        return None
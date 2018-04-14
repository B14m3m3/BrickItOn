from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
from brain.helpers import *

tf.logging.set_verbosity(tf.logging.INFO)

class Trainer:
    def run(self):
        (train_data, train_labels) = loadDataset("brain/dataset/sign_mnist_train_small.csv")
        #(eval_data, eval_labels) = loadDataset("brain/dataset/sign_mnist_test.csv")
        #(predict_data, predict_labels) = loadDataset("brain/dataset/sign_mnist_predict.csv")

        print(train_data)

        whitelist = [0, 1, 2, 6];
        print("After")



        #train_data = train_data[train_data[:, 0] in whitelist]
        #print(train_data)
        quit()
        print("Training data: ", len(train_data))
        print("Eval data: ", len(eval_data))
        print("Predict data: ", len(predict_data))

        mnist_classifier = getEstimator()

        # Set up logging for predictions
        # Log the values in the "Softmax" tensor with label "probabilities"
        tensors_to_log = {
            "probabilities": "softmax_tensor",
        }
        logging_hook = tf.train.LoggingTensorHook(
            tensors=tensors_to_log, every_n_iter=50)

        # Train the model
        train_input_fn = tf.estimator.inputs.numpy_input_fn(
            x={"x": train_data},
            y=train_labels,
            batch_size=100,
            num_epochs=None,
            shuffle=True)

        # Evaluate the model and print results
        eval_input_fn = tf.estimator.inputs.numpy_input_fn(
            x={"x": eval_data},
            y=eval_labels,
            num_epochs=1,
            shuffle=False)

        for i in range(1000):
            mnist_classifier.train(
                input_fn=train_input_fn,
                steps=1000,
                hooks=[logging_hook])

            eval_results = mnist_classifier.evaluate(input_fn=eval_input_fn)
            print(eval_results)
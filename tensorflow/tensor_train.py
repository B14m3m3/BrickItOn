from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
from helpers import *

tf.logging.set_verbosity(tf.logging.INFO)

def main(unused_argv):
    (train_data, train_labels) = loadDataset("dataset/sign_mnist_train.csv")
    (eval_data, eval_labels) = loadDataset("dataset/sign_mnist_test.csv")
    (predict_data, predict_labels) = loadDataset("dataset/sign_mnist_predict.csv")

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

    for i in range(1,1):
        #print("-------------------------------------- Training run " + str(i) + " ---------------------------------------------")
        mnist_classifier.train(
            input_fn=train_input_fn,
            steps=100,
            hooks=[logging_hook])

        eval_results = mnist_classifier.evaluate(input_fn=eval_input_fn)
        print(eval_results)


tf.app.run()

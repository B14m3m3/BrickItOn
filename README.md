# BrickItOn
Hackaton team project using Machine Learning Tensorflow to recognize gestures and move a Lego Mindstorm robot using Python

# Demo
![Tensorflow Lego Demo](TensorflowHackaton.gif)

# Setup
Here is the guide for installing required packages.

### Config
Copy the config sample and put your settings into it:
```
cp config_sample.py config.py
nano config.py
```

### Tensorflow
Install dependencies:
```
pip install tensorflow
pip install pillow
pip install numpy
```

Then unzip dataset file into tensorflow/dataset/

### Webcam
Install OpenCV:
```
pip install opencv-python
```

Now setup environment variable PYTHONPATH to point to the root dir of this project.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def load_data(data_file):
    """ loads fer2013.csv dataset
    # Arguments: data_file fer2013.csv
    # Returns: faces and emotions
            faces: shape (35887,48,48,1)
            emotions: are one-hot-encoded
    """
    data = pd.read_csv(data_file)
    pixels = data['pixels'].tolist()
    width, height = 48,48
    faces = []
    for pixel_sequence in pixels:
        face = [int(pixel) for pixel in pixel_sequence.split(' ')]
        face = np.asarray(face).reshape(width,height)
        faces.append(face)
    faces = np.asarray(faces)
    print(faces.shape)
    #faces = preprocess_input(faces)
    faces = np.expand_dims(faces,-1)
    df = pd.get_dummies(data['emotion'])
    emotions = df.as_matrix()
    return faces, emotions
def preprocess_input(images):
    """ preprocess input by substracting the train mean
    # Arguments: images or image of any shape
    # Returns: images or image with substracted train mean (129)
    """
    images = images/255.0
    return images
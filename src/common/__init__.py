#!/usr/bin/env python3

"""Commonly used functions, just so that we don't have to rewrite them
in every file.
"""

import numpy as np
import keras
import csv

def import_train(filename):
    """
    Imports training data and parses it
    """
    with open(filename,'r') as dest_f:
        data_iter = csv.reader(dest_f, delimiter=',')
        data = [data for data in data_iter]

    # remove first row (column labels), first column (id)
    data_array = np.asarray(data)[1:, 1:]

    # convert to 32-bit int
    data_array = data_array.astype(np.int32)
     
    #  remove last column (label)
    X_train = data_array[:, :-1]
    #  keep last column (label) and make into one hot vector
    Y_train = keras.utils.np_utils.to_categorical(data_array[:, -1])

    return X_train, Y_train

def import_test(filename):
    """
    Imports test data and parses it
    """
    with open(filename,'r') as dest_f:
        data_iter = csv.reader(dest_f, delimiter=',')
        data = [data for data in data_iter]
    # remove first row (column labels), first column (id)
    data_array = np.asarray(data)[1:, 1:]
    X_train = data_array.astype(np.float32)
    return X_train
    

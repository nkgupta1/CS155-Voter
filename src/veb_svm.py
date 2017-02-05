#!/usr/bin/env python3

import numpy as np
import time
from common import *
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.externals import joblib
from veb_common import *

X_train, Y_train = normalized_data()

in_sample_accuracy = lambda clf: np.mean(clf.predict(X_train) == Y_train)

def SVM(kernel='linear', cv=True, frac_train=False, degree=3):
    '''
    param: cv: if cv is false, does not cross validate, trains on full data, 
    and pickles the result.
    param: frac_train: fraction of training to use for training (if False, 
    use all of the training data)
    '''
    print('learning', kernel, cv, frac_train)
    start = time.time()
    if frac_train:
        X = X_train[:int(frac_train * X_train.shape[0])]
        Y = Y_train[:int(frac_train * Y_train.shape[0])]
    else:  X, Y = X_train, Y_train
    clf = SVC(kernel=kernel, verbose=False, degree=degree)
    if cv:
        scores = cross_val_score(clf, X, Y, cv=5, 
            scoring='accuracy', verbose=True)
        print('cross-validation accuracy:', np.mean(scores))
    else:
        clf.fit(X, Y)
        finish = time.time()
        # print np.mean(clf.predict(X_train)), np.mean(Y_train)
        save_name = 'a-SVM_'
        if kernel == 'poly':
            save_name += str(degree)
        save_name += kernel + '-' + str(in_sample_accuracy(clf)) + '-'
        save_name += str(frac_train) + '-' + str(int(time.time() - start))
        joblib.dump(clf, 'saved_models/' + save_name)
    print('finished in', (time.time() - start), 'seconds')



SVM(kernel='linear', cv=True, frac_train=0.1)

#clf_to_prediction(2008, 'a-SVM_linear-0.762351740455-0.1-124')


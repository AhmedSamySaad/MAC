
import os
import time
import datetime
import random
import json
import argparse
import numpy as np
import keras.backend as K
# from sklearn.metrics import confusion_matrix
import tensorflow as tf
from sklearn.metrics import f1_score
# from keras.optimizers import Adam
from tensorflow.keras.optimizers import Adam
from keras.utils import np_utils
from keras.models import load_model
import data_loader
from keras.models import model_from_json


import densenet
im_size = 320



model = densenet.DenseNet(nb_classes=1, img_dim=(320,320,1), depth=22, nb_dense_block=4, growth_rate=12, nb_filter=16, dropout_rate=0.2, weight_decay=1E-4)
# model.load_weights('./save_models/MURA_modle@epochs10.h5') #model_10_epochs
model.load_weights('../models/XR_HUMERUS/MURA_modle@epochs40.h5') #model_52_epochs
# model.load_weights('./save_models/best_MURA_modle@epochs14.h5')
X_valid_path, Y_valid = data_loader.load_path(root_path = '../valid/XR_HUMERUS', size = im_size)
X_valid = data_loader.load_image(X_valid_path,im_size)

y1 = model.predict(X_valid, batch_size=None, verbose=0, steps=None)
prediction= [] #othman edit
j = len(y1)

for i in range (0, j):
	if y1[i]>0.5 :
		# print(X_valid_path[i],":\t","Positive\t", y1[i])
		prediction.append(1) #othman edit
	else:
		# print(X_valid_path[i],":\t","Negative\t", y1[i])
		prediction.append(0) #othman edit


# print(len(Y_valid)== len(prediction)) #othman edit

Y_valid = np.array(Y_valid)
prediction= np.array(prediction)
print("Accuracy: ",(Y_valid==prediction).sum()/len(Y_valid))

print(f"confusion_matrix: {tf.math.confusion_matrix(Y_valid, prediction)}")
print(f"f_1 score: {f1_score(Y_valid, prediction)}")
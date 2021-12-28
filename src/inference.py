from src import densenet
from src import data_loader
import numpy as np
import cv2
import keras.backend as K


class Inference:
    def __init__(self,image,bone_type):
        self.image=image
        self.bone_type=bone_type
        self.model = densenet.DenseNet(nb_classes=1, img_dim=(320,320,1), depth=22, nb_dense_block=4, growth_rate=12, nb_filter=16, dropout_rate=0.2, weight_decay=1E-4)


    def predict(self):
        if self.bone_type == "XR_ELBOW":
            self.model.load_weights('./best_models/Best_MURA_model_XR_ELBOW@epochs40.h5')
        elif self.bone_type == "XR_FINGER":
            self.model.load_weights('./best_models/Best_MURA_model_XR_FINGER@epochs40.h5')
        elif self.bone_type == "XR_FOREARM":
            self.model.load_weights('./best_models/Best_MURA_model_XR_FOREARMepochs40.h5')
        elif self.bone_type == "XR_HAND":
            self.model.load_weights('./best_models/Best_MURA_model_XR_HAND@epochs40.h5')
        elif self.bone_type == "XR_HUMERUS":
            self.model.load_weights('./best_models/Best_MURA_model_XR_HUMERUS@epochs40.h5')
        elif self.bone_type == "XR_SHOULDER":
            self.model.load_weights('./best_models/Best_MURA_model_XR_SHOULDER@epochs40.h5')
        else: #XR_WRIST
            self.model.load_weights('./best_models/Best_MURA_model_XR_WRIST@epochs40.h5')

        prediction = self.model.predict(self.preprocessing(320), batch_size=None, verbose=0, steps=None)
        if prediction > 0.5:
            return "Abnormal"
        else:
            return "Normal"
    
    def preprocessing(self,size):
        #convert string data to numpy array
        npimg = np.fromstring(self.image.read(), np.uint8)
        # convert numpy array to image
        img = cv2.imdecode(npimg, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img,(size,size))
        img = data_loader.randome_rotation_flip(img,size)
        img = np.asarray(img).astype('float32')
        mean = np.mean(img)			#normalization
        std = np.std(img)
        img = (img - mean) / std
        if K.image_data_format() == "channels_first":
            img = np.expand_dims(img,axis=1)		   #Extended dimension 1
        if K.image_data_format() == "channels_last":
            img = np.expand_dims(img,axis=3)             #Extended dimension 3(usebackend tensorflow:aixs=3; theano:axixs=1) 
        return img
    # def get_label(self):
    #     pass
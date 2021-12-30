from src import densenet
from src import data_loader
from albumentations import ToFloat, Compose
from skimage.transform import resize
import numpy as np
import cv2
import keras.backend as K
import keras


class Inference:
    def __init__(self,image_path,bone_type,model_name):
        self.image_path=image_path
        self.bone_type=bone_type
        self.model_name=model_name
        if model_name == "densenet":
            self.model = densenet.DenseNet(nb_classes=1, img_dim=(320,320,1), depth=22, nb_dense_block=4, growth_rate=12, nb_filter=16, dropout_rate=0.2, weight_decay=1E-4)


    def predict(self):
        if self.model_name == "densenet":
            if self.bone_type == "XR_ELBOW":
                self.model.load_weights('./best_models/densenet/Best_MURA_model_XR_ELBOW@epochs52.h5')
            elif self.bone_type == "XR_FINGER":
                self.model.load_weights('./best_models/densenet/Best_MURA_model_XR_FINGER@epochs40.h5')
            elif self.bone_type == "XR_FOREARM":
                self.model.load_weights('./best_models/densenet/Best_MURA_model_XR_FOREARMepochs40.h5')
            elif self.bone_type == "XR_HAND":
                self.model.load_weights('./best_models/densenet/Best_MURA_model_XR_HAND@epochs40.h5')
            elif self.bone_type == "XR_HUMERUS":
                self.model.load_weights('./best_models/densenet/Best_MURA_model_XR_HUMERUS@epochs40.h5')
            elif self.bone_type == "XR_SHOULDER":
                self.model.load_weights('./best_models/densenet/Best_MURA_model_XR_SHOULDER@epochs40.h5')
            else: #XR_WRIST
                self.model.load_weights('./best_models/densenet/Best_MURA_model_XR_WRIST@epochs40.h5')

            prediction = self.model.predict(self.preprocessing(320), batch_size=None, verbose=0, steps=None)

            if prediction[0][0] > 0.5:
                return "Abnormal"
            else:
                return "Normal"

        elif self.model_name == "inceptionv3":
            if self.bone_type == "XR_ELBOW":
                self.model = keras.models.load_model('./best_models/inceptionv3/Best_MURA_model_XR_ELBOW@epochs18.h5')
            elif self.bone_type == "XR_FINGER":
                self.model = keras.models.load_model('./best_models/inceptionv3/Best_MURA_model_XR_FINGER@epochs40.h5')
            elif self.bone_type == "XR_FOREARM":
                self.model = keras.models.load_model('./best_models/inceptionv3/Best_MURA_model_XR_FOREARMepochs40.h5')
            elif self.bone_type == "XR_HAND":
                self.model = keras.models.load_model('./best_models/inceptionv3/Best_MURA_model_XR_HAND@epochs40.h5')
            elif self.bone_type == "XR_HUMERUS":
                self.model = keras.models.load_model('./best_models/inceptionv3/Best_MURA_model_XR_HUMERUS@epochs40.h5')
            elif self.bone_type == "XR_SHOULDER":
                self.model = keras.models.load_model('./best_models/inceptionv3/Best_MURA_model_XR_SHOULDER@epochs40.h5')
            else: #XR_WRIST
                self.model = keras.models.load_model('./best_models/inceptionv3/Best_MURA_model_XR_WRIST@epochs40.h5')
            

            y_pred=  self.model.predict(self.preprocessing())
            print(y_pred)

    def img_transform():
                return Compose([
                                ToFloat(max_value=255)
                                ])

    def crop_center(img,cropx,cropy):
        y,x,_ = img.shape
        startx = x//2-(cropx//2)
        starty = y//2-(cropy//2)    
        return img[starty:starty+cropy,startx:startx+cropx]

    def preprocessing(self,size=320):
        if self.model_name == "densenet":
            img = cv2.imread(self.image_path,cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img,(size,size))
            img = data_loader.randome_rotation_flip(img,size)
            img = np.asarray([img]).astype('float32')
            mean = np.mean(img)			#normalization
            std = np.std(img)
            img = (img - mean) / std
            if K.image_data_format() == "channels_first":
                img = np.expand_dims(img,axis=1)		   #Extended dimension 1
            if K.image_data_format() == "channels_last":
                img = np.expand_dims(img,axis=3)             #Extended dimension 3(usebackend tensorflow:aixs=3; theano:axixs=1) 
            return img
        elif self.model_name == "inceptionv3":
            img= cv2.imread(self.image_path)
            img= Inference.img_transform()(image=img)["image"]
            img= resize(img,(300,300,3))
            img= Inference.crop_center(img,224,224)
            img= img/255.0
            return img
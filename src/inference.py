from src import densenet

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
            self.model.load_weights('best_models/Best_MURA_model_XR_HUMERUS@epochs40.h5')
        elif self.bone_type == "XR_SHOULDER":
            self.model.load_weights('./best_models/Best_MURA_model_XR_SHOULDER@epochs40.h5')
        else: #XR_WRIST
            self.model.load_weights('./best_models/Best_MURA_model_XR_WRIST@epochs40.h5')

        prediction = self.model.predict(self.image, batch_size=None, verbose=0, steps=None)
        if prediction > 0.5:
            return "Abnormal"
        else:
            return "Normal"
    # def get_label(self):
    #     pass
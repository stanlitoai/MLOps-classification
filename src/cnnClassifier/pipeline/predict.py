import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image  
import os



class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename


    
    def predict(self):
        model = load_model(os.path.join("artifacts","training", "model.h5"))
        imagename = self.filename

        img = image.load_img(self.filename, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)

        x = np.argmax(model.predict(x), axis=1)
        print(x)
        if x[0] == 1:
            prediction = "Healthy"
            return [{"image" : prediction}]
        else:

            prediction = "Coccidiosis"
            return [{"image" : prediction}]
        
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np



new_model = load_model('models/imageclassifier.h5')

def predict(image):
    resise=tf.image.resize(image, (256,256))
    ypred=new_model.predict(np.expand_dims(resise/255, 0))
    return [ypred.argmax(),ypred.max()]
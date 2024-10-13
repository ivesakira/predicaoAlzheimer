import os
import numpy as np
from keras.models import load_model

class PredicaoAlzheimer:
    modelPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model')
    model = load_model(rf'{modelPath}\alzheimer.keras')
    
    classes = {
        0:'Sem Alzheimer',
        1:'Alzheimer Muito Leve',    
        2:'Alzheimer Leve',
        3:'Alzheimer Moderada'
        }

    def PredicaoImagem(self, imagem):
        predicao = self.model.predict(imagem)
        predicaoArgmax = np.argmax(predicao, axis=1)
        predicaoClasse = self.classes.get(predicaoArgmax[0], 1)
        return predicaoClasse


class PredicaoEM:
    modelPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model')
    model = load_model(rf'{modelPath}\MS.keras')
    
    classes = {
        0:'Sem EM',
        1:'EM'
        }

    def PredicaoImagem(self, imagem):
        predicao = self.model.predict(imagem)
        predicaoArgmax = np.argmax(predicao, axis=1)
        predicaoClasse = self.classes.get(predicaoArgmax[0], 1)
        return predicaoClasse

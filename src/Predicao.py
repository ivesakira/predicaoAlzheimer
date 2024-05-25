import os
import numpy as np
from keras.models import load_model

class Predicao:
    modelPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model')
    model = load_model(rf'{modelPath}\alzheimer.keras')
    
    classes = {
        0:'Saudavel',
        1:'Demência Muito Leve',    
        2:'Demência Leve',
        3:'Demência Moderada'
        }

    def PredicaoImagem(imagem):
        predicao = Predicao.model.predict(imagem)
        predicaoArgmax = np.argmax(predicao, axis=1)
        predicaoClasse = Predicao.classes.get(predicaoArgmax[0], 1)
        return predicaoClasse

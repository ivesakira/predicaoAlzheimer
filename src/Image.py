from glob import glob
import numpy as np
import cv2
import os

class Imagem:
    inputPath = os.getcwd() + '\\Input'
    tamanhoPadrao = 100

    def LeituraImagem():
        imagensPath = glob(f"{Imagem.inputPath}\*.jpg")
    
        if not imagensPath: # Se a lista estiver vazia retorna None
            return None
    
        path = imagensPath[0]
        image = Imagem.__TratamentoImagem(cv2.imread(path, cv2.IMREAD_GRAYSCALE))
        os.remove(path)
        return image
    
    def __TratamentoImagem(imagem):
        tamanho = (Imagem.tamanhoPadrao, Imagem.tamanhoPadrao)
        imagemBlur = cv2.GaussianBlur(imagem, (3,3), 0)
        imagemResize = cv2.resize(imagemBlur, tamanho)
        # imagemTratada = np.array(list(imagemResize))/255.0
        imageReshape = np.expand_dims(np.expand_dims(imagemResize, axis=-1), axis=0)
        return imageReshape
from Image import Imagem
from Predicao import PredicaoAlzheimer, PredicaoEM

def main():
    image = Imagem.LeituraImagem()
    if image is not None:
        resultadoAlzheimer = PredicaoAlzheimer.PredicaoImagem(image)
        resultadoEM = PredicaoEM.PredicaoImagem(image)
        print(resultadoAlzheimer, resultadoEM)

if __name__ == '__main__':
    main()
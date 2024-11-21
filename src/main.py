from Image import Imagem
from Predicao import PredicaoAlzheimer, PredicaoEM

def main():
    image = Imagem.LeituraImagem()
    if image is not None:
        alzheimer = PredicaoAlzheimer(image)
        EM = PredicaoEM(image)
        resultadoAlzheimer = alzheimer.predicao
        resultadoEM = EM.predicao
        print(f'{resultadoAlzheimer}, {resultadoEM}')

if __name__ == '__main__':
    main()
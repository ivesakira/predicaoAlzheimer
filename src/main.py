from Image import Imagem
from Predicao import Predicao

def main():
    image = Imagem.LeituraImagem()
    if image is not None:
        resultado = Predicao.PredicaoImagem(image)
        print(resultado)

if __name__ == '__main__':
    main()
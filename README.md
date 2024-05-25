# Predição Alzheimer

Projeto para leitura de imagem e predição de caso de alzheimer

## Configuração

### Pré-requisitos

- Python 3.7 ou superior
- Git

### Passos para Configuração

1. Clone o repositório:

   ```cmd
   git clone https://github.com/ivesakira/predicaoAlzheimer.git
   cd predicaoAlzheimer
   ```
2. Crie um ambiente virtual e instale as dependências:

   ```cmd
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Execute o script principal:

   ```cmd
   python src\main.py
   ```

## Estrutura do Projeto

- `src/`: Contém os módulos principais do projeto.
  - `main.py`: Script principal.
  - `Image.py`: Manipulação e carga da imagem.
  - `Predicao.py`: Aplicação do modelo.
- `Input/`: Contém a entrada das imagens.
- `requirements.txt`: Arquivo de dependências do projeto.
- `README.md`: Documentação do projeto.

## Dependências

- `cv2`
- `numpy`
- `keras`
- `tensorflow`

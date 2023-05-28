# Ponderada 3

Primeiramente, seguindo o tutorial disponibilizado, criei uma cópia do notebook e fiz as importações necessárias, incluindo o YOLOv7. Em seguida, clonei o repositório "Official YOLOv7". Baixamos o arquivo "yolov7-seg.pt", que será usado para realizar as segmentações de imagem usando o modelo YOLOv7, e defini a variável WEIGHTS_PATH como o caminho desse arquivo.

Em seguida, realizei o setup do ambiente utilizando a API Key fornecida pelo RoboFlow. No site do RoboFlow, escolhemos o data-set pré-treinado que queremos utilizar, optando pelo conjunto de dados "Crack" para realizar o reconhecimento de rachaduras. Em seguida, executei o script "train.py" para realizar um treinamento personalizado com o modelo de detecção do YOLOv7.

Para testar o modelo treinado, baixei o "crackDetector"(modelo feito) no meu PC. Em seguida, criei um código simples em Python utilizando as bibliotecas OpenCV e YOLO para utilizar a webcam do meu computador e testar o modelo. Tanto o Jupyter Notebook quanto o arquivo de teste em Python junto ao modelo estão disponíveis no repositório.

Para assistir ao vídeo de teste realizado, você pode acessar o link abaixo: 

[https://drive.google.com/file/d/1t4lDsM1chL4AxxzgZFERjSbm5BywHKmE/view?usp=sharing].


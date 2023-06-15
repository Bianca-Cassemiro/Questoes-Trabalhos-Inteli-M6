
# Aplicação de OpenCV com Yolo - atividade4

Para realizar a atividade de simulação com OpenCV e Yolo, utilizei um arquivo que contém um modelo (best.pt), uma imagem que foi previamente salva localmente e um script em Python.

Neste script, realizamos duas ações principais. Primeiro, utilizamos o modelo para fazer a predição na imagem, aplicando técnicas de visão computacional com o OpenCV e Yolo. Em seguida, estabelecemos a comunicação entre o código e o banco de dados utilizando o FastAPI.

Após realizar a predição na imagem, realizamos a conversão do arquivo resultante para o formato Base64. Em seguida, enviamos essa representação em Base64 para o nosso banco de dados no Supabase. Isso nos permite armazenar a imagem predita juntamente com outros dados relevantes.

Durante o vídeo de demonstração, realizo novamente a conversão da representação em Base64 para imagem. Essa etapa é feita com o objetivo de realizar testes e exibir visualmente os resultados obtidos.

# Vídeo demonstração
https://drive.google.com/file/d/1KTWGtiwdwfT8JkIrhdjbJlxQflld8GeV/view?usp=sharing

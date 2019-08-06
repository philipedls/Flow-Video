# YouTube Video Maker

Uma ferramenta para criação automática de vídeos e upload no YouTube.

## Getting Started

Estas instruções mostrarão como essa ferramenta funciona e como colocar o projeto em funcionamento na sua máquina local.

### Pré-requisitos

FFmpeg (versão usada: 4.1.1-1)

```
$ sudo apt-get install ffmpeg   # Para Sistemas baseados em Debian
$ sudo yum install ffmpeg       # Para Sistemas baseados em Red Hat
```

Bibliotecas bibliotecas:

```
Sugestão: Criar um ambiente virtual 'venv' para o python 3.7

$ pip3 install google_images_download      # 2.5.0
$ pip3 install wikipedia                   # 1.4.0
$ pip3 install nltk                        # 3.4
$ pip3 install watson_developer_cloud      # 2.8.0
$ pip3 install google-api-python-client    # 1.7.8
$ pip3 install oauth2client                # 4.1.3
```
É necessário usar o NLTK Downloader para obter o punkt.
Então abra o terminal dentro do diretorio do projeto e execute os seguintes comandos :

```
$ python3
>>> import nltk                           # nltk é um biblioteca de processamento de linguagem natural
>>> nltk.download("punkt")                # dependência necessária para usar o "Tokenizer" nas strings das sentenças
>>> exit()                                # sair do enterpretador python
```

### Faça o Clone do Repositório:

```
$ git clone https://github.com/crhenr/youtube-video-maker.git
```

### Adicione suas API's Keys:

Coloque suas chaves de API do IBM Watson em ``` searchrobot.py  ``` file:
```
...
iam_apikey = "YOUR_API_KEY_HERE",
url = "YOUR_URL_HERE"
...
```
Coloque sua Google API keys em ``` clients_secret.json ``` file:
```
...
"client_id": "YOUR_CLIENT_ID_HERE",
"client_secret": "YOUR_CLIENT_SECRET_HERE",
...
```

### Rodando o Projeto:

Após de concluir todas as configurações, tente rodar o arquivo automation_video_maker.py:
```
$ cd automation+-video-maker/src
$ python3 automation_video_maker.py
```

# Como funciona?

O programa se comporta da seguinte maneira:

 * Procura o termo de pesquisa e o prefixo na Wikipedia;
 * Pega as primeiras frases do resumo da Wikipedia que corresponde ao termo de pesquisa;
 * Remove informações desnecessárias;
 * Envia cada frase para o Watson para obter as palavras-chave correspondentes;
 * Faz o download de algumas imagens do Google Images com base nas palavras-chave;
 * Renomeia e converte as imagens para JPG;
 * Faz o vídeo, adiciona as frases como legendas e adicione uma música (Modo de renderização usando o FFmpeg);
 * Envie o vídeo final para o YouTube com título, descrição e tags.

NOTA: Todos os arquivos (imagens, vídeos e legendas) são salvos na pasta do usuário, em um diretório com o nome do termo de pesquisa.

Exemplo: [final_video.mp4](examples/final_video.mp4)


## Bugs para corrigir:
 * Ter imagens melhores.             #Prentenção de usar o imageMagick para melhorar a qualidade das images
 * Corrigir o erro que faz com que o quinto subtítulo seja ignorado.
 * Melhorar efeitos de transição 

# Script para baixar as imagens do site xkcd.com
import bs4
import requests
import os

# exist_ok=True - serve para verificar se a pasta já existe
os.makedirs('12.1-xkcd', exist_ok=True) #makedirs cria pasta

for i in range(1,11):
    url = "https://xkcd.com/" + str(i)# Grava a url do site
    xkcd = requests.get(url) # Importa o código html do site
    xkcd.raise_for_status()
    soup = bs4.BeautifulSoup(xkcd.text, 'html.parser') # Convert o site em html

    comic_elem = soup.select('#comic img')[0] # Localiza o id=comic e a tag img
    comic_url = 'http:' + comic_elem.get('src')

    print(f'Baixando a imagem {comic_url}...') # Aviso de download da url
    res = requests.get(comic_url) # Faz o download da imagem
    res.raise_for_status # Verifica se o download foi feito com sucesso

    image_file = os.path.join('12.1-xkcd', os.path.basename(comic_url)) # Grava o nome da imagem
    with open(image_file,'wb') as f: # Abre o arquivo para escrita em binário
        f.write(res.content) # Escreve o conteúdo da imagem no arquivo

    print(f'Imagem salva em {image_file}')






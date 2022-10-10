import requests
from PIL import Image
import urllib.request

def pegar_habilidade(poke):
    print('Habilidade do ', poke['name'] )
    for i in poke['abilities']:
        print(i['ability']['name'])

def info_basicas(poke):
    print('Status do ', poke['name'])
    for i in poke['stats']:
        print(i['stat']['name'],i['base_stat'])

def imagem_poke(poke):
    print(poke['sprites']['back_default'])
    pkm_image = poke['sprites']['back_default']
    with urllib.request.urlopen(pkm_image) as url:
        im = Image.open(url)
        im.show()

def main():
    global pokemon
    pokemon = input('Digite o pokemon solicitado: ')
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    res = requests.get(api)
    poke = res.json()
    pegar_habilidade(poke)
    info_basicas(poke)
    imagem_poke(poke)


if __name__ == '__main__':
    main()
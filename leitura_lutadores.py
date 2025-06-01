from get_lutador import get_lutador

def leitura_lutadores():
  x_rapidapi_key = ''
  with open("lutadores.txt") as lutadores:
    arquivo = open("invictos.txt", "w")
    arquivo.close()
    for lutador in lutadores:
      nome = lutador.strip().split()
      if(len(nome) == 1):
        get_lutador(nome[0], '', '', x_rapidapi_key)
      if(len(nome) == 2):
        get_lutador(nome[0], '', nome[1], x_rapidapi_key)
      elif(len(nome) == 3):
        get_lutador(nome[0], nome[1], nome[2], x_rapidapi_key)
from get_lutador import get_lutador

def leitura_lutadores():
  with open("lutadores.txt") as lutadores:
    arquivo = open("invictos.txt", "w")
    arquivo.close()
    for lutador in lutadores:
      nome = lutador.strip().split()
      if(len(nome) == 1):
        get_lutador(nome[0], '', '')
      if(len(nome) == 2):
        get_lutador(nome[0], '', nome[1])
      elif(len(nome) == 3):
        get_lutador(nome[0], nome[1], nome[2])
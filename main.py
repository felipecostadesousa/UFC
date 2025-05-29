from getLutador import getLutador
from sort import sort

with open("lutadores.txt") as lutadores:
  for lutador in lutadores:
    nome = lutador.strip().split()
    if(len(nome) == 1):
      getLutador(nome[0], '', '')
    if(len(nome) == 2):
      getLutador(nome[0], '', nome[1])
    elif(len(nome) == 3):
      getLutador(nome[0], nome[1], nome[2])
sort()
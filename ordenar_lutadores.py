from extrair_numero import extrair_numero

def ordenar_lutadores():
  with open("invictos.txt", "r", encoding="utf-8") as invictos:
    linhas = [linha.strip() for linha in invictos if linha.strip()]
  linhas_ordenadas = sorted(linhas, key=extrair_numero, reverse=True)
  with open("invictos_ordenados.txt", "w", encoding="utf-8") as invictos_ordenados:
    for linha in linhas_ordenadas:
      invictos_ordenados.write(linha + "\n")
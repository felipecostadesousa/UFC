def extrair_numero(texto):
  return int(texto.split('(')[-1].strip(')'))
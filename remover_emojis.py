import re

def remover_emojis(texto):
  return re.sub(r"[^\w\s\-\'.]", "", texto)
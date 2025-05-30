import asyncio
from playwright.async_api import async_playwright
from remover_emojis import remover_emojis

async def coletar_lutadores():
  async with async_playwright() as p:
    navegador = await p.chromium.launch(headless=True)
    pagina = await navegador.new_page()
    await pagina.goto("https://www.roster.watch", wait_until="networkidle")
    await pagina.wait_for_selector("div.rt-tr-group", timeout=60000)
    lutadores = set()
    while True:
      grupos = await pagina.query_selector_all("div.rt-tr-group")
      for grupo in grupos:
        primeira_celula = await grupo.query_selector("div.rt-td")
        if not primeira_celula:
          continue
        nome_tag = await primeira_celula.query_selector("a[href^='/fighters/']")
        if nome_tag:
          nome = await nome_tag.inner_text()
        else:
          nome = await primeira_celula.inner_text()
        if nome:
          nome_limpo = remover_emojis(nome.strip())
          lutadores.add(nome_limpo)
      botao_next = await pagina.query_selector("button.rt-next-button")
      if not botao_next:
        break
      disabled = await botao_next.get_attribute("disabled")
      if disabled is not None:
        break
      await botao_next.click()
      await pagina.wait_for_timeout(1000)
    paragrafos = await pagina.query_selector_all("p")
    for p in paragrafos:
      texto = await p.inner_text()
      if "Fighters with booked bouts not yet listed:" in texto or "Fighters also not yet listed:" in texto:
        partes = texto.split(":")
        if len(partes) > 1:
          nomes_brutos = partes[1].split(",")
          for nome in nomes_brutos:
            nome_limpo = remover_emojis(nome.strip())
            lutadores.add(nome_limpo)
    await navegador.close()
    with open("lutadores.txt", "w", encoding="utf-8") as f:
      for nome in sorted(lutadores):
        if(nome == 'Bruno Gustavo da Silva'):
          nome = 'Bruno Silva'
        if(nome == 'Elizeu Zaleski dos Santos'):
          nome = 'Elizeu dos Santos'
        if(nome == 'Douglas Silva de Andrade'):
          continue
        f.write(nome + "\n")
asyncio.run(coletar_lutadores())
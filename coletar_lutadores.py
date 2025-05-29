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
    await navegador.close()
    lutadores_adicionais = ["Andreas Gustafsson", "Jeka Saragih", "Seok Hyun Ko", "Tofiq Musayev", "Lauren Murphy", "Islam Dulatov", "Alberto Montes", "Austin Bashi", "Austin Vanderford", "Djorden Santos", "Kevin Christian", "Nikolay Veretennikov", "Tuco Tokkos", "Uran Satybaldiev", "Yadier DelValle"]
    for nome in lutadores_adicionais:
      lutadores.add(remover_emojis(nome.strip()))
    with open("lutadores.txt", "w", encoding="utf-8") as f:
      for nome in sorted(lutadores):
        f.write(nome + "\n")
    print(f"Total de lutadores encontrados (incluindo adicionais): {len(lutadores)}")
asyncio.run(coletar_lutadores())
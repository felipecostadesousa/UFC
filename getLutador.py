import requests

def getLutador(firstName, middleName, lastName):
  url = "https://ufc_fighter_stats.p.rapidapi.com/fighter"
  querystring = {"firstName": firstName, "middleName": middleName, "lastName": lastName}
  headers = {"x-rapidapi-key": "7b4ef99412msha2707ae4be4d7a4p15fc0ajsnf0cd1f224e20","x-rapidapi-host": "ufc_fighter_stats.p.rapidapi.com"}
  response = requests.get(url, headers=headers, params=querystring)
  nome = " ".join(part for part in [firstName, middleName, lastName] if part)
  if response.status_code == 200:
    if(response.json()["record"]["losses"] == 0):
      print(f"✅ {nome} ({response.json()['record']['wins']})")
      f = open("/home/felipe-costa/Documentos/Python/invictos.txt", "a")
      f.write(f"{nome} ({response.json()['record']['wins']})\n")
      f.close()
    else:
      print(f"❌ {nome} ({response.json()['record']['wins']} - {response.json()['record']['losses']})")
  else:
    print(f"⚠️ {nome} (ERRO)")
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_lutador(firstName, middleName, lastName):
  url = "https://ufc_fighter_stats.p.rapidapi.com/fighter"
  querystring = {"firstName": firstName, "middleName": middleName, "lastName": lastName}
  headers = {"x-rapidapi-key": "7b4ef99412msha2707ae4be4d7a4p15fc0ajsnf0cd1f224e20","x-rapidapi-host": "ufc_fighter_stats.p.rapidapi.com"}
  response = requests.get(url, headers=headers, params=querystring, verify=False)
  nome = " ".join(part for part in [firstName, middleName, lastName] if part)
  if response.status_code == 200:
    if(response.json()["record"]["losses"] == 0):
      if(not((nome == 'Alberto Montes') or (nome == 'Islam Dulatov') or (nome == 'Kevin Christian') or (nome == 'Seokhyeon Ko'))):
        print(f"✅ {nome} ({response.json()['record']['wins']})")
        f = open("/home/felipe-costa/Documentos/Python/invictos.txt", "a")
        if(nome == "DongHun Choi"):
          f.write(f"{nome} (9)\n")
        else:
          f.write(f"{nome} ({response.json()['record']['wins']})\n")
        f.close()
    else:
      print(f"❌ {nome} ({response.json()['record']['wins']} - {response.json()['record']['losses']})")
  else:
    print(f"⚠️ {nome} (ERRO)")
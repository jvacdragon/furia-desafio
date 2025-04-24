import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
PANDASCORE_TOKEN = os.getenv("PANDASCORE_TOKEN")

headers = {"Authorization": f"Bearer {PANDASCORE_TOKEN}"}

# Buscar partidas da FURIA
url = "https://api.pandascore.co/csgo/matches"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    matches = response.json()
    print(json.dumps(matches, indent=4, ensure_ascii=False))
    for match in matches[:5]: 
        """ if("FURIA" in match['name']): """
        print(f"{match['name']} - {match['begin_at']}")
else:
    print("Erro:", response.status_code, response.text)

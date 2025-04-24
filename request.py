import requests
import json

PANDASCORE_TOKEN = "g2UUe2R5laJNgtNZS4YQl1PF9dR5dGuUnbtvZGzXs7afVInenX4"
headers = {"Authorization": f"Bearer {PANDASCORE_TOKEN}"}

# Buscar partidas da FURIA
url = "https://api.pandascore.co/csgo/matches?filter[opponent.slug]=furia"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    matches = response.json()
    print(json.dumps(matches, indent=4, ensure_ascii=False))
    """ for match in matches[:5]:  # Exibe os 5 primeiros
        print(f"{match['name']} - {match['begin_at']}") """
else:
    print("Erro:", response.status_code, response.text)

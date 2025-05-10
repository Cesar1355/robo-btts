import os
import requests
import time

API_KEY = os.getenv("API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def obter_sinais():
    url = f"https://api.sinaisbtts.com.br/sinais?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def enviar_mensagem(mensagem):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mensagem
    }
    requests.post(url, data=payload)

def main():
    while True:
        sinais = obter_sinais()
        for sinal in sinais:
            mensagem = f"Jogo: {sinal['jogo']}\nHorário: {sinal['horario']}\nSinal: {sinal['sinal']}"
            enviar_mensagem(mensagem)
        time.sleep(3600)  # Aguarda 1 hora antes de buscar novos sinais

if __name__ == "__main__":
    main()

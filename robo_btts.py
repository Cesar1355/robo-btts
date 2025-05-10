import os
import requests
import time
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Sinais simulados
sinais_teste = [
    {"jogo": "Flamengo x Vasco", "horario": "16:00", "sinal": "Ambas Marcam"},
    {"jogo": "Barcelona x Real Madrid", "horario": "18:30", "sinal": "Ambas Marcam"},
    {"jogo": "Liverpool x Chelsea", "horario": "21:00", "sinal": "Ambas Marcam"},
]

def enviar_mensagem(mensagem):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mensagem
    }
    requests.post(url, data=payload)

def main():
    while True:
        agora = datetime.now().strftime("%H:%M:%S")
        for sinal in sinais_teste:
            mensagem = f"[{agora}]\nJogo: {sinal['jogo']}\nHorário: {sinal['horario']}\nSinal: {sinal['sinal']}"
            enviar_mensagem(mensagem)
            time.sleep(3)  # espera 3 segundos entre sinais
        time.sleep(60)  # espera 1 minuto e envia tudo de novo

if __name__ == "__main__":
    main()

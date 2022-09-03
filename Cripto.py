from bs4 import BeautifulSoup  #del módulo bs4, necesitamos BeautifulSoup
import requests
from requests import get
import schedule

"""
def bot_send_text(bot_message):
    
    bot_token = '5594916318:AAHEYFZcD47IvN5Lb1BeufoFvHzMq3_3IlU'
    bot_chatID = '1514482331'
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}'

    response = requests.get(send_text)

    return response
"""

#test_bot = bot_send_text('¡Hola, Telegram!')

def btc_scraping():
    url = requests.get('https://awebanalysis.com/es/coin-details/bitcoin/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('td', {'class': "text-larger text-price"})
    format_result = "El precio actual del Bitcoin es: " + result.text

    return format_result


def report():
    btc_price = f'El precio de Bitcoin es de {btc_scraping()}'
    return btc_price

"""
if __name__ == '__main__':
        
    schedule.every().day.at("21:51").do(report)

    while True:
        schedule.run_pending()
        """















#resp="https://api.telegram.org/bot5594916318:AAHEYFZcD47IvN5Lb1BeufoFvHzMq3_3IlU/getUpdates"
request= get("https://api.telegram.org/bot5594916318:AAHEYFZcD47IvN5Lb1BeufoFvHzMq3_3IlU/getUpdates")

print(request)

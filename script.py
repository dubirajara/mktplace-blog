import sys

import requests


url = 'http://fpcm.es/category/empleo/'

try:
    r = requests.get(url)
    r.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
    sys.exit(1)


# print(len(r.text))


def bot_sendmsg(bot_message):
    # Send text message
    bot_token = '272760357:AAF-iH_BGX5JyvLVWxq260YBpihogOmKyqo'
    bot_chatID = '-233689022'
    send_msg = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}'

    requests.get(send_msg)


with open('log', 'r') as file:
    match = file.read()

if str(len(r.text)) != match:
    message = f'Hola @dalbero, la pagina web {url} ha sido actualizada!!!'
    print(message)
    with open('log', 'w') as file:
        file.write(str(len(r.text)))
    bot_sendmsg(message)

else:
    print('No changes')

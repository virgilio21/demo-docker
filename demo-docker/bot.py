import logging
import requests

from common import config

logging.basicConfig(
    level = logging.INFO, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()

def send_message(token, chat_id, message):
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}')


if __name__ == '__main__':

    telegram_config = config()
    chat_id = telegram_config.get('chat_id')
    token_bot = telegram_config.get('token_bot')

    message_mx = input("¿A que equipo de la liga MX le vas? ")

    try:
        if message_mx == 'america':
            send_message(token_bot, chat_id, '¿Neta le vas al america wey?, ¿de casualidad votaste por el PRI tambien?'.replace(' ', '%20'))
        else:
            send_message(token_bot, chat_id, 'Mientras no sea el odiame más todo bien wey'.replace(' ', '%20'))
    except Exception as e:
        logger.error(f'Ha ocurrido un error: {e}')

    finally:
        logger.info('Se envio un mensaje muy educado al grupo :D')
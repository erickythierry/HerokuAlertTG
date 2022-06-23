# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : fabston                 #
# File Name             : handler.py              #
# ----------------------------------------------- #

from telegram import Bot

import config


def send_alert(data):
    # msg = json.dumps(data, indent=4)
    nomeApp = data['data']['app']['name']
    estado = data['data']['state']
    action = data['action']
    msg = f'__*Alerta*__\n\n*APP:* _{nomeApp}_\n*Estado:* _{estado}_\n*Ação:* _{action}_'
    

    if config.send_telegram_alerts:
        tg_bot = Bot(token=config.tg_token)
        try:
            tg_bot.sendMessage(
                config.chat,
                msg,
                parse_mode='MarkdownV2'
            )
        except KeyError:
            tg_bot.sendMessage(
                config.chat,
                msg
            )
        except Exception as e:
            print("[X] Telegram Erro:\n>", e)
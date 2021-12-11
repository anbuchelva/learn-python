import requests
telegram_token = "<hidden>"
telegram_channel = "<hidden>"


def send_message(message):
    parameters = {
        "chat_id": telegram_channel,
        "text": {message},
        "parse_mode": "Markdown"
    }
    response = requests.get(url=f"https://api.telegram.org/bot{telegram_token}/sendMessage?",
                            params=parameters)
    response.raise_for_status()

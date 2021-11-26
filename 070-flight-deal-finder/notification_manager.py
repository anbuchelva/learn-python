import requests

TELEGRAM_BOT_TOKEN = "<hidden>"
TELEGRAM_CHAT_ID = "@essbasedev"


class NotificationManager():
    def alert(self, alert_message):
        token = TELEGRAM_BOT_TOKEN
        parameters = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": alert_message,
            "parse_mode": "Markdown",
            "disable_notification": True
        }
        response = requests.get(url=f"https://api.telegram.org/bot{token}/sendMessage?",
                                params=parameters)
        print(response.text)
        response.raise_for_status()

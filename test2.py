from donationalerts.asyncio_api import Alert
import requests

alert = Alert("i7xLtifVTseTU3nUCxfZ")

print('Система приёма донатов запущена');

@alert.event()
async def handler(event):
    print(f"{event.username} пожертвовал {event.amount}")
    payload = {'id_user': event.username, 'summ': event.amount}
    requests.get('https://mtchat.site/memecoin_bot/donate.php', params=payload)
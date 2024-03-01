from donationalerts.asyncio_api import Alert
import requests
import sys

sys.stdout.reconfigure(encoding='utf-8')

alert = Alert("i7xLtifVTseTU3nUCxfZ")

print('The donation acceptance system is running');

@alert.event()
async def handler(event):
    print(f"{event.username} donate {event.amount}")
    payload = {'id_user': event.username, 'summ': event.amount}
    requests.get('https://mtchat.site/memecoin_bot/donate.php', params=payload)

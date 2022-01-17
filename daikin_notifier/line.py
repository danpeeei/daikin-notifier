import os
from urllib import parse, request

LINE_ENDPOINT = "https://notify-api.line.me/api/notify"
LINE_API_TOKEN = os.getenv("LINE_API_TOKEN")


def send_message(message: str):
    headers = {
        "Authorization": f"Bearer {LINE_API_TOKEN}",
    }
    data = {"message": message}
    req = request.Request(
        LINE_ENDPOINT, parse.urlencode(data).encode(), headers=headers, method="POST",
    )
    with request.urlopen(req) as res:
        body = res.read()
    print(body)

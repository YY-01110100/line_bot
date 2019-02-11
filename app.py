from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('uSGZIJg2rOwVbgl+kR+v2l6pIcOFaU2gZcrcrgBu2UZOJLviEyetuCuWfCX5P4I8CIXrkFqfZfq6T6qz5+MKULPU5/C1Fz9YEKa8JAXFR4ZQdB4oSHkvSc9LWtjS3ffg1pfo3j3x96SEHl+STUE75wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('58dd37ccf2ab419df2e76ed9a0ee6bff')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我看不懂'

    if msg == 'hi'：
        r = 'hi'
    elif msg == '你吃饭了么'
        r = '还没'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()
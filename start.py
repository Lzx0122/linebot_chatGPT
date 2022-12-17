from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import configparser

import random


# 呼叫爬蟲
from chatGPT import runChatGPT

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')


line_bot_api = LineBotApi(config.get('line-bot', 'tokens'))
handler = WebhookHandler(config.get('line-bot', 'secret'))

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():

    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        print(body, signature)
        handler.handle(body, signature)

    except InvalidSignatureError:

        abort(400)

    return 'OK'



@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    print(event.message.text)
    msg = get_msg(event.message.text)
    print(msg)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg)
    )


def get_msg(input):
    print("test")
    if input[0] == "!":

        if input == "指令":
            msg = "chatGPT\n!<問題>"
            return msg

        return runChatGPT(input[1:len(input)])

    


if __name__ == "__main__":
    app.run()
from flask import Flask
from flask import Flask, request, json
from settings import *
import messageHandler
import vk
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Саня конеченный уебан'

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object']['message'], token)
        return 'ok'
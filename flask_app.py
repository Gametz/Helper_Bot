from flask import Flask
from flask import Flask, request, json
from settings import *
import messageHandler
import vk
import random
import git

app = Flask(__name__)

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('path/to/git_repo')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

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
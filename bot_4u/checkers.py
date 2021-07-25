import vk_api
import requests
import bs4
import datetime
import random
import json
import time
import os.path
import threading
import sys

from bot_4u.config import *

def carcheck(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["car"] == "":
        return "Нет"
    else:
        return ff["car"]

def homecheck(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["home"] == "":
        return "Нет"
    else:
        return ff["home"]

def phonecheck(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["phone"] == "":
        return "Нет"
    else:
        return ff["phone"]

def farmcheck(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["gpu"] == "":
        return "Нет"
    else:
        return ff["gpu"] + " (x" + str(ff["gpu_amount"]) + ")"

def profbancheck(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["banned"] == "NO":
        return "🚫"
    else:
        r = ff["banned"].split(" ")[-1]
        return "✅ | " + r

def ifstaff(id):
    if id in admins or id in moders:
        if id in admins:
            return '✅ | Администратор'
        if id in moders:
            return '✅ | Бета-тестер'
    else:
        return '🚫 | Пользователь'

def lvlchk2(id,lvl):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if lvl <= ff["level"]:
        return "✅"
    else:
        return "⛔"
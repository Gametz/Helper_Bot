import vkapi
import os
import importlib
from command_system import command_list

def load_modules():
   files = os.listdir("mysite/commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])

def get_answer(body):
    message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
    attachment = ''
    for c in command_list:
        if body in c.keys:
            message, attachment = c.process()
    return message, attachment

def create_answer(data, token):
   load_modules()
   user_id = data['from_id']
   message, attachment = get_answer(data['text'].lower())
   vkapi.send_message(user_id, token, message, attachment)
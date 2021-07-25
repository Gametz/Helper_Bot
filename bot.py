# -*- coding: utf-8 -*-
import vk_api
import requests
import bs4
import datetime
import random
import json
import time
import os.path
import threading
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from bot_4u.checkers import *
from bot_4u.config import *
from bot_4u.keyboards import *
from bot_4u.games import *
from bot_4u.hackgame import *
from bot_4u.texts import *
from bot_4u.work import *
from bot_4u.shop import *
from bot_4u.btcshop import *
from bot_4u.btcexchge import *

def res():
    return time.strftime("%x %X", time.localtime())

users = next(os.walk("json/"))[2]

vk = vk_api.VkApi(token=token)
vk._auth_token()

def log(id, body):
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.writelines("\n[" + res() + "] " + str(id) + " " + str(body) + " | Успешно!")
    print("\n[" + res() + "] " + str(id) + " " + str(body) + " | Успешно!")

def prof(id):
    x = {
        "id": id,
        "balance": 1000,
        "bank": 0,
        "btc": 0.0,
        "farm": 0.0,
        "gpu": "",
        "gpu_amount": 0,
        "farmed": 0.0,
        "farming": False,
        "level": 1,
        "exp": 0,
        "nick": "",
        "kwin": 0,
        "klose": 0,
        "mwin": 0,
        "mlose": 0,
        "work": "",
        "wstatus": False,
        "reg": res(),
        "lbonus": 1623869110,
        "car": "",
        "phone": "",
        "home": "",
        "banned": "NO",
        "hlevel": 1,
        "hexp": 0,
        "hhp": 20,
        "hplvl": 1,
        "hdamage": 1,
        "damagelvl": 1,
        "hdef": 1,
        "deflvl": 1,
        "pdamage": 0,
        "php": 0,
        "pdef": 0,
        "hvpn": "",
        "hcomp": "",
        "hsheltr": ""
    }
    try:
        with open('json/' + str(id) + '.json') as f:
            ff = json.loads(f.read())
    except:
        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(x, indent=4))
        vk.method("messages.send", {"peer_id": 419760643,
                                    "message": "💎 Новый пользователь! | vk.com/id" + str(id),
                                    "random_id": random.randint(1, 2147483647)})
        return '💬 Добро пожаловать! Я вижу ты здесь новенький, используй "хелп" для помощи и развлекайся!' \
               '\n💲 А еще,держи свой бонус в размере 1000$\n\n' + prof(str(id))

    return 'Ваш профиль\n\n' + \
           '🔎 id: ' + str(ff["id"]) + \
           '\n📋 Ник: ' + str(ff["nick"]) + \
           '\n💰 Баланс: ' + str(ff["balance"]) + "$" + \
           '\n💳 Банк: ' + str(ff["bank"]) + "$" + \
           '\n💴 Биткоины: ' + str(round(ff["btc"],5)) + "₿" + \
           '\n💼 Работа: ' + str(ff["work"]) + \
           '\n📶 Уровень: ' + str(ff["level"]) + \
           '\n💡 Опыт: ' + str(ff["exp"]) + \
           '\n' \
           '\n🔑 Имущество:' \
           '\n&#12288;🚗 Машина: ' + carcheck(id) + \
           '\n&#12288;🏡 Дом: ' + homecheck(id) +  \
           '\n&#12288;📱 Телефон: ' + phonecheck(id) + \
           '\n&#12288;🎞 Видеокарта: ' + farmcheck(id) + \
           '\n' \
           '\n👔 Вы персонал: ' + ifstaff(id) + \
           '\n⛔ Блокировка: ' + profbancheck(id) + \
           '\n📅 Дата регистрации: ' + str(ff["reg"]) + ver

def dprof(idd):
    idd = ids(idd)
    with open('json/' + str(idd) + '.json') as f:
        ff = json.loads(f.read())
    return 'Ссылка на профиль: vk.com/id' + idd + \
           '\n🔎 id: ' + str(ff["id"]) + \
           '\n📋 Ник: ' + str(ff["nick"]) + \
           '\n💰 Баланс: ' + str(ff["balance"]) + \
           '\n💳 Банк: ' + str(ff["bank"]) + \
           '\n💴 Биткоины: ' + str(ff["btc"]) + \
           '\n📶 Уровень: ' + str(ff["level"]) + \
           '\n💡 Опыт: ' + str(ff["exp"]) + \
           '\n👔 Персонал: ' + ifstaff(int(idd)) + \
           '\n' \
           '\n🔑 Имущество:' \
           '\n&#12288;🚗 Машина: ' + carcheck(idd) + \
           '\n&#12288;🏡 Дом: ' + homecheck(idd) +  \
           '\n&#12288;📱 Телефон: ' + phonecheck(idd) + \
           '\n&#12288;🎞 Видеокарта: ' + farmcheck(idd) + \
           '\n' \
           '\n⛔ Блокировка: ' + profbancheck(idd) + \
           '\n📅 Дата регистрации: ' + str(ff["reg"])

def giveban(id,idd,rsn):
    idd = ids(idd)
    path = "json/"
    f=os.listdir(path)
    for i in range (len(f)):
        f[i] = str(f[i][:-5])
    if idd in f:
        with open('json/' + str(idd) + '.json') as f:
            ff = json.loads(f.read())
        if ff["banned"] == "NO":
            s = str(id) + " " + rsn
            ff["banned"] = s
            with open('json/' + str(idd) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            vk.method("messages.send", {"peer_id": idd,
                                        "message": "⚠ Вы были заблокированы по причине: " + rsn + "\nЕсли не согласны с баном,напишите в репорт",
                                        "random_id": random.randint(1, 2147483647)})
            return "Пользователь успешно заблокирован!"
        else:
            return "Пользователь уже забанен!"
    else:
        return "Такого пользователя не существует!"

def unban(idd):
    idd = ids(idd)
    path = "json/"
    f=os.listdir(path)
    for i in range (len(f)):
        f[i] = str(f[i][:-5])
    if idd in f:
        with open('json/' + str(idd) + '.json') as f:
            ff = json.loads(f.read())
        if ff["banned"] != "NO":
            ff["banned"] = "NO"
            with open('json/' + str(idd) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            vk.method("messages.send", {"peer_id": idd,
                                        "message": "Поздравляю!🎉 Вы были разблокированы!",
                                        "random_id": random.randint(1, 2147483647)})
            return "Пользователь успешно разблокирован!"
        else:
            return "Пользователь не имеет блокировки"
    else:
        return "Такого пользователя не существует!"

def nick(id, nick):
    if len(nick) <= 15:
        with open('json/' + str(id) + '.json', encoding='utf-8') as f:
            ff = json.loads(f.read())
        ff["nick"] = nick
        with open('json/' + str(id) + '.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(ff, indent=4))
        return "Теперь ваш ник: " + nick
    else:
        return "Ваш ник больше 15 символов!"


def dnick(id, nick):
    if len(nick) <= 15:
        with open('json/' + str(id) + '.json') as f:
            ff = json.loads(f.read())
        ff["nick"] = nick
        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(ff, indent=4))
        return "Ник " + id + " теперь: " + str(ff["nick"])
    else:
        return "Ник больше 15 символов!"

def clvl (id, val):
    if int(val) >= 1 and int(val) <= 5:
        with open('json/' + str(id) + '.json') as f:
            ff = json.loads(f.read())
        try:
            ff["level"] = int(val)
        except:
            return "Введите целое число!"
        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(ff, indent=4))
        return "Теперь у вас " + str(ff["level"]) + " уровень"
    else:
        return "Вы ввели значение меньше 1 или больше 5"

def cexp (id, val):
    if int(val) >= 0 and int(val) <= 500:
        with open('json/' + str(id) + '.json') as f:
            ff = json.loads(f.read())
        try:
            ff["exp"] = int(val)
        except:
            return "Введите целое число!"
        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(ff, indent=4))
        return "Теперь у вас " + str(ff["exp"]) + " опыта"
    else:
        return "Вы ввели значение меньше 1 или больше 5"

def bank(id, type, amount):
    with open('json/' + str(id) + '.json', encoding='utf-8') as f:
        ff = json.loads(f.read())

    if type == "положить" and amount == "все" or amount == "всё":
        amount = ff["balance"]
    if type == "снять" and amount == "все" or amount == "всё":
        amount = ff["bank"]
    if type == "положить" and amount == "половину":
        amount = int(ff["balance"] / 2)
    if type == "снять" and amount == "половину":
        amount = int(ff["bank"] / 2)

    if int(amount) > 0 and int(amount) <= ff["balance"] and type == "положить":
        ff["balance"] -= int(amount)
        ff["bank"] += int(amount)
        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(ff, indent=4))
        return "Вы успешно положили " + str(amount) + "$ в банк!"

    elif int(amount) > 0 and int(amount) <= ff["bank"] and type == "снять":
        ff["balance"] += int(amount)
        ff["bank"] -= int(amount)
        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(ff, indent=4))
        return "Вы успешно сняли " + str(amount) + "$ со счёта!"

    else:
        return "Сумма превышает баланс или меньше 0\n" + bal(id)

def bal(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    return '💰Ваш баланс: ' + str(ff["balance"]) + "$\n💴 Биткоины: " + str(round(ff["btc"],5)) + " ₿"

def cbal(id,val):
    if int(val) >= 0 and int(val) <= 1000000:
            with open('json/' + str(id) + '.json') as f:
                ff = json.loads(f.read())
            try:
                ff["balance"] = int(val)
            except:
                return "Введите целое число!"

            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Теперь ваш баланс: " + str(ff["balance"])
    else:
        return "Вы ввели значение меньше нуля или больше 1 000 000"

def dbal (idd,val):
    idd = ids(idd)
    if int(val) >= 0 and int(val) <= 1000000000:
        with open('json/' + str(idd) + '.json') as f:
            ff = json.loads(f.read())
        try:
            ff["balance"] = int(val)
        except:
            return "Введите целое число!"

        with open('json/' + str(idd) + '.json', 'w') as f:
            f.write(json.dumps(ff, indent=4))
        return "Теперь баланс " + idd + ": " + str(ff["balance"])
    else:
        return "Вы ввели значение меньше нуля или больше 1 000 000 000"

def cbtc (id, val):
    if float(val) >= 0 and float(val) <= 5000:
        with open('json/' + str(id) + '.json') as f:
            ff = json.loads(f.read())
        ff["btc"] = round(float(val),5)
        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(ff, indent=4))
        return "Теперь у вас " + str(ff["btc"]) + "₿"
    else:
        return "Вы ввели значение меньше нуля или больше 5000"

def pay(id, idd, val):
    idd = ids(idd)
    if str(id) == str(idd):
        return "🙃 Нельзя переводить самому себе!"
    with open('json/' + str(id) + '.json', encoding='utf-8') as f:
        per = json.loads(f.read())
    try:
        with open('json/' + str(idd) + '.json', encoding='utf-8') as f:
            pol = json.loads(f.read())
    except:
        return "Такого пользователя не существует!"

    if int(val) > 0 and int(val) <= per["balance"]:
        per["balance"] -= int(val)
        pol["balance"] += int(val)
        with open('json/' + str(id) + '.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(per, indent=4))
        with open('json/' + str(idd) + '.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(pol, indent=4))
        if per["nick"] != '':
            vk.method("messages.send", {"peer_id": idd,
                                "message": "💎 | Вы получили перевод от " + "@id" + str(id) + " (" + ff["nick"] + ")" + " в размере: " + val + "$",
                                "random_id": random.randint(1, 2147483647)})
        else:
            user = vk.method("users.get", {"user_ids": id})
            vk.method("messages.send", {"peer_id": idd,
                                "message": "💎 | Вы получили перевод от " + "@id" + str(id) + " (" + user[0]['first_name'] + ") в размере: " + val + "$",
                                "random_id": random.randint(1, 2147483647)})
        return "Перевод успешно выполнен! \nВаш баланс: " + str(per["balance"]) + "$"
    else:
        return "Сумма превышает ваш баланс или Сумма меньше 0\n" + bal(id)

def ulist():
    c=1
    path = "json/"
    f=os.listdir(path)
    for i in range (len(f)):
        f[i] = '[' + str(c) + '] ' + "vk.com/id" + str(f[i][:-5])
        c += 1
    a = '\n'.join(f)
    return "Список пользователей\n\n" + a

def getanekdot():
    z = ''
    s = requests.get('http://anekdotme.ru/random')
    b = bs4.BeautifulSoup(s.text, "html.parser")
    p = b.select('.anekdot_text')
    for x in p:
        s = (x.getText().strip())
        z = z + s + '\n\n'
    return s

def stats2(nick, idd):
    url = "https://call-of-duty-modern-warfare.p.rapidapi.com/multiplayer/" + nick + "%23" + idd + "/battle"

    headers = {
        'x-rapidapi-key': "3d7ffcf6eemsheb0b038baa4b97ep118126jsnd220b4b88e25",
        'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com",
    }
    time.sleep(1)
    response = requests.request("GET", url, headers=headers)
    r = str(response.text).split(",")
    p=["level", "levelXpRemainder", "levelXpGained", "prestige"]
    a=[]
    b=[]
    c=0
    for i in range (len(r)):
        for j in range(len(p)):
            if p[j] in r[i+c] and p[j] not in a:
                a.append(i)
                ++c
                break
    a = a[0:(len(p))]
    a = list(map(int, a))
    for i in range (len(a)):
        b.append(r[a[i]])
    if len(r) > 3:
        #level
        lvl = "\n🏷Уровень: " + b[0][8:]
        #prestige
        pr = "\n🔰Престиж: " + b[3][11:]
        #lvlxp
        lvlxp = "\n📋Прогресс уровня: " + b[1][19:] + "/" + b[2][16:] + "\n"
        stat2 = lvl + pr + lvlxp
        return stat2
    else:
        return 0

def stats(nick, idd):
    url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone/" + nick + "%23" + idd + "/battle"

    headers = {
        'x-rapidapi-key': "3d7ffcf6eemsheb0b038baa4b97ep118126jsnd220b4b88e25",
        'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers)
    r = str(response.text).split(",")

    if len(r) > 3:
        # WINS
        wins = "\n🎉Побед: " + r[0][14:999]
        # KILLS
        kills = "\n🥴Убийств: " + r[1][8:999]
        # KD
        kd = "\n📈К/Д: " + r[2][10:14]
        # DEATHS
        deaths = "\n☠Смертей: " + r[15][9:999]
        # top25
        top25 = "\n2️⃣5️⃣Топ-25: " + r[4][16:999]
        # top10
        top10 = "\n1️⃣0️⃣Топ-10: " + r[5][9:999]
        # contracts
        contracts = "\n🎟Контракты: " + r[6][12:999]
        # revives
        revives = "\n➕Поднятий: " + r[7][10:999]
        # DOWNS
        downs = "\n🔻Нокдауны: " + r[3][8:999]
        # top5
        top5 = "\n5️⃣Топ-5: " + r[8][10:999]
        # matches
        matches = "\n\n⌨Всего игр: " + r[11][14:999]
        # score
        score = "\n💡Всего EXP: " + r[9][8:999]
        # scorePM
        spm = r[13][17:999]
        sppm = round(float(spm))
        scorePM = "\n🎛EXP в минуту: " + str(sppm)
        # timeplayed
        ttt = (datetime.timedelta(seconds=int(r[10][13:999])))
        totaltime = "\n💻Всего отыграно времени: " + str(ttt)
        # avgkills
        avgk = int(r[1][8:999]) / int(r[11][14:999])
        avgkills = "\n😵Ср.Убийств: " + str(round(avgk, 2))
        stat = "📊Статистика " + nick + "#" + idd + matches + "\n" + kills + avgkills + "\n" + downs + revives + "\n" + deaths + "\n" + kd + "\n" + wins + "\n" + score + scorePM + contracts + "\n" + stats2(nick, idd) + top5 + top10 + top25 + "\n" + totaltime + "\n\nby @gamtz" + ver
        vk.method("messages.send", {"peer_id": id, "message": stat, "random_id": random.randint(1, 2147483647)})
    else:
        vk.method("messages.send", {"peer_id": id,
                                    "message": "⚠Ошибка! Проверьте ник и id⚠\nТакже проверьте настройки "
                                               "приватности.\nПодробности в статье: vk.com/@cod_stats-help",
                                    "random_id": random.randint(1, 2147483647)})

def stats20(nick, idd):
    a = []
    p = ["kills", "headshots", "killsPerGame", "headshotPercentage", "objectiveTeamWiped", "assists", "deaths",
         "kdRatio", "score", "scorePerMinute", "gulagKills", "gulagDeaths", "damageDone", "damageTaken",
         "distanceTraveled", "avgLifeTime", "timePlayed"]
    url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone-matches/" + nick + "%23" + idd + "/battle"
    headers = {
        'x-rapidapi-key': "3d7ffcf6eemsheb0b038baa4b97ep118126jsnd220b4b88e25",
        'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    r = str(response.text).split(",")
    c = 0
    for i in range(len(r)):
        for j in range(len(p)):
            if p[j] in r[i + c] and p[j] not in a:
                a.append(i)
                var = ++c
                break
    a = a[0:(len(p))]
    a = list(map(int, a))
    if len(r) > 3:
        #    kills
        kills = "\n\n🥴Убийств: " + r[a[0]][27:999]
        #    fsquad
        fsquad = "\n👥Сквадов уничтожено: " + r[a[1]][21:999]
        #    avglife
        if round(float(r[a[2]][14:999])) > 0:
            avgl = round(float(r[a[2]][14:999]))
            avglife = "\n⌛Среднее время жизни: " + str((datetime.timedelta(seconds=int(avgl))))
        else:
            avglife = "\n⌛Среднее время жизни: " + "⚠Cыграйте больше игр⚠"
        #    score
        score = "\n💡Всего exp: " + r[a[3]][8:999]
        #    hs
        hs = "\n💀Убийства в голову: " + r[a[4]][12:999]
        #    assists
        assists = "\n♻Помощи: " + r[a[5]][10:999]
        #    avgkills
        avgkills = "\n😵Ср.убийств: " + r[a[6]][15:999]
        #    scorepm
        if round(float(r[a[7]][17:999])) > 0:
            scorepm = "\n🎛Exp в минуту: " + str(round(float(r[a[7]][17:999])))
        else:
            scorepm = "\n🎛Exp в минуту: " + "⚠Cыграйте больше игр⚠"
        #    distance
        distance = "\n🗺Пройденная дистанция: " + str(round(float(r[a[8]][19:999]) / 100000))
        #    deaths
        deaths = "\n☠Смертей: " + r[a[9]][9:999]
        #    kd
        kd = "\n📈К/Д: " + str(round(float(r[a[10]][10:999]), 2))
        #    gulagdeaths
        gdeaths = "\n🕳Смертей в гулаге: " + r[a[11]][14:999]
        #    totaltime
        if round(float(r[a[12]][13:999])) > 0:
            tt = round(float(r[a[12]][13:999]))
            totaltime = "\n💻Всего отыграно времени: " + str((datetime.timedelta(seconds=int(tt))))
        else:
            totaltime = "\n💻Всего отыграно времени: " + "⚠Cыграйте больше игр⚠"
        #    hsper
        hsper = "\n🧠Процент убийств в голову: " + str(round(float(r[a[13]][21:999]), 2))
        #    gulagkills
        gkills = "\n👮Убийств в гулаге: " + r[a[14]][13:999]
        #    damagegive
        gdamage = "\n🔫Нанесено урона: " + r[a[15]][13:999]
        #    damagetaken
        td = r[a[16]].split("}")
        tdamage = "\n🥊Получено урона: " + td[0][14:999]
        #   gulagkd
        gkd = "\n📊Гулаг К/Д: " + str(round(float(int(gkills[20:999]) / int(gdeaths[20:999])), 2))

        stat20 = "📊статистика " + nick + "#" + idd + " за последние 20 матчей" + kills + hs + avgkills + hsper + fsquad + "\n" + assists + "\n" + deaths + "\n" + kd + "\n" + score + scorepm + "\n" + gkills + gdeaths + gkd + "\n" + gdamage + tdamage + "\n" + distance + avglife + totaltime + "\n\nby @gamtz" + ver
        vk.method("messages.send", {"peer_id": id, "message": stat20, "random_id": random.randint(1, 2147483647)})
    else:
        vk.method("messages.send", {"peer_id": id,
                                    "message": "⚠Ошибка! Проверьте ник и id⚠\nТакже проверьте настройки приватности.\nПодробности в статье: vk.com/@cod_stats-help",
                                    "random_id": random.randint(1, 2147483647)})

def uplf(iddd, purl):
    global d
    p = requests.get(purl[1])
    out = open("films/" + iddd + ".jpg", "wb")
    out.write(p.content)
    out.close()

    a = vk.method("photos.getMessagesUploadServer")
    b = requests.post(a['upload_url'], files={'photo': open('films/' + iddd + '.jpg', 'rb')}).json()
    c = vk.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
    d = "photo{}_{}".format(c["owner_id"], c["id"])

def rfilm():
    global iddd
    iddd = str(random.randrange(1, 99999))
    url = 'https://kinopoiskapiunofficial.tech/api/v2.1/films/' + iddd
    headers = {
        'X-API-KEY': '79e32931-ef2c-4921-9e01-dac1d164971b',
    }
    response = requests.get(url, headers=headers)
    r = str(response.text).split(",")
    p=["nameRu", "webUrl", "posterUrl", "posterUrlPreview", "year"]
    a=[]
    b=[]
    c=0
    for i in range(len(r)):
        for j in range(len(p)):
            if p[j] in r[i+c] and p[j] not in a:
                a.append(i)
                ++c
                break
    a = a[0:(len(p))]
    a = list(map(int, a))
    for i in range(len(a)):
        b.append(r[a[i]])
    #
    name = 'Название: ' + b[0][9:]
    #
    kkurl = (b[1][9:]).split('"')
    kurl = 'Ссылка на Кинопоиск: ' + kkurl[1]
    #
    purl = (b[2][12:]).split('"')
    #
    year = 'Год выпуска: ' + (b[4][7:])
    res = name + "\n" + year + '\n' + kurl
    uplf (iddd, purl)
    return (res)

def lvlcheck(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())

    if ff["exp"] > 50 and ff["level"] == 1:
        ff["level"] = 2
        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(ff, indent=4))
        vk.method("messages.send", {"peer_id": id,
                                "message": "💎 Поздравляю! Вы повысили свой уровень до " + str(ff["level"]),
                                "random_id": random.randint(1, 2147483647)})
        return

    if ff["exp"] > 150 and ff["level"] == 2:
        ff["level"] = 3
        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(ff, indent=4))
        vk.method("messages.send", {"peer_id": id,
                                "message": "💎 Поздравляю! Вы повысили свой уровень до " + str(ff["level"]),
                                "random_id": random.randint(1, 2147483647)})
        return

    if ff["exp"] > 300 and ff["level"] == 3:
        ff["level"] = 4
        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(ff, indent=4))
        vk.method("messages.send", {"peer_id": id,
                                "message": "💎 Поздравляю! Вы повысили свой уровень до " + str(ff["level"]),
                                "random_id": random.randint(1, 2147483647)})
        return

    if ff["exp"] >= 500 and ff["level"] == 4:
        ff["level"] = 5
        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(ff, indent=4))
        vk.method("messages.send", {"peer_id": id,
                                "message": "💎 Поздравляю! Вы повысили свой уровень до " + str(ff["level"]),
                                "random_id": random.randint(1, 2147483647)})
        return

def works(id):

    s= "Список работ:" \
           "\n\n" \
           + str(lvlchk2(id,1)) + " 1 уровень" \
           "\n&#12288;1) 🚕 FakeTAXI - 100$ | 20 секунд | 2 опыта" \
           "\n&#12288;2) 👨‍🌾 Ферма - 180$ | 40 секунд | 4 опыта" \
           "\n\n" \
           + str(lvlchk2(id,2)) + " 2 уровень" \
           "\n&#12288;3) 💻 Тестировщик игр - 420$ | 1 минута | 6 опыта" \
           "\n&#12288;4) ☕ Работник кофейни - 600$ | 1:30 минуты | 9 опыта" \
           "\n\n" \
           + str(lvlchk2(id,3)) + " 3 уровень" \
           "\n&#12288;5) 🏭 Рабочий на заводе - 1 080$ | 2 минуты | 12 опыта" \
           "\n&#12288;6) 🍷 Дегустатор вина - 1 600$ | 3 минуты | 18 опыта" \
           "\n\n" \
           + str(lvlchk2(id,4)) + " 4 уровень" \
           "\n&#12288;7) 💨 Продавец в Verdax - 3 600$ | 5 минут | 30 опыта" \
           "\n&#12288;8) 🌸 Дизайнер - 7 000$ | 10 минут | 60 опыта" \
           "\n\n" \
           + str(lvlchk2(id,5)) + " 5 уровень" \
           "\n&#12288;9) 🍥 Режиссёр Аниме - 18 000$ | 20 минут" \
           "\n&#12288;10) 👽 Директор Natflex - 36 000$ | 40 минут" \
           "\n\n" \
           "\nЧтобы устроиться на работу 'устроиться {номер}'"
    return s

def work(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())

    if ff["wstatus"] == False:
        if ff["work"] != "":
            if ff["level"] >= 1:
                if ff["work"] == "FakeTAXI":
                    work = 1
                    ff["wstatus"] = True
                    threading.Timer(20.0, workend, args=(id, work,)).start()
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    return "✅ Вы начали работать в FakeTAXI! \nЗакончите через 20 секунд"

                if ff["work"] == "Ферма":
                    ff["wstatus"] = True
                    work = 2
                    threading.Timer(40.0, workend, args=(id, work,)).start()
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    return "✅ Вы начали работать на Ферме! \nЗакончите через 40 секунд"

            if ff["level"] >= 2:
                if ff["work"] == "Тестировщик игр":
                    ff["wstatus"] = True
                    work = 3
                    threading.Timer(60.0, workend, args=(id, work,)).start()
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    return "✅ Вы начали работать Тестировщиком игр! \nЗакончите через 1 минуту"

                if ff["work"] == "Работник кофейни":
                    ff["wstatus"] = True
                    work = 4
                    threading.Timer(90.0, workend, args=(id, work,)).start()
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    return "✅ Вы начали работать в кофейне! \nЗакончите через 1:30 минуты"
            else:
                return "У вас слишком маленький уровень! \nНеобходим: 2\nВаш уровень: " + str(ff["level"])

            if ff["level"] >= 3:
                if ff["work"] == "Рабочий на заводе":
                    ff["wstatus"] = True
                    work = 5
                    threading.Timer(120.0, workend, args=(id, work,)).start()
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    return "✅ Вы начали работать на Заводе! \nЗакончите через 2 минуты"

                if ff["work"] == "Дегустатор вина":
                    ff["wstatus"] = True
                    work = 6
                    threading.Timer(180.0, workend, args=(id, work,)).start()
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    return "✅ Вы начали работать Дегустатором вина! \nЗакончите через 3 минуты"
            else:
                return "У вас слишком маленький уровень! \nНеобходим: 3\nВаш уровень: " + str(ff["level"])

            if ff["level"] >= 4:
                if ff["work"] == "Продавец в Verdax":
                    ff["wstatus"] = True
                    work = 7
                    threading.Timer(300.0, workend, args=(id, work,)).start()
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    return "✅ Вы начали работать продавцом в Verdax'e! \nЗакончите через 5 минут"

                if ff["work"] == "Дизайнер":
                    ff["wstatus"] = True
                    work = 8
                    threading.Timer(600.0, workend, args=(id, work,)).start()
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    return "✅ Вы начали работать Дизайнером! \nЗакончите через 10 минут"
            else:
                return "У вас слишком маленький уровень! \nНеобходим: 4\nВаш уровень: " + str(ff["level"])

            if ff["level"] >= 5:
                if ff["work"] == "Режиссёр Аниме":
                    ff["wstatus"] = True
                    work = 9
                    threading.Timer(1200.0, workend, args=(id, work,)).start()
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    return "✅ Вы начали работать Режиссёром Аниме! \nЗакончите через 20 минут"

                if ff["work"] == "Директор Natflex":
                    ff["wstatus"] = True
                    work = 10
                    threading.Timer(2400.0, workend, args=(id, work,)).start()
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    return "✅ Вы начали работать Директором Natflex'a! \nЗакончите через 40 минут"
            else:
                return "⚠ У вас слишком маленький уровень! \nНеобходим: 5\nВаш уровень: " + str(ff["level"])
        else:
            return "⚠ Вы не устроены на работу!\nСписок работ: 'работы'"
    else:
        return "⚠ Вы уже работаете!"

def workend(id,work):
    work = str(work)
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if work == "1":
        slr = 100
        exp = 2
    if work == "2":
        slr = 180
        exp = 4
    if work == "3":
        slr = 420
        exp = 6
    if work == "4":
        slr = 600
        exp = 9
    if work == "5":
        slr = 1080
        exp = 12
    if work == "6":
        slr = 1600
        exp = 18
    if work == "7":
        slr = 3600
        exp = 30
    if work == "8":
        slr = 7000
        exp = 60
    if work == "9":
        slr = 18000
        exp = 0
    if work == "10":
        slr = 36000
        exp = 0
    print(slr)
    ff["wstatus"] = False
    ff["balance"] += slr
    if ff["level"] < 5:
        ff["exp"] += exp
    with open('json/' + str(id) + '.json', 'w') as f:
        f.write(json.dumps(ff, indent=4))
    lvlcheck(id)
    if work == "9" or work == "10":
        vk.method("messages.send", {"peer_id": id,
                                    "message": "💎 Вы закончили работу!\nВам начислена зарплата в размере: \n" + str(
                                        slr) + "$",
                                    "random_id": random.randint(1, 2147483647)})
    else:
        vk.method("messages.send", {"peer_id": id,
                                    "message": "💎 Вы закончили работу!\nВам начислена зарплата в размере: \n" + str(slr) + "$" + " и " + str(exp) + " опыта",
                                    "random_id": random.randint(1, 2147483647)})

def report(id, msg):
    if len(msg) <= 100:
        vk.method("messages.send", {"peer_id": 419760643,
                                    "message": "⚠ Репорт | vk.com/gim196468884?sel=" + id + " | " + msg,
                                    "random_id": random.randint(1, 2147483647)})
        return "✅ Репорт отправлен!"
    else:
        return "⚠ Ваш репорт превышает 100 символов"

def cgbonus(id):
    vk.method("messages.send", {"peer_id": id,
                                "message": "💎 Вам снова доступен бонус!\nИспользуйте 'бонус', чтобы получить его",
                                "keyboard": bonusmenu.get_keyboard(),
                                "random_id": random.randint(1, 2147483647)})

def gbonus(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    o = (int(time.time()) - (ff["lbonus"] + 300)) * -1
    if (int(time.time())) - ff["lbonus"] >= 300:
        ff["balance"] += 300
        ff["lbonus"] = int(time.time())
        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(ff, indent=4))
        threading.Timer(300.0, cgbonus, args=(id,)).start()
        vk.method("messages.send", {"peer_id": id,
                                    "sticker_id": 8484,
                                    "random_id": random.randint(1, 2147483647)})
        return "💎 Вы получили бонус в размере 300$!\nВаш баланс: " + str(ff["balance"]) + "$"
    else:
        return "Бонус можно получать раз в 5 минут!\nВозвращайтесь через " + str(o) + " секунд"

def idsearch(id):
    path = "json/"
    f=os.listdir(path)
    for i in range (len(f)):
        f[i] = str(f[i][:-5])
    id_ = id.split('/')[-1]
    try:
        id = str(vk.method('users.get', {'user_ids': id_})[0]['id'])
    except:
        return "Пример использования:\nид vk.com/gamtz"
    if id in f:
        try:
            return "👤 ID пользователя: " + id + "\n👔 Персонал: " + ifstaff(int(id))
        except:
            return "Пример использования:\nид vk.com/gamtz"
    else:
        return "Такого пользователя не существует!"

def ids(id):
    path = "json/"
    f = os.listdir(path)
    for i in range(len(f)):
        f[i] = str(f[i][:-5])
    if "@" in id:
        id_ = id.split('@')[-1][:-1]
    else:
        id_ = id.split('/')[-1]
    try:
        id = str(vk.method('users.get', {'user_ids': id_})[0]['id'])
    except:
        return "USER GET ERROR"
    if id in f:
        try:
            return id
        except:
            return "USER NOT EXIST"

def congrts(id):
    vk.method("messages.send", {"peer_id": id,
                                "sticker_id": 11788,
                                "random_id": random.randint(1, 2147483647)})
# Bytecoin
#магазин

def farmstatus(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    return "Состояние вашей фермы:" \
           "\n" \
           "\n&#12288;📄 Видеокарты: " + farmcheck(id) + \
           "\n&#12288;🔋 Добыча: " + str(ff["farm"] * ff["gpu_amount"]) + " ₿ / 5 мин" + \
           "\n&#12288;💴 Добыто в биткоинах: " + str(round(ff["farmed"] * ff["gpu_amount"],5)) + " ₿" + \
           "\n&#12288;💵 Добыто в долларах: " + str(int(ff["farmed"] * 10000 * ff["gpu_amount"])) + " $" + \
           "\n" \
           "\n📌 Для снятия используйте 'сбитки'" \
#магазин

def sellbtc(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())

    if ff["farmed"] != 0.0:
        temp = str(round(ff["farmed"],5))

        ff["farmed"] = 0.0
        ff["btc"] += float(temp)

        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(ff, indent=4))

        return "💱 Вы успешно перевели " + temp + " на основной счет"\
        "\n💴 Ваш баланс: " + str(ff["btc"])  + " ₿"
    else:
        return "У вас нет накопившихся ₿"

def btcfarm(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    ff["farmed"] += ff["farm"] * ff["gpu_amount"]
    ff["farm"] = round(ff["farm"] * ff["gpu_amount"],5)
    with open('json/' + str(id) + '.json', 'w') as f:
        f.write(json.dumps(ff, indent=4))
    threading.Thread(target=btcfarmstart, args=(id,)).start()
    return 0

def btcfarmstart(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    threading.Timer(300.0, btcfarm, args=(id,)).start()
    return 0

def btcfarmreload():
    path = "json/"
    f=list(os.listdir(path))
    for i in range (len(f)):
        f[i] = str(f[i][:-5])
    for i in range (len(f)):
        id = f[i]
        btcfarmstart(id)
    return 0

# Bytecoin

# Топ
def sortbybal(str):
    a = int(str.split(":")[0])
    return a

def sortbybtc(str):
    a = float(str.split(":")[0])
    return a

def baltop():
    a=[]
    path = "json/"
    f=list(os.listdir(path))
    for i in range (len(f)):
        f[i] = str(f[i][0:-5])
    for i in f:
        id = i
        with open('json/' + str(id) + '.json') as f:
            ff = json.loads(f.read())
        if ff["balance"] != 0:
            if ff["nick"] != "":
                a.append(str(str(ff["balance"]) + ":" + "@id" + str(id) + " (" + ff["nick"] + ")"))
            else:
                user = vk.method("users.get", {"user_ids": id})
                a.append(str(str(ff["balance"]) + ":" + "@id" + str(id) + " (" + user[0]['first_name'] + ")"))
    a = sorted(a, key=sortbybal, reverse=True)
    for i in range(len(a)):
            a[i] = str(i+1) + ". " + str(a[i].split(":")[1]) + " | " + str(a[i].split(":")[0]) + "$"
    threading.Thread(target=reloadtop, args=()).start()
    global topbal
    topbal = "📜 Топ по балансу:\n\n" + "\n".join(a) + "\n\nОбновление каждые 5 минут"

def btctop():
    a=[]
    path = "json/"
    f=list(os.listdir(path))
    for i in range (len(f)):
        f[i] = str(f[i][0:-5])
    for i in f:
        id = i
        with open('json/' + str(id) + '.json') as f:
            ff = json.loads(f.read())
        if ff["btc"] != 0.0:
            if ff["nick"] != "":
                a.append(str(str(ff["btc"]) + ": " + "@id" + str(id) + " (" + ff["nick"] + ")"))
            else:
                user = vk.method("users.get", {"user_ids": id})
                a.append(str(str(ff["btc"]) + ": " + "@id" + str(id) + " (" + user[0]['first_name'] + ")"))
    a = sorted(a, key=sortbybtc, reverse=True)
    for i in range(len(a)):
            a[i] = str(i+1) + ". " + str(a[i].split(":")[1]) + " | " + str(round(float(a[i].split(":")[0]),5)) + "₿"
    global topbtc
    topbtc = "📜 Топ по биткоинам:\n\n" + "\n".join(a) + "\n\nОбновление каждые 5 минут"
    threading.Thread(target=reloadtopbtc, args=()).start()

def reloadtop():
    threading.Timer(300.0, baltop, args=()).start()

def reloadtopbtc():
    threading.Timer(300.0, btctop, args=()).start()
# Топ

def mailing(body):
    path = "json/"
    f = list(os.listdir(path))
    for i in range(len(f)):
        f[i] = str(f[i][0:-5])
    for i in f:
        id = i
        vk.method("messages.send", {"peer_id": id,
                                    "message": body,
                                    "random_id": random.randint(1, 2147483647)})
    return "Рассылка завершена!"


btcfarmreload()
baltop()
btctop()
# btcratestart()

print("[" + res() +"] ✅Бот запущен!")
log("system", "Бот запущен")
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1 and messages["items"][0]["conversation"]["peer"]["type"] == 'user':
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            c = 1
            path = "json/"
            u = os.listdir(path)
            for i in range(len(u)):
                u[i] = str(u[i][:-5])
                c += 1
            if str(id) not in u:
                vk.method("messages.send", {"peer_id": id,
                                            "message": prof(id) + "\n\n💎 Добро пожаловать в главное меню",
                                            "keyboard": mainmenu.get_keyboard(),
                                            "random_id": random.randint(1, 2147483647)})

            with open('json/' + str(id) + '.json') as f:
                ff = json.loads(f.read())

            allow = ["репорт", "профиль", "проф", "unban"]
            if True and str(body) != "":
                    print(id, body)
                    if ff["banned"] == "NO" or body.lower().split(" ")[0] in allow:
                        if str(body.lower()).split()[0] == 'репорт':
                            temp = str(body.lower()).split("репорт")
                            msg = temp[1]
                            if len(msg) > 1:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": report(str(id), msg),
                                                            "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "⚠ Вы пытаетесь отправить пустой репорт!",
                                                            "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif str(body.lower()).split()[0] == "toall":
                            if id in admins:
                                temp = str(body).split("toall")[1]
                                vk.method("messages.send", {"peer_id": id,
                                                        "message": mailing(temp),
                                                        "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                        "message": "Вы не Администратор!",
                                                        "random_id": random.randint(1, 2147483647)})

                        # Меню
                        elif body.lower() == "🏠 главное меню":
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": "💎 Добро пожаловать в главное меню",
                                                    "keyboard": mainmenu.get_keyboard(),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == "начать" or body.lower() == "start":
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": "Удачи в развитии!",
                                                    "keyboard": mainmenu.get_keyboard(),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)
                        # Меню

                        elif body.lower() == 'пинг':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": "Не Миша,всё хуйня! Давай по новой!",
                                                        "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == 'хелп' or body.lower() == 'помощь' or body.lower() == 'команды':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": help(),
                                                        "keyboard": mainmenu.get_keyboard(),
                                                        "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == 'пхелп':
                            if id in admins or id in moders:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": staffhelp(),
                                                            "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Вы не Администратор или Модератор!",
                                                            "random_id": random.randint(1, 2147483647)})

                        elif body.lower() == 'админпанель':
                            if id in admins or id in moders:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Ну раз тебе так хочется,то на",
                                                            "keyboard": adminmenu.get_keyboard(),
                                                            "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Вы не Администратор или Модератор!",
                                                            "random_id": random.randint(1, 2147483647)})

                        elif body.lower() == 'профиль' or body.lower() == 'проф':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": prof(id),
                                                        "keyboard": mainmenu.get_keyboard(),
                                                        "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == 'баланс' or body.lower() == 'бал':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": bal(id),
                                                        "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == 'стата':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": gstats(id),
                                                        "keyboard": mainmenu.get_keyboard(),
                                                        "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == "анекдот":
                            vk.method("messages.send",
                                      {"peer_id": id, "message": getanekdot(), "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif str(body.lower()).split()[0] == 'кстата':
                            if len(str(body).split()) == 3:
                                temp = str(body).split(" ")
                                nick = temp[1]
                                idd = temp[2]
                                stats(nick, idd)
                                log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "⚠Для показа статистики введите ник и id Battle.net через пробел. Пример: кстата Vlad 214228⚠",
                                                            "random_id": random.randint(1, 2147483647)})

                        elif str(body.lower()).split()[0] == 'кстат20':
                            if len(body.split(" ")) == 3:
                                temp = str(body).split(" ")
                                nick = temp[1]
                                idd = temp[2]
                                stats20(nick, idd)
                                log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "⚠Для показа статистики введите ник и id Battle.net через пробел. Пример: кстат20 Vlad 214228⚠",
                                                            "random_id": random.randint(1, 2147483647)})

                        elif str(body.lower()).split()[0] == 'сбал':
                            if id in admins or id in moders:
                                if len(str(body).split()) == 2:
                                    temp = str(body).split(" ")
                                    val = temp[1]
                                    vk.method("messages.send", {"peer_id": id,
                                                            "message": cbal(id,val),
                                                            "random_id": random.randint(1, 2147483647)})
                                    log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Вы не Администратор или Модератор!",
                                                            "random_id": random.randint(1, 2147483647)})

                        elif str(body.lower()).split()[0] == 'дбал':
                            if id in admins:
                                if len(str(body).split()) == 3:
                                    temp = str(body).split(" ")
                                    val = temp[2]
                                    idd = temp[1]
                                    vk.method("messages.send", {"peer_id": id,
                                                                "message": dbal(idd, val),
                                                                "random_id": random.randint(1, 2147483647)})
                                    log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Вы не Администратор!",
                                                            "random_id": random.randint(1, 2147483647)})

                        elif str(body.lower()).split()[0] == 'дпроф':
                            if id in admins or id in moders:
                                if len(str(body).split()) == 2:
                                    temp = str(body).split(" ")
                                    idd = temp[1]
                                    vk.method("messages.send", {"peer_id": id,
                                                            "message": dprof(idd),
                                                            "random_id": random.randint(1, 2147483647)})
                                    log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Вы не Администратор или Модератор!",
                                                            "random_id": random.randint(1, 2147483647)})

                        elif str(body.lower()).split()[0] == 'сбитк':
                            if id in admins or id in moders:
                                if len(str(body).split()) == 2:
                                    temp = str(body).split(" ")
                                    val = temp[1]
                                    vk.method("messages.send", {"peer_id": id,
                                                            "message": cbtc(id, val),
                                                            "random_id": random.randint(1, 2147483647)})
                                    log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Вы не Администратор или Модератор!",
                                                            "random_id": random.randint(1, 2147483647)})

                        elif str(body.lower()).split()[0] == 'слвл':
                            if id in admins or id in moders:
                                if len(str(body).split()) == 2:
                                    temp = str(body).split(" ")
                                    val = temp[1]
                                    vk.method("messages.send", {"peer_id": id,
                                                            "message": clvl(id, val),
                                                            "random_id": random.randint(1, 2147483647)})
                                    log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Вы не Администратор или Модератор!",
                                                            "random_id": random.randint(1, 2147483647)})

                        elif str(body.lower()).split()[0] == 'сопыт':
                            if id in admins or id in moders:
                                if len(str(body).split()) == 2:
                                    temp = str(body).split(" ")
                                    val = temp[1]
                                    vk.method("messages.send", {"peer_id": id,
                                                            "message": cexp(id, val),
                                                            "random_id": random.randint(1, 2147483647)})
                                    log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Вы не Администратор или Модератор!",
                                                            "random_id": random.randint(1, 2147483647)})

                        elif body.lower() == 'пoлная накрутка':
                            if id in admins or id in moders:
                                with open('json/' + str(id) + '.json') as f:
                                    ff = json.loads(f.read())
                                cbal(id, "1000000")
                                cbtc(id, "5000.0")
                                clvl(id, "5")
                                cexp(id, "500")
                                ff["balance"] = 1000000
                                ff["bank"] = 1000000
                                ff["car"] = "Tesla model S"
                                ff["home"] = "Личный остров со шлюхами"
                                ff["phone"] = "iPhone 12 Gold Edition"
                                ff["gpu"] = "nVidia Tesla A100"
                                ff["farming"] = True
                                ff["gpu_amount"] = 5
                                ff["farm"] = 0.1
                                with open('json/' + str(id) + '.json', 'w') as f:
                                    f.write(json.dumps(ff, indent=4))
                                vk.method("messages.send", {"peer_id": id,
                                                        "message": "Накрутка завершена!",
                                                        "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Вы не Администратор или Модератор!",
                                                            "random_id": random.randint(1, 2147483647)})
                        elif body.lower() == 'oбнуление':
                            if id in admins or id in moders:
                                with open('json/' + str(id) + '.json') as f:
                                    ff = json.loads(f.read())
                                cbal(id, "1000")
                                cbtc(id, "0.0")
                                clvl(id, "1")
                                cexp(id, "0")
                                ff["balance"] = 0
                                ff["bank"] = 0
                                ff["car"] = ""
                                ff["home"] = ""
                                ff["phone"] = ""
                                ff["gpu"] = ""
                                ff["gpu_amount"] = 0
                                ff["farm"] = 0.0
                                with open('json/' + str(id) + '.json', 'w') as f:
                                    f.write(json.dumps(ff, indent=4))
                                vk.method("messages.send", {"peer_id": id,
                                                        "message": "Обнуление завершено!",
                                                        "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Вы не Администратор или Модератор!",
                                                            "random_id": random.randint(1, 2147483647)})

                        elif body.lower() == "игры" or body.lower() == "⬅ игры":
                            vk.method("messages.send",
                                      {"peer_id": id,
                                       "message": games(),
                                       "keyboard": gamesmenu.get_keyboard(),
                                       "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == "биткоины" or body.lower() == "биткоин" or body.lower() == "битки" or body.lower() == "битк":
                            vk.method("messages.send",
                                      {"peer_id": id,
                                       "message": "Выберите что вы хотите сделать\n" + bal(id),
                                       "keyboard": btcmenu.get_keyboard(),
                                       "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif str(body.lower()).split()[0] == 'казино' or str(body).split()[0] == 'казик':
                            if len(str(body).split()) == 2:
                                temp = str(body).split(" ")
                                amount = temp[1]
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": kaz(id, amount),
                                                            "keyboard": kazmenu.get_keyboard(),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Добро пожаловать в казино!",
                                                            "keyboard": kazmenu.get_keyboard(),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)

                        elif str(body.lower()).split()[0] == 'казино' or str(body).split()[0] == 'казик':
                            if len(str(body).split()) == 2:
                                temp = str(body).split(" ")
                                amount = temp[1]
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": kaz(id, amount),
                                                            "keyboard": kazmenu.get_keyboard(),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)

                        elif str(body.lower()).split()[0] == 'монеточка' or str(body.lower()).split()[0] == 'монетка':
                            if len(str(body).split()) >= 3:
                                temp = str(body).split(" ")
                                side = temp[1]
                                amount = temp[2]
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": monetka(id, side , amount),
                                                            "keyboard": monetkasidemenu.get_keyboard(),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Обычная игра в монеточку\nВыберите сторону [Орел или Решка] и укажите сткаву\nПример: Монетка орел 1000",
                                                            "keyboard": monetkasidemenu.get_keyboard(),
                                                            "random_id": random.randint(1, 2147483647)})

                        elif body.lower() == "орел":
                            vk.method("messages.send",
                                      {"peer_id": id,
                                       "message": "Вы выбрали Орла",
                                       "keyboard": monetkaorelmenu.get_keyboard(),
                                       "random_id": random.randint(1, 2147483647)})
                            log(id, body)
                        elif body.lower() == "решка":
                            vk.method("messages.send",
                                      {"peer_id": id,
                                       "message": "Вы выбрали Решку",
                                       "keyboard": monetkareshkamenu.get_keyboard(),
                                       "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif str(body.lower()).split()[0] == 'сник':
                            if len(str(body).split()) >= 2:
                                temp = str(body).split("сник")
                                nickk = temp[1][1:]
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": nick(id, nickk),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Ваш ник пустой\nПример: 'сник Владимир Путин'",
                                                            "random_id": random.randint(1, 2147483647)})

                        elif str(body.lower()).split()[0] == 'дник':
                            if id in admins:
                                if len(str(body).split()) == 3:
                                    temp = str(body).split(" ")
                                    idd = temp[1]
                                    nickk = temp[2]
                                    vk.method("messages.send", {"peer_id": id,
                                                                "message": dnick(idd, nickk),
                                                                "random_id": random.randint(1, 2147483647)})
                                    log(id, body)

                        elif body.lower()  == 'работать':
                            vk.method("messages.send", {"peer_id": id,
                                "message": work(str(id)),
                                "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower()  == 'уволиться':
                            vk.method("messages.send", {"peer_id": id,
                                "message": dwork(str(id)),
                                "keyboard": mainworkmenu.get_keyboard(),
                                "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif str(body.lower()).split()[0] == 'устроиться':
                            if len(str(body).split()) == 2:
                                temp = str(body).split(" ")
                                val = temp[1]
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": hwork(str(id), val),
                                                            "keyboard": worksmenu.get_keyboard(),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": works(id),
                                                            "keyboard": worksmenu.get_keyboard(),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)

                        elif body.lower() == 'users':
                            if id in admins or id in moders:
                                if len(str(body).split()) == 1:
                                    vk.method("messages.send", {"peer_id": id,
                                                                "message": ulist(),
                                                            "random_id": random.randint(1, 2147483647)})
                                    log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Вы не Администратор или Модератор!",
                                                            "random_id": random.randint(1, 2147483647)})
                        elif str(body.lower()).split()[0] == 'gban':
                            if id in admins:
                                if len(str(body).split()) == 3:
                                    temp = str(body).split(" ")
                                    idd = temp[1]
                                    rsn = temp[2]
                                    vk.method("messages.send", {"peer_id": id,
                                                                "message": giveban(id, idd, rsn),
                                                                "random_id": random.randint(1, 2147483647)})
                                    log(id, body)
                                else:
                                    vk.method("messages.send", {"peer_id": id,
                                                                "message": "Используйте:\n'gban {id} {причина}'",
                                                                "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Вы не Администратор!",
                                                            "random_id": random.randint(1, 2147483647)})

                        elif str(body.lower()).split()[0] == 'unban':
                            if id in admins or id in moders:
                                if len(str(body).split()) == 2:
                                    temp = str(body).split(" ")
                                    idd = temp[1]
                                    vk.method("messages.send", {"peer_id": id,
                                                                "message": unban(idd),
                                                                "random_id": random.randint(1, 2147483647)})
                                    log(id, body)
                                else:
                                    vk.method("messages.send", {"peer_id": id,
                                                                "message": "Используйте:\n'unban {id}'",
                                                                "random_id": random.randint(1, 2147483647)})
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Вы не Администратор!",
                                                            "random_id": random.randint(1, 2147483647)})

                        elif body.lower() == 'staff' or body.lower() == 'админы' or body.lower() == 'модеры' or body.lower() == 'стафф':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": staff(),
                                                        "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == 'фильм':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": rfilm(),
                                                        "attachment": d,
                                                        "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == 'работа' or body.lower() == '⬅ работа':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": "💎 Выберите действие",
                                                        "keyboard": mainworkmenu.get_keyboard(),
                                                        "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == 'уровни':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": levels(),
                                                        "keyboard": mainmenu.get_keyboard(),
                                                        "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif str(body.lower()).split()[0] == 'передать' or str(body.lower()).split()[0] == 'перевод':
                            # if id in admins or id in moders:
                            #     vk.method("messages.send", {"peer_id": id,
                            #                                 "message": "Персоналу запрещено передавать деньги",
                            #                                 "random_id": random.randint(1, 2147483647)})
                            # else:
                                if len(str(body).split()) == 3:
                                    temp = str(body).split(" ")
                                    idd = temp[1]
                                    val = temp[2]
                                    vk.method("messages.send", {"peer_id": id,
                                                                "message": pay(id, idd, val),
                                                                "random_id": random.randint(1, 2147483647)})
                                    log(id, body)
                                else:
                                    vk.method("messages.send", {"peer_id": id,
                                                                "message": "Используйте:\nПередать {id} {сумма}\n\nЧтобы узнать ID - используйте 'ид {ссылка на профиль}'",
                                                                "random_id": random.randint(1, 2147483647)})

                        elif str(body.lower()).split()[0] == 'банк' or body.lower() == 'Банк баланс':
                            temp = str(body.lower()).split(" ")
                            if len(temp) == 3:
                                type = temp[1]
                                amount = temp[2]
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": bank(id, type, amount),
                                                            "keyboard": bankmenu.get_keyboard(),
                                                            "random_id": random.randint(1, 2147483647)})
                            else:
                                with open('json/' + str(id) + '.json', encoding='utf-8') as f:
                                    ff = json.loads(f.read())
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "💳 Баланс счёта: " + str(ff["bank"]) + "$\n\n⚠ Используйте:\nБанк положить {сумма}\nили\nБанк снять {сумма}",
                                                            "keyboard": bankmenu.get_keyboard(),
                                                            "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == 'бонус':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": gbonus(id),
                                                        "keyboard": mainmenu.get_keyboard(),
                                                        "random_id": random.randint(1, 2147483647)})
                            log(id, body)


                        elif str(body.lower()).split()[0] == "ид":
                            if len(str(body).split()) == 2:
                                temp = str(body).split(" ")
                                idd = temp[1]
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": idsearch(idd),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Чтобы узнать ID - используйте 'ид {ссылка на профиль}'",
                                                            "random_id": random.randint(1, 2147483647)})

                        # Магазин
                        elif body.lower() == 'магазин' or body.lower() == "⬅ магазин":
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": shop(),
                                                        "keyboard": shopmenu.get_keyboard(),
                                                        "random_id": random.randint(1, 2147483647)})
                        elif body.lower() == 'продать':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": sell(),
                                                        "keyboard": sellmenu.get_keyboard(),
                                                        "random_id": random.randint(1, 2147483647)})
                        elif body.lower() == 'машины':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": cars(),
                                                        "keyboard": carsmenu.get_keyboard(),
                                                        "random_id": random.randint(1, 2147483647)})
                        elif body.lower() == 'телефоны':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": phones(),
                                                        "keyboard": phonemenu.get_keyboard(),
                                                        "random_id": random.randint(1, 2147483647)})
                        elif body.lower() == 'дома':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": homes(),
                                                        "keyboard": homemenu.get_keyboard(),
                                                        "random_id": random.randint(1, 2147483647)})

                        elif str(body.lower()).split()[0] == 'кмашину':
                            if len(str(body).split()) == 2:
                                temp = str(body).split(" ")
                                n = temp[1]
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": bcar(id, n),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Неверное использование команды!\nПример: кмашину 1",
                                                            "random_id": random.randint(1, 2147483647)})
                        elif body.lower() == 'пмашину':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": sellcar(id),
                                                        "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif str(body.lower()).split()[0] == 'ктел':
                            if len(str(body).split()) == 2:
                                temp = str(body).split(" ")
                                n = temp[1]
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": bphone(id, n),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Неверное использование команды!\nПример: ктел 1",
                                                            "random_id": random.randint(1, 2147483647)})
                        elif  body.lower() == 'птел':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": sellphone(id),
                                                        "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif str(body.lower()).split()[0] == 'кдом':
                            if len(str(body).split()) == 2:
                                temp = str(body).split(" ")
                                n = temp[1]
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": bhome(id, n),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Неверное использование команды!\nПример: ктел 1",
                                                            "random_id": random.randint(1, 2147483647)})
                        elif  body.lower() == 'пдом':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": sellhome(id),
                                                        "random_id": random.randint(1, 2147483647)})
                            log(id, body)
                        # Магазин

                        elif  body.lower() == 'ихелп':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": prophelp(),
                                                        "random_id": random.randint(1, 2147483647)})

                        # Bytecoin
                        elif  body.lower() == 'видеокарты':
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": fshop(),
                                                        "keyboard": gpumenu.get_keyboard(),
                                                        "random_id": random.randint(1, 2147483647)})

                        elif str(body.lower()).split()[0] == 'ккарту':
                            if len(str(body).split()) == 2:
                                temp = str(body).split(" ")
                                n = temp[1]
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": bfarm(id, n),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Неверное использование команды!\nПример: ккарту 1",
                                                            "random_id": random.randint(1, 2147483647)})
                        elif body.lower() == 'пкарту':
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": sfarm(id),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == "ферма":
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": farmstatus(id),
                                                    "keyboard": farmmenu.get_keyboard(),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == "♻ обновить":
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": farmstatus(id),
                                                    "keyboard": farmmenu.get_keyboard(),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == "сбитки":
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": sellbtc(id),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == "бкурс":
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": btcrateshow(),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif str(body.lower()).split()[0] == 'пбитк':
                            if len(str(body).split()) == 2:
                                temp = str(body).split(" ")
                                n = temp[1]
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": btctousd(id, n),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Неверное использование команды!\nПример: пбитк 1.25",
                                                            "random_id": random.randint(1, 2147483647)})

                        elif str(body.lower()).split()[0] == 'кбитк':
                            if len(str(body).split()) == 2:
                                temp = str(body).split(" ")
                                n = temp[1]
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": usdtobtc(id, n),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                            else:
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": "Неверное использование команды!\nПример: пбитк 1.25",
                                                            "random_id": random.randint(1, 2147483647)})

                        # Bytecoin

                        elif body.lower() == 'топ':
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": "Какй топ вы хотите посмтореть?"
                                                               "\nБалтоп - топ по балансу"
                                                               "\nБитктоп - топ по кол-ву биткоинов",
                                                    "keyboard": topmenu.get_keyboard(),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == 'битктоп':
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": topbtc,
                                                    "keyboard": topmenu.get_keyboard(),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == 'балтоп':
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": topbal,
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        # Хакерство
                        elif body.lower() == 'хакерство' or body.lower() == "⬅ хакерство" or body.lower() == "🏠 хакерство":
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": hackmenu(id),
                                                    "keyboard": mainhackmenu.get_keyboard(),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == 'darkshop' or body.lower() == "⬅ darkshop":
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": darkshop(),
                                                    "keyboard": dsmenu.get_keyboard(),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == 'компы' or body.lower() == 'компьютеры' or body.lower() == 'комп':
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": comps(),
                                                    "keyboard": compmenu.get_keyboard(),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)
                        elif body.lower() == 'впн' or body.lower() == 'vpn':
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": vpns(),
                                                    "keyboard": vpnmenu.get_keyboard(),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)
                        elif body.lower() == 'убежища' or body.lower() == 'убежище' or body.lower() == 'убеж':
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": shltrs(),
                                                    "keyboard": shltrmenu.get_keyboard(),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif str(body.lower()).split()[0] == 'ккомп':
                            if len(str(body).split()) == 2:
                                temp = str(body).split(" ")
                                n = temp[1]
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": bcomp(id, n),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                        elif str(body.lower()).split()[0] == 'квпн':
                            if len(str(body).split()) == 2:
                                temp = str(body).split(" ")
                                n = temp[1]
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": bvpn(id, n),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                        elif str(body.lower()).split()[0] == 'кубежище' or str(body.lower()).split()[0] == 'кубеж':
                            if len(str(body).split()) == 2:
                                temp = str(body).split(" ")
                                n = temp[1]
                                vk.method("messages.send", {"peer_id": id,
                                                            "message": bshltr(id, n),
                                                            "random_id": random.randint(1, 2147483647)})
                                log(id, body)
                        elif body.lower() == 'прoдать':
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": "Выберите что продать"
                                                               "\n"
                                                               "\n&#12288;💻 Пкомп" \
                                                               "\n&#12288;🛡 Пвпн" \
                                                               "\n&#12288;🚪 Пубежище",
                                                    "keyboard": selldarkmenu.get_keyboard(),
                                                    "random_id": random.randint(1, 2147483647)})

                        elif body.lower() == 'пкомп':
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": scomps(id),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)
                        elif body.lower() == 'пвпн':
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": svpn(id),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)
                        elif body.lower() == 'пубежище' or body.lower() == 'пубеж':
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": sshltr(id),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == 'улучшения' or body.lower() == 'улучшение' or body.lower() == '⬅ улучшения':
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": upl(),
                                                    "keyboard": uplmenu.get_keyboard(),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif body.lower() == 'хп' or body.lower() == '💊 хп':
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": hpup(),
                                                    "keyboard": phpmenu.get_keyboard(),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)
                        elif body.lower() == 'защита' or body.lower() == '🕶 защита':
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": defup(),
                                                    "keyboard": pdefmenu.get_keyboard(),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)
                        elif body.lower() == 'урон' or body.lower() == '🔫 урон':
                            vk.method("messages.send", {"peer_id": id,
                                                    "message": dmgup(),
                                                    "keyboard": pdamagemenu.get_keyboard(),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif str(body.lower()).split()[0] == 'пхп' or body.lower() == "прокачать хп":
                            temp = str(body.lower()).split(" ")
                            try:
                                if temp[1] == "хп":
                                    val = ""
                                else:
                                    val = temp[1]
                            except:
                                val = ""

                            vk.method("messages.send", {"peer_id": id,
                                                    "message": php(val),
                                                    "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif str(body.lower()).split()[0] == 'пдеф' or body.lower() == "прокачать защиту":
                            temp = str(body.lower()).split(" ")
                            try:
                                if temp[1] == "защиту":
                                    val = ""
                                else:
                                    val = temp[1]
                            except:
                                val = ""

                            vk.method("messages.send", {"peer_id": id,
                                                        "message": pdef(val),
                                                        "random_id": random.randint(1, 2147483647)})
                            log(id, body)

                        elif str(body.lower()).split()[0] == 'пурон' or body.lower() == "прокачать урон":
                            temp = str(body.lower()).split(" ")
                            try:
                                if temp[1] == "урон":
                                    val = ""
                                else:
                                    val = temp[1]
                            except:
                                val = ""

                            vk.method("messages.send", {"peer_id": id,
                                                        "message": pdmg(val),
                                                        "random_id": random.randint(1, 2147483647)})
                            log(id, body)
                        # Хакерство

                        else:
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": "Увы, но такой команды нет\nПосмотреть их список можно написав 'команды'",
                                                        "keyboard": errormenu.get_keyboard(),
                                                        "random_id": random.randint(1, 2147483647)})

                    else:
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": "⚠ Вы заблокированы",
                                                    "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id,
                                        "message": "К сожалению,я могу распознать только текст :(",
                                        "keyboard": mainmenu.get_keyboard(),
                                        "random_id": random.randint(1, 2147483647)})

    except BaseException as E:
        print(E)
        #vk.method("messages.send",
         #         {"peer_id": 419760643, "message": E, "random_id": random.randint(1, 2147483647)})
        #log("system | ", E)
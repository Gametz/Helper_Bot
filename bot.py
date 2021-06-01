# -*- coding: utf-8 -*-
import vk_api
import dropbox
import requests
import bs4
import datetime
import random
import json
import time
import os.path
import threading

def res():
    return time.strftime("%x %X", time.localtime())

ver = "\n\nv1.2 от 01.06.2021 3:25 МСК"
users = next(os.walk("json/"))[2]
token = "2d26f19312dd93258ca84a1c533fefb1cffbb3a9d63d775e78ae3c62bd4254806825bdf2af924f8408d78"
vk = vk_api.VkApi(token=token)
vk._auth_token()

admins = [419760643]
moders = [361585264, 190114998, 418333599]

def log(id, body):
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.writelines("\n[" + res() + "] " + str(id) + " " + str(body) + " | Успешно!")

def glog():
    with open('log.txt', 'rb') as file:
        dbx = dropbox.Dropbox('sl.Ax5pyyTfcRNz4V0QRhG8hupqL8F5fvJImM67I0F0qinlhxi2eTObol6Skf1Tvg4oVgVPrhrwa6-6QzI6JNlI0VeuZWgbcyyL9KYS4aQmbzeGFHpEtQzu5acc6wUDxdceXoqxH0X0iLLv')
        r = dbx.files_delete_v2('/log.txt')
        if 'UploadWriteFailed(reason=WriteError(' in str(r):
            r = dbx.files_upload(file.read(), '/log.txt')
            l = dbx.sharing_create_shared_link('/log.txt')
            return l
        else:
            r = dbx.files_upload(file.read(), '/log.txt')
            l = dbx.sharing_create_shared_link('/log.txt')
            return l

def ifstaff(id):
    if id in admins or id in moders:
        if id in admins:
            return '✅ | Администратор'
        if id in moders:
            return '✅ | Модератор'
    else:
        return '🚫'

def prof(id):
    x = {
        "id": id,
        "balance": 1000,
        "level": 1,
        "exp": 0,
        "nick": "",
        "kwin": 0,
        "klose": 0,
        "mwin": 0,
        "mlose": 0,
        "wstatus": False,
        "reg": res()
    }
    try:
        with open('json/' + str(id) + '.json') as f:
            ff = json.loads(f.read())
    except:
        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(x, indent=4))
        with open('json/' + str(id) + '.json') as f:
            ff = json.loads(f.read())
        vk.method("messages.send", {"peer_id": 419760643,
                                    "message": "💎 Новый пользователь!",
                                    "random_id": random.randint(1, 2147483647)})
        return '💬 Добро пожаловать! Я вижу ты здесь новенький, используй "хелп" для помощи и развлекайся!\n💲 А еще,держи свой бонус в размере 1000$\n\n' + prof(str(id))

    return 'Ваш профиль\n\n' + \
           '🔎 id: ' + str(ff["id"]) + \
           '\n📋 Ник: ' + str(ff["nick"]) + \
           '\n💰 Баланс: ' + str(ff["balance"]) + \
           '\n📶 Уровень: ' + str(ff["level"]) + \
           '\n💡 Опыт: ' + str(ff["exp"]) + \
           '\n👥 Всего пользователей: ' + str(len(users)) + \
           '\n👔 Вы персонал: ' + ifstaff(id) + \
           '\n' \
           '\n📅 Дата регистрации: ' + str(ff["reg"]) + ver

def dprof(idd):
    with open('json/' + str(idd) + '.json') as f:
        ff = json.loads(f.read())
    print(idd)
    return 'Ссылка на профиль: vk.com/id' + idd + \
           '\n🔎 id: ' + str(ff["id"]) + \
           '\n📋 Ник: ' + str(ff["nick"]) + \
           '\n💰 Баланс: ' + str(ff["balance"]) + \
           '\n📶 Уровень: ' + str(ff["level"]) + \
           '\n💡 Опыт: ' + str(ff["exp"]) + \
           '\n👔 Персонал: ' + ifstaff(int(idd)) + \
           '\n' \
           '\n📅 Дата регистрации: ' + str(ff["reg"])

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

def bal(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    return '💰Ваш баланс: ' + str(ff["balance"]) + "$"

def cbal(id,val):
    if int(val) > 0 and int(val) < 1000000000:
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
        return "Вы ввели значение меньше нуля или больше 1 000 000 000"

def dbal (idd,val):
    if int(val) > 0 and int(val) < 1000000000:
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

def pay(id, idd, val):
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
        if per["nick"] == '':
            vk.method("messages.send", {"peer_id": idd,
                                "message": "Вы получили перевод от " + str(id) + " в размере: " + val + "$",
                                "random_id": random.randint(1, 2147483647)})
        else:
            vk.method("messages.send", {"peer_id": idd,
                                "message": "Вы получили перевод от " + per["nick"] + " в размере: " + val + "$",
                                "random_id": random.randint(1, 2147483647)})
        return "Перевод успешно выполнен! Ваш баланс: " + str(per["balance"]) + "$"
    else:
        return "Сумма превышает ваш баланс/Сумма меньше 0"

def ulist():
    c=1
    path = "json/"
    f=os.listdir(path)
    for i in range (len(f)):
        f[i] = '[' + str(c) + '] ' + "vk.com/id" + str(f[i][:-5])
        c += 1
    a = '\n'.join(f)
    return "Список пользователей\n\n" + a

def kaz(id,amount):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if int(amount) <= ff["balance"] and int(amount) > 0:
        r = random.randrange(0,7)
        if r == 0 or r == 1 or r == 2 or r == 3:
            ff["balance"] -= int(amount)
            ff["klose"] += int(round(int(amount)))
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))

            return "🚫Вы проиграли всю ставку!\n💰Ваш баланс: " + str(ff["balance"]) + "$"
        elif r == 4:
            win = int(amount)*1.5
            ff["balance"] += int(round(win))
            ff["kwin"] += int(round(win))
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))

            return "✅Вы выйграли: " + str(int(win)) + "$ (1.5x)" + "\n💰Ваш баланс: " + str(ff["balance"]) + "$"
        elif r == 5:
            win = int(amount) * 2
            ff["balance"] += int(round(win))
            ff["kwin"] += int(round(win))
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))

            return "✅Вы выйграли: " + str(int(win)) + "$ (2x)" + "\n💰Ваш баланс: " + str(ff["balance"]) + "$"
        elif r == 6:
            win = int(amount) * 5
            ff["balance"] += int(round(win))
            ff["kwin"] += int(round(win))
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))

            return "✅Вы выйграли: " + str(int(win)) + "$ (5x)" + "\n💰Ваш баланс: " + str(ff["balance"]) + "$"
    else:
        return "У вас недостаточно денег или сумма меньше 0!"

def monetka(id,amount):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if int(amount) <= ff["balance"] and int(amount) > 0:
        r = random.randrange(0, 2)
        if r == 0:
            ff["balance"] -= int(amount)
            ff["mlose"] += int(amount)
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "🚫Выпала решка,вы проиграли!" + "\n💰Ваш баланс: " + str(ff["balance"]) + "$"
        elif r == 1:
            win = int(amount) * 3
            ff["balance"] += int(round(win))
            ff["mwin"] += int(round(win))
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
        return "✅Вы выйграли,выпал Орел: " + str(int(win)) + "$ (3x)" + "\n💰Ваш баланс: " + str(ff["balance"]) + "$"
    else:
        return "У вас недостаточно денег или сумма меньше 0!"

def staff():
    return 'Список персонала\n\n' + 'Администраторы:\n' + '@gamtz (Влад Богданов)\n\n' + 'Модераторы:\n @lymar1 (Алексей Лымар)\n@plz_helpme_die (Денис Швец)\n@yatox1c (Ефим Ефименко)'

def help():
    return "📚 Основные команды\n&#12288;📖 Профиль/Проф - посмотреть свой профиль" \
           "\n&#12288;💲 Баланс/Бал - проверить свой баланс" \
           "\n&#12288;🤝 Передать {id} {сумма} - перевести денег другому игроку" \
           "\n&#12288;📋 Сник {ник} - изменить свой ник" \
           "\n&#12288;📊 Стата - статистика по развлекательным играм" \
           "\n&#12288;📶 Уровни - информация по распределению опыта" \
           "\n&#12288;👔 Staff/Админы/Модеры - список персонала " \
           "\n&#12288;⚠ Репорт {текст} - написать админу" \
           "\n" \
           "\n🎉Развлекательные команды" \
           "\n&#12288;💼 Работы - список доступных работ для заработка $" \
           "\n&#12288;🎰 Казино/Казик {сумма} - попытать удачу в казино" \
           "\n&#12288;🦅 Монетка {сумма} - flip! Подбрось монетку" \
           "\n&#12288;🤣 Анекдот - ну просто анекдот (Ха-Ха)" \
           "\n&#12288;📽 Фильм - случайный фильм из kinopoisk" \
           "\n&#12288;🔫 Ктата {nick} {id} - статистика в COD:Warzone за всё время" \
           "\n&#12288;🔫 Кстат20 {nick} {id} - статистика в COD:Warzone за последние 20 матчей " \
           "\n" \
           "\n📕 Команды для персонала" \
           "\n&#12288;💸 сбал {сумма} - изменить баланс себе (от Модератора)" \
           "\n&#12288;💳 дбал {id} {сумма} - изменить баланс другому игроку (от Администратора)" \
           "\n&#12288;👤 Дпроф {id} - просмотр чужого профиля (от Модератора)" \
           "\n&#12288;✒ Дник {id} {ник} - изменить чужой ник (от Администратора)" \
           "\n&#12288;👥 Users - список всех пользователей (от Модератора)" \
           #"\n&#12288;📄 Логи - просмотр использования команд (от Модератора)"

def gstats(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    twin = ff["kwin"] + ff["mwin"]
    tlose = ff["klose"] + ff["mlose"]
    return "📊 Статистика по играм\n\n🎰 Казино\n&#12288;📈 Всего выиграно в казино: " + str(ff["kwin"]) + "$" + " \n&#12288;📉 Всего проиграно в казино: " + str(ff["klose"]) + "$" + "\n🦅 Монетка\n&#12288;📈 Всего выиграно в монетке: " + str(ff["mwin"]) + "$" + " \n&#12288;📉 Всего проиграно в монетке: " + str(ff["mlose"]) + "$" + " \n\n📈Всего выиграно: " + str(twin) + "$" + " \n📉Всего проиграно: " + str(tlose) + "$"

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

def levels():
    return "📚 Информация об уровнях:" \
           "\n\nВсего 5 уровней:" \
           "\n1 уровень - 0-50 опыта" \
           "\n2 уровень - 51-150 опыта" \
           "\n3 уровень - 151-300 опыта" \
           "\n4 уровень - 301-500 опыта" \
           "\n5 уровень - 500+ опыта" \
           "\n\nНа каждом уровне открываются новые работы" \
           "\nЧтобы заработать опыт необходимо работать (работы)" \
           "\nПри достижении 5 уровня,опыт не копится"

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

def lvlchk2(id,lvl):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if lvl <= ff["level"]:
        return "✅"
    else:
        return "⛔"

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
           "\nЧтобы работать используйте 'работать {номер}'"
    return s

def work(id,work):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())

    if ff["wstatus"] == False:
        if ff["level"] >= 1:
            if work == "1":
                ff["wstatus"] = True
                threading.Timer(20.0, workend, args=(id, work,)).start()
                with open('json/' + str(id) + '.json', 'w') as f:
                    f.write(json.dumps(ff, indent=4))
                return "✅ Вы начали работать в FakeTAXI! \nЗакончите через 20 секунд"

            if work == "2":
                ff["wstatus"] = True
                threading.Timer(40.0, workend, args=(id, work,)).start()
                with open('json/' + str(id) + '.json', 'w') as f:
                    f.write(json.dumps(ff, indent=4))
                return "✅ Вы начали работать на Ферме! \nЗакончите через 40 секунд"

        if ff["level"] >= 2:
            if work == "3":
                ff["wstatus"] = True
                threading.Timer(60.0, workend, args=(id, work,)).start()
                with open('json/' + str(id) + '.json', 'w') as f:
                    f.write(json.dumps(ff, indent=4))
                return "✅ Вы начали работать Тестировщиком игр! \nЗакончите через 1 минуту"

            if work == "4":
                ff["wstatus"] = True
                threading.Timer(90.0, workend, args=(id, work,)).start()
                with open('json/' + str(id) + '.json', 'w') as f:
                    f.write(json.dumps(ff, indent=4))
                return "✅ Вы начали работать в кофейне! \nЗакончите через 1:30 минуты"
        else:
            return "У вас слишком маленький уровень! \nНеобходим: 2\nВаш уровень: " + str(ff["level"])

        if ff["level"] >= 3:
            if work == "5":
                ff["wstatus"] = True
                threading.Timer(120.0, workend, args=(id, work,)).start()
                with open('json/' + str(id) + '.json', 'w') as f:
                    f.write(json.dumps(ff, indent=4))
                return "✅ Вы начали работать на Заводе! \nЗакончите через 2 минуты"

            if work == "6":
                ff["wstatus"] = True
                threading.Timer(180.0, workend, args=(id, work,)).start()
                with open('json/' + str(id) + '.json', 'w') as f:
                    f.write(json.dumps(ff, indent=4))
                return "✅ Вы начали работать Дегустатором вина! \nЗакончите через 3 минуты"
        else:
            return "У вас слишком маленький уровень! \nНеобходим: 3\nВаш уровень: " + str(ff["level"])

        if ff["level"] >= 4:
            if work == "7":
                ff["wstatus"] = True
                threading.Timer(300.0, workend, args=(id, work,)).start()
                with open('json/' + str(id) + '.json', 'w') as f:
                    f.write(json.dumps(ff, indent=4))
                return "✅ Вы начали работать продавцом в Verdax'e! \nЗакончите через 5 минут"

            if work == "8":
                ff["wstatus"] = True
                threading.Timer(600.0, workend, args=(id, work,)).start()
                with open('json/' + str(id) + '.json', 'w') as f:
                    f.write(json.dumps(ff, indent=4))
                return "✅ Вы начали работать Дизайнером! \nЗакончите через 10 минут"
        else:
            return "У вас слишком маленький уровень! \nНеобходим: 4\nВаш уровень: " + str(ff["level"])

        if ff["level"] >= 5:
            if work == "9":
                ff["wstatus"] = True
                threading.Timer(1200.0, workend, args=(id, work,)).start()
                with open('json/' + str(id) + '.json', 'w') as f:
                    f.write(json.dumps(ff, indent=4))
                return "✅ Вы начали работать Режиссёром Аниме! \nЗакончите через 20 минут"

            if work == "10":
                ff["wstatus"] = True
                threading.Timer(2400.0, workend, args=(id, work,)).start()
                with open('json/' + str(id) + '.json', 'w') as f:
                    f.write(json.dumps(ff, indent=4))
                return "✅ Вы начали работать Директором Natflex'a! \nЗакончите через 40 минут"
        else:
            return "У вас слишком маленький уровень! \nНеобходим: 5\nВаш уровень: " + str(ff["level"])
    else:
        return "⚠ Вы уже работаете!"

def workend(id,work):
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

print("[" + res() +"] ✅Бот запущен!")
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]

            if id in moders or id in admins:
            #if id in admins:
            #if True:
                if body.lower() == 'пинг':
                    vk.method("messages.send", {"peer_id": id,
                                                "message": "Не Миша,всё хуйня! Давай по новой!",
                                                "random_id": random.randint(1, 2147483647)})
                    log(id, body)

                elif body.lower() == 'хелп' or body.lower() == 'помощь':
                    vk.method("messages.send", {"peer_id": id,
                                                "message": help(),
                                                "random_id": random.randint(1, 2147483647)})
                    log(id, body)

                elif body.lower() == 'профиль' or body.lower() == 'начать' or body.lower() == 'проф' or body.lower() == 'start':
                    vk.method("messages.send", {"peer_id": id,
                                                "message": prof(id),
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
                                                "random_id": random.randint(1, 2147483647)})
                    log(id, body)

                elif "анекдот" in body.lower():
                    vk.method("messages.send",
                              {"peer_id": id, "message": getanekdot(), "random_id": random.randint(1, 2147483647)})
                    log(id, body)

                if 'кстата' in body.lower():
                    if len(str(body).split()) == 3:
                        temp = str(body).split(" ")
                        nick = temp[1]
                        idd = temp[2]
                        stats(nick, idd)
                        log(id, body)
                    else:
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": "⚠Для показа статистики введите ник и id Battle.net через пробел. Пример: стата Vlad 214228⚠",
                                                    "random_id": random.randint(1, 2147483647)})

                elif 'кстат20' in body.lower():
                    if len(body) > 5:
                        temp = str(body).split(" ")
                        nick = temp[1]
                        idd = temp[2]
                        stats20(nick, idd)
                        log(id, body)
                    else:
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": "⚠Для показа статистики введите ник и id Battle.net через пробел. Пример: стат20 Vlad 214228⚠",
                                                    "random_id": random.randint(1, 2147483647)})

                elif 'сбал' in body.lower():
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

                elif 'дбал' in body.lower():
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

                elif 'дпроф' in body.lower():
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

                elif 'казино' in body.lower() or 'казик' in body.lower():
                    if len(str(body).split()) == 2:
                        temp = str(body).split(" ")
                        amount = temp[1]
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": kaz(id, amount),
                                                    "random_id": random.randint(1, 2147483647)})
                        log(id, body)

                elif 'монеточка' in body.lower() or 'монетка' in body.lower():
                    if len(str(body).split()) == 2:
                        temp = str(body).split(" ")
                        amount = temp[1]
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": monetka(id, amount),
                                                    "random_id": random.randint(1, 2147483647)})
                        log(id, body)
                    else:
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": "Обычная игра в монеточку\nЕсли выпадет Орел - вы выйграете,Решка - проиграете\nУдачи!\n'монетка {сумма}'",
                                                    "random_id": random.randint(1, 2147483647)})

                elif 'сник' in body.lower():
                    if len(str(body).split()) == 2:
                        temp = str(body).split(" ")
                        nickk = temp[1]
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": nick(id, nickk),
                                                    "random_id": random.randint(1, 2147483647)})
                        log(id, body)
                    else:
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": "Ваш ник содержит пробелы или пустой",
                                                    "random_id": random.randint(1, 2147483647)})

                elif 'дник' in body.lower():
                    if id in admins:
                        if len(str(body).split()) == 3:
                            temp = str(body).split(" ")
                            idd = temp[1]
                            nickk = temp[2]
                            vk.method("messages.send", {"peer_id": id,
                                                        "message": dnick(idd, nickk),
                                                        "random_id": random.randint(1, 2147483647)})
                            log(id, body)


                elif 'работать' in body.lower():
                    if len(str(body).split()) == 2:
                        temp = str(body).split(" ")
                        val = temp[1]
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": work(str(id), val),
                                                    "random_id": random.randint(1, 2147483647)})
                        log(id, body)

                elif 'users' in body.lower():
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

                elif body.lower() == 'работы':
                    vk.method("messages.send", {"peer_id": id,
                                                "message": works(id),
                                                "random_id": random.randint(1, 2147483647)})
                    log(id, body)

                elif body.lower() == 'уровни':
                    vk.method("messages.send", {"peer_id": id,
                                                "message": levels(),
                                                "random_id": random.randint(1, 2147483647)})
                    log(id, body)

                elif body.lower() == 'логи':
                    if id in admins or id in moders:
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": glog(),
                                                    "random_id": random.randint(1, 2147483647)})
                        log(id, body)
                    else:
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": "Вы не Администратор или Модератор!",
                                                    "random_id": random.randint(1, 2147483647)})

                elif 'передать' in body.lower():
                    if len(str(body).split()) == 3:
                        temp = str(body).split(" ")
                        idd = temp[1]
                        val = temp[2]
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": pay(id, idd, val),
                                                    "random_id": random.randint(1, 2147483647)})
                        log(id, body)

                elif 'репорт' in body.lower():
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
            else:
                vk.method("messages.send", {"peer_id": id,
                                            "message": "⚠ Технические работы! Приносим свои извинения",
                                            "random_id": random.randint(1, 2147483647)})
    except BaseException as E:
        print(E)
        vk.method("messages.send",
                  {"peer_id": 419760643, "message": E, "random_id": random.randint(1, 2147483647)})
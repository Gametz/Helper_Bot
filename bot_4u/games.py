import json
import random

def games():
    return "🎮 Список игр:" \
           "\n" \
           "\n&#12288;🎰 Казино" \
           "\n&#12288;🦅 Монетка"

def kaz(id,amount):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    try:
        if amount == "все" or amount == "всё":
            amount = ff["balance"]
        if amount == "половина":
            amount = int(ff["balance"] / 2)
        if int(amount) <= ff["balance"] and int(amount) > 0:
            r = random.randrange(0,15)
            if r == 0 or r == 1 or r == 2 or r == 3 or r == 4 or r == 5 or r == 6:
                ff["balance"] -= int(amount)
                ff["klose"] += int(round(int(amount)))
                with open('json/' + str(id) + '.json', 'w') as f:
                    f.write(json.dumps(ff, indent=4))
                return "🚫Вы проиграли всю ставку!\n💰Ваш баланс: " + str(ff["balance"]) + "$"
            elif r == 7 or r == 8 or r == 9 or r == 10:
                win = int(amount)*1.5
                ff["balance"] += int(round(win))
                ff["kwin"] += int(round(win))
                with open('json/' + str(id) + '.json', 'w') as f:
                    f.write(json.dumps(ff, indent=4))
                return "✅Вы выйграли: " + str(int(win)) + "$ (1.5x)" + "\n💰Ваш баланс: " + str(ff["balance"]) + "$"
            elif r == 11 or r == 12 or r == 13:
                win = int(amount) * 2
                ff["balance"] += int(round(win))
                ff["kwin"] += int(round(win))
                with open('json/' + str(id) + '.json', 'w') as f:
                    f.write(json.dumps(ff, indent=4))
                return "✅Вы выйграли: " + str(int(win)) + "$ (2x)" + "\n💰Ваш баланс: " + str(ff["balance"]) + "$"
            elif r == 14:
                win = int(amount) * 5
                ff["balance"] += int(round(win))
                ff["kwin"] += int(round(win))
                with open('json/' + str(id) + '.json', 'w') as f:
                    f.write(json.dumps(ff, indent=4))

                return "✅Вы выйграли: " + str(int(win)) + "$ (5x)" + "\n💰Ваш баланс: " + str(ff["balance"]) + "$"
        else:
            return "У вас недостаточно денег или сумма меньше 0!\n" + bal(id)
    except:
        return "Введите целое число!"

def monetka(id, side, amount):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if amount == "все" or amount == "всё":
        amount = ff["balance"]
    if int(amount) <= ff["balance"] and int(amount) > 0:
        if side == "орел":
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
        elif side == "решка":
            r = random.randrange(0, 2)
            if r == 0:
                ff["balance"] -= int(amount)
                ff["mlose"] += int(amount)
                with open('json/' + str(id) + '.json', 'w') as f:
                    f.write(json.dumps(ff, indent=4))
                return "🚫Выпал Орел,вы проиграли!" + "\n💰Ваш баланс: " + str(ff["balance"]) + "$"
            elif r == 1:
                win = int(amount) * 3
                ff["balance"] += int(round(win))
                ff["mwin"] += int(round(win))
                with open('json/' + str(id) + '.json', 'w') as f:
                    f.write(json.dumps(ff, indent=4))
            return "✅Вы выйграли,выпала Решка: " + str(int(win)) + "$ (3x)" + "\n💰Ваш баланс: " + str(ff["balance"]) + "$"
        return "У монетки есть только 2 стороны - Орел и Решка"
    else:
        return "У вас недостаточно денег или сумма меньше 0!\n" + bal(id)

def gstats(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    twin = ff["kwin"] + ff["mwin"]
    tlose = ff["klose"] + ff["mlose"]
    return "📊 Статистика по играм\n\n🎰 Казино\n&#12288;📈 Всего выиграно в казино: " + str(ff["kwin"]) + "$" + " \n&#12288;📉 Всего проиграно в казино: " + str(ff["klose"]) + "$" + "\n🦅 Монетка\n&#12288;📈 Всего выиграно в монетке: " + str(ff["mwin"]) + "$" + " \n&#12288;📉 Всего проиграно в монетке: " + str(ff["mlose"]) + "$" + " \n\n📈Всего выиграно: " + str(twin) + "$" + " \n📉Всего проиграно: " + str(tlose) + "$"

import json
import random

def hackmenu(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    return "📋 Твой профиль:" \
           "\n" \
           "\n🔎 Уровень: " + str(ff["hlevel"]) + \
           "\n💊 ХП: " + str(ff["hhp"]) + " (+" + str(ff["php"]) + ")" + \
           "\n🔫 Урон: " + str(ff["hdamage"]) + " (+" + str(ff["pdamage"]) + ")" + \
           "\n🕶 Защита: " + str(ff["hdef"]) + " (+" + str(ff["pdef"]) + ")" + \
           "\n" \
           "\n🔑 Имущество" \
           "\n&#12288;💻 Комп: " + ff["hcomp"] + \
           "\n&#12288;🛡 VPN: " + ff["hvpn"] + \
           "\n&#12288;🚪 Убежище: " + ff["hsheltr"] \

def darkshop():
    return "🎴 DarkShop 🎴" \
           "\n" \
           "\n&#12288;💻 Компы - атака" \
           "\n&#12288;🛡 VPN - защита" \
           "\n&#12288;🚪 Убежища - хп" \
           "\n" \
           "\n📌 Для просмотра категории используйте ее название"

def comps():
    return "💻 Компы 💻" \
           "\nУровень | Название | Баффы | Цена" \
           "\n" \
           "\n&#12288;💎 1. &#12288;2 | Калькулятор | +1 к атаке | 20₿" \
           "\n&#12288;💎 2. &#12288;5 | 4 ядра, 4 гига | +3 к атаке | 100₿" \
           "\n&#12288;💎 3. &#12288;15 | Офисный | +5 к атаке | 300₿" \
           "\n&#12288;💎 4. &#12288;30 | Игровой | +10 к атаке | 500₿" \
           "\n&#12288;💎 5. &#12288;50 | Квантовый | +20 к атаке | 1500₿" \
           "\n" \
           "\n📌 Для покупки используйте 'ккомп [номер]'"

def vpns():
    return "🛡 VPN 🛡" \
           "\nУровень | Название | Баффы | Цена" \
           "\n" \
           "\n&#12288;💎 1. &#12288;3 | Wi-Fi соседа | +1 к защите | 20₿" \
           "\n&#12288;💎 2. &#12288;7 | С форума | +4 к защите | 170₿" \
           "\n&#12288;💎 3. &#12288;18 | Приватный | +8 к защите | 350₿" \
           "\n&#12288;💎 4. &#12288;35 | Игровой | +15 к защите | 550₿" \
           "\n&#12288;💎 5. &#12288;55 | Собственный | +20 к защите | 1700₿" \
           "\n" \
           "\n📌 Для покупки используйте 'квпн [номер]'"

def shltrs():
    return "🚪 Убежища 🚪" \
           "\nУровень | Название | Баффы | Цена" \
           "\n" \
           "\n&#12288;💎 1. &#12288;5 | Подвал дома | +2 к хп | 35₿" \
           "\n&#12288;💎 2. &#12288;12 | Гараж деда | +5 к хп | 200₿" \
           "\n&#12288;💎 3. &#12288;25 | Съемная квартира | +9 к хп | 400₿" \
           "\n&#12288;💎 4. &#12288;50 | Бункер в горах | +16 к хп | 1800₿" \
           "\n&#12288;💎 5. &#12288;60 | Дом Путина | +21 к хп | 2000₿" \
           "\n" \
           "\n📌 Для покупки используйте 'кубежище [номер]'"

def bcomp(id, n):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["hcomp"] == "":
        if n == '1' and ff["btc"] >= 20 and ff["hlevel"] >= 2:
            ff["btc"] -= 20
            ff["hcomp"] = "Калькулятор"
            ff["pdamage"] += 1
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id) # noqa
            return "Вы купили " + str(ff["hcomp"]) + " за 20₿\nВаш баланс: \n" + bal(id) # noqa

        elif n == '2' and ff["btc"] >= 100 and ff["hlevel"] >= 5:
            ff["btc"] -= 100
            ff["hcomp"] = "4 ядра, 4 гига"
            ff["pdamage"] += 3
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id) # noqa
            return "Вы купили " + str(ff["hcomp"]) + " за 100₿\nВаш баланс: \n" + bal(id) # noqa

        elif n == '3' and ff["btc"] >= 300 and ff["hlevel"] >= 15:
            ff["btc"] -= 300
            ff["hcomp"] = "Офисный"
            ff["pdamage"] += 5
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id) # noqa
            return "Вы купили " + str(ff["hcomp"]) + " за 300₿\nВаш баланс: \n" + bal(id) # noqa

        elif n == '4' and ff["btc"] >= 500 and ff["hlevel"] >= 30:
            ff["btc"] -= 500
            ff["hcomp"] = "Игровой"
            ff["pdamage"] += 10
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id) # noqa
            return "Вы купили " + str(ff["hcomp"]) + " за 500₿\nВаш баланс: \n" + bal(id) # noqa

        elif n == '5' and ff["btc"] >= 1500 and ff["hlevel"] >= 50:
            ff["btc"] -= 1500
            ff["hcomp"] = "Квантовый"
            ff["pdamage"] += 20
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id) # noqa
            return "Вы купили " + str(ff["hcomp"]) + " за 1500₿\nВаш баланс: \n" + bal(id) # noqa

        else:
            return "У вас не хватает денег/опыта или вы неправильно используете команду!\nПример: ккомп 1"
    else:
        return "У вас уже есть комп или вы неправильно используете команду!\nПример: ккомп 1\nЧтобы продать его, используйте 'пкомп'"

def scomps(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["hcomp"] != "":
        if ff["hcomp"] == "Калькулятор":
            temp = ff["hcomp"]
            ff["hcomp"] = ""
            ff["btc"] += 20
            ff["pdamage"] = 0
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали " + temp + " за 20₿\n" + bal(id) # noqa

        elif ff["hcomp"] == "4 ядра, 4 гига":
            temp = ff["hcomp"]
            ff["hcomp"] = ""
            ff["btc"] += 100
            ff["pdamage"] = 0
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали " + temp + " за 100₿\n" + bal(id) # noqa

        elif ff["hcomp"] == "Офисный":
            temp = ff["hcomp"]
            ff["hcomp"] = ""
            ff["btc"] += 300
            ff["pdamage"] = 0
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали " + temp + " за 300₿\n" + bal(id) # noqa

        elif ff["hcomp"] == "Игровой":
            temp = ff["hcomp"]
            ff["hcomp"] = ""
            ff["btc"] += 500
            ff["pdamage"] = 0
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали " + temp + " за 500₿\n" + bal(id) # noqa

        elif ff["hcomp"] == "Квантовый":
            temp = ff["hcomp"]
            ff["hcomp"] = ""
            ff["btc"] += 1500
            ff["pdamage"] = 0
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали " + temp + " за 1500₿\n" + bal(id) # noqa
    else:
        return 'У вас нет компа!'

def bvpn(id, n):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["hvpn"] == "":
        if n == '1' and ff["btc"] >= 20 and ff["hlevel"] >= 3:
            ff["btc"] -= 20
            ff["hvpn"] = "Wi-Fi соседа"
            ff["pdef"] += 1
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id) # noqa
            return "Вы купили " + str(ff["hvpn"]) + " за 20₿\nВаш баланс: \n" + bal(id) # noqa

        elif n == '2' and ff["btc"] >= 170 and ff["hlevel"] >= 7:
            ff["btc"] -= 100
            ff["hvpn"] = "С форума"
            ff["pdef"] += 4
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id) # noqa
            return "Вы купили " + str(ff["hvpn"]) + " за 100₿\nВаш баланс: \n" + bal(id) # noqa

        elif n == '3' and ff["btc"] >= 350 and ff["hlevel"] >= 18:
            ff["btc"] -= 300
            ff["hvpn"] = "Приватный"
            ff["pdef"] += 8
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id) # noqa
            return "Вы купили " + str(ff["hvpn"]) + " за 300₿\nВаш баланс: \n" + bal(id) # noqa

        elif n == '4' and ff["btc"] >= 550 and ff["hlevel"] >= 35:
            ff["btc"] -= 500
            ff["hvpn"] = "Игровой"
            ff["pdef"] += 15
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id) # noqa
            return "Вы купили " + str(ff["hvpn"]) + " за 500₿\nВаш баланс: \n" + bal(id) # noqa

        elif n == '5' and ff["btc"] >= 1700 and ff["hlevel"] >= 55:
            ff["btc"] -= 1500
            ff["hvpn"] = "Собственный"
            ff["pdef"] += 20
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id) # noqa
            return "Вы купили " + str(ff["hvpn"]) + " за 1500₿\nВаш баланс: \n" + bal(id) # noqa

        else:
            return "У вас не хватает денег/опыта или вы неправильно используете команду!\nПример: квпн 1"
    else:
        return "У вас уже есть VPN или вы неправильно используете команду!\nПример: квпн 1\nЧтобы продать его, используйте 'пвпн'"

def svpn(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["hvpn"] != "":
        if ff["hvpn"] == "Wi-Fi соседа":
            temp = ff["hvpn"]
            ff["hvpn"] = ""
            ff["btc"] += 20
            ff["pdef"] = 0
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали " + temp + " за 20₿\n" + bal(id) # noqa

        elif ff["hvpn"] == "С форума":
            temp = ff["hvpn"]
            ff["hvpn"] = ""
            ff["btc"] += 170
            ff["pdef"] = 0
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали " + temp + " за 170₿\n" + bal(id) # noqa

        elif ff["hvpn"] == "Приватный":
            temp = ff["hvpn"]
            ff["hvpn"] = ""
            ff["btc"] += 350
            ff["pdef"] = 0
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали " + temp + " за 350₿\n" + bal(id) # noqa

        elif ff["hvpn"] == "Игровой":
            temp = ff["hvpn"]
            ff["hvpn"] = ""
            ff["btc"] += 550
            ff["pdef"] = 0
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали " + temp + " за 550₿\n" + bal(id) # noqa

        elif ff["hvpn"] == "Собственный":
            temp = ff["hvpn"]
            ff["hvpn"] = ""
            ff["btc"] += 1700
            ff["pdef"] = 0
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали " + temp + " за 1700₿\n" + bal(id) # noqa
    else:
        return 'У вас нет VPN!'

def bshltr(id, n):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["hsheltr"] == "":
        if n == '1' and ff["btc"] >= 35 and ff["hlevel"] >= 5:
            ff["btc"] -= 35
            ff["hsheltr"] = "Подвал дома"
            ff["php"] += 1
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id) # noqa
            return "Вы купили " + str(ff["hsheltr"]) + " за 35₿\nВаш баланс: \n" + bal(id) # noqa

        elif n == '2' and ff["btc"] >= 200 and ff["hlevel"] >= 12:
            ff["btc"] -= 200
            ff["hsheltr"] = "Гараж деда"
            ff["php"] += 5
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id) # noqa
            return "Вы купили " + str(ff["hsheltr"]) + " за 200₿\nВаш баланс: \n" + bal(id) # noqa

        elif n == '3' and ff["btc"] >= 400 and ff["hlevel"] >= 25:
            ff["btc"] -= 400
            ff["hsheltr"] = "Съемная квартира"
            ff["php"] += 9
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id) # noqa
            return "Вы купили " + str(ff["hsheltr"]) + " за 400₿\nВаш баланс: \n" + bal(id) # noqa

        elif n == '4' and ff["btc"] >= 1800 and ff["hlevel"] >= 50:
            ff["btc"] -= 1800
            ff["hsheltr"] = "Бункер в горах"
            ff["php"] += 16
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id) # noqa
            return "Вы купили " + str(ff["hsheltr"]) + " за 1800₿\nВаш баланс: \n" + bal(id) # noqa

        elif n == '5' and ff["btc"] >= 2000 and ff["hlevel"] >= 60:
            ff["btc"] -= 2000
            ff["hsheltr"] = "Дом Путина"
            ff["php"] += 21
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id) # noqa
            return "Вы купили " + str(ff["hsheltr"]) + " за 2000₿\nВаш баланс: \n" + bal(id) # noqa

        else:
            return "У вас не хватает денег/опыта или вы неправильно используете команду!\nПример: кубежище 1"
    else:
        return "У вас уже есть убежище или вы неправильно используете команду!\nПример: кубежище 1\nЧтобы продать его, используйте 'пубежище'"

def sshltr(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["hsheltr"] != "":
        if ff["hsheltr"] == "Подвал дома":
            temp = ff["hsheltr"]
            ff["hsheltr"] = ""
            ff["btc"] += 35
            ff["php"] = 0
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали " + temp + " за 35₿\n" + bal(id) # noqa

        elif ff["hsheltr"] == "Гараж деда":
            temp = ff["hsheltr"]
            ff["hsheltr"] = ""
            ff["btc"] += 200
            ff["php"] = 0
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали " + temp + " за 200₿\n" + bal(id) # noqa

        elif ff["hsheltr"] == "Съемная квартира":
            temp = ff["hsheltr"]
            ff["hsheltr"] = ""
            ff["btc"] += 400
            ff["php"] = 0
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали " + temp + " за 400₿\n" + bal(id) # noqa

        elif ff["hsheltr"] == "Бункер в горах":
            temp = ff["hsheltr"]
            ff["hsheltr"] = ""
            ff["btc"] += 1800
            ff["php"] = 0
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали " + temp + " за 1800₿\n" + bal(id) # noqa

        elif ff["hsheltr"] == "Дом Путина":
            temp = ff["hsheltr"]
            ff["hsheltr"] = ""
            ff["btc"] += 2000
            ff["php"] = 0
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали " + temp + " за 2000₿\n" + bal(id) # noqa
    else:
        return 'У вас нет убежища!'

def upl():
    return "Выберите что хотите улучшить" \
           "\n&#12288;💊 ХП" \
           "\n&#12288;🔫 Урон" \
           "\n&#12288;🕶 Защита" \
           "\n" \
           "\n📌 Для просмотра категории используйте ее название"

def hpup(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    return "🔎 Ваш уровень: " + str(ff["hlevel"]) + \
           "\n💊 ХП: " + str(ff["hhp"]) + \
           "\n" \
           "\n♻ Уровень прокачки: " + str(ff["hplvl"]) + \
           "\n💰 Стоимость прокачки: " + str(ff["hplvl"] * 10) + "₿" + \
           "\n" \
           "\n📌 Для прокачки используйте - Пхп"

def defup(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())

    return "🔎 Ваш уровень: " + str(ff["hlevel"]) + \
           "\n🕶 Защита: " + str(ff["hdef"]) + \
           "\n" \
           "\n♻ Уровень прокачки: " + str(ff["deflvl"]) + \
           "\n💰 Стоимость прокачки: " + str(ff["deflvl"] * 10) + "₿" + \
           "\n" \
           "\n📌 Для прокачки используйте - Пдеф"

def dmgup(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())

    return "🔎 Ваш уровень: " + str(ff["hlevel"]) + \
           "\n🔫 Урон: " + str(ff["hdamage"]) + \
           "\n" \
           "\n♻ Уровень прокачки: " + str(ff["damagelvl"]) + \
           "\n💰 Стоимость прокачки: " + str(ff["damagelvl"] * 10) + "₿" + \
           "\n" \
           "\n📌 Для прокачки используйте - Пурон"

def php(id,val):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())

    if val == "":
        value = 1
    else:
        value = int(val)

    p = ff["hplvl"] ** 3
    if ff["hplvl"] <= 100 and ff["hplvl"] + value <= 100:
        if ff["btc"] >= p * value:
            ff["btc"] -= p * value
            ff["hplvl"] += value
            ff["hhp"] += 10 * value
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "✅ Вы успешно прокачали ХП на " + str(value) + " уровень!\n💊 ХП: " + str(ff["hhp"]) + "\n" + "♻ Уровень ХП: " + str(ff["hplvl"]) + "\n\n💰 Стоимость следующей прокачки: " + str(p) + "₿"
        else:
            return "У вас недостаточно биткоинов для прокачки!"
    else:
        return "У вас максимальный уровень - 100!"

def pdef(id,val):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())

    if val == "":
        value = 1
    else:
        value = int(val)

    p = ff["deflvl"] ** 3
    if ff["deflvl"] <= 100 and ff["deflvl"] + value <= 100:
        if ff["btc"] >= p * value:
            ff["btc"] -= p * value
            ff["deflvl"] += value
            ff["hdef"] += 10 * value
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "✅ Вы успешно прокачали Защиту на " + str(value) + " уровень!\n💊 ХП: " + str(ff["hdef"]) + "\n" + "♻ Уровень Защиты: " + str(ff["deflvl"]) + "\n\n💰 Стоимость следующей прокачки: " + str(p) + "₿"
        else:
            return "У вас недостаточно биткоинов для прокачки!"
    else:
        return "У вас максимальный уровень - 100!"

def pdmg(id,val):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())

    if val == "":
        value = 1
    else:
        value = int(val)

    p = ff["damagelvl"] ** 3
    if ff["damagelvl"] <= 100 and ff["damagelvl"] + value <= 100:
        if ff["btc"] >= p * value:
            ff["btc"] -= p * value
            ff["damagelvl"] += value
            ff["hdamage"] += 10 * value
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "✅ Вы успешно прокачали ХП на " + str(value) + " уровень!\n💊 ХП: " + str(ff["hdamage"]) + "\n" + "♻ Уровень ХП: " + str(ff["damagelvl"]) + "\n\n💰 Стоимость следующей прокачки: " + str(p) + "₿"
        else:
            return "У вас недостаточно биткоинов для прокачки!"
    else:
        return "У вас максимальный уровень - 100!"



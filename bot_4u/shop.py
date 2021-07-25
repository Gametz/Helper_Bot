import json

def congrts(id):
    vk.method("messages.send", {"peer_id": id,
                                "sticker_id": 11788,
                                "random_id": random.randint(1, 2147483647)})

def shop():
    return "Магазин:" \
           "\n" \
           "\n&#12288;🚗 Машины" \
           "\n&#12288;📱 Телефоны" \
           "\n&#12288;🏡 Дома" \
           "\n&#12288;🎞 Видеокарты" \
           "\n&#12288;₿ Биткоины" \
           "\n" \
           "\n📌 Для просмотра категории используйте ее название"

def sell():
    return "Продажа:" \
           "\n" \
           "\n&#12288;🚗 Пмашину - Продать свою машину" \
           "\n&#12288;📱 Птел - Продать свой телефон" \
           "\n&#12288;🏡 Пдом - Продать свой дом" \
           "\n&#12288;🎞 Пкарту - Продать свю видеокарту"

def cars():
    return "🚗 Машины:" \
           "\n" \
           "\n&#12288;💎 1. ВАЗ 2115 | 2.000$" \
           "\n&#12288;💎 2. LADA Vesta | 4.000$" \
           "\n&#12288;💎 3. Audi Q7 | 8.000$" \
           "\n&#12288;💎 4. BMW M8 | 15.000$" \
           "\n&#12288;💎 5. Range Rover | 50.000$" \
           "\n&#12288;💎 6. Rolls-Royce | 150.000$" \
           "\n" \
           "\n📌 Для покупки транспорта используйте 'кмашину [номер]'\n" \
           "Например: кмашину 1"

def phones():
    return "📱 Телефоны:" \
           "\n" \
           "\n&#12288;💎 1. Fly Ezzy Flip | 200$" \
           "\n&#12288;💎 2. Sony Xperia XA1 | 1.000$" \
           "\n&#12288;💎 3. Xiaomi Mi 11 | 10.000$" \
           "\n&#12288;💎 4. Samsung Galaxy S21 | 50.000$" \
           "\n&#12288;💎 5. iPhone 12 | 200.000$" \
           "\n" \
           "\n📌 Для покупки телефона используйте 'ктел [номер]'\n" \
           "Например: ктел 1"

def homes():
    return "🏡 Дома:" \
           "\n" \
           "\n&#12288;💎 1. Картонная коробка | 100$" \
           "\n&#12288;💎 2. Дом на дереве | 2.000$" \
           "\n&#12288;💎 3. Деревянный дом | 10.000$" \
           "\n&#12288;💎 4. Квартира в новостройке | 50.000$" \
           "\n&#12288;💎 5. Особняк | 150.000$" \
           "\n&#12288;💎 6. Дом на Рублёвке | 300.000$" \
           "\n&#12288;💎 7. Личный остров | 500.000$" \
           "\n&#12288;💎 8. Дворец в Геленджике | 1.000.000$" \
           "\n" \
           "\n📌 Для покупки транспорта используйте 'кдом [номер]'\n" \
           "Например: кдом 1"

def bcar(id, n):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["car"] == "":
        if n == '1' and ff["balance"] >= 2000:
            ff["balance"] -= 2000
            ff["car"] = "ВАЗ 2115"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["car"]) + " за 2.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif n == '2' and ff["balance"] >= 4000:
            ff["balance"] -= 4000
            ff["car"] = "LADA Vesta"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["car"]) + " за 4.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif n == '3' and ff["balance"] >= 8000:
            ff["balance"] -= 8000
            ff["car"] = "Audi Q7"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["car"]) + " за 8.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif n == '4' and ff["balance"] >= 15000:
            ff["balance"] -= 15000
            ff["car"] = "BMW M8"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["car"]) + " за 15.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif n == '5' and ff["balance"] >= 50000:
            ff["balance"] -= 50000
            ff["car"] = "Range Rover"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["car"]) + " за 50.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif n == '6' and ff["balance"] >= 150000:
            ff["balance"] -= 150000
            ff["car"] = "Rolls-Royce"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["car"]) + " за 150.000$\nВаш баланс: " + str(ff["balance"]) + "$"
        else:
            return "У вас не хватает денег или вы неправильно используете команду!\nПример: кмашину 1"
    else:
        return "У вас уже есть машина или вы неправильно используете команду!\nПример: кмашину 1\nЧтобы продать её, используйте 'пмашину'"

def sellcar(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["car"] != "":
        if ff["car"] == "ВАЗ 2115":
            ff["car"] = ""
            ff["balance"] += 2000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою машину за 2.000$\nВаш баланс: " + str(ff["balance"]) + "$"
        if ff["car"] == "LADA Vesta":
            ff["car"] = ""
            ff["balance"] += 4000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою машину за 4.000$\nВаш баланс: " + str(ff["balance"]) + "$"
        if ff["car"] == "Audi Q7":
            ff["car"] = ""
            ff["balance"] += 8000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою машину за 8.000$\nВаш баланс: " + str(ff["balance"]) + "$"
        if ff["car"] == "BMW M8":
            ff["car"] = ""
            ff["balance"] += 15000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою машину за 15.000$\nВаш баланс: " + str(ff["balance"]) + "$"
        if ff["car"] == "Range Rover":
            ff["car"] = ""
            ff["balance"] += 50000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою машину за 50.000$\nВаш баланс: " + str(ff["balance"]) + "$"
        if ff["car"] == "Rolls-Royce":
            ff["car"] = ""
            ff["balance"] += 150000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою машину за 150.000$\nВаш баланс: " + str(ff["balance"]) + "$"
    else:
        return 'У вас нет машины!'
#машины

#телефоны
def bphone(id, n):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["phone"] == "":
        if n == '1' and ff["balance"] >= 200:
            ff["balance"] -= 200
            ff["phone"] = "Fly Ezzy Flip"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["phone"]) + " за 200$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif n == '2' and ff["balance"] >= 1000:
            ff["balance"] -= 1000
            ff["phone"] = "Sony Xperia XA1"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["phone"]) + " за 1.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif n == '3' and ff["balance"] >= 10000:
            ff["balance"] -= 10000
            ff["phone"] = "Xiaomi Mi 11"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["phone"]) + " за 10.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif n == '4' and ff["balance"] >= 50000:
            ff["balance"] -= 50000
            ff["phone"] = "Samsung Galaxy S21"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["phone"]) + " за 50.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif n == '5' and ff["balance"] >= 200000:
            ff["balance"] -= 200000
            ff["phone"] = "iPhone 12"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["phone"]) + " за 200.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        else:
            return "У вас не хватает денег или вы неправильно используете команду!\nПример: ктел 1"
    else:
        return "У вас уже есть телефон или вы неправильно используете команду!\nПример: ктел 1\nЧтобы продать его, используйте 'птел'"

def sellphone(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["phone"] != "":
        if ff["phone"] == "Fly Ezzy Flip":
            ff["balance"] += 200
            ff["phone"] = ""
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свой телефон за 200$\nВаш баланс: " + str(ff["balance"]) + "$"

        if ff["phone"] == "Sony Xperia XA1":
            ff["phone"] = ""
            ff["balance"] += 1000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свой телефон за 1.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        if ff["phone"] == "Xiaomi Mi 11":
            ff["phone"] = ""
            ff["balance"] += 10000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свой телефон за 10.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        if ff["phone"] == "Samsung Galaxy S21":
            ff["phone"] = ""
            ff["balance"] += 50000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свой телефон за 50.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        if ff["phone"] == "iPhone 12":
            ff["phone"] = ""
            ff["balance"] += 200000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свой телефон за 200.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        if ff["phone"] == "iPhone 12 Gold Edition":
            ff["phone"] = ""
            ff["balance"] += 1000000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свой телефон за 1.000.000$\nВаш баланс: " + str(ff["balance"]) + "$"
    
    else:
        return 'У вас нет телефона!'
#телефоны

#дома
def bhome(id, n):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["home"] == "":
        if n == '1' and ff["balance"] >= 100:
            ff["balance"] -= 100
            ff["home"] = "Картонная коробка"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["home"]) + " за 100$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif n == '2' and ff["balance"] >= 2000:
            ff["balance"] -= 2000
            ff["home"] = "Дом на дереве"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["home"]) + " за 2.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif n == '3' and ff["balance"] >= 10000:
            ff["balance"] -= 10000
            ff["home"] = "Деревянный дом"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["home"]) + " за 10.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif n == '4' and ff["balance"] >= 50000:
            ff["balance"] -= 50000
            ff["home"] = "Квартира в новостройке"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["home"]) + " за 50.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif n == '5' and ff["balance"] >= 150000:
            ff["balance"] -= 150000
            ff["home"] = "Особняк"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["home"]) + " за 150.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif n == '6' and ff["balance"] >= 300000:
            ff["balance"] -= 300000
            ff["home"] = "Дом на Рублёвке"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["home"]) + " за 300.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif n == '7' and ff["balance"] >= 500000:
            ff["balance"] -= 500000
            ff["home"] = "Личный остров"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["home"]) + " за 500.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif n == '8' and ff["balance"] >= 1000000:
            ff["balance"] -= 1000000
            ff["home"] = "Дворец в Геленджике"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            congrts(id)
            return "Вы купили " + str(ff["home"]) + " за 1.000.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        else:
            return "У вас не хватает денег или вы неправильно используете команду!\nПример: кдом 1"
    else:
        return "У вас уже есть дом или вы неправильно используете команду!\nПример: кдом 1\nЧтобы продать его, используйте 'пдом'"

def sellhome(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["home"] != "":
        if ff["home"] == "Картонная коробка":
            ff["balance"] += 100
            ff["home"] = ""
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свой дом за 100$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["home"] == "Дом на дереве":
            ff["home"] = ""
            ff["balance"] += 2000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свой дом за 2.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["home"] == "Деревянный дом":
            ff["home"] = ""
            ff["balance"] += 10000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свой дом за 10.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["home"] == "Квартира в новостройке":
            ff["home"] = ""
            ff["balance"] += 50000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свой дом за 50.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["home"] == "Особняк":
            ff["home"] = ""
            ff["balance"] += 150000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свой дом за 150.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["home"] == "Дом на Рублёвке":
            ff["home"] = ""
            ff["balance"] += 300000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свой дом за 300.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["home"] == "Личный остров":
            ff["home"] = ""
            ff["balance"] += 500000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свой дом за 500.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["home"] == "Дворец в Геленджике":
            ff["home"] = ""
            ff["balance"] += 1000000
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свой дом за 1.000.000$\nВаш баланс: " + str(ff["balance"]) + "$"
    else:
        return 'У вас нет дома!'
#дома
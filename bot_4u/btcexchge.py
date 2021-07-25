import json

def bal(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    return '💰Ваш баланс: ' + str(ff["balance"]) + "$\n💴 Биткоины: " + str(round(ff["btc"],5)) + " ₿"

def btcrateshow():
    return "📈 Курс биткоина на данный момент - 1000$ за 1₿"

def btctousd(id, n):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if n == "все" or n == "всё":
        n = round(ff["btc"],5)
    if float(n) <= ff["btc"] and float(n) > 0:
        temp = float(n) * 10000
        ff["btc"] -= float(n)
        ff["balance"] += int(float(n) * 10000)
        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(ff, indent=4))
        return "Вы успешно перевели " + str(n) + "₿ в " + str(int(temp)) + "$\n" + bal(id)
    return "У вас недостаточно биткоинов или вы ввели 0\n" + bal(id)

def usdtobtc(id, n):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if n == "все" or n == "всё":
        n = int(ff["balance"] / 10000)
    temp = int(float(n) * 10000)  # в $
    if temp <= ff["balance"] and float(n) > 0:
        ff["btc"] += round(float(n),5)
        ff["balance"] -= temp
        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(ff, indent=4))
        return "Вы успешно купили " + str(round(float(n),5)) + "₿ за " + str(temp) + "$\n" + str(bal(id))
    else:
        return "У вас недостаточно денег или вы ввели 0\n" + bal(id)
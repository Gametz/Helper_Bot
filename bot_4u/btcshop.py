import json

def congrts(id):
    vk.method("messages.send", {"peer_id": id,
                                "sticker_id": 11788,
                                "random_id": random.randint(1, 2147483647)})

def fshop():
    return "Магазин видеокарт" \
           "\nНазвание | Добыча | Стоимость" \
           "\n" \
           "\nNvidia:" \
           "\n&#12288;💎 1. GF 210 | 0.00025 ₿ | 10.000$" \
           "\n&#12288;💎 2. GF GTX 750 Ti | 0.0005 ₿ | 50.000$" \
           "\n&#12288;💎 3. GF GTX 1050 Ti | 0.001 ₿ | 100.000$" \
           "\n&#12288;💎 4. GF GTX 1660S | 0.005 ₿ | 300.000$" \
           "\n&#12288;💎 5. GF RTX 2080S | 0.01 ₿ | 500.000$" \
           "\n&#12288;💎 6. GF RTX 3090 Mining ver | 0.05 ₿ | 1.500.000$" \
           "\n" \
           "\nAMD:" \
           "\n&#12288;💎 7. R5 220 | 0.00025 ₿ | 10.000$" \
           "\n&#12288;💎 8. R7 360 | 0.0005 ₿ | 50.000$" \
           "\n&#12288;💎 9. R9 380 | 0.001 ₿ | 100.000$" \
           "\n&#12288;💎 10. RX 580 | 0.005 ₿ | 300.000$" \
           "\n&#12288;💎 11. RX5700 | 0.01 ₿ | 500.000$" \
           "\n&#12288;💎 12. RX6900XT | 0.05 ₿ | 1.500.000$" \
           "\n" \
           "\n📌 Для покупки видеокарты используйте 'ккарту [номер]" \
           "\n❗ Максимальное кол-во видеокарт - 5"

def bfarm(id, n):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
        if ff["gpu_amount"] < 5:
            if n == "1" or n == "7": p = 10000
            elif n == "2" or n == "8": p = 50000
            elif n == "3" or n == "9": p = 100000
            elif n == "4" or n == "10": p = 300000
            elif n == "5" or n == "11": p = 500000
            elif n == "6" or n == "12": p = 1500000

            if n == '1' and ff["balance"] >= p:
                if ff["gpu"] == "GF 210" or ff["gpu"] == "":
                    ff["balance"] -= p
                    ff["gpu"] = "GF 210"
                    ff["gpu_amount"] += 1
                    ff["farm"] = 0.00025
                    ff["farming"] = True
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    congrts(id)
                    return "Вы купили " + str(ff["gpu"]) + " за " + str(p) + "$\nВаш баланс: " + str(ff["balance"]) + "$"
                else:
                    return "Вы можете купить только несколько одинаковых видеокарт"

            elif n == '2' and ff["balance"] >= p:
                if ff["gpu"] == "GF GTX 750 Ti" or ff["gpu"] == "":
                    ff["balance"] -= p
                    ff["gpu"] = "GF GTX 750 Ti"
                    ff["gpu_amount"] += 1
                    ff["farm"] = 0.0005
                    ff["farming"] = True
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    congrts(id)
                    return "Вы купили " + str(ff["gpu"]) + " за " + str(p) + "$\nВаш баланс: " + str(ff["balance"]) + "$"
                else:
                    return "Вы можете купить только несколько одинаковых видеокарт"

            elif n == '3' and ff["balance"] >= p:
                if ff["gpu"] == "GF GTX 1050 Ti" or ff["gpu"] == "":
                    ff["balance"] -= p
                    ff["gpu"] = "GF GTX 1050 Ti"
                    ff["gpu_amount"] += 1
                    ff["farm"] = 0.001
                    ff["farming"] = True
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    congrts(id)
                    return "Вы купили " + str(ff["gpu"]) + " за " + str(p) + "$\nВаш баланс: " + str(ff["balance"]) + "$"
                else:
                    return "Вы можете купить только несколько одинаковых видеокарт"

            elif n == '4' and ff["balance"] >= p:
                if ff["gpu"] == "GF GTX 1660S" or ff["gpu"] == "":
                    ff["balance"] -= p
                    ff["gpu"] = "GF GTX 1660S"
                    ff["gpu_amount"] += 1
                    ff["farm"] = 0.005
                    ff["farming"] = True
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    congrts(id)
                    return "Вы купили " + str(ff["gpu"]) + " за " + str(p) + "$\nВаш баланс: " + str(ff["balance"]) + "$"
                else:
                    return "Вы можете купить только несколько одинаковых видеокарт"

            elif n == '5' and ff["balance"] >= p:
                if ff["gpu"] == "GF RTX 2080S" or ff["gpu"] == "":
                    ff["balance"] -= p
                    ff["gpu"] = "GF RTX 2080S"
                    ff["gpu_amount"] += 1
                    ff["farm"] = 0.01
                    ff["farming"] = True
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    congrts(id)
                    return "Вы купили " + str(ff["gpu"]) + " за " + str(p) + "$\nВаш баланс: " + str(ff["balance"]) + "$"
                else:
                    return "Вы можете купить только несколько одинаковых видеокарт"

            elif n == '6' and ff["balance"] >= p:
                if ff["gpu"] == "GF RTX 3090 Mining ver" or ff["gpu"] == "":
                    ff["balance"] -= p
                    ff["gpu"] = "GF RTX 3090 Mining ver"
                    ff["gpu_amount"] += 1
                    ff["farm"] = 0.05
                    ff["farming"] = True
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    congrts(id)
                    return "Вы купили " + str(ff["gpu"]) + " за " + str(p) + "$\nВаш баланс: " + str(ff["balance"]) + "$"
                else:
                    return "Вы можете купить только несколько одинаковых видеокарт"

            elif n == '7' and ff["balance"] >= p:
                if ff["gpu"] == "R5 220" or ff["gpu"] == "":
                    ff["balance"] -= p
                    ff["gpu"] = "R5 220"
                    ff["gpu_amount"] += 1
                    ff["farm"] = 0.00025
                    ff["farming"] = True
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    congrts(id)
                    return "Вы купили " + str(ff["gpu"]) + " за " + str(p) + "$\nВаш баланс: " + str(ff["balance"]) + "$"
                else:
                    return "Вы можете купить только несколько одинаковых видеокарт"

            elif n == '8' and ff["balance"] >= p:
                if ff["gpu"] == "R7 360" or ff["gpu"] == "":
                    ff["balance"] -= p
                    ff["gpu"] = "R7 360"
                    ff["gpu_amount"] += 1
                    ff["farm"] = 0.0005
                    ff["farming"] = True
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    congrts(id)
                    return "Вы купили " + str(ff["gpu"]) + " за " + str(p) + "$\nВаш баланс: " + str(ff["balance"]) + "$"
                else:
                    return "Вы можете купить только несколько одинаковых видеокарт"

            elif n == '9' and ff["balance"] >= p:
                if ff["gpu"] == "R9 380" or ff["gpu"] == "":
                    ff["balance"] -= p
                    ff["gpu"] = "R9 380"
                    ff["gpu_amount"] += 1
                    ff["farm"] = 0.001
                    ff["farming"] = True
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    congrts(id)
                    return "Вы купили " + str(ff["gpu"]) + " за " + str(p) + "$\nВаш баланс: " + str(ff["balance"]) + "$"
                else:
                    return "Вы можете купить только несколько одинаковых видеокарт"

            elif n == '10' and ff["balance"] >= p:
                if ff["gpu"] == "RX 580" or ff["gpu"] == "":
                    ff["balance"] -= p
                    ff["gpu"] = "RX 580"
                    ff["gpu_amount"] += 1
                    ff["farm"] = 0.005
                    ff["farming"] = True
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    congrts(id)
                    return "Вы купили " + str(ff["gpu"]) + " за " + str(p) + "$\nВаш баланс: " + str(ff["balance"]) + "$"
                else:
                    return "Вы можете купить только несколько одинаковых видеокарт"

            elif n == '11' and ff["balance"] >= p:
                if ff["gpu"] == "RX5700" or ff["gpu"] == "":
                    ff["balance"] -= p
                    ff["gpu"] = "RX5700"
                    ff["gpu_amount"] += 1
                    ff["farm"] = 0.01
                    ff["farming"] = True
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    congrts(id)
                    return "Вы купили " + str(ff["gpu"]) + " за " + str(p) + "$\nВаш баланс: " + str(ff["balance"]) + "$"
                else:
                    return "Вы можете купить только несколько одинаковых видеокарт"

            elif n == '12' and ff["balance"] >= p:
                if ff["gpu"] == "RX6900XT" or ff["gpu"] == "":
                    ff["balance"] -= p
                    ff["gpu"] = "RX6900XT"
                    ff["gpu_amount"] += 1
                    ff["farm"] = 0.05
                    ff["farming"] = True
                    with open('json/' + str(id) + '.json', 'w') as f:
                        f.write(json.dumps(ff, indent=4))
                    congrts(id)
                    return "Вы купили " + str(ff["gpu"]) + " за " + str(p) + "$\nВаш баланс: " + str(ff["balance"]) + "$"
                else:
                    return "Вы можете купить только несколько одинаковых видеокарт"

            else:
                return "У вас не хватает денег или вы неправильно используете команду!\nПример: ккарту 1"
        else:
            return "У вас максимальное кол-во видеокарт - 5"

def sfarm(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["gpu"] != "":
        if ff["gpu"] == "GF 210":
            ff["balance"] += 10000
            if ff["gpu_amount"] == 1:
                ff["gpu"] = ""
            ff["gpu_amount"] -= 1
            ff["farm"] = 0.0
            ff["farming"] = False
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою видеокарту за 1000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["gpu"] == "GF GTX 750 Ti":
            if ff["gpu_amount"] == 1:
                ff["gpu"] = ""
            ff["gpu_amount"] -= 1
            ff["balance"] += 50000
            ff["farm"] = 0.0
            ff["farming"] = False
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою видеокарту за 50.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["gpu"] == "GF GTX 1050 Ti":
            if ff["gpu_amount"] == 1:
                ff["gpu"] = ""
            ff["gpu_amount"] -= 1
            ff["balance"] += 100000
            ff["farm"] = 0.0
            ff["farming"] = False
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою видеокарту за 100.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["gpu"] == "GF GTX 1660S":
            if ff["gpu_amount"] == 1:
                ff["gpu"] = ""
            ff["gpu_amount"] -= 1
            ff["balance"] += 300000
            ff["farm"] = 0.0
            ff["farming"] = False
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою видеокарту за 300.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["gpu"] == "GF RTX 2080S":
            if ff["gpu_amount"] == 1:
                ff["gpu"] = ""
            ff["gpu_amount"] -= 1
            ff["balance"] += 500000
            ff["farm"] = 0.0
            ff["farming"] = False
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою видеокарту за 500.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["gpu"] == "GF RTX 3090 Mining ver":
            if ff["gpu_amount"] == 1:
                ff["gpu"] = ""
            ff["gpu_amount"] -= 1
            ff["balance"] += 1500000
            ff["farm"] = 0.0
            ff["farming"] = False
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою видеокарту за 1.500.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["gpu"] == "R5 220":
            ff["balance"] += 10000
            if ff["gpu_amount"] == 1:
                ff["gpu"] = ""
            ff["gpu_amount"] -= 1
            ff["farm"] = 0.0
            ff["farming"] = False
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою видеокарту за 1000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["gpu"] == "R7 360":
            if ff["gpu_amount"] == 1:
                ff["gpu"] = ""
            ff["gpu_amount"] -= 1
            ff["balance"] += 50000
            ff["farm"] = 0.0
            ff["farming"] = False
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою видеокарту за 50.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["gpu"] == "R9 380":
            if ff["gpu_amount"] == 1:
                ff["gpu"] = ""
            ff["gpu_amount"] -= 1
            ff["balance"] += 100000
            ff["farm"] = 0.0
            ff["farming"] = False
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою видеокарту за 100.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["gpu"] == "RX 580":
            if ff["gpu_amount"] == 1:
                ff["gpu"] = ""
            ff["gpu_amount"] -= 1
            ff["balance"] += 300000
            ff["farm"] = 0.0
            ff["farming"] = False
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою видеокарту за 300.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["gpu"] == "RX5700":
            if ff["gpu_amount"] == 1:
                ff["gpu"] = ""
            ff["gpu_amount"] -= 1
            ff["balance"] += 500000
            ff["farm"] = 0.0
            ff["farming"] = False
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою видеокарту за 500.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["gpu"] == "RX6900XT":
            if ff["gpu_amount"] == 1:
                ff["gpu"] = ""
            ff["gpu_amount"] -= 1
            ff["balance"] += 1500000
            ff["farm"] = 0.0
            ff["farming"] = False
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою видеокарту за 1.500.000$\nВаш баланс: " + str(ff["balance"]) + "$"

        elif ff["gpu"] == "nVidia Tesla A100":
            if ff["gpu_amount"] == 1:
                ff["gpu"] = ""
            ff["gpu_amount"] -= 1
            ff["balance"] += 5000000
            ff["farm"] = 0.0
            ff["farming"] = False
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "Вы продали свою видеокарту за 5.000.000$\nВаш баланс: " + str(ff["balance"]) + "$"
    else:
        return 'У вас нет видеокарты!'
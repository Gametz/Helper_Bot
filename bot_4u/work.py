import json

def hwork(id,work):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["work"] == "":
        if work == "1" and ff["level"] >= 1:
            ff["work"] = "FakeTAXI"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "✅ Поздравляем! Теперь ваша работа " + ff["work"]

        elif work == "2" and ff["level"] >= 1:
            ff["work"] = "Ферма"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "✅ Поздравляем! Теперь ваша работа " + ff["work"]

        elif work == "3" and ff["level"] >= 2:
            ff["work"] = "Тестировщик игр"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "✅ Поздравляем! Теперь ваша работа " + ff["work"]

        elif work == "4" and ff["level"] >= 2:
            ff["work"] = "Работник кофейни"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "✅ Поздравляем! Теперь ваша работа " + ff["work"]

        elif work == "5" and ff["level"] >= 3:
            ff["work"] = "Рабочий на заводе"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "✅ Поздравляем! Теперь ваша работа " + ff["work"]

        elif work == "6" and ff["level"] >= 3:
            ff["work"] = "Дегустатор вина"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "✅ Поздравляем! Теперь ваша работа " + ff["work"]

        elif work == "7" and ff["level"] >= 4:
            ff["work"] = "Продавец в Verdax"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "✅ Поздравляем! Теперь ваша работа " + ff["work"]

        elif work == "8" and ff["level"] >= 4:
            ff["work"] = "Дизайнер"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "✅ Поздравляем! Теперь ваша работа " + ff["work"]

        elif work == "9" and ff["level"] >= 5:
            ff["work"] = "Режиссёр Аниме"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "✅ Поздравляем! Теперь ваша работа " + ff["work"]

        elif work == "10" and ff["level"] >= 5:
            ff["work"] = "Директор Natflex"
            with open('json/' + str(id) + '.json', 'w') as f:
                f.write(json.dumps(ff, indent=4))
            return "✅ Поздравляем! Теперь ваша работа " + ff["work"]

        else:
            return "⚠ Недостаточный уровень или неправильно выбрана работа\nПример: устроиться 1"
    else:
        return "⚠ Вы уже устроены на работу!\n'уволиться' - чтобы стать безработным"

def dwork(id):
    with open('json/' + str(id) + '.json') as f:
        ff = json.loads(f.read())
    if ff["work"] != "":
        ff["work"] = ""
        with open('json/' + str(id) + '.json', 'w') as f:
            f.write(json.dumps(ff, indent=4))
        return "✅ Теперь вы безработный"
    else:
        return "⚠ Вы нигде не работаете"
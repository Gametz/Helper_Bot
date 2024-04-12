import json

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
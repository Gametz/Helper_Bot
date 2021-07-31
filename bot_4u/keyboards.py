import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from bot_4u.config import *

def mainmenu(id):
    mainmenu = VkKeyboard(one_time=False)
    mainmenu.add_button(label="Профиль")
    mainmenu.add_line()
    mainmenu.add_button(label="Бонус", color=VkKeyboardColor.PRIMARY)
    mainmenu.add_button(label="Банк")
    mainmenu.add_button(label="Баланс", color=VkKeyboardColor.POSITIVE)
    mainmenu.add_line()
    mainmenu.add_button(label="Магазин")
    mainmenu.add_button(label="Работа")
    mainmenu.add_button(label="Игры")
    mainmenu.add_line()
    mainmenu.add_button(label="Ферма")
    mainmenu.add_button(label="Стата")
    mainmenu.add_button(label="Топ")
    mainmenu.add_line()
    if id in admins or id in moders:
        mainmenu.add_button(label="Админпанель", color=VkKeyboardColor.NEGATIVE)
        mainmenu.add_button(label="Хакерство", color=VkKeyboardColor.PRIMARY)
        mainmenu.add_button(label="Команды", color=VkKeyboardColor.SECONDARY)
    else:
        mainmenu.add_button(label="Команды", color=VkKeyboardColor.SECONDARY)
    return mainmenu

def mainworkmenu():
    mainworkmenu = VkKeyboard(one_time=False)
    mainworkmenu.add_button(label="Работать")
    mainworkmenu.add_line()
    mainworkmenu.add_button(label="Устроиться", color=VkKeyboardColor.PRIMARY)
    mainworkmenu.add_line()
    mainworkmenu.add_button(label="Уволиться", color=VkKeyboardColor.NEGATIVE)
    mainworkmenu.add_line()
    mainworkmenu.add_button(label="Уровни")
    mainworkmenu.add_line()
    mainworkmenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    return mainworkmenu

def worksmenu():
    worksmenu = VkKeyboard(one_time=False)
    worksmenu.add_button(label="Устроиться 1")
    worksmenu.add_button(label="Устроиться 2")
    worksmenu.add_line()
    worksmenu.add_button(label="Устроиться 3")
    worksmenu.add_button(label="Устроиться 4")
    worksmenu.add_line()
    worksmenu.add_button(label="Устроиться 5")
    worksmenu.add_button(label="Устроиться 6")
    worksmenu.add_line()
    worksmenu.add_button(label="Устроиться 7")
    worksmenu.add_button(label="Устроиться 8")
    worksmenu.add_line()
    worksmenu.add_button(label="Устроиться 9")
    worksmenu.add_button(label="Устроиться 10")
    worksmenu.add_line()
    worksmenu.add_button(label="⬅ Работа", color=VkKeyboardColor.PRIMARY)
    worksmenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    return worksmenu

def shopmenu():
    shopmenu = VkKeyboard(one_time=False)
    shopmenu.add_button(label="Машины")
    shopmenu.add_line()
    shopmenu.add_button(label="Телефоны")
    shopmenu.add_line()
    shopmenu.add_button(label="Дома")
    shopmenu.add_line()
    shopmenu.add_button(label="Видеокарты")
    shopmenu.add_line()
    shopmenu.add_button(label="Биткоины")
    shopmenu.add_line()
    shopmenu.add_button(label="Продать", color=VkKeyboardColor.NEGATIVE)
    shopmenu.add_line()
    shopmenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    return shopmenu

def carsmenu():
    carsmenu = VkKeyboard(one_time=False)
    carsmenu.add_button(label="Кмашину 1")
    carsmenu.add_button(label="Кмашину 2")
    carsmenu.add_button(label="Кмашину 3")
    carsmenu.add_line()
    carsmenu.add_button(label="Кмашину 4")
    carsmenu.add_button(label="Кмашину 5")
    carsmenu.add_button(label="Кмашину 6")
    carsmenu.add_line()
    carsmenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    carsmenu.add_button(label="⬅ Магазин", color=VkKeyboardColor.PRIMARY)
    return carsmenu

def phonemenu():
    phonemenu = VkKeyboard(one_time=False)
    phonemenu.add_button(label="Ктел 1")
    phonemenu.add_button(label="Ктел 2")
    phonemenu.add_button(label="Ктел 3")
    phonemenu.add_line()
    phonemenu.add_button(label="Ктел 4")
    phonemenu.add_button(label="Ктел 5")
    phonemenu.add_line()
    phonemenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    phonemenu.add_button(label="⬅ Магазин", color=VkKeyboardColor.PRIMARY)
    return phonemenu

def homemenu():
    homemenu = VkKeyboard(one_time=False)
    homemenu.add_button(label="Кдом 1")
    homemenu.add_button(label="Кдом 2")
    homemenu.add_button(label="Кдом 3")
    homemenu.add_line()
    homemenu.add_button(label="Кдом 4")
    homemenu.add_button(label="Кдом 5")
    homemenu.add_button(label="Кдом 6")
    homemenu.add_line()
    homemenu.add_button(label="Кдом 7")
    homemenu.add_button(label="Кдом 8")
    homemenu.add_line()
    homemenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    homemenu.add_button(label="⬅ Магазин", color=VkKeyboardColor.PRIMARY)
    return homemenu

def gpumenu():
    gpumenu = VkKeyboard(one_time=False)
    gpumenu.add_button(label="Ккарту 1")
    gpumenu.add_button(label="Ккарту 2")
    gpumenu.add_button(label="Ккарту 3")
    gpumenu.add_line()
    gpumenu.add_button(label="Ккарту 4")
    gpumenu.add_button(label="Ккарту 5")
    gpumenu.add_button(label="Ккарту 6")
    gpumenu.add_line()
    gpumenu.add_button(label="Пкарту", color=VkKeyboardColor.NEGATIVE)
    gpumenu.add_line()
    gpumenu.add_button(label="Ккарту 7")
    gpumenu.add_button(label="Ккарту 8")
    gpumenu.add_button(label="Ккарту 9")
    gpumenu.add_line()
    gpumenu.add_button(label="Ккарту 10")
    gpumenu.add_button(label="Ккарту 11")
    gpumenu.add_button(label="Ккарту 12")
    gpumenu.add_line()
    gpumenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    gpumenu.add_button(label="⬅ Магазин", color=VkKeyboardColor.PRIMARY)
    return gpumenu

def sellmenu():
    sellmenu = VkKeyboard(one_time=False)
    sellmenu.add_button(label="Пмашину", color=VkKeyboardColor.NEGATIVE)
    sellmenu.add_line()
    sellmenu.add_button(label="Птел", color=VkKeyboardColor.NEGATIVE)
    sellmenu.add_line()
    sellmenu.add_button(label="Пдом", color=VkKeyboardColor.NEGATIVE)
    sellmenu.add_line()
    sellmenu.add_button(label="Пкарту", color=VkKeyboardColor.NEGATIVE)
    sellmenu.add_line()
    sellmenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    sellmenu.add_button(label="⬅ Магазин", color=VkKeyboardColor.PRIMARY)
    return sellmenu

def farmmenu():
    farmmenu = VkKeyboard(one_time=False)
    farmmenu.add_button(label="Сбитки")
    farmmenu.add_line()
    farmmenu.add_button(label="♻ Обновить")
    farmmenu.add_line()
    farmmenu.add_button(label="Биткоины")
    farmmenu.add_line()
    farmmenu.add_button(label="Видеокарты", color=VkKeyboardColor.PRIMARY)
    farmmenu.add_line()
    farmmenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    return farmmenu

def adminmenu():
    adminmenu = VkKeyboard(one_time=False)
    adminmenu.add_button(label="Пoлная накрутка", color=VkKeyboardColor.POSITIVE)
    adminmenu.add_button(label="Oбнуление", color=VkKeyboardColor.NEGATIVE)
    adminmenu.add_line()
    adminmenu.add_button(label="Сбал 1000000")
    adminmenu.add_line()
    adminmenu.add_button(label="Сбитк 5000")
    adminmenu.add_line()
    adminmenu.add_button(label="Слвл 5")
    adminmenu.add_line()
    adminmenu.add_button(label="Сопыт 500")
    adminmenu.add_line()
    adminmenu.add_button(label="Users")
    adminmenu.add_line()
    adminmenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    return adminmenu

def monetkasidemenu():
    monetkasidemenu = VkKeyboard(one_time=False, inline=True)
    monetkasidemenu.add_button(label="Орел")
    monetkasidemenu.add_button(label="Решка")
    return monetkasidemenu

def monetkaorelmenu():
    monetkaorelmenu = VkKeyboard(one_time=False)
    monetkaorelmenu.add_button(label="Монетка орел 1000")
    monetkaorelmenu.add_button(label="Монетка орел 10000")
    monetkaorelmenu.add_line()
    monetkaorelmenu.add_button(label="Монетка орел 100000")
    monetkaorelmenu.add_button(label="Монетка орел 500000")
    monetkaorelmenu.add_line()
    monetkaorelmenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    monetkaorelmenu.add_button(label="⬅ Игры", color=VkKeyboardColor.PRIMARY)
    return monetkaorelmenu

def monetkareshkamenu():
    monetkareshkamenu = VkKeyboard(one_time=False)
    monetkareshkamenu.add_button(label="Монетка решка 1000")
    monetkareshkamenu.add_button(label="Монетка решка 10000")
    monetkareshkamenu.add_line()
    monetkareshkamenu.add_button(label="Монетка решка 100000")
    monetkareshkamenu.add_button(label="Монетка решка 500000")
    monetkareshkamenu.add_line()
    monetkareshkamenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    monetkareshkamenu.add_button(label="⬅ Игры", color=VkKeyboardColor.PRIMARY)
    return monetkareshkamenu

def kazmenu():
    kazmenu = VkKeyboard(one_time=False)
    kazmenu.add_button(label="Казино всё")
    kazmenu.add_button(label="Казино половина")
    kazmenu.add_line()
    kazmenu.add_button(label="Казино 1000")
    kazmenu.add_button(label="Казино 50000")
    kazmenu.add_line()
    kazmenu.add_button(label="Казино 100000")
    kazmenu.add_button(label="Казино 500000")
    kazmenu.add_line()
    kazmenu.add_button(label="Казино 1000000")
    kazmenu.add_button(label="Казино 5000000")
    kazmenu.add_line()
    kazmenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    kazmenu.add_button(label="⬅ Игры", color=VkKeyboardColor.PRIMARY)
    return kazmenu

def gamesmenu():
    gamesmenu = VkKeyboard(one_time=False)
    gamesmenu.add_button(label="Монетка")
    gamesmenu.add_button(label="Казино")
    gamesmenu.add_line()
    gamesmenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    return gamesmenu

def btcmenu():
    btcmenu = VkKeyboard(one_time=False)
    btcmenu.add_button(label="Кбитк все", color=VkKeyboardColor.POSITIVE)
    btcmenu.add_line()
    btcmenu.add_button(label="Кбитк 1")
    btcmenu.add_button(label="Кбитк 10")
    btcmenu.add_button(label="Кбитк 100")
    btcmenu.add_line()
    btcmenu.add_button(label="Пбитк все", color=VkKeyboardColor.NEGATIVE)
    btcmenu.add_line()
    btcmenu.add_button(label="Пбитк 1")
    btcmenu.add_button(label="Пбитк 10")
    btcmenu.add_button(label="Пбитк 100")
    btcmenu.add_line()
    btcmenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    return btcmenu

def bankmenu():
    bankmenu = VkKeyboard(one_time=False)
    bankmenu.add_button(label="Банк положить всё", color=VkKeyboardColor.PRIMARY)
    bankmenu.add_button(label="Банк положить половину", color=VkKeyboardColor.PRIMARY)
    bankmenu.add_line()
    bankmenu.add_button(label="Банк снять всё", color=VkKeyboardColor.POSITIVE)
    bankmenu.add_button(label="Банк снять половину", color=VkKeyboardColor.POSITIVE)
    bankmenu.add_line()
    bankmenu.add_button(label="Банк баланс")
    bankmenu.add_line()
    bankmenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    return bankmenu

def topmenu():
    topmenu = VkKeyboard(one_time=False)
    topmenu.add_button(label="Балтоп")
    topmenu.add_button(label="Битктоп")
    topmenu.add_line()
    topmenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    return topmenu
    # Хакерство

def mainhackmenu():
    mainhackmenu = VkKeyboard(one_time=False)
    mainhackmenu.add_button(label="Битва")
    mainhackmenu.add_line()
    mainhackmenu.add_button(label="Улучшение")
    mainhackmenu.add_line()
    mainhackmenu.add_button(label="DarkShop", color=VkKeyboardColor.PRIMARY)
    mainhackmenu.add_line()
    mainhackmenu.add_button(label="🏠 Главное меню", color=VkKeyboardColor.POSITIVE)
    return mainhackmenu

def dsmenu():
    dsmenu = VkKeyboard(one_time=False)
    dsmenu.add_button(label="Компы")
    dsmenu.add_line()
    dsmenu.add_button(label="VPN")
    dsmenu.add_line()
    dsmenu.add_button(label="Убежища")
    dsmenu.add_line()
    dsmenu.add_button(label="Прoдать", color=VkKeyboardColor.NEGATIVE)
    dsmenu.add_line()
    dsmenu.add_button(label="🏠 Хакерство", color=VkKeyboardColor.POSITIVE)
    return dsmenu

def compmenu():
    compmenu = VkKeyboard(one_time=False)
    compmenu.add_button(label="Ккомп 1")
    compmenu.add_button(label="Ккомп 2")
    compmenu.add_button(label="Ккомп 3")
    compmenu.add_line()
    compmenu.add_button(label="Ккомп 4")
    compmenu.add_button(label="Ккомп 5")
    compmenu.add_line()
    compmenu.add_button(label="🏠 Хакерство", color=VkKeyboardColor.POSITIVE)
    compmenu.add_button(label="⬅ DarkShop", color=VkKeyboardColor.PRIMARY)
    return compmenu

def vpnmenu():
    vpnmenu = VkKeyboard(one_time=False)
    vpnmenu.add_button(label="Квпн 1")
    vpnmenu.add_button(label="Квпн 2")
    vpnmenu.add_button(label="Квпн 3")
    vpnmenu.add_line()
    vpnmenu.add_button(label="Квпн 4")
    vpnmenu.add_button(label="Квпн 5")
    vpnmenu.add_line()
    vpnmenu.add_button(label="🏠 Хакерство", color=VkKeyboardColor.POSITIVE)
    vpnmenu.add_button(label="⬅ DarkShop", color=VkKeyboardColor.PRIMARY)
    return vpnmenu

def shltrmenu():
    shltrmenu = VkKeyboard(one_time=False)
    shltrmenu.add_button(label="Кубежище 1")
    shltrmenu.add_button(label="Кубежище 2")
    shltrmenu.add_button(label="Кубежище 3")
    shltrmenu.add_line()
    shltrmenu.add_button(label="Кубежище 4")
    shltrmenu.add_button(label="Кубежище 5")
    shltrmenu.add_line()
    shltrmenu.add_button(label="🏠 Хакерство", color=VkKeyboardColor.POSITIVE)
    shltrmenu.add_button(label="⬅ DarkShop", color=VkKeyboardColor.PRIMARY)
    return shltrmenu

def selldarkmenu():
    selldarkmenu = VkKeyboard(one_time=False)
    selldarkmenu.add_button(label="Пкомп")
    selldarkmenu.add_line()
    selldarkmenu.add_button(label="Пвпн")
    selldarkmenu.add_line()
    selldarkmenu.add_button(label="Пубежище")
    selldarkmenu.add_line()
    selldarkmenu.add_button(label="🏠 Хакерство", color=VkKeyboardColor.POSITIVE)
    selldarkmenu.add_button(label="⬅ DarkShop", color=VkKeyboardColor.PRIMARY)
    return selldarkmenu

def uplmenu():
    uplmenu = VkKeyboard(one_time=False)
    uplmenu.add_button(label="💊 ХП")
    uplmenu.add_button(label="🔫 Урон")
    uplmenu.add_button(label="🕶 Защита")
    uplmenu.add_line()
    uplmenu.add_button(label="🏠 Хакерство", color=VkKeyboardColor.POSITIVE)
    return uplmenu

def phpmenu():
    phpmenu = VkKeyboard(one_time=False, inline=True)
    phpmenu.add_button(label="Прокачать ХП")
    return phpmenu

def pdefmenu():
    pdefmenu = VkKeyboard(one_time=False, inline=True)
    pdefmenu.add_button(label="Прокачать Защиту")
    return pdefmenu

def pdamagemenu():
    pdamagemenu = VkKeyboard(one_time=False, inline=True)
    pdamagemenu.add_button(label="Прокачать Урон")
    return pdamagemenu

def battlemenu():
    battlemenu = VkKeyboard(one_time=False)
    battlemenu.add_button(label="С Ботом", color=VkKeyboardColor.PRIMARY)
    battlemenu.add_button(label="В разработке...")
    battlemenu.add_line()
    battlemenu.add_button(label="🏠 Хакерство", color=VkKeyboardColor.POSITIVE)
    return battlemenu
    # Хакерство

def rework():
    errormenu = VkKeyboard(one_time=False, inline=True)
    errormenu.add_button(label="💻 Работать", color=VkKeyboardColor.POSITIVE)
    return errormenu

def errormenu():
    errormenu = VkKeyboard(one_time=False, inline=True)
    errormenu.add_button(label="Команды", color=VkKeyboardColor.POSITIVE)
    return errormenu

def bonusmenu():
    bonusmenu = VkKeyboard(one_time=False, inline=True)
    bonusmenu.add_button(label="Бонус", color=VkKeyboardColor.POSITIVE)
    return bonusmenu
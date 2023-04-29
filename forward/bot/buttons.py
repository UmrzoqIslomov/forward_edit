from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

from bot.Globals import TEXTS
from bot.models import Category, Subctg


def btns(type=None, lang=1, ctg=None, ctgs=None):
    btn = []
    if type == "menu":
        btn = [
            [KeyboardButton(TEXTS['Lokatsiya📍'][lang]), KeyboardButton(TEXTS['forward_academy.uz'][lang])],
            [KeyboardButton(TEXTS["Instagram"][lang]), KeyboardButton(TEXTS['Telegram'][lang])],
            [KeyboardButton(TEXTS["Telegram Support"][lang]), KeyboardButton(TEXTS['Call center'][lang])],
            [KeyboardButton(TEXTS['Testt'][lang])],
            [KeyboardButton(TEXTS['Settings'][lang])]
        ]

    elif type == 'contact':
        btn = [
            [KeyboardButton(TEXTS['CON'][lang], request_contact=True)]
        ]

    elif type == "lang":
        btn = [
            [KeyboardButton("🇺🇿Uz"), KeyboardButton("🇷🇺Ru"), KeyboardButton("🇺🇸En")],
        ]

    elif type == "langg":
        btn = [
            [KeyboardButton("🇺🇿 Uz"), KeyboardButton("🇷🇺 Ru"), KeyboardButton("🇺🇸 En")],
        ]

    elif type == "ctg":
        btn = []
        ctgs = Category.objects.all()
        for i in range(1, len(ctgs), 3):

            if lang == 1:
                btn1 = ctgs[i - 1].name_uz
            elif lang == 2:
                btn1 = ctgs[i - 1].name_ru
            else:
                btn1 = ctgs[i - 1].name_en

            if lang == 1:
                btn2 = ctgs[i].name_uz
            elif lang == 2:
                btn2 = ctgs[i].name_ru
            else:
                btn2 = ctgs[i].name_en
            btn.append([
                KeyboardButton(btn1), KeyboardButton(btn2)
            ])
        if len(ctgs) % 2:

            if lang == 1:
                btn1 = ctgs[len(ctgs) - 1].name_uz
            elif lang == 2:
                btn1 = ctgs[len(ctgs) - 1].name_ru
            else:
                btn1 = ctgs[len(ctgs) - 1].name_en
            btn.append([KeyboardButton(btn1)])

    elif type == "subctg":
        btn = []
        subctgs = Subctg.objects.filter(ctg=ctg)
        # subctgs = Subctg.objects.all()
        if not subctgs:
            return ReplyKeyboardMarkup([], resize_keyboard=True)
        for i in range(1, len(subctgs), 2):
            btn.append([
                KeyboardButton(subctgs[i - 1].name), KeyboardButton(subctgs[i].name),
            ])

        if len(subctgs) % 2:
            btn.append([
                KeyboardButton(subctgs[len(subctgs) - 1].name)
            ])
        # btn.append([KeyboardButton(TEXTS['Back'][lang])])

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def admin_btn(type=None, lang=1):
    btn = []
    if type == "admin_menu":
        btn = [
            [KeyboardButton('Reklama yuborish'), KeyboardButton('Users 👤')],
            [KeyboardButton('Botga qaytish 🏘')]
        ]

    elif type == 'conf':
        btn = [
            [KeyboardButton('Ha'), KeyboardButton("Yo'q")]
        ]

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def inline_btns(type=None):
    btn = []

    if type == "rek":
        btn = [
            [InlineKeyboardButton("Start Test", callback_data="refr",
                                  url="https://t.me/forwardacademy_test_bot")]
        ]

    return InlineKeyboardMarkup(btn)
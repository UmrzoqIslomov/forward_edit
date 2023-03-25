from telegram.ext import CallbackContext
from telegram import Update, Bot
from bot.buttons import btns
from bot.models import *
from bot.tgadmin import TGAdmin, rek_rasm, rek_video
from bot.Globals import TEXTS


def start(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()

    if not tglog:
        tglog = Log()
        tglog.user_id = user.id
        tglog.messages = {"state": 0}
        tglog.save()

    log = tglog.messages

    if not tg_user:
        tg_user = User()
        tg_user.user_id = user.id
        tg_user.username = user.username
        tg_user.first_name = user.first_name
        tg_user.save()
        log['state'] = 0
    else:
        if tg_user.menu == 1:
            log.clear()
            log['admin_state'] = 1
            tglog.messages = log
            tglog.save()
            TGAdmin(update, context)
            return 0

    tg_user.menu_log = 0
    tg_user.save()
    tglog.messages = log
    tglog.save()
    if log['state'] == 0:
        update.message.reply_text(TEXTS['START'], reply_markup=btns("lang"))
    else:
        if log['state'] >= 4:
            log.clear()
            log['state'] = 4
            update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
        else:
            log['state'] = 0
            update.message.reply_html(TEXTS['START'], reply_markup=btns("lang"))


def photo_handler(update, context):
    user = update.message.from_user
    tg_user = User.objects.filter(user_id=user.id).first()
    tglog = Log.objects.filter(user_id=user.id).first()
    log = tglog.messages
    state = log.get('state', 0)
    astate = log.get('admin_state', 0)
    if astate == 100:
        rek_rasm(update, context)
        return 0


def video_handler(update, context):
    user = update.message.from_user
    video = update.message.video
    tg_user = User.objects.filter(user_id=user.id).first()
    print(update.message.message_id, user.id)

    tglog = Log.objects.filter(user_id=user.id).first()
    log = tglog.messages
    state = log.get('state', 0)
    astate = log.get('admin_state', 0)
    print("state:", state, "astatte", astate)
    if astate == 100:
        rek_video(update, context)
        return 0


def message_handler(update: Update, context: CallbackContext):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    log = tglog.messages
    tg_user = User.objects.filter(user_id=user.id).first()
    msg = update.message.text
    state = log.get('state', 0)
    print(log, state)

    if tg_user.menu == 1:
        TGAdmin(update, context)
        return 0

    if msg == "/Forward":
        update.message.reply_text(TEXTS['Admin_Parol'][tg_user.lang])
        log['admin_state'] = 0
        tglog.messages = log
        tglog.save()
        return 0

    elif log.get('admin_state') == 0:
        if msg == "424":
            tg_user.menu = 1
            tg_user.save()
            log.clear()
            log['admin_state'] = 1
            tglog.messages = log
            tglog.save()
            TGAdmin(update, context)
            return 0
        else:
            update.message.reply_text(TEXTS['Error_password'][tg_user.lang])
            return 0

    if state == 0:
        log['state'] = 1
        if msg == "🇺🇿Uz":
            print("uz")
            tg_user.lang = 1
            tg_user.save()
        elif msg == "🇷🇺Ru":
            print("A")
            tg_user.lang = 2
            tg_user.save()
        elif msg == "🇺🇸En":
            print("A")
            tg_user.lang = 3
            tg_user.save()
        else:
            update.message.reply_text(TEXTS['START'], reply_markup=btns("lang"))
            return 0
        update.message.reply_text(TEXTS['NAME'][tg_user.lang])
        tglog.messages = log
        tglog.save()
        return 0

    if log['state'] == 1:
        log['name'] = msg
        log['state'] = 2
        update.message.reply_text(TEXTS["HURMATLI"][tg_user.lang], reply_markup=btns('ctg', lang=tg_user.lang))

    elif log['state'] == 2:
        log['ctg'] = msg
        log['state'] = 3
        if tg_user.lang == 1:
            d = {
                "name_uz": msg
            }
        elif tg_user.lang == 2:
            d = {
                "name_ru": msg
            }
        else:
            d = {
                "name_en": msg
            }
        ctg = Category.objects.filter(**d).first()
        if not ctg:
            update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
            return 0
        update.message.reply_text(TEXTS['save info'][tg_user.lang], reply_markup=btns('subctg', ctg=ctg))

    elif log['state'] == 3:
        log['subctg'] = msg
        log['state'] = 4
        update.message.reply_text(TEXTS['CONTACT2'][tg_user.lang], reply_markup=btns('contact', lang=tg_user.lang))

    elif msg == TEXTS["Lokatsiya📍"][tg_user.lang]:
        log['state'] = 10
        update.message.reply_text("https://yandex.uz/maps/-/CCUruXCP3B")

    if msg == TEXTS["Instagram"][tg_user.lang]:
        log['state'] = 10
        update.message.reply_text("https://www.instagram.com/forwardacademy.uz/")

    elif msg == TEXTS['forward_academy.uz'][tg_user.lang]:
        log['state'] = 10
        update.message.reply_text("https://forwardacademy.uz/")

    elif msg == TEXTS['Telegram'][tg_user.lang]:
        log['state'] = 10
        update.message.reply_text("https://t.me/forwardacademyuz")

    elif msg == TEXTS['Telegram Support'][tg_user.lang]:
        log['state'] = 10
        update.message.reply_text("https://t.me/ForwardAcademy_uz")

    elif msg == TEXTS['Call center'][tg_user.lang]:
        log['state'] = 10
        update.message.reply_html("+998-55-508-84-84")

    # if msg == TEXTS['Back'][tg_user.lang]:
    #     if log['state'] == 4:
    #         log['state'] = 3
    #         log['ctg'] = msg
    #         update.message.reply_text(TEXTS["HURMATLI"][tg_user.lang], reply_markup=btns('ctg', lang=tg_user.lang))
    #         tglog.messages = log
    #         tglog.save()
    #     return 0

    elif msg == TEXTS['Settings'][tg_user.lang]:
        log['state'] = 40
        log['til'] = msg
        update.message.reply_text(TEXTS["LANG"][tg_user.lang], reply_markup=btns("langg", lang=tg_user.lang))
        tglog.messages = log
        tglog.save()
        return 0

    elif msg == "🇺🇿 Uz":
        log['state'] = 41
        tg_user.lang = 1
        tg_user.save()
        update.message.reply_text(TEXTS['SET'][tg_user.lang])
        update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
        tglog.messages = log
        tglog.save()
        return 0

    elif msg == "🇷🇺 Ru":
        log['state'] = 42
        tg_user.lang = 2
        tg_user.save()
        update.message.reply_text(TEXTS['SET'][tg_user.lang])
        update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
        tglog.messages = log
        tglog.save()
        return 0

    elif msg == "🇺🇸 En":
        log['state'] = 43
        tg_user.lang = 3
        tg_user.save()
        update.message.reply_text(TEXTS['SET'][tg_user.lang])
        update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
        tglog.messages = log
        tglog.save()
        return 0

    tglog.messages = log
    tglog.save()


def contact_handler(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()
    log = tglog.messages

    msg = update.message.contact
    contact = update.message.contact
    log['contact'] = contact.phone_number

    print(log)
    if log['state'] == 4:
        tg_user.name = log['name']
        tg_user.ctg = log['ctg']
        tg_user.subctg = log['subctg']
        tg_user.phone = log['contact']
        print("saved")
        tg_user.save()
        update.message.reply_text(TEXTS["save info2"][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
    else:
        update.message.reply_text("Bunday buyruq yo'q")

    tglog.messages = log
    tglog.save()

from telegram import user

from bot.models import User


TEXTS = {
    "START": "🇺🇿 Assalamu Alaykum «Forward Academy» o'quv markaziga xush kelibsiz.\n\n"
             "🇷🇺 Здравствуйте добро пожаловать в учебный центр «Forward Academy».\n\n"
             "🇬🇧 Hello, welcome to the «Forward Academy» educational center.",

    "NAME": {
        1: 'Ismingizni kiriting 🖊',
        2: 'Введите имя 🖊',
        3: "Enter your name 🖊",
    },
    "HURMATLI": {
        1: f'Hurmatli  so bolasa',
        2: f'Hurmatli  so bolasa ruuu',
        3: f'Hurmatli  so bolasa eng',
    },
    "CONTACT": {
        1: "'Raqamni yuborish 📲' tugmasini bosgan holda raqamingizni yuboring",
        2: 'Отправьте нам свой номер, нажав кнопку «Отправить номер 📲»',
        3: "Send us your number by clicking the «Send number 📲» button"
    },
    'ERROR1': {
        1: 'Iltimos ismingizni text formatida kiriting ❗',
        2: 'Пожалуйста, введите свое имя в текстовом формате ❗',
        3: "Please enter your name in text format ❗️"
    },
    "CONTACT2": {
        1: "Quyidagi 'Raqamni yuborish 📲' tugmasini bosing ❗️",
        2: "Нажмите кнопку «Отправить номер 📲» ниже ❗️",
        3: "Click the «Send number 📲» button below ❗️"
    },
    'MENU1': {
        1: "O'zingizni qizitirgan malumot olishingiz mumkin 📚",
        2: "Вы можете получить интересующую Вас информацию 📚",
        3: "You can get the information you are interested in 📚"
    },
    'CON': {
        1: "Raqamni yuborish 📲",
        2: "Отправить номер 📲",
        3: "«Send number 📲»"
    },
    'Settings': {
        1: "Sozlama ⚙",
        2: "Настройка ⚙",
        3: "Setting ⚙"
    },
    'Lokatsiya📍': {
        1: 'Lokatsiya📍',
        2: 'Локация📍',
        3: "Location 📍"
    },
    'forward_academy.uz': {
        1: "Website 🌐",
        2: "Веб-сайт 🌐",
        3: "Website 🌐"
    },
    'Instagram': {
        1: "Instagram",
        2: "Instagram",
        3: "Instagram"
    },
    'Telegram': {
        1: "Telegram",
        2: "Telegram",
        3: "Instagram"
    },
    "level": {
        1: "level uzzzz",
        2: "level ruuuu",
        3: "level enggg"
    },
    "save info": {
        1: "Sizning ma`lumotlaringiz saqlandi ✅, siz bizning qaysi kursimizga qiziqyapsiz 😊",
        2: "Вашы данныу сохранены ✅, мы свяжемся с Вами в ближайшее время! 😊",
        3: "Your information has been saved ✅, we will contact you soon! 😊"
    },
    "LANG": {
        1: "Tilni tanlang !!!",
        2: "Выберите язык !!!",
        3: "Select a language !!!"
    },
    "SET": {
        1: "Til o'zgartirldi ✅",
        2: "Язык изменен ✅",
        3: "The language has been changed ✅"
    },
    "Telegram Support": {
        1: "Support 👩‍💻",
        2: "Support 👩‍💻",
        3: "Support 👩‍💻"
    },
    "Call center": {
        1: "Сall-center ☎️",
        2: "Сall-центр ☎️",
        3: "Сall-center ☎️"
    },
    "Beginner": {
        1: "Beginner",
        2: "Beginner",
        3: "Beginner"
    },
    "Elementary": {
        1: "Elementary",
        2: "Elementary",
        3: "Elementary"
    },
    "Pre-Intermediate": {
        1: "Pre-Intermediate",
        2: "Pre-Intermediate",
        3: "Pre-Intermediate"
    },
    "Intermediate": {
        1: "Intermediate",
        2: "Intermediate",
        3: "Intermediate"
    },
    "Upper-Intermediate": {
        1: "Upper-Intermediate",
        2: "Upper-Intermediate",
        3: "Upper-Intermediate"
    },
    "IELTS": {
        1: "IELTS",
        2: "IELTS",
        3: "IELTS"
    },
    "Ingliz tili": {
        1: "Ingliz tili",
        2: "Ingliz tili ruu",
        3: "Ingliz tili eng"
    },
    "Rus tili": {
        1: "Rus tili",
        2: "Rus tili ruu",
        3: "Rus tili eng"
    },


}

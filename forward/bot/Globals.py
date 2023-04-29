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
        1: '🧐 Sizni qaysi kurslarimiz qiziqtiryapti ?',
        2: '🧐 Какие курсы Вас интересуют ?',
        3: '🧐 What courses are you interested in?',
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
        1: "🤔 Qaysi daraja sizni qiziqtiryapti ?",
        2: "🤔 Какой уровень Вас интересует ?",
        3: "🤔 What level are you interested in ?"
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
    "Admin_Parol": {
        1: "Parolni kiriting",
        2: "Введите пароль",
        3: "Enter the password"
    },
    "Error_password": {
        1: "Siz parolni noto'g'ri kiritdingiz",
        2: "Вы неправильно ввели пароль",
        3: "You entered the password incorrectly",
    },
    "Xush_kelibsiz": {
        1: "Admin bo'limiga xush kelibsiz",
        2: "Добро пожаловать в админ панелу",
        3: "Welcome to the admin section",
    },
    "Back": {
        1: "◀ Orqaga",
        2: "◀ Назад",
        3: "◀ Back",
    },
    "ERROR": {
        1: "Bu bo'limgaga oid hech qanday bo'lim topilmadi  ❗️",
        2: "Разделов для этого раздела не найдено ❗️",
        3: "ERROR"
    },
    "save info2": {
        1: "Sizning ma`lumotlaringiz saqlandi ✅, siz bilan tez orada bog'lanamiz! 😊",
        2: "Вашы данныу сохранены ✅, мы свяжемся с Вами в ближайшее время! 😊",
        3: "Your information has been saved ✅, we will contact you soon! 😊"
    },
    "Testt": {
        1: "Test your English 🇬🇧",
        2: "Test your English 🇬🇧",
        3: "Test your English 🇬🇧",
    }
}

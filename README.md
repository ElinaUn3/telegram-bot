# telegram-bot
// Этот код создает Telegram-бота, который скачивает видео с YouTube по ссылке, отправленный тобой (пользователем)
// import telebot: Импортирем библиотеку telebot, которая позволяет взаимодействовать с Telegram API
// from pytube import YouTube: Импортируем класс YouTube из библиотеки pytube, чтобы скачивать видео с YouTube
// os: Модуль для работы с операционной системой, используется для удаления временного файла видео
// TOKEN = 'ТУТ ТОКЕН': Здесь я добавляю свой токин (который дается при создании бота через BotFather)
// bot = telebot.TeleBot(TOKEN): Создаем объект бота, используя токен
// @bot.message_handler(commands=['start']): Этот декоратор указывает, что функция start будет обрабатывать команду /start
// def start(message):: Эта функция отправляет приветствие при получении команды /start
//@bot.message_handler(func=lambda message: True): Этот декоратор указывает, что функция download_video будет обрабатывать все текстовые сообщения
//def download_video(message):: Эта функция скачивает видео по ссылке, отправленной тобой (пользователем). Она использует библиотеку pytube для скачивания видео и отправляет его тебе (пользователю)

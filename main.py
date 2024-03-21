import telebot
from pytube import YouTube
import os

# Укажите токен вашего Telegram-бота
TOKEN = '7134603561:AAFgcP2zcACujqiBen95fin0m7fwl4lMPHA'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Отправь мне ссылку на видео с YouTube, и я скачаю его для тебя.")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    try:
        youtube_url = message.text
        yt = YouTube(youtube_url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download()

        bot.send_message(message.chat.id, "Видео успешно скачано! 🎉")
        with open(video_stream.default_filename, 'rb') as video_file:
            bot.send_video(message.chat.id, video_file)

        os.remove(video_stream.default_filename)
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка при скачивании видео: {e}")

if __name__ == '__main__':
    bot.polling(none_stop=True)
from config import TOKEN, API_KEY, SECRET_KEY
from PIL import Image
import base64
from random import randint
import requests
from io import BytesIO
import telebot
from logic import Text2ImageAPI,text2img

#from telebot.types import ReplyKeyboardMarkup, KeyboardButton
bot = telebot.TeleBot(TOKEN)
#keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat,id, 'Привет! Я бот для генерации картинок.')



#                                                1 вариант
#@bot.message_handler(commands=['image'])
#def generate_image(message):
#   input_file = "C:/Users/User/Desktop/asdfghjkl/text.txt"
#   output_image = "C:/Users/User/Desktop/asdfghjkl/image.png"
#   with open(input_file, "r") as file:
#        base64_text = file.read()
#        image_data = base64.b64decode(base64_text)
#        image = Image.open(BytesIO(image_data))
#        image.save(output_image)
#
#
#        with open(output_image, "rb") as photo:
#            bot.send_photo(message.chat.id, photo, 'Вот сгенерированная картинка!')


#                                            2 вариант


@bot.message_handler(commands=['prompt'])
def make_img(message):
    prompt_text = telebot.util.extract_arguments(message.text)
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', API_KEY, SECRET_KEY)
    model_id = api.get_model()
    uuid = api.generate(prompt_text, model_id)
    images = api.check_generation(uuid)[0]

    file_path = f'image_{randint(1000000 , 10000000)}.jpg'
    img = text2img(images, file_path)
    with open(file_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, 'Вот сгенерированная картинка!')



bot.infinity_polling()
# UPLOAD INSTA POST USING PYTHON
# pip install instabot
from instabot import bot
bot = Bot()
bot.login(username = "user_name",password = "user_password")
bot.upload_photo("YourPhoto.jpg", caption = "caption of Post Here")
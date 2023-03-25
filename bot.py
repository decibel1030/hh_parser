import time
from aiogram import Bot, Dispatcher, executor, types
import logging
import main
TOKEN = "6249987142:AAHm1RtpLODBjWu0gdHzSWvP9PCohj2zaEQ"

logging.basicConfig(level=logging.INFO)
logging.getLogger("bot")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    logging.info(f"user: @{message.from_user.username}")
    await message.answer("Бот стартанул")
    if message.from_user.username == "undefiend_usr":
        while True:
            data = main.get_data()
            for item in data:
                link = item['link']
                text = f"<b>{item['name']}</b>\n" \
                       f"<b>Место: </b><i>{item['area']}</i>\n" \
                       f"<b>Статус: </b><i>{item['status']}</i>\n" \
                       f"<b>Работадатель:</b><i>{item['employer-name']}</i>\n" \
                       f"<b>Предлагаемая роль: </b> <i>{item['role']}</i>\n\n" \
                       f"<b>з/п: </b> <code>💵{item['sol']}</code>\n\n" \
                       f"<a href='{link}'>Изучить вакансию</a>🔫"
                await message.answer(text=text, parse_mode="html")
                time.sleep(1800)
            time.sleep(7200)
            main.rewrite_data()

if __name__ == '__main__':
    executor.start_polling(dp)

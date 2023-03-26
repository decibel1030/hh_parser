import time
from aiogram import Bot, Dispatcher, executor, types
import main
TOKEN = "6249987142:AAHm1RtpLODBjWu0gdHzSWvP9PCohj2zaEQ"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Бот созданный для вывода новых вакансий в чат."
                         " На данный момент бот в тестирований")


@dp.message_handler(commands=["check"])
async def check(message: types.Message):
    print(message.from_user.username)
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
                await bot.send_message(text=text, chat_id=message.chat.id, parse_mode="HTML")
                time.sleep(100)
            time.sleep(7200)
            main.rewrite_data()


if __name__ == '__main__':
    executor.start_polling(dp)

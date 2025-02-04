API_TOKEN = "7553842523:AAEGtGV8tsbyfMhALmbe2jEYMiTPkgGiSN0"
web_app_url = "https://ulkov.github.io/tsum_web_app_bot/"

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
    Message,
    WebAppData,
)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(F.text == "/start")
async def start_command(message: Message):
    web_app_button = KeyboardButton(
        text="Open Mini App",
        web_app=WebAppInfo(url=web_app_url),
    )
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[web_app_button]], resize_keyboard=True  # Note: List of lists
    )
    await message.answer(
        "Press the button to open the Mini App:", reply_markup=keyboard
    )


@dp.message(F.web_app_data)
async def handle_web_app_data(message: Message):
    web_app_data = message.web_app_data
    if web_app_data:
        await message.answer(f"Received data: {web_app_data.data}")
    else:
        await message.answer("No data received from Web App.")


if __name__ == "__main__":
    import asyncio

    asyncio.run(dp.start_polling(bot))

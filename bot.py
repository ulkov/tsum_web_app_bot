import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command  # Используем фильтр для команд
from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup, Message

API_TOKEN = '7553842523:AAEGtGV8tsbyfMhALmbe2jEYMiTPkgGiSN0'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: Message):
    web_app_url = "https://example.com"
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Открыть Web App", web_app=WebAppInfo(url=web_app_url))]
        ]
    )

    await message.answer("Привет! Нажми кнопку ниже, чтобы открыть Web App:", reply_markup=keyboard)

@dp.message(lambda message: message.web_app_data)
async def web_app_data_handler(message: Message):
    data = message.web_app_data.data  # Полученные данные из Web App
    await message.answer(f"Получены данные: {data}")

async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())

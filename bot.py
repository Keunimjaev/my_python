from aiogram import types,executor,Bot,Dispatcher
from req import send_answer


API = '7123298961:AAGZX5rXRRzRIcSC2uHCyyP4UqaMqJVGGUc'
bot = Bot(token=API)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def say_hi(message:types.Message):
    await message.answer(text='bizge soraw jazin!')

@dp.message_handler()
async def save(message:types.Message):
    answer = await send_answer(message.text)
    await message.answer(answer)


if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)

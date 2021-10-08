from main import bot, dp, types, get_some, get_last, save_note



@dp.message_handler(commands=['gs'])
async def send_some(message: types.Message):

    try:
      num_rec = int(message.get_args())
    except Exception:
       num_rec = 1
    await message.reply(get_some(num_rec))


@dp.message_handler(commands=['gl'])
async def send_last(message: types.Message):
    try:
        num_rec = int(message.get_args())
    except Exception:
        num_rec = 1
    await message.reply(get_last(num_rec))

@dp.message_handler()
async def echo(message: types.Message):
    save_note(message.text)
    await message.answer('!')

@dp.message_handler(lambda  message: message.text.startswith('/del'))
async def del_expense(message: types.Message):


    answer_message = "Удалил"
    await message.answer(answer_message)

@dp.message_handler()
async def sendalarm(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)
    await bot.send_message(admin_id, "кто-то вводит пишет прост")
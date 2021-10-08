from orm_tv import *

from random import randint


import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN,admin_id


def get_some(qnt=1):
    str_notes = ''
    notes = Notes.select()
    last_id = 16 + len(notes)


    for i in range(qnt):
        randind = randint(16,last_id)
        nt = Notes.get(Notes.id == randind)
        str_notes += '-------- \n' + nt.datetime.strftime('%d/%m/%Y, %H:%M') + '\n ' + nt.note + '\n\n'
    return str_notes

def get_last(qnt=1):
    str_notes = ''
    notes = Notes.select()
    last_id = 16 + len(notes)
    for i in range(last_id-qnt, last_id):
        nt = Notes.get(Notes.id == i+1)

        str_notes += '-------- \n' + nt.datetime.strftime('%d/%m/%Y, %H:%M') + '\n ' + nt.note + '\n\n'
    return str_notes

def save_note(txt,usr_id=12345):
      new_note = Notes(note=txt,user_id=usr_id)
      new_note.save()
      return 0

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    conn.create_tables([Notes])
    conn.close()

    from handlers import dp
    executor.start_polling(dp, skip_updates=True)


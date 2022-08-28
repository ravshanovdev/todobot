from aiogram import  Bot,Dispatcher, executer, types

import logging
logging.basicConfig(level=logging.debug)

bot = Bot(token="", parse_mode='html')

dp = Dispatcher(bot=bot)




if __name__=='__main__':
    executer.start_polling(dispatcher=dp)

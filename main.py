from bot import dp
from aiogram.utils import executor
from handlers import client, admin, fsm
from background import keep_alive


admin.register_handler_admin()
fsm.register_handler_FSM()
client.register_handler_client()
#keep_alive()
executor.start_polling(dp, skip_updates=True)

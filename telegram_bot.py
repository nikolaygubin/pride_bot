from aiogram import executor, types
from create_bot import dp, bot
from handlers import client, admin
from data_base import sqlite_db
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from work_with_pairs import *
import logging
import os

scheduler = AsyncIOScheduler()

admin.register_handlers_admin(dp)
client.register_handlers_client(dp)

logging.basicConfig(level=logging.INFO)
    
async def on_startup(dp):
    # await bot.set_webhook('https://pride-bot.1967gubin.deployme.tech')
    # scheduler.add_job(make_extra_pairs, 'cron', second='*', timezone='Europe/Moscow')
    # await bot.set_webhook(os.environ.get('URL'))
    sqlite_db.start_sql()
    # scheduler.add_job(make_pairs, 'cron', day_of_week='0-3', hour='*', minute='*', second=35, timezone='Europe/Moscow')
    # scheduler.add_job(make_extra_pairs, 'cron', day_of_week='0-3', hour='*', minute=40, timezone='Europe/Moscow')
    # scheduler.add_job(ask_impress, 'cron', day_of_week='0-3', hour='*', minute='*', second='*/20', timezone='Europe/Moscow')
    # scheduler.add_job(is_active, 'cron', day_of_week='0-3', hour='*', minute='*', second=20, timezone='Europe/Moscow')
    # scheduler.add_job(update_paid, 'cron', second='*/10', timezone='Europe/Moscow')
    scheduler.start()
    await bot.set_webhook(os.environ.get('URL'))
    sqlite_db.start_sql()

def start_bot():
    sqlite_db.start_sql()
    print('Бот и база данных успешно запустились!')

async def on_shutdown(dp):
    await bot.delete_webhook()

if __name__ == "__main__" :
    executor.start_webhook(
        dispatcher = dp,
        webhook_path = '',
        skip_updates = True,
        on_startup = on_startup,
        on_shutdown = on_shutdown,
        host = "0.0.0.0",
        port = int(os.environ.get("PORT", 5000))
    )


import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from loguru import logger

from router_loader import RoutersLoader


async def main():
    logger.info("Starting bot")

    bot: Bot = Bot(token="", default=DefaultBotProperties(parse_mode="HTML"))
    dp: Dispatcher = Dispatcher()

    routers_loader = RoutersLoader('src/example/handlers', dp)
    routers_loader.load()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")

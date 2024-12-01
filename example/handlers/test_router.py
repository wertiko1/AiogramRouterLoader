from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def start(msg: types.Message) -> None:
    await msg.answer("Test handler...")

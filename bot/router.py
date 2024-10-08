from aiogram import Router

from bot.handlers.start import start_router
from bot.handlers.admin.load_pic import load_pic_router
from bot.handlers.search import search_router

main_router = Router()

main_router.include_router(start_router)
main_router.include_router(load_pic_router)
main_router.include_router(search_router)
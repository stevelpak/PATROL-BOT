from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("ro", "Faqat o'qish rejimi"),
            types.BotCommand("unro", "O'qish rejimidan chiqarish"),
            types.BotCommand("ban", "Foydalanuvchini guruhdan haydash"),
            types.BotCommand("set_photo", "Guruh rasmini o'zgartirish"),
            types.BotCommand("set_title", "Guruh nomini o'zgartirish"),
            types.BotCommand("set_description", "Guruh tavsifini o'zgartirish"),
        ]
    )

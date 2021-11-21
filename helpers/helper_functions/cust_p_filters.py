from pyrogram import (
    filters
)
from pyrobot.helper_functions.admin_check import admin_check

async def admin_filter_f(filt, client, message):
    return await admin_check(message)


admin_fliter = filters.create(
    func=admin_filter_f,
    name="AdminFilter"
)

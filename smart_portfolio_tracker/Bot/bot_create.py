"""
TrekB | Smart Portfolio Tracker
:copyright: (c) 2023 by Dmitrii Davletshin (@dmitriidavs)
:license: BSD-3-Clause, see LICENSE for more details
"""

from bot import LiteBot
from creds import (
    BOT_API_TOKEN, BOT_ARCH_TYPE,
    USERS_DB_CONN, BOT_FSM_STORAGE_TYPE,
    UTIL_DB_HOST, UTIL_DB_PORT, UTIL_DB_FSM_DB
)


# TODO: create bot class depending on ARCH_TYPE
BaseBot = LiteBot(
    api_token=BOT_API_TOKEN,
    arch_type=BOT_ARCH_TYPE,
    users_db_conn=USERS_DB_CONN,
    util_db_host=UTIL_DB_HOST,
    util_db_port=UTIL_DB_PORT,
    util_db_fsm_db=UTIL_DB_FSM_DB,
    storage_type=BOT_FSM_STORAGE_TYPE
)
bot = BaseBot.bot
dispatcher = BaseBot.dispatcher

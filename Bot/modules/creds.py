import os

from .validation import validate_env_vars


# validate environment variables
env_vars = validate_env_vars({
    'timezone': os.environ.get('TIMEZONE'),
    'bot_arch_type': os.environ.get('BOT_ARCH_TYPE'),
    'bot_address': os.environ.get('BOT_ADDRESS'),
    'bot_fsm_storage_type': os.environ.get('BOT_FSM_STORAGE_TYPE'),
    'bot_api_token': os.environ.get('BOT_API_TOKEN'),
    'users_db_conn': os.environ.get('USERS_DB_CONN'),
    'cache_host': os.environ.get('CACHE_HOST'),
    'cache_port': os.environ.get('CACHE_PORT'),
    'broker_host': os.environ.get('BROKER_HOST'),
    'broker_port': os.environ.get('BROKER_PORT'),
    'cache_ttl': os.environ.get('CACHE_TTL'),
    'fsm_ttl': os.environ.get('FSM_TTL'),
    'broker_ttl': os.environ.get('BROKER_TTL'),
    'log_folder_path': os.environ.get('LOG_FOLDER_PATH'),
    'log_host': os.environ.get('LOG_HOST'),
    'log_port': os.environ.get('LOG_PORT'),
})

TIMEZONE = env_vars['timezone']
BOT_ARCH_TYPE = env_vars['bot_arch_type']
BOT_ADDRESS = env_vars['bot_address']
BOT_FSM_STORAGE_TYPE = env_vars['bot_fsm_storage_type']
BOT_API_TOKEN = env_vars['bot_api_token']
USERS_DB_CONN = env_vars['users_db_conn']
CACHE_HOST = env_vars['cache_host']
CACHE_PORT = env_vars['cache_port']
BROKER_HOST = env_vars['broker_host']
BROKER_PORT = env_vars['broker_port']
CACHE_TTL = env_vars['cache_ttl']
FSM_TTL = env_vars['fsm_ttl']
broker_ttl = env_vars['broker_ttl']
LOG_FOLDER_PATH = env_vars['log_folder_path']
LOG_HOST = env_vars['log_host']
LOG_PORT = env_vars['log_port']

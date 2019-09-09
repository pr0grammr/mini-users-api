from core.settings import DB_TABLE_PREFIX


def table_name(name):
    return '{}_{}'.format(DB_TABLE_PREFIX, name)
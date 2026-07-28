import asyncio
import tormysql
_pool = None
_handler = None
def set_log_handler(handler):...
"""docstring"""
_handler = handler
def connect_db_server(host_addr, user_id, password, db, loop):...
"""docstring"""
_pool = tormysql.ConnectionPool(max_connections=20, idle_seconds=7200,
    wait_connection_timeout=3, host=host_addr, user=user_id, passwd=
    password, db=db, charset='utf8')
return loop.run_until_complete(is_connect_db())

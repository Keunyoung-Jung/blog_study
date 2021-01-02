import pymysql

MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect(
    host = MYSQL_HOST,
    user='keyog',
    passwd='keyog1234',
    db='keyog',
    charset='utf8'
)

def conn_mysqldb() :
    if not MYSQL_CONN.open :
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN
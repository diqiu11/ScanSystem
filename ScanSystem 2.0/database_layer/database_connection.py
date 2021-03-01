import pymysql

class DTConnet:
    def __init__(self):
        self.dt_connect()

    def dt_connect(self):
        host = '127.0.0.1'
        user = 'root'
        password = 'my.ini'
        database = 'scanresult'
        try:
            db = pymysql.connect(host=host, user=user, password=password, database=database, charset='utf8')
            return db
        except Exception as e:
            print("db连接异常：%s", e)
            return None
from database_layer import database_connection
import pymysql
class Sqlhanding:
    def __init__(self,tableName):
        self.tableName = tableName

    def createTable(self):
        database = database_connection.DTConnet().dt_connect()
        try:
            values = 'ID INT primary key auto_increment,`IP` VARCHAR(16),`BRAND` VARCHAR(255),`PORT21` VARCHAR(10),`PORT22` VARCHAR(10),`PORT23` VARCHAR(10),`PORT80` VARCHAR(10),`PORT135` VARCHAR(10),`PORT139` VARCHAR(10),`PORT445` VARCHAR(10),`PORT3306` VARCHAR(10),`PORT3389` VARCHAR(10),`PORT8080` VARCHAR(10)'
            cursor = database.cursor()
            sql_create = 'CREATE TABLE %s (%s)' % (self.tableName, values)
            cursor.execute(sql_create)
            database.commit()
        except pymysql.connect.Error as e:
            print('创建失败',str(e))
        finally:
            database.close()

    def createStable(self):
        database = database_connection.DTConnet().dt_connect()
        try:
            values = 'ID INT primary key auto_increment,`IP` VARCHAR(16),`BRAND` VARCHAR(255),`SERV21` VARCHAR(255),`SERV22` VARCHAR(255),`SERV23` VARCHAR(255),`SERV80` VARCHAR(255),`SERV135` VARCHAR(255),`SERV139` VARCHAR(255),`SERV445` VARCHAR(255),`SERV3306` VARCHAR(255),`SERV3389` VARCHAR(255),`SERV8080` VARCHAR(255)'
            cursor = database.cursor()
            sql_create = 'CREATE TABLE %s (%s)' % (self.tableName, values)
            cursor.execute(sql_create)
            database.commit()
        except pymysql.connect.Error as e:
            print('创建失败', str(e))
        finally:
            database.close()

    def insertnews(self,id,ip,brand,port21,port22,port23,port80,port135,port139,port445,port3306,port3389,port8080):
        database = database_connection.DTConnet().dt_connect()
        try:
            cursor = database.cursor()
            sql_insert = "INSERT INTO %s" % self.tableName + "(ID,`IP`,`BRAND`,`PORT21`,`PORT22`,`PORT23`,`PORT80`,`PORT135`,`PORT139`,`PORT445`,`PORT3306`,`PORT3389`,`PORT8080`)" + "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql_insert, (
            id, ip, brand, port21, port22, port23, port80, port135, port139, port445, port3306, port3389, port8080))
            database.commit()
        except pymysql.connect.Error as e:
            database.rollback()
            print('插入失败',str(e))
        finally:
            database.close()

    def insertServnews(self,id,ip,brand,serv21,serv22,serv23,serv80,serv135,serv139,serv445,serv3306,serv3389,serv8080):
        database = database_connection.DTConnet().dt_connect()
        try:
            cursor = database.cursor()
            stablename = self.tableName+'_serv'
            sql_insert = "INSERT INTO %s" % stablename + "(ID,`IP`,`BRAND`,`SERV21`,`SERV22`,`SERV23`,`SERV80`,`SERV135`,`SERV139`,`SERV445`,`SERV3306`,`SERV3389`,`SERV8080`)" + "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql_insert, (
            id, ip, brand, serv21, serv22, serv23, serv80, serv135, serv139, serv445, serv3306, serv3389, serv8080))
            database.commit()
        except pymysql.connect.Error as e:
            database.rollback()
            print('插入失败',str(e))
        finally:
            database.close()

    def queryhostnum(self):
        database = database_connection.DTConnet().dt_connect()
        try:
            cursor = database.cursor()
            num_sql = 'select count(*) from %s;' % (self.tableName)
            cursor.execute(num_sql)
            database.commit()
            num = cursor.fetchone()[0]
            return num
        except pymysql.connect.Error as e:
            print('查询失败',str(e))
        finally:
            database.close()

    def getsystemnum(self):
        database = database_connection.DTConnet().dt_connect()
        try:
            sql_tb_system = "select BRAND from %s" % self.tableName
            win_num = 0
            linux_num = 0
            other_num = 0
            cursor = database.cursor()
            cursor.execute(sql_tb_system)
            lists = cursor.fetchall()
            for system in lists:
                if 'Windows' in system[0]:
                    win_num = win_num + 1
                elif 'Linux' in system[0]:
                    linux_num = linux_num + 1
                else:
                    other_num = other_num + 1
            return win_num, linux_num, other_num
        except pymysql.connect.Error as e:
            print('查询失败', str(e))
        finally:
            database.close()


    def getwebportnum(self):
        database = database_connection.DTConnet().dt_connect()
        try:
            sql_80port = "select count(port80) from %s" % (self.tableName) + " where port80='open';"
            sql_3306port = "select count(port3306) from %s" % (self.tableName) + " where port3306='open';"
            sql_8080port = "select count(port8080) from %s" % (self.tableName) + " where port8080='open';"
            cursor = database.cursor()
            # 得到80开放数量
            cursor.execute(sql_80port)
            op80num = cursor.fetchone()
            # 得到3306开放数量
            cursor.execute(sql_3306port)
            op3306num = cursor.fetchone()
            # 得到8080开放数量
            cursor.execute(sql_8080port)
            op8080num = cursor.fetchone()
            return op80num, op3306num, op8080num
        except pymysql.connect.Error as e:
            print('查询失败', str(e))
        finally:
            database.close()


    def getloginportnum(self):
        database = database_connection.DTConnet().dt_connect()
        try:
            sql_22port = "select count(port22) from %s" % (self.tableName) + " where port22='open';"
            sql_23port = "select count(port23) from %s" % (self.tableName) + " where port23='open';"
            sql_3389port = "select count(port3389) from %s" % (self.tableName) + " where port3389='open';"
            cursor = database.cursor()
            # 得到22开放数量
            cursor.execute(sql_22port)
            op22num = cursor.fetchone()
            # 得到23开放数量
            cursor.execute(sql_23port)
            op23num = cursor.fetchone()
            # 得到3389开放数量
            cursor.execute(sql_3389port)
            op3389num = cursor.fetchone()
            return op22num, op23num, op3389num
        except pymysql.connect.Error as e:
            print('查询失败', str(e))
        finally:
            database.close()

    def getfileportnum(self):
        database = database_connection.DTConnet().dt_connect()
        try:
            sql_135port = "select count(port135) from %s" % (self.tableName) + " where port135='open';"
            sql_139port = "select count(port139) from %s" % (self.tableName) + " where port139='open';"
            sql_445port = "select count(port445) from %s" % (self.tableName) + " where port445='open';"
            sql_21port = "select count(port21) from %s" % (self.tableName) + " where port21='open';"
            cursor = database.cursor()
            # 得到21开放数量
            cursor.execute(sql_21port)
            op21num = cursor.fetchone()
            # 得到135开放数量
            cursor.execute(sql_135port)
            op135num = cursor.fetchone()
            # 得到139开放数量
            cursor.execute(sql_139port)
            op139num = cursor.fetchone()
            # 得到445开放数量
            cursor.execute(sql_445port)
            op445num = cursor.fetchone()
            return op21num, op135num, op139num, op445num
        except pymysql.connect.Error as e:
            print('查询失败', str(e))
        finally:
            database.close()

    def getserv(self):
        database = database_connection.DTConnet().dt_connect()
        try:
            cursor = database.cursor()
            servnamesql = "select SERV21,SERV22,SERV23,SERV80,SERV135,SERV139,SERV445,SERV3306,SERV3389,SERV8080 from %s" % (self.tableName)
            num =cursor.execute(servnamesql)
            text = cursor.fetchall()
            #可以遍历清理数据
            return text,num
        except pymysql.connect.Error as e:
            print('查询失败', str(e))
        finally:
            database.close()

    def booltable(self):
        database = database_connection.DTConnet().dt_connect()
        try:
            cursor = database.cursor()
            tbsql = "select count(*) from information_schema.TABLES where TABLE_NAME='%s'" % (self.tableName)
            cursor.execute(tbsql)
            flag = cursor.fetchone()
            return flag[0]
        except pymysql.connect.Error as e:
            print('查询失败',str(e))
            flag = 0
            return flag
        finally:
            database.close()

    def delete_table(self):
        database = database_connection.DTConnet().dt_connect()
        try:
            cursor = database.cursor()
            delsql = "drop table %s" % (self.tableName)
            cursor.execute(delsql)

        except pymysql.connect.Error as e:
            print('删除失败', str(e))

        finally:
            database.close()

class DataShow:
    def __init__(self):
        self.gettablename()

    def gettablename(self):
        database = database_connection.DTConnet().dt_connect()
        try:
            cursor = database.cursor()
            namesql = "show tables"
            cursor.execute(namesql)
            names = cursor.fetchall()
            numtablesql = "SELECT COUNT(*) TABLES, table_schema FROM information_schema.TABLES WHERE table_schema = 'scanresult' GROUP BY table_schema;"
            cursor.execute(numtablesql)
            numtables = cursor.fetchone()
            return names,numtables
        except pymysql.connect.Error as e:
            print('查询失败', str(e))
        finally:
            database.close()

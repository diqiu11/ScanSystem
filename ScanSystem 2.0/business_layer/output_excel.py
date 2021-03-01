import xlwt
from database_layer import database_connection
import pymysql
class ExExcel:
    def __init__(self,tableName):
        self.tableName = tableName
        self.exportExcel()

    def exportExcel(self):
        # 生成excel表
        workexcel = xlwt.Workbook()
        worksheet = workexcel.add_sheet(self.tableName)
        tableSName = self.tableName+'_serv'
        worksheet_serv = workexcel.add_sheet(tableSName)
        # 连接数据库
        database = database_connection.DTConnet().dt_connect()
        try:
            cursor = database.cursor()
            # 写入数据表字段
            column_count = cursor.execute("desc %s" % self.tableName)
            for i in range(column_count):
                lists = cursor.fetchone()
                worksheet.write(0, i, lists[0])
            # 写记录
            row_count = cursor.execute("select * from %s" % self.tableName)
            for i in range(row_count):
                lists = cursor.fetchone()
                for j in range(column_count):
                    worksheet.write(i + 1, j, lists[j])

            #生成另一张sheet
            column_count_serv = cursor.execute("desc %s" % tableSName)
            for i in range(column_count_serv):
                lists = cursor.fetchone()
                worksheet_serv.write(0,i,lists[0])
            row_count_serv = cursor.execute("select * from %s" % tableSName)
            for i in range(row_count_serv):
                lists = cursor.fetchone()
                for j in range(column_count_serv):
                    worksheet_serv.write(i+1,j,lists[j])

        except pymysql.connect.Error as e:
            print('装excel失败',str(e))
        finally:
            database.close()
            workexcel.save("..\\" + self.tableName + ".xls")

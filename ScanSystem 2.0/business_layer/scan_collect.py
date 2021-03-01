import nmap
from persistence_layer import datahanding
from concurrent.futures import ThreadPoolExecutor #线程池
import threading

class ScanCollect:
    def __init__(self,ip,mask,tableName):
        self.ip = ip
        self.mask = mask
        self.tableName = tableName
        self.threadLock = threading.Lock()   #锁实例化
        self.thread_pool = ThreadPoolExecutor(10)    #线程池
        #self.process_pool = ProcessPoolExecutor(2) #进程池
        self.create_table()
        self.addscan()  #特定端口扫描


    def create_table(self):
        try:
            #insert_upgrade.create_table(self.tableName)
            create_tb = datahanding.Sqlhanding(self.tableName)
            create_tb.createTable()
            serv_name = self.tableName + '_serv'
            create_tb_serv = datahanding.Sqlhanding(serv_name)
            create_tb_serv.createStable()
        except:
            print("表存在")



    def addscan(self):
        nm = nmap.PortScanner()
        nm.scan(self.ip + '/' + self.mask, '21,22,23,80,135,139,445,3306,3389,8080')
        index = 1
        #引入多线程
        for num_i in nm.all_hosts():
            self.call_do_add(num_i,index)
            index += 1
    #线程池
    def call_do_add(self,num_i,index):
        self.thread_pool.submit(self.do_add(num_i,index))
    #每个IP扫描的端口为一个线程
    def do_add(self,num_i,index):
        self.threadLock.acquire()
        nm = nmap.PortScanner()
        try:
            port21_result = nm.scan(hosts=num_i, arguments='-sV -p 21')#-sS -Pn -n -T4 --min-hostgroup 1024 --min-parallelism 10 --host-timeout 30
            port21_status = port21_result["scan"][num_i]['tcp'][21]['state']
            serv21_product = port21_result["scan"][num_i]['tcp'][21]['product']
            serv21_version = port21_result["scan"][num_i]['tcp'][21]['version']
            serv21 = serv21_product+''+serv21_version
        except:
            port21_status = 'close'
            serv21 = 'None'
        try:
            port22_result = nm.scan(hosts=num_i, arguments='-sV -p 22')
            port22_status = port22_result["scan"][num_i]['tcp'][22]['state']
            serv22_product = port22_result["scan"][num_i]['tcp'][22]['product']
            serv22_version = port22_result["scan"][num_i]['tcp'][22]['version']
            serv22 = serv22_product + '' + serv22_version
        except:
            port22_status = 'close'
            serv22 = ''
        try:
            port23_result = nm.scan(hosts=num_i, arguments='-sV -p 23')
            port23_status = port23_result["scan"][num_i]['tcp'][23]['state']
            serv23_product = port23_result["scan"][num_i]['tcp'][23]['product']
            serv23_version = port23_result["scan"][num_i]['tcp'][23]['version']
            serv23 = serv23_product + '' + serv23_version
        except:
            port23_status = 'close'
            serv23 = ''
        try:
            port139_result = nm.scan(hosts=num_i, arguments='-sV -p 139')
            port139_status = port139_result["scan"][num_i]['tcp'][139]['state']
            serv139_product = port139_result["scan"][num_i]['tcp'][139]['product']
            serv139_version = port139_result["scan"][num_i]['tcp'][139]['version']
            serv139 = serv139_product + '' + serv139_version
        except:
            port139_status = 'close'
            serv139 = ''
        try:
            port3306_result = nm.scan(hosts=num_i, arguments='-sV -p 3306')
            port3306_status = port3306_result["scan"][num_i]['tcp'][3306]['state']
            serv3306_product = port3306_result["scan"][num_i]['tcp'][3306]['product']
            serv3306_version = port3306_result["scan"][num_i]['tcp'][3306]['version']
            serv3306 = serv3306_product + '' + serv3306_version
        except:
            port3306_status = 'close'
            serv3306 = ''
        try:
            port3389_result = nm.scan(hosts=num_i, arguments='-sV -p 3389')
            port3389_status = port3389_result["scan"][num_i]['tcp'][3389]['state']
            serv3389_product = port3389_result["scan"][num_i]['tcp'][3389]['product']
            serv3389_version = port3389_result["scan"][num_i]['tcp'][3389]['version']
            serv3389 = serv3389_product + '' + serv3389_version
        except:
            port3389_status = 'close'
            serv3389 = ''
        try:
            port8080_result = nm.scan(hosts=num_i, arguments='-sV -p 8080')
            port8080_status = port8080_result["scan"][num_i]['tcp'][8080]['state']
            serv8080_product = port8080_result["scan"][num_i]['tcp'][8080]['product']
            serv8080_version = port8080_result["scan"][num_i]['tcp'][8080]['version']
            serv8080 = serv8080_product + '' + serv8080_version
        except:
            port8080_status = 'close'
            serv8080 = ''
        try:
            port445_result = nm.scan(hosts=num_i, arguments='-sV -p 445')
            port445_status = port445_result["scan"][num_i]['tcp'][445]['state']
            serv445_product = port445_result["scan"][num_i]['tcp'][445]['product']
            serv445_version = port445_result["scan"][num_i]['tcp'][445]['version']
            serv445 = serv445_product + '' + serv445_version
        except:
            port445_status = 'close'
            serv445 = ''
        try:
            port80_result = nm.scan(hosts=num_i, arguments='-sV -p 80')
            port80_status = port80_result["scan"][num_i]['tcp'][80]['state']
            serv80_product = port80_result["scan"][num_i]['tcp'][80]['product']
            serv80_version = port80_result["scan"][num_i]['tcp'][80]['version']
            serv80 = serv80_product + '' + serv80_version
        except:
            port80_status = 'close'
            serv80 = ''
        try:
            port135_result = nm.scan(hosts=num_i, arguments='-sV -p 135')
            port135_status = port135_result["scan"][num_i]['tcp'][135]['state']
            serv135_product = port135_result["scan"][num_i]['tcp'][135]['product']
            serv135_version = port135_result["scan"][num_i]['tcp'][135]['version']
            serv135 = serv135_product + '' + serv135_version
        except:
            port135_status = 'close'
            serv135 = ''

        try:
            result_os = nm.scan(hosts=num_i, arguments='-O')
            os_status = result_os["scan"][num_i]['osmatch'][0]['name']
        except:
            os_status = 'None'
        """
        insert_upgrade.insert_table(self.tableName, index, num_i, os_status, port21_status, port22_status, port23_status
                                    , port80_status, port135_status, port139_status
                                    , port445_status, port3306_status, port3389_status, port8080_status)
        """

        handing = datahanding.Sqlhanding(self.tableName)
        handing.insertnews(index, num_i, os_status, port21_status, port22_status, port23_status
                           , port80_status, port135_status, port139_status
                           , port445_status, port3306_status, port3389_status, port8080_status)
        handing.insertServnews(index,num_i,os_status,serv21,serv22,serv23,serv80,serv135,serv139,serv445,serv3306,serv3389,serv8080)

        self.threadLock.release()

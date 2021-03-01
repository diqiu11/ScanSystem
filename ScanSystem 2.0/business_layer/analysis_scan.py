import matplotlib.pyplot as plt
import numpy as np
import pdfkit as pdf
from business_layer import html_mod
from persistence_layer import datahanding
from wordcloud import WordCloud
import os
class EXReport:
    def __init__(self,tableName):
        self.tableName = tableName
        self.systempie()
        self.portwebbarh()
        self.portfilebarh()
        self.portloginbarh()
        self.servcloud()
        self.exportPDF()

    def systempie(self):
        plt.clf()
        #win, Linux, other = datahanding.Sqlhanding.getsystemnum(self.tableName)
        system = datahanding.Sqlhanding(self.tableName)
        win, Linux, other = system.getsystemnum()
        sum = win + Linux + other
        # 显示中文
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 设置图饼
        data = [win / sum, Linux / sum, other / sum]
        labels = ['Windows', 'Linux/Unix', 'Other']
        explode = [0, 0, 0.3]
        colors = ['red', 'magenta', 'purple']
        plt.axes(aspect='equal')
        plt.xlim(0, 8)
        plt.ylim(0, 8)
        # 绘图
        plt.pie(x=data,  # 绘图数据
                labels=labels,  # 占比标签
                explode=explode,  # 突出显示
                colors=colors,  # 图饼自定义填充色
                autopct='%.3f%%',  # 百分比保留数
                pctdistance=0.8,  # 百分比与标签距离
                labeldistance=1.15,  # 标签与圆心距离
                startangle=180,  # 饼图初始角度
                center=(4, 4),  # 饼图圆心
                radius=3.8,  # 饼图半径
                counterclock=False,  # 是否逆时针
                wedgeprops={'linewidth': 1, 'edgecolor': 'green'},  # 设置饼图内外边界的属性值
                textprops={'fontsize': 12, 'color': 'black'},  # 文本标签属性值
                frame=1  # 是否显示饼图圆圈
                )

        # 不显示xy的刻度值
        plt.xticks(())
        plt.yticks(())
        # 添加图形标签
        plt.title(u'操作系统类型占比图')
        # 显示图形
        plt.savefig('..\\img\\system.jpg')
        # plt.show()

    def portwebbarh(self):
        plt.clf()
        web=datahanding.Sqlhanding(self.tableName)
        op80num, op3306num, op8080num = web.getwebportnum()
        op80NUM = int(op80num[0])
        op3306NUM = int(op3306num[0])
        op8080NUM = int(op8080num[0])
        x_data = ['80 Port', '3306 Port', '8080 Port']
        y_data = [op80NUM, op3306NUM, op8080NUM]  # 主机端口开放数量
        bar_width = 0.5
        plt.barh(y=range(len(x_data)), width=y_data, label='开放端口主机数量', color='steelblue', alpha=0.5, height=bar_width)
        # 在柱状图上显示具体数值，ha参数控制水平对齐方式，va参数控制垂直对齐方式
        for y, x in enumerate(y_data):
            plt.text(x + 0.1, y - bar_width / 2, '%s' % x, ha='center', va='bottom')
        plt.yticks(np.arange(len(x_data)), x_data)
        plt.title("关于Web常用端口开启情况图")
        # 设置坐标名称
        plt.xlabel("主机数")
        plt.ylabel("开启端口")
        # 显示图
        plt.legend()
        plt.savefig('..\\img\\webport.jpg')
        # plt.show()

    def portfilebarh(self):
        plt.clf()
        file = datahanding.Sqlhanding(self.tableName)
        op21num, op135num, op139num, op445num = file.getfileportnum()
        op21NUM = int(op21num[0])
        op135NUM = int(op135num[0])
        op139NUM = int(op139num[0])
        op445NUM = int(op445num[0])
        x_data = ['21 Port', '135 Port', '139 Port', '445 Port']
        y_data = [op21NUM, op135NUM, op139NUM, op445NUM]  # 主机端口开放数量
        bar_width = 0.5
        plt.barh(y=range(len(x_data)), width=y_data, label='开放端口主机数量', color='steelblue', alpha=0.5, height=bar_width)
        # 在柱状图上显示具体数值，ha参数控制水平对齐方式，va参数控制垂直对齐方式
        for y, x in enumerate(y_data):
            plt.text(x + 0.1, y - bar_width / 2, '%s' % x, ha='center', va='bottom')
        plt.yticks(np.arange(len(x_data)), x_data)
        plt.title("关于文件共享常用端口开启情况图")
        # 设置坐标名称
        plt.xlabel("主机数")
        plt.ylabel("开启端口")
        # 显示图
        plt.legend()
        plt.savefig('..\\img\\fileport.jpg')
        # plt.show()

    def portloginbarh(self):
        plt.clf()
        login = datahanding.Sqlhanding(self.tableName)
        op22num, op23num, op3389num = login.getloginportnum()
        op22NUM = int(op22num[0])
        op23NUM = int(op23num[0])
        op3389NUM = int(op3389num[0])
        x_data = ['22 Port', '23 Port', '3389 Port']
        y_data = [op22NUM, op23NUM, op3389NUM]  # 主机端口开放数量
        bar_width = 0.5
        plt.barh(y=range(len(x_data)), width=y_data, label='开放端口主机数量', color='steelblue', alpha=0.5, height=bar_width)
        # 在柱状图上显示具体数值，ha参数控制水平对齐方式，va参数控制垂直对齐方式
        for y, x in enumerate(y_data):
            plt.text(x + 0.1, y - bar_width / 2, '%s' % x, ha='center', va='bottom')
        plt.yticks(np.arange(len(x_data)), x_data)
        plt.title("关于远程登录常用端口开启情况图")
        # 设置坐标名称
        plt.xlabel("主机数")
        plt.ylabel("开启端口")
        # 显示图
        plt.legend()
        plt.savefig('..\\img\\loginport.jpg')
        # plt.show()

    def servcloud(self):
        servname = self.tableName+'_serv'
        serv = datahanding.Sqlhanding(servname)
        text,num = serv.getserv()
        fp = open('serv.txt', 'w')
        for i in range(num):
            for j in range(10):
                if text[i][j] == '':
                    pass
                else:
                    newtext = text[i][j].replace(' ', '_')
                    fp.write(newtext + ' ')
        fp.close()
        word = open('serv.txt', encoding='UTF-8').read()
        wordcloud = WordCloud(width=550,height=350,margin=2,background_color='black',font_path='..\\tools\\consolai.ttf')
        wordcloud.generate(word)
        wordcloud.to_file('..\\img\\serv.jpg')
        path = '.\\serv.txt'
        os.remove(path)

    def exportPDF(self):
        # 以html为模板，把图表这些插入到html里面，然后转换为PDF文件

        html_mod.html_ressult(self.tableName)
        # 输出PDF
        option = {
            'enable-local-file-access': None
        }
        config = pdf.configuration(wkhtmltopdf=r"..\\tools\\lib\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
        pdf.from_file(r'..\\' + self.tableName + '_Report.html', r'..\\' + self.tableName + '_Report.pdf', configuration=config,
                      options=option)
import time
from persistence_layer import datahanding
def html_ressult(Tabel_Name):
    #Tabel_Name = scan_tkinter_gui.variable_tab.get()
    html = open(r'..\\'+Tabel_Name+'_Report.html','w',encoding="utf-8")

    html.write(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Report</title>
            <style type="text/css">
                h1 { font-family:宋体}
                div { margin:0 auto;}
                div.div_head{ width:100%;text-align:center;overflow-x:hidden}
                div.div_summary{ width:70%;overflow-y:hidden}
                p { font-family:宋体;font-size:14px;}
                table.tb{ font-family:宋体;font-size:14px;border:1px;cellpadding:5%;width:500px;margin:0 auto;text-align:center;margin-top:50px;}
                div.div_system{ width:500px;height:450px;margin:0 auto;margin-top:50px;}
                div.div_portweb{ width:550px;height:450px;margin:0 auto;margin-top:50px;}
                div.div_portlogin{ width:550px;height:350px;margin:0 auto;margin-top:50px;}
                div.div_portfile{ width:550px;height:350px;margin:0 auto;margin-top:50px;}
                div.div_serv{ width:550px;height:350px;margin:0 auto;margin-top:50px;}
            </style>
        </head>
        <body>
            <!--报告头部标题-->
            <div class="div_head">
        
        """)

    html.write("<h1>%s Report</h1>"%(Tabel_Name))
    html.write("""<hr style="color:black">""")
    localtime = time.asctime(time.localtime(time.time()))
    html.write("<p >报告时间：%s</p></div>"%(localtime))
    html.write("""
    <!--报告概述内容:
    1、统计表格
    2、系统饼图
    3、各种类型的端口柱形图
    4、服务词云图
    -->
    
    <div class="div_summary">
        <h3>扫描数据统计：</h3>
          <table class="tb" border="1">
              <tr>
                  <td>存活主机数量</td>
                  <td>开放端口总数</td>
                  <td>Windows主机总数</td>
                  <td>Linux主机总数</td>
                  <td>其他主机总数</td>
              </tr>
    """)
    #数据库统计存活主机------统计表格
    #sum_alive = 5
    #sum_alive = select_delete.get_hostnum(Tabel_Name)
    sum = datahanding.Sqlhanding(Tabel_Name)
    sum_alive = sum.queryhostnum()
    html.write("<tr><!--动态写入数据--><td>%s</td>"%(sum_alive))
    html.write("<!--动态写入数据--><td>%s</td>"%(sum_alive))
    html.write("<!--动态写入数据--><td>%s</td>"%(sum_alive))
    html.write("<!--动态写入数据--><td>%s</td>"%(sum_alive))
    html.write("<td>..........</td></tr></table>")
    html.write("<h3>可视化数据统计：</h3>")
    html.write("""
    <div class="div_system">
        <h4>图中描述本次收集的主机操作系统类型信息。</h4>
        <!--动态写入饼图-->
    """)
    html.write("<img src=%s width=%s height=%s /></div>"%('./img/system.jpg','500px','350px'))

    html.write("""
        <div class="div_portweb">
            <!--动态写入webport柱状图-->
        """)
    html.write("<img src=%s width=%s height=%s /></div>" % ('./img/webport.jpg', '550px', '350px'))
    #analysis_scan.Portlogin_barh(Tabel_Name)
    html.write("""
            <div class="div_portlogin">
                <!--动态写入loginport柱状图-->
            """)
    html.write("<img src=%s width=%s height=%s /></div>" % ('./img/loginport.jpg', '550px', '350px'))

    #analysis_scan.Portfile_barh(Tabel_Name)
    html.write("""
                <div class="div_portfile">
                    <!--动态写入fileport柱状图-->
                """)
    html.write("<img src=%s width=%s height=%s /></div>" % ('./img/fileport.jpg', '550px', '350px'))

    html.write("""
                    <div class="div_serv">
                        <!--动态写入serv柱状图-->
                    """)
    html.write("<img src=%s width=%s height=%s /></div>" % ('./img/serv.jpg', '550px', '350px'))

    html.write('</body></html>')
    html.close()
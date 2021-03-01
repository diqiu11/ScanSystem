import tkinter as tk
from tkinter import ttk
from business_layer import scan_collect
from business_layer import output_excel
from business_layer import analysis_scan
from tkinter.messagebox import *
from tools import ipcheck
import time
from persistence_layer import datahanding
localtime = time.strftime("%Y-%m-%d %X",time.localtime())
class GUISystem(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        #self.place()
        self.createtitle()  #自定义标题
        self.tbName()       #自定义表名
        self.inputscan()    #输入栏
        self.fileoutput()   #输出栏
        self.pointout()     #提示栏

    def createtitle(self):
        self.label_title = tk.Label(self.master,text="Scan System",bg="black",fg="red",font=("Comic Sans MS",17))
        self.label_table = tk.Label(self.master, text="Storage Name：", font=("Comic Sans MS", 12))

        # 标题显示
        self.label_title.place(x=0, y=0, width=150, height=40)
        self.label_table.place(x=190, y=10)

    def tbName(self):
        self.variable_tab = tk.StringVar()
        self.tabName_entry = tk.Entry(self.master, font=("Comic Sans MS", 13), textvariable=self.variable_tab)
        self.tabName_entry.place(x=300, y=10, width=150, height=30)

    def inputscan(self):
        # 扫描输入栏
        self.label_ip = tk.Label(self.master, text="IP：", font=("Comic Sans MS", 12))
        self.label_mask = tk.Label(self.master, text="MASK：", font=("Comic Sans MS", 12))
        self.variable_ip = tk.StringVar()
        self.ip_entry = tk.Entry(self.master, font=("Comic Sans MS", 13), textvariable=self.variable_ip)
        self.ip_entry.insert(0, "192.168.0.1")
        self.variable_mask = tk.StringVar()
        self.mask_entry = tk.Entry(self.master, font=("Comic Sans MS", 13), textvariable=self.variable_mask)
        self.mask_entry.insert(0, "24")
        self.start_button = tk.Button(self.master, text="START", font=("Comic Sans MS", 12), command=self.do_scan)

        # 输入栏显示
        self.label_ip.place(x=40, y=80)
        self.label_mask.place(x=260, y=80)
        self.ip_entry.place(x=80, y=80, width=150, height=30)
        self.mask_entry.place(x=330, y=80, width=50, height=30)
        self.start_button.place(x=400, y=80, width=60, height=30)



    def do_scan(self):
        self.ip = self.variable_ip.get()
        self.mask = self.variable_mask.get()
        self.Table_Name = self.variable_tab.get()
        dataA = datahanding.Sqlhanding(self.Table_Name)
        if dataA.booltable() == 1:
            tip = localtime + '  与数据库表名称重叠，请重新输入。\n'
            self.get_tip(tip)
            return
        if self.Table_Name=='':
            print("Storage Name项为空，请重新输入。")
            tip = localtime+'  Storage Name项为空，请重新输入。\n'
            self.get_tip(tip)
            return
        elif self.ip=='' or self.mask=='':
            print("IP或MASK项为空，请重新输入。")
            tip = localtime+'  IP或MASK项为空，请重新输入。\n'
            self.get_tip(tip)
            return
        elif ipcheck.check_ip(self.ip) == False:
            print("输入IP项不符合规范，请重新输入。")
            tip = localtime+'  输入IP项不符合规范，请重新输入。\n'
            self.get_tip(tip)
            return
        elif ipcheck.check_mask(self.mask) == False:
            print("输入MASK项不符合规范，请重新输入。")
            tip = localtime + '  输入MASK项不符合规范，请重新输入。\n'
            self.get_tip(tip)
            return
        else:
            try:
                scan_collect.ScanCollect(self.ip, self.mask, self.Table_Name)
                tip = localtime + '  扫描成功。\n'
                self.get_tip(tip)
                return
            except:
                tip = localtime + '  扫描失败，请检查数据库。\n'
                self.get_tip(tip)
                return



    def fileoutput(self):
        # 输出按钮
        self.xml_button = tk.Button(self.master, text="输出表格文件", font=("黑体", 15), command=self.do_out_ex)
        self.html_button = tk.Button(self.master, text="输出统计文件", font=("黑体", 15), command=self.do_out_pdf)
        # 输出栏信息
        self.xml_button.place(x=80, y=140, width=150, height=40)
        self.html_button.place(x=260, y=140, width=150, height=40)

    def do_out_ex(self):
        self.Table_Name = self.variable_tab.get()
        dataA = datahanding.Sqlhanding(self.Table_Name)
        if dataA.booltable() == 0:
            tip = localtime + '  数据库表不存在，请重新输入。\n'
            self.get_tip(tip)
            return
        if self.Table_Name == '':
            print("Storage Name项为空，请重新输入。")
            tip = localtime + '  Storage Name项为空，请重新输入。\n'
            self.get_tip(tip)
            return
        else:
            try:
                # output_excel.export_excel(self.Table_Name)
                exc = output_excel.ExExcel(self.Table_Name)
                exc.exportExcel()
                tip = localtime + '  输出'+self.Table_Name+'.xls'+'成功。\n'
                self.get_tip(tip)
            except:
                tip = localtime + '  输出失败，未知错误。\n'
                self.get_tip(tip)
                return


    def do_out_pdf(self):
        self.Table_Name = self.variable_tab.get()
        dataA = datahanding.Sqlhanding(self.Table_Name)
        if dataA.booltable() == 0:
            tip = localtime + '  数据库表不存在，请重新输入。\n'
            self.get_tip(tip)
            return
        if self.Table_Name == '':
            print("Storage Name项为空，请重新输入。")
            tip = localtime + '  Storage Name项为空，请重新输入。\n'
            self.get_tip(tip)
            return
        else:
            try:
                # analysis_scan.export_report(self.Table_Name)
                analysis_scan.EXReport(self.Table_Name)
                tip = localtime + '  输出' + self.Table_Name + '_Report.pdf' + '成功。\n'
                self.get_tip(tip)
            except:
                tip = localtime + '  输出失败，未知错误。\n'
                self.get_tip(tip)
                return


    # tip栏
    def pointout(self):
        # 信息提示栏
        self.scroll = tk.Scrollbar()
        self.text = tk.Text(self.master, font=("Comic Sans MS", 10))
        self.scroll.config(command=self.text.yview)  # 关联
        self.text.config(yscrollcommand=self.scroll.set, state='disabled')
        # 提示栏显示
        self.text.place(x=30, y=200, width=420, height=140)
        self.scroll.place(x=450, y=200, width=19, height=140)

    def get_tip(self,tip):
        self.text.config(state='normal')
        self.text.insert('end', tip)
        self.text.config(state='disabled')
    #tipflush
    def flush_tip(self):
        self.text.config(state='normal')
        self.text.delete('1.0', 'end')
        self.text.config(state='disabled')

class GUIDelete(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.newstable()
        self.deleteButton()
        self.quitButton()

    def newstable(self):
        self.label_table_name = tk.Label(self.master,text="Record Name：",font=("Comic Sans MS", 12))
        columns = ['序号','记录名称']
        self.scrollbar_y = tk.Scrollbar(self.master)
        self.table = ttk.Treeview(self.master,height=10,columns=columns,show='headings',yscrollcommand=self.scrollbar_y.set)
        self.table.heading('序号',text='序号')
        self.table.heading('记录名称', text='记录名称')
        self.table.column('序号',width=40,anchor='center')
        self.table.column('记录名称', width=200,anchor='center')
        self.label_table_name.place(x=10,y=10,width=150,height=30)
        self.table.place(x=20,y=50)
        #表格滚动条
        self.scrollbar_y.config(command=self.table.yview)
        self.scrollbar_y.place(x=264,y=50,width=15,height=230)
        #数据处理插入数据
        self.show_data()

    def deleteButton(self):
        self.delete_button = tk.Button(self.master, text="删除扫描记录", font=("黑体", 15), command=self.call_do_delete)
        self.delete_button.place(x=300,y=150,width=150,height=40)

    def quitButton(self):
        self.quit_button = tk.Button(self.master, text="退出", font=("黑体", 15), command=self.master.destroy)
        self.quit_button.place(x=325, y=230, width=100, height=40)

    def call_do_delete(self):
        selection = self.table.selection()
        # self.flag = showinfo('提示','确认删除此信息？')
        # if self.flag:
        for item in selection:
            getname = self.table.item(item)
            do_del = datahanding.Sqlhanding(getname['values'][1])
            do_del.delete_table()
        self.show_data()


    def show_data(self):
        children = self.table.get_children()
        for child in children:
            self.table.delete(child)
        showdata = datahanding.DataShow()
        data,num = showdata.gettablename()
        for i in range(num[0]):
            self.table.insert("",i,values=(i,data[i][0]))



def main():
    # 窗口
    win = tk.Tk()
    win.title("ScanSystem")
    win.geometry("500x350+200+50")
    win.resizable(0, 0)
    # 菜单
    menubar = tk.Menu(win)
    def deleteTable():
        #弹出新窗口有一个表格显示数据库表，一个选中功能，一个删除按钮
        win_two = tk.Tk()
        win_two.title("DeleteManager")
        win_two.geometry("500x300+700+100")
        win_two.resizable(0, 0)
        two_app = GUIDelete(master=win_two)
        win_two.iconbitmap("..\\img\\Burn.ico")
        win_two.mainloop()

    menubar.add_cascade(label='管理记录',command=deleteTable)

    def about_system():
        showinfo('关于','林狄秋3119000071-毕业设计')
    menubar.add_cascade(label='关于',command=about_system)

    def quit_system():
        win.quit()
        win.destroy()


    menubar.add_cascade(label='退出', command=quit_system)
    app = GUISystem(master = win)
    
    
    # 显示菜单
    win.config(menu=menubar)
    win.iconbitmap("..\\img\\Burn.ico")
    win.mainloop()



if __name__ == '__main__':
    main()

# -*-coding: utf-8-*-

from tkinter import Tk
from time import sleep
from tkinter.messagebox import showwarning  # 导入Tkinter和tkMessageBox是为了使用showwarning消息框来终止演示
import win32com.client as win32

warn = lambda app: showwarning(app, 'Exit?')
RANGE = range(3, 8)


def excel():
    app = 'Excel'
    x1 = win32.gencache.EnsureDispatch('%s.Application' % app)  # 指定应用程序？第一步
    ss = x1.Workbooks.Add()  # 添加工作簿？
    sh = ss.ActiveSheet  # 正在显示的活动表格的句柄？第二步
    x1.Visible = True  # Visble必须标记为True，这样才能让应用程序显示在桌面上。就是第三步
    sleep(1)

    # 本程序的应用部分，第四步
    sh.Cells(1, 1).Value = 'Python-to-%s Demo' % app  # 演示的标题，被写在左上角的第一格，即A1。
    sleep(1)
    for i in RANGE:
        sh.Cells(i, 1).Value = 'Line %d' % i  # 在i1写入Line i
        sleep(1)
    sh.Cells(i + 2, 1).Value = "Th-th-th-that's all folks!"  # 在A9显示Th-th-th-that's all folks!

    warn(app)  # 弹出showwarning对话框，显示内容见warn匿名函数的定义
    ss.Close(False)  # 表示电子表格关闭时不会被保存，但是本人在演示时仍然弹出是否保存的对话框。第五步
    x1.Application.Quit()  # 退出应用，第六步


if __name__ == "__main__":
    Tk().withdraw()  # 隐藏顶层窗口
    excel()

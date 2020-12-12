import os
import pandas as pd
import numpy as np

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import library.base as base

from library.colors import color_main
from library.colors import color_dop
from library.colors import color_knop
from library.colors import color_text

def exp1():
    """
    Функция сохранения текстового отчета. 
    """
    np.savetxt(r'output\flight_time.txt', base.table_n1[['Рейс','Время']], fmt='%s')
def exp2():
    """
    Функция сохранения текстового отчета. 
    """
    np.savetxt(r'output\code_flight.txt', base.table_n1[['Код авиакомпании','Рейс']], fmt='%s')
def exp3():
    """
    Функция сохранения текстового отчета. 
    """
    np.savetxt(r'output\code_flight_time.txt', base.table_n1[['Код авиакомпании','Рейс', 'Время']], fmt='%s')
def exp4():
    """
    Функция сохранения текстового отчета. 
    """
    np.savetxt(r'output\code_flight_plane.txt', base.table_n1[['Код авиакомпании','Рейс', 'Самолёт']], fmt='%s')
def exp5():
    """
    Функция сохранения текстового отчета. 
    """
    np.savetxt(r'output\code_departure_destination.txt', base.table_n1[['Рейс','Отправление', 'Назначение']], fmt='%s')
def exp6():
    """
    Функция сохранения текстового отчета. 
    """
    np.savetxt(r'output\code_flight_departure_destination.txt', base.table_n1[['Код авиакомпании', 'Рейс','Отправление', 'Назначение']], fmt='%s')
def exp7():
    """
    Функция сохранения текстового отчета. 
    """
    np.savetxt(r'output\code_plane.txt', base.table_n1[['Код авиакомпании','Самолёт']], fmt='%s')
def exp8():
    """
    Функция сохранения текстового отчета. 
    """
    np.savetxt(r'output\flight_terminal_gate.txt', base.table_n1[['Рейс','Терминал','Выход']], fmt='%s')
def exp9():
    """
    Функция сохранения текстового отчета. 
    """
    np.savetxt(r'output\flight.txt', base.table_n1[['Рейс']], fmt='%s')
def exp10():
    """
    Функция сохранения текстового отчета. 
    """
    np.savetxt(r'output\code.txt', base.table_n1[['Код авиакомпании']], fmt='%s')
def exp11():
    """
    Функция сохранения текстового отчета. 
    """
    np.savetxt(r'output\plane.txt', base.table_n1[['Самолёт']], fmt='%s')
def exp12():
    """
    Функция сохранения текстового отчета. 
    """
    np.savetxt(r'output\time.txt', base.table_n1[['Время']], fmt='%s')
def exp13():
    """
    Функция сохранения текстового отчета. 
    """
    np.savetxt(r'output\board.txt', base.table_n1, fmt='%s')
def exp14():
    """
    Функция сохранения текстового отчета. 
    """
    np.savetxt(r'output\flight_status.txt', base.table_n1[['Рейс','Статус']], fmt='%s')                                                                                                                                                                                                                                           

def export_excel():
    """
    Функция записи таблицы рейсов в таблицу
    """ 
    writer = pd.ExcelWriter(r'output\table.xlsx', engine='xlsxwriter')
    base.table_n1.to_excel(writer, 'Sheet1')
    writer.save()
def report1(table_dn,table_n3):
    """
    Верстка окна выбора графика
    """
    root=Tk()
    root.minsize(500,400)
    root.maxsize(500,450)
    root.resizable(False,False)
    root.configure(bg=color_main)
    def Plot(table_dn):
             """
             Окно графиков распределения по аэропортам.
             Параметры:
             table_dn - переменная БД.
             """
             def save_plot():
                 """
                 Функция сохранения графика с возможностью выбора имени и пути файла.
                 """
                 name=fd.asksaveasfilename(filetypes=(("PNG","*.png"),("all files","*.*")))
                 fmt=name+".png"
                 fig.savefig(fmt)
             def ColSPrice():
                 """
                 Строит столбчатую диаграмму по аэропорту прибытия.
                 """
                 ax.cla()
                 ax.set_title("Аэропорт прибытия")
                 ax.set_ylabel("Количество вылетов",rotation=90)
                 Types = table_dn['Назначение'].unique()
                 ax.set_xticklabels(Types, fontsize = 8)
                 ax.grid(axis='y')
                 n, bins, patches = ax.hist(table_dn['Назначение'], 50,color ='royalblue', histtype='barstacked',) 
                 graph.draw()
                 pplf.update()
             def BWPrice():
                 """
                 Строит круговую диаграмму по аэропорту прибытия.
                 """
                 ax.cla()
                 ax.set_title("Аэропорт прибытия")
                 Types = table_dn['Назначение'].unique()
                 TTypes = []
                 for Type in Types:
                     SEL = (table_dn['Назначение'] == Type)
                     TTypes.append(len(table_dn[SEL]))
                 ax.grid()
                 ax.pie(TTypes,labels=Types,autopct='%1.1f%%', pctdistance=0.9,shadow=False, startangle=90)
                 ax.axis('equal')
                 graph.draw()
                 pplf.update()
             def ScPrice():
                 """
                 Строит диаграмму рассеивания по аэропорту прибытия.
                 """
                 ax.cla()
                 ax.set_title("Аэропорты прибытия")
                 Types = table_dn['Назначение'].unique()
                 ax.set_xlabel("Количество вылетов")
                 TTypes = []
                 for Type in Types:
                     SEL = (table_dn['Назначение'] == Type)
                     TTypes.append(len(table_dn[SEL]))
                 ax.grid()
                 ax.boxplot(TTypes ,vert=False,widths=1)
                 ax.axis('equal')
                 graph.draw()
                 pplf.update()
             def ColRate():
                 """
                 Строит столбчатую диаграмму по аэропорту отправления.
                 """
                 ax.cla()
                 ax.set_title("Аэропорт отправления")
                 ax.set_ylabel("Количество вылетов",rotation=90)
                 Types = table_dn['Отправление'].unique()
                 ax.set_xticklabels(Types, fontsize = 8)
                 ax.grid(axis='y')
                 n, bins, patches = ax.hist(table_dn['Отправление'], 50,color ='royalblue', histtype='barstacked',) 
                 graph.draw()
                 pplf.update()
             def BWRate():
                 """
                 Строит круговую диаграмму по аэропорту отправления.
                 """
                 ax.cla()
                 ax.set_title("Аэропорт отправления")
                 Types = table_dn['Отправление'].unique()
                 TTypes = []
                 for Type in Types:
                     SEL = (table_dn['Отправление'] == Type)
                     TTypes.append(len(table_dn[SEL]))
                 ax.grid()
                 ax.pie(TTypes,labels=Types,autopct='%1.1f%%', shadow=False, startangle=90)
                 ax.axis('equal')
                 graph.draw()
                 pplf.update()
             def ScRate():
                 """
                 Строит диаграмму рассеивания по аэропорту отправления.
                 """
                 ax.cla()
                 ax.set_title("Аэропорты отправления")
                 Types = table_dn['Отправление'].unique()
                 ax.set_xlabel("Количество вылетов")
                 TTypes = []
                 for Type in Types:
                     SEL = (table_dn['Отправление'] == Type)
                     TTypes.append(len(table_dn[SEL]))
                 ax.grid()
                 ax.boxplot(TTypes ,vert=False,widths=1)
                 ax.axis('equal')
                 graph.draw()
                 pplf.update() 
             pplf = Toplevel(master = root)
             pplf.title("Графики")
             pplf.minsize(800,600)
             pplf.maxsize(800,600)
             pplf.resizable(False,False)
             pplf.configure(bg=color_main)
             controls1 = Frame(pplf,height = 50,width = 400,bg=color_main)
             controls1.pack(side = TOP,pady=3)
             PriceText = Label(controls1,bg=color_main,text="Аэропорт прибытия",font=("Arial", 15),fg=color_text)
             PriceText.pack(side = LEFT,padx=5,pady=3)
             ColTable1 = Button(controls1,text="Столбчатая\nдиаграмма",font=("Arial", 12),bg=color_knop,fg=color_text,width=15,height=2,command=ColSPrice)
             ColTable1.pack(side=LEFT,padx=5,pady=3)
             BVTable1 = Button(controls1,text="Круговая\nдиаграмма",font=("Arial", 12),bg=color_knop,fg=color_text,width=15,height=2,command=BWPrice)
             BVTable1.pack(side=LEFT,padx=5,pady=3)
             DispTable1 = Button(controls1,text="Диаграмма\nразмаха",font=("Arial", 12),bg=color_knop,fg=color_text,width=15,height=2,command=ScPrice)
             DispTable1.pack(side=LEFT,padx=5,pady=3)
             controls2 = Frame(pplf,height = 50,width = 400,bg=color_main)
             controls2.pack(side = TOP,pady=3)
             RateText = Label(controls2,bg=color_main,text="Аэропорт отправления",font=("Arial", 15),fg=color_text)
             RateText.pack(side = LEFT,padx=5,pady=3)
             ColTable2 = Button(controls2,text="Столбчатая\nдиаграмма",font=("Arial", 12),bg=color_knop,fg=color_text,width=15,height=2,command=ColRate)
             ColTable2.pack(side=LEFT,padx=5,pady=3)
             BVTable2 = Button(controls2,text="Круговая\nдиаграмма",font=("Arial", 12),bg=color_knop,fg=color_text,width=15,height=2,command=BWRate)
             BVTable2.pack(side=LEFT,padx=5,pady=3)
             DispTable2 = Button(controls2,text="Диаграмма\nразмаха",font=("Arial", 12),bg=color_knop,fg=color_text,width=15,height=2,command=ScRate)
             DispTable2.pack(side=LEFT,padx=5,pady=3)
             fig = Figure()
             ax = fig.add_subplot(111)
             ax.grid()
             graph=FigureCanvasTkAgg(fig,master=pplf)
             graph.get_tk_widget().pack(side=TOP,fill=BOTH,pady=7,expand=True)
             Other = Frame(pplf,height = 50,width = 400,bg=color_main)
             Other.pack(side = TOP,pady = 3)
             SaveBut = Button(Other,text="Сохранить",bg=color_knop,fg=color_text,width=15,height=1,command=save_plot)
             SaveBut.pack(side=LEFT,padx=5,pady=3)
             StopBut = Button(Other,text="Выход",bg=color_knop,fg=color_text,width=15,height=1,command = lambda: pplf.destroy())
             StopBut.pack(side=LEFT,padx=5,pady=3)
             pplf.mainloop()
    def PP():
        """
        Вспомогательная функция вызова окна графиков распределения по аэропортам.
        """
        Plot(table_dn)

    def EPlot(table_dn, title, y, collumn):
             """
             Окно построения графиков распределения по терминалам.
             Параметры:
             table_dn - переменная БД.
            
             """
             def save_plot():
                 """
                 Функция сохранения графика с возможностью выбора имени и пути файла.
                 """
                 name=fd.asksaveasfilename(filetypes=(("PNG","*.png"),("all files","*.*")))
                 fmt=name+".png"
                 fig.savefig(fmt)
             def ColSPrice():
                 """
                 Строит столбчатую диаграмму распределения по терминалам.
                 """
                 ax.cla()
                 ax.set_title(title)
                 ax.grid()
                 ax.set_ylabel(y,rotation=90)
                 Types = table_dn[collumn].unique()
                 TTypes = []
                 for Type in Types:
                     SEL = (table_dn[collumn] == Type)
                     TTypes.append(len(table_dn[SEL]))
                 ax.set_xticklabels(Types,rotation = 0, fontsize = 8)
                 ax.grid()
                 fig.set_figwidth(12)
                 ax.bar(Types,TTypes,color='royalblue')
                 graph.draw()
                 pplf.update()
             def BWPrice():
                 """
                 Строит круговую диаграмму по терминалу.
                 """
                 ax.cla()
                 ax.set_title(title)
                 Types = table_dn[collumn].unique()
                 TTypes = []
                 for Type in Types:
                     SEL = (table_dn[collumn] == Type)
                     TTypes.append(len(table_dn[SEL]))
                 ax.grid()
                 ax.pie(TTypes,labels=Types,autopct='%1.1f%%', shadow=False, startangle=90)
                 ax.axis('equal')
                 graph.draw()
                 pplf.update()
             pplf = Toplevel(master = root)
             pplf.title("Графики")
             pplf.minsize(800,600)
             pplf.maxsize(800,600)
             pplf.resizable(False,False)
             pplf.configure(bg=color_main)
             controls1 = Frame(pplf,height = 50,width = 400,bg=color_main)
             controls1.pack(side = TOP,pady=3)
             PriceText = Label(controls1,bg=color_main,text=title,fg=color_text)
             PriceText.pack(side = LEFT,padx=5,pady=3)
             ColTable1 = Button(controls1,text="Столбчатая\nдиаграмма",bg=color_knop,fg=color_text,width=15,height=2,command=ColSPrice)
             ColTable1.pack(side=LEFT,padx=5,pady=3)
             BVTable1 = Button(controls1,text="Круговая\nдиаграмма",bg=color_knop,fg=color_text,width=15,height=2,command=BWPrice)
             BVTable1.pack(side=LEFT,padx=5,pady=3)
             fig = Figure()
             ax = fig.add_subplot(111)
             ax.grid()
             graph=FigureCanvasTkAgg(fig,master=pplf)
             graph.get_tk_widget().pack(side=TOP,fill=BOTH,pady=7,expand=True)
             Other = Frame(pplf,height = 50,width = 400,bg=color_main)
             Other.pack(side = TOP,pady = 3)
             SaveBut = Button(Other,text="Сохранить",bg=color_knop,fg=color_text,width=15,height=1,command=save_plot)
             SaveBut.pack(side=LEFT,padx=5,pady=3)
             StopBut = Button(Other,text="Выход",bg=color_knop,fg=color_text,width=15,height=1,command = lambda: pplf.destroy())
             StopBut.pack(side=LEFT,padx=5,pady=3)
             pplf.mainloop() 
    def EP(title, y, collumn):
        """
        Вспомогательная функция вызова окна графиков распределения по терминалам.
        """
        EPlot(table_dn, title, y, collumn)


    def CPlot(table_dn):
             """
             Окно построения графиков распределения по авиакомпаниям.
             Параметры:
             table_dn - переменная БД.
             """
             def save_plot():
                 """
                 Функция сохранения графика с возможностью выбора имени и пути файла.
                 """
                 name=fd.asksaveasfilename(filetypes=(("PNG","*.png"), ("all files","*.*")))
                 fmt=name+".png"
                 fig.savefig(fmt)
             def ColType():
                 """
                 Строит столбчатую диаграмму распределения по авиакомпаниям.
                 """
                 ax.cla()
                 ax.set_title("Авиакомпании")
                 ax.set_ylabel("Количество вылетов",rotation=90)
                 Types = table_dn['Код авиакомпании'].unique()
                 ax.set_xticklabels(Types, fontsize = 8)
                 ax.grid(axis='y')
                 n, bins, patches = ax.hist(table_dn['Код авиакомпании'], 50,color ='royalblue', histtype='barstacked',) 
                 graph.draw()
                 pplf.update()
             def BWType():
                 """
                 Строит круговую диаграмму распределения по авиакомпаниям.
                 """
                 ax.cla()
                 ax.set_title("Авиакомпании")
                 Types = table_dn['Код авиакомпании'].unique()
                 TTypes = []
                 for Type in Types:
                     SEL = (table_dn['Код авиакомпании'] == Type)
                     TTypes.append(len(table_dn[SEL]))
                 ax.grid()
                 ax.pie(TTypes,labels=Types,autopct='%1.1f%%', shadow=False, startangle=90)
                 ax.axis('equal')
                 graph.draw()
                 pplf.update()
             def BW1Type():
                 """
                 Строит диаграмму рассеивания по авиакомпаниям.
                 """
                 ax.cla()
                 ax.set_title("Авиакомпании")
                 Types = table_dn['Код авиакомпании'].unique()
                 ax.set_xlabel("Количество вылетов")
                 TTypes = []
                 for Type in Types:
                     SEL = (table_dn['Код авиакомпании'] == Type)
                     TTypes.append(len(table_dn[SEL]))
                 ax.grid()
                 ax.boxplot(TTypes ,vert=False,widths=1)
                 ax.axis('equal')
                 graph.draw()
                 pplf.update()  
             pplf = Toplevel(master = root)
             pplf.minsize(800,600)
             pplf.maxsize(800,600)
             pplf.resizable(False,False)
             pplf.configure(bg=color_main)
             controls1 = Frame(pplf,height = 50,width = 400,bg=color_main)
             controls1.pack(side = TOP,pady=3)
             PriceText = Label(controls1,bg=color_main,text="Авиакомпания",fg=color_text)
             PriceText.pack(side = LEFT,padx=5,pady=3)
             ColTable1 = Button(controls1,text="Столбчатая\nдиаграмма",bg=color_knop,fg=color_text,width=15,height=2,command=ColType)
             ColTable1.pack(side=LEFT,padx=5,pady=3)
             BVTable1 = Button(controls1,text="Круговая\nдиаграмма",bg=color_knop,fg=color_text,width=15,height=2,command=BWType)
             BVTable1.pack(side=LEFT,padx=5,pady=3)
             DispTable1 = Button(controls1,text="Диаграмма\nразмаха",bg=color_knop,fg=color_text,width=15,height=2,command=BW1Type)
             DispTable1.pack(side=LEFT,padx=5,pady=3)
             fig = Figure()
             ax = fig.add_subplot(111)
             ax.grid()
             graph=FigureCanvasTkAgg(fig,master=pplf)
             graph.get_tk_widget().pack(side=TOP,fill=BOTH,pady=7,expand=True)
             Other = Frame(pplf,height = 50,width = 400,bg=color_main)
             Other.pack(side = TOP,pady = 3)
             SaveBut = Button(Other,text="Сохранить",bg=color_knop,fg=color_text,width=15,height=1,command=save_plot)
             SaveBut.pack(side=LEFT,padx=5,pady=3)
             StopBut = Button(Other,text="Выход",bg=color_knop,fg=color_text,width=15,height=1,command = lambda: pplf.destroy())
             StopBut.pack(side=LEFT,padx=5,pady=3)
             pplf.mainloop()
    def CP():
        """
        Вспомогательная функция вызова окна графиков распределения по авиакомпаниям.
        """
        CPlot(table_dn)
    def ClPlot(table_dn,table_n3):
             """
             Окно построения графиков распределения по самолетам.
             Параметры:
             table_dn - переменная БД.
             """
             def save_plot():
                 """
                 Функция сохранения графика с возможностью выбора имени и пути файла.
                 """
                 name=fd.asksaveasfilename(filetypes=(("PNG","*.png"),("all files","*.*")))
                 fmt=name+".png"
                 fig.savefig(fmt)
             def ColType():
                 """
                 Строит столбчатую диаграмму распределения по самолетам.
                 """
                 ax.cla()
                 ax.set_title("Самолёты")
                 ax.set_ylabel("Количество вылетов",rotation=90)
                 Types = table_dn['Самолёт'].unique()
                 ax.set_xticklabels(Types,rotation = 40, fontsize = 8)
                 ax.grid(axis='y')
                 n, bins, patches = ax.hist(table_dn['Самолёт'], 50,color ='royalblue', histtype='barstacked',) 
                 graph.draw()
                 pplf.update()
             def BWType():
                 """
                 Строит  круговую диаграмму  распределения по самолетам.
                 """
                 ax.cla()
                 ax.set_title("Самолёты")
                 Types = table_dn['Самолёт'].unique()
                 TTypes = []
                 for Type in Types:
                     SEL = (table_dn['Самолёт'] == Type)
                     TTypes.append(len(table_dn[SEL]))
                 ax.grid()
                 ax.pie(TTypes,labels=Types,autopct='%1.1f%%', shadow=False, startangle=90)
                 ax.axis('equal')
                 graph.draw()
                 pplf.update()
             def BTType():
                 """
                 Строит диаграмму рессеивания распределения по вместимости самолетов.
                 """
                 ax.cla()
                 ax.set_title("Самолёты")
                 Types = table_dn['Самолёт'].unique()
                 TTypes = []
                 for Type in Types:
                     SEL = (table_dn['Самолёт'] == Type)
                     TTypes.append(len(table_dn[SEL]))
                 ax.set_ylabel("Количество вылетов",rotation=90)
                 ax.set_xlabel("Наименивание самолета")
                 ax.grid()
                 ax.set_xticklabels(Types,rotation = 40, fontsize = 8)
                 ax.scatter(Types, TTypes,table_n3['Вместимость'], c="royalblue")
                 table_n3[['Вместимость']] = table_n3[['Вместимость']].apply(pd.to_numeric)
                 graph.draw()
                 pplf.update()
             pplf = Toplevel(master = root)
             pplf.minsize(1100,600)
             pplf.maxsize(1100,600)
             pplf.resizable(False,False)
             pplf.configure(bg=color_main)
             controls1 = Frame(pplf,height = 50,width = 400,bg=color_main)
             controls1.pack(side = TOP,pady=3)
             PriceText = Label(controls1,bg=color_main,text="Самолеты",fg=color_text)
             PriceText.pack(side = LEFT,padx=5,pady=3)
             ColTable1 = Button(controls1,text="Столбчатая\nдиаграмма",bg=color_knop,fg=color_text,width=10,height=2,command=ColType)
             ColTable1.pack(side=LEFT,padx=5,pady=3)
             BVTable1 = Button(controls1,text="Круговая\nдиаграмма",bg=color_knop,fg=color_text,width=10,height=2,command=BWType)
             BVTable1.pack(side=LEFT,padx=5,pady=3)
             DispTable1 = Button(controls1,text="Диаграмма\nрассеивания",bg=color_knop,fg=color_text,width=10,height=2,command=BTType)
             DispTable1.pack(side=LEFT,padx=5,pady=3)
             fig = Figure()
             ax = fig.add_subplot(111)
             ax.grid()
             graph=FigureCanvasTkAgg(fig,master=pplf)
             graph.get_tk_widget().pack(side=TOP,fill=BOTH,pady=7,expand=True)
             Other = Frame(pplf,height = 50,width = 400,bg=color_main)
             Other.pack(side = TOP,pady = 3)
             SaveBut = Button(Other,text="Сохранить",bg=color_knop,fg=color_text,width=15,height=1,command=save_plot)
             SaveBut.pack(side=LEFT,padx=5,pady=3)
             StopBut = Button(Other,text="Выход",bg=color_knop,fg=color_text,width=15,height=1,command = lambda: pplf.destroy())
             StopBut.pack(side=LEFT,padx=5,pady=3)
             pplf.mainloop()
    def ClP():
        """
        Вспомогательная функция вызова окна графиков распределения по самолетам.
        """
        ClPlot(table_dn,table_n3)
    def TTPlot(table_dn):
             """
             Окно построения графиков распределения по выходам.
             Параметры:
             table_dn - переменная БД.
             """
             def save_plot():
                 """
                 Функция сохранения графика с возможностью выбора имени и пути файла.
                 """
                 name=fd.asksaveasfilename(filetypes=(("PNG","*.png"),("all files","*.*")))
                 fmt=name+".png"
                 fig.savefig(fmt)
             def ColType():
                 """
                 Строит столбчатую диаграмму по выходам.
                 """
                 ax.cla()
                 ax.set_title("Выходы")
                 ax.grid()
                 ax.set_ylabel("Число вылетов",rotation=90)
                 Types = table_dn['Выход'].unique()
                 TTypes = []
                 for Type in Types:
                     SEL = (table_dn['Выход'] == Type)
                     TTypes.append(len(table_dn[SEL]))
                 ax.set_xticklabels(Types,rotation = 0, fontsize = 8)
                 ax.grid()
                 fig.set_figwidth(12)
                 ax.bar(Types,TTypes,color='royalblue')
                 graph.draw()
                 pplf.update()
             def BWType():
                 """
                 Строит  круговую диаграмму  распределения по выходам.
                 """
                 ax.cla()
                 ax.set_title("Выходы")
                 Types = table_dn['Выход'].unique()
                 TTypes = []
                 for Type in Types:
                     SEL = (table_dn['Выход'] == Type)
                     TTypes.append(len(table_dn[SEL]))
                 ax.grid()
                 ax.pie(TTypes,labels=Types,autopct='%1.1f%%', shadow=False, startangle=90)
                 ax.axis('equal')
                 graph.draw()
                 pplf.update()
             pplf = Toplevel(master = root)
             pplf.minsize(900,680)
             pplf.maxsize(900,680)
             pplf.resizable(False,False)
             pplf.configure(bg=color_main)
             controls1 = Frame(pplf,height = 50,width = 400,bg=color_main)
             controls1.pack(side = TOP,pady=3)
             PriceText = Label(controls1,bg=color_main,text="Выходы",fg=color_text)
             PriceText.pack(side = LEFT,padx=5,pady=3)
             ColTable1 = Button(controls1,text="Столбчатая\nдиаграмма",bg=color_knop,fg=color_text,width=15,height=2,command=ColType)
             ColTable1.pack(side=LEFT,padx=5,pady=3)
             BVTable1 = Button(controls1,text="Круговая\nдиаграмма",bg=color_knop,fg=color_text,width=15,height=2,command=BWType)
             BVTable1.pack(side=LEFT,padx=5,pady=3)
             fig = Figure()
             ax = fig.add_subplot(111)
             ax.grid()
             graph=FigureCanvasTkAgg(fig,master=pplf)
             graph.get_tk_widget().pack(side=TOP,fill=BOTH,pady=7,expand=True)
             Other = Frame(pplf,height = 50,width = 400,bg=color_main)
             Other.pack(side = TOP,pady = 3)
             SaveBut = Button(Other,text="Сохранить",bg=color_knop,fg=color_text,width=15,height=1,command=save_plot)
             SaveBut.pack(side=LEFT,padx=5,pady=3)
             StopBut = Button(Other,text="Выход",bg=color_knop,fg=color_text,width=15,height=1,command = lambda: pplf.destroy())
             StopBut.pack(side=LEFT,padx=5,pady=3)
             pplf.mainloop()
    def TTP():
        """
        Вспомогательная функция вызова окна графиков распределения по выходам.
        """
        TTPlot(table_dn)
    def TTPlot1(table_dn):
             """
             Окно построения категоризованных графиков.
             Параметры:
             table_dn - переменная БД.
            """
             def save_plot():
                 """
                 Функция сохранения графика с возможностью выбора имени и пути файла.
                 """
                 name=fd.asksaveasfilename(filetypes=(("PNG","*.png"),("all files","*.*")))
                 fmt=name+".png"
                 fig.savefig(fmt)
    """
    Верстка кнопок выбора графика
    """
    but1=Button(root,text="Аэропорты",font=("Arial", 15),bg=color_knop,fg=color_text,
                width=20,command=PP)
    but1.place(x=135,y=50)
    but4=Button(root,text="Терминалы",font=("Arial", 15),bg=color_knop,fg=color_text,
                width=20,command=EP("Терминалы", "количество вылетов", 'Терминал'))
    but4.place(x=135,y=120)
    but5=Button(root,text="Авиакомпании",font=("Arial", 15),bg=color_knop,fg=color_text,
                width=20,command=CP)
    but5.place(x=135,y=190)
    but6=Button(root,text="Самолеты",font=("Arial", 15),bg=color_knop,fg=color_text,
                width=20,command=ClP)
    but6.place(x=135,y=260)
    but12=Button(root,text="Выходы",font=("Arial", 15),bg=color_knop,fg=color_text,
                 width=20,command=TTP)
    but12.place(x=135,y=330)
    root.mainloop()
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import pandas as pd
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog as fd
from tkinter import colorchooser

import library.script as ms
import library.base as base
import library.reports as rp

from library.colors import color_main
from library.colors import color_dop
from library.colors import color_knop
from library.colors import color_text

import datetime
from tkinter import messagebox as mb

def window():
    """
    Функция отрисовки интерфейса главного меню
    """
    root2 = tk.Tk()
    root2.tk.call('wm', 'iconphoto', root2._w, tk.PhotoImage(file='/home/vasuyan/airport/pics/plane.png'))
    root2.geometry("600x400")
    x = 350
    y = 170
    root2.wm_geometry("+%d+%d" % (x, y))
    root2.title("Меню")
    root2.configure(bg=color_main)
    def click():
        """
        Функция выхода из главного меню
        """

        def click_close():
            """
            Функция закрытия окна
            """
            root.destroy()
            
        newtable = base.table_n1
        
        def Show_table_n1():
            """
            Функция открытия и отрисовки таблицы "Рейсы"
            """
            
            def IFadd_row():
                """
                Функция добавления новой строки
                """

                def foo_time(s):
                        """
                        Функция проверки временной строки
                        """                    
                        try:
                            s = str(datetime.time(int(s[:2]), int(s[3:5])))
                            print(s)
                            return True
                        except:
                            return False
                def data_format_time(event):
                        """
                        Функция преобразования временной строки
                        """
                        if len(entry_time.get()) is 2:
                            entry_time.insert(END,":")
                        elif len(entry_time.get()) is 6:
                            entry_time.delete(5, END)
                        if not foo_time(entry_time.get()) and (len(entry_time.get()) is 5):
                            mb.showerror('Ошибка', 'Неверный ввод данных\nПовторите ввод')
                            entry_time.delete(0, END)                  
                
                input = Toplevel(root)
                input.geometry("375x250")
                x = 400
                y = 150
                input.wm_geometry("+%d+%d" % (x, y))
                input.config(bg=color_main)

                def check(k):                    
                    return k.isdigit()

                def digit(c):
                    """
                    Функция преобразования строки в число
                    """
                    if (c.isdigit() == True):
                        return int(c)

                def get():
                    """
                    Функция получения новых значений
                    """                 
                    t=1
                    time = entry_time.get()
                    airline = entry_airline.get()
                    flight = entry_flight.get()
                    if (flight.isdigit() == False):
                        t=2
                    plane = entry_plane.get()
                    departure = entry_departure.get()
                    if (departure.isupper() == False):
                        t=2
                    destination = entry_destination.get()
                    if (destination.isupper() == False):
                        t=2
                    terminal = entry_terminal.get()
                    gate = entry_gate.get()
                    status = entry_status.get()

                    print(time, airline,flight,plane,departure,destination,terminal,gate,status)

                    if (t==2):
                        Err = Toplevel(input)
                        Err.geometry("365x60")
                        Err.config(bg=color_main)
                        x = 400
                        y = 200
                        Err.wm_geometry("+%d+%d" % (x, y))
                        lbl = tk.Label(Err, text="Ошибка. Проверьте правильность \nвведенных данных!", bg=color_knop,
                                       fg=color_text, bd=2,
                                       font=("Times", 18))
                        lbl.grid(column=1, row=1)
                    else:
                        k = ms.Add_row(time,airline, flight,plane,departure,destination,terminal,gate,status)
                        if (k == 0):
                            Err = Toplevel(input)
                            Err.geometry("300x200")
                            Err.config(bg=color_main)
                            x = 400
                            y = 200
                            Err.wm_geometry("+%d+%d" % (x, y))
                            lbl = tk.Label(Err, text="Рейс успешно добавлен. \nОбновить таблицу? ", bg=color_knop,
                                           fg=color_text, font=('Arial', 12), bd=1, width=35, height=2)
                            lbl.grid(column=1, row=1)

                            def deln():
                                Err.destroy()
                                input.destroy()
                                root.destroy()
                                Show_table_n1()

                            def deln2():
                                Err.destroy()
                                input.destroy()

                            btn = tk.Button(Err, text="Да", bg=color_knop, fg=color_text, bd=2,
                                font=("Arial", 14), height=1, width=10, command=deln)
                            btn2 = tk.Button(Err, text="Нет", bg=color_knop, fg=color_text, bd=2,
                                font=("Arial", 14), height=1, width=10, command=deln2)
                            btn.place(x=95, y=60)
                            btn2.place(x=95, y=120)
                            Err.mainloop()
                        else:
                            if (k == 1):
                                   Err = Toplevel(input)
                                   Err.geometry("180x120")
                                   Err.config(bg=color_main)
                                   x = 400
                                   y = 200
                                   Err.wm_geometry("+%d+%d" % (x, y))
                                   lbl = tk.Label(Err, text="Строка не изменена, \nсуществует дубликат.", bg=color_main,
                                                  fg=color_text, bd=2,
                                                  font=('Arial', 13))
                                   lbl.grid(column=1, row=1)
                                    
                                   def deln():
                                       """
                                       Функция закрытия окона с ошибкой
                                       """ 
                                       
                                       Err.destroy()

                                   btn = tk.Button(Err, text="Ок", bg=color_knop, fg=color_text, bd=2,
                                                   font=('Arial', 13), command=deln)
                                   btn.grid(column=1, row=2)
                                   Err.mainloop()

                lbl = tk.Label(input, text="Время", bg=color_knop, fg=color_text, bd=1, relief=tk.SUNKEN,
                               font=("Arial", 12), width=20)
                lbl.grid(column=0, row=0)

                lbl3 = tk.Label(input, text="Код авиакомпании", bg=color_knop, fg=color_text, bd=1, relief=tk.SUNKEN,
                                font=("Arial", 12), width=20)
                lbl3.grid(column=0, row=2)
                
                lbl2 = tk.Label(input, text="Рейс", bg=color_knop, fg=color_text, bd=1, relief=tk.SUNKEN,
                                font=("Arial", 12), width=20)
                lbl2.grid(column=0, row=1)

                lbl4 = tk.Label(input, text="Самолёт", bg=color_knop, fg=color_text, bd=1, relief=tk.SUNKEN,
                                font=("Arial", 12), width=20)
                lbl4.grid(column=0, row=3)

                lbl5 = tk.Label(input, text="Отправление", bg=color_knop, fg=color_text, bd=1, relief=tk.SUNKEN,
                                font=("Arial", 12), width=20)
                lbl5.grid(column=0, row=4)

                lbl6 = tk.Label(input, text="Назначение", bg=color_knop, fg=color_text, bd=1, relief=tk.SUNKEN,
                                font=("Arial", 12), width=20)
                lbl6.grid(column=0, row=5)

                lbl7 = tk.Label(input, text="Терминал", bg=color_knop, fg=color_text, bd=1, relief=tk.SUNKEN,
                                font=("Arial", 12), width=20)
                lbl7.grid(column=0, row=6)

                lbl8 = tk.Label(input, text="Выход", bg=color_knop, fg=color_text, bd=1, relief=tk.SUNKEN,
                                font=("Arial", 12), width=20)
                lbl8.grid(column=0, row=7)

                lbl9 = tk.Label(input, text="Статус", bg=color_knop, fg=color_text, bd=1, relief=tk.SUNKEN,
                                font=("Arial", 12), width=20)
                lbl9.grid(column=0, row=8)

                entry_time = tk.Entry(input, width=30)
                entry_time.bind('<KeyRelease>', data_format_time) # entry_time - поле ввода          
                entry_time.grid(column=1, row=0)
                
                entry_airline = tk.Entry(input,  width=30)
                entry_airline.grid(column=1, row=2)

                entry_flight = tk.Entry(input,  width=30)
                entry_flight.grid(column=1, row=1)

                entry_plane = tk.Entry(input, width=30)
                entry_plane.grid(column=1, row=3)

                entry_departure = tk.Entry(input, width=30)
                entry_departure.grid(column=1, row=4)
                
                entry_destination = tk.Entry(input,  width=30)
                entry_destination.grid(column=1, row=5)

                entry_terminal = ttk.Combobox(input, state="readonly",width=27, values=("A", "B","C","D","E","F"))
                entry_terminal.grid(column=1, row=6)

                entry_gate = ttk.Combobox(input, state="readonly" ,width=27, values=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
                entry_gate.grid(column=1, row=7)

                entry_status = ttk.Combobox(input,state="readonly",width=27, values=('ожидается', 'регистрация', 'посадка', 'задерживается',
                                                          'отменён', 'улетел'))
                entry_status.grid(column=1, row=8)

                butt = tk.Button(input, text="Добавить", bg=color_knop, fg=color_text, bd=2,
                     font=("Arial", 15), height=1, width=15, command=get)
                butt.place(x=100, y=205)


            def otch():
                """
                Функция открытия и отрисовки окна "Отчёты"
                """
                
                new = Toplevel(root)
                new.geometry("300x200")
                x = 500
                y = 30
                new.wm_geometry("+%d+%d" % (x, y))
                new.config(bg=color_main)

                def click():
                    """
                    Функция открытия и отрисовки окна отчётов
                    """
                    
                    rp.report1(base.table_n1,base.table_n3)

                def click_8():
                    """
                    Функция закрытия окна отчётов
                    """
                    new.destroy()

                lbl = tk.Label(new, text="Графические \n отчеты: ", bg=color_main, fg=color_text, bd=3,
                               font=("Arial", 15), height=2, width=18)
                lbl.place(x=50, y=20)

                btn = tk.Button(new, text="Отчет",  bg=color_knop, fg=color_text, bd=2,
                                font=("Arial", 14), height=1, width=10,
                                command=click)
                btn.place(x=90, y=100)

                btn8 = tk.Button(new, text="Назад", bg=color_knop, fg=color_text, bd=2,
                                 font=("Arial", 14), height=1, width=10,
                                 command=click_8)
                btn8.place(x=90, y=150)
                
            def otchTXT():
                """
                Функция открытия и отрисовки окна "Текстовые Отчёты"
                """
                
                new = Toplevel(root)
                new.geometry("300x300")
                x = 500
                y = 30
                new.wm_geometry("+%d+%d" % (x, y))
                new.config(bg=color_main)

                def click():
                    """
                    Функция открытия и отрисовки окна отчётов
                    """
                    
                    Err = Toplevel(new)
                    Err.geometry("505x325")
                    Err.config(bg=color_main)
                    x = 400
                    y = 200
                    Err.wm_geometry("+%d+%d" % (x, y))
                    
                    def click1():
                        """
                        Функция Экспорта статистики Авиакомпаний
                        """
                        df=base.table_n1[['Код авиакомпании']]
                        count = len(df)
                        df = df.groupby(['Код авиакомпании']).size().reset_index(name='count')
                        df['Частота']=(df['count']/count)*100
                        np.savetxt(r'output\AviaCorpTXT.txt', df, fmt='%s')
                        Err1 = Toplevel(Err)
                        Err1.geometry("505x100")
                        Err1.config(bg=color_main)
                        x = 400
                        y = 200
                        Err1.wm_geometry("+%d+%d" % (x, y))
                        lblh = tk.Label(Err1, text="Отчет скопирован в папку Output", 
                                   bg=color_main, fg=color_text, bd=2, font=('Arial', 15))
                        lblh.place(x=10, y=10)
                        
                    def click2():
                        """
                        Функция Экспорта статистики Самолетов
                        """
                        df=base.table_n1[['Самолёт']]
                        count = len(df)
                        df = df.groupby(['Самолёт']).size().reset_index(name='count')
                        df['Частота']=(df['count']/count)*100
                        np.savetxt(r'output\PlaneTXT.txt', df, fmt='%s')
                        Err1 = Toplevel(Err)
                        Err1.geometry("505x100")
                        Err1.config(bg=color_main)
                        x = 400
                        y = 200
                        Err1.wm_geometry("+%d+%d" % (x, y))
                        lblh = tk.Label(Err1, text="Отчет скопирован в папку Output", 
                                   bg=color_main, fg=color_text, bd=2, font=('Arial', 15))
                        lblh.place(x=10, y=10)
                        
                    def click3():
                        """
                        Функция Экспорта статистики Отправлений
                        """
                        df=base.table_n1[['Отправление']]
                        count = len(df)
                        df = df.groupby(['Отправление']).size().reset_index(name='count')
                        df['Частота']=(df['count']/count)*100
                        np.savetxt(r'output\DepartureTXT.txt', df, fmt='%s')
                        Err1 = Toplevel(Err)
                        Err1.geometry("505x100")
                        Err1.config(bg=color_main)
                        x = 400
                        y = 200
                        Err1.wm_geometry("+%d+%d" % (x, y))
                        lblh = tk.Label(Err1, text="Отчет скопирован в папку Output", 
                                   bg=color_main, fg=color_text, bd=2, font=('Arial', 15))
                        lblh.place(x=10, y=10)
                        
                    def click4():
                        """
                        Функция Экспорта статистики Назначений
                        """
                        df=base.table_n1[['Назначение']]
                        count = len(df)
                        df = df.groupby(['Назначение']).size().reset_index(name='count')
                        df['Частота']=(df['count']/count)*100
                        np.savetxt(r'output\DestinationTXT.txt', df, fmt='%s')
                        Err1 = Toplevel(Err)
                        Err1.geometry("505x100")
                        Err1.config(bg=color_main)
                        x = 400
                        y = 200
                        Err1.wm_geometry("+%d+%d" % (x, y))
                        lblh = tk.Label(Err1, text="Отчет скопирован в папку Output", 
                                   bg=color_main, fg=color_text, bd=2, font=('Arial', 15))
                        lblh.place(x=10, y=10)
                        
                    def click5():
                        """
                        Функция Экспорта статистики Терминалов
                        """
                        df=base.table_n1[['Терминал']]
                        count = len(df)
                        df = df.groupby(['Терминал']).size().reset_index(name='count')
                        df['Частота']=(df['count']/count)*100
                        np.savetxt(r'output\TerminalTXT.txt', df, fmt='%s')
                        Err1 = Toplevel(Err)
                        Err1.geometry("505x100")
                        Err1.config(bg=color_main)
                        x = 400
                        y = 200
                        Err1.wm_geometry("+%d+%d" % (x, y))
                        lblh = tk.Label(Err1, text="Отчет скопирован в папку Output", 
                                   bg=color_main, fg=color_text, bd=2, font=('Arial', 15))
                        lblh.place(x=10, y=10)
                
                    lblh = tk.Label(Err, text="Выберите параметры для вывода в текстовый файл", 
                                   bg=color_main, fg=color_text, bd=2, font=('Arial', 15))
                    lblh.place(x=10, y=10)
                    
                    btn1 = tk.Button(Err, text="Авиакомпании", bg=color_knop, fg=color_text, bd=3,
                                font=("Arial", 12), height=1, width=18,
                                command=click1)
                    btn1.place(x=160, y=60)
                
                    btn2 = tk.Button(Err, text="Самолеты", bg=color_knop, fg=color_text, bd=3,
                                font=("Arial", 12), height=1, width=18,
                                command=click2)
                    btn2.place(x=160, y=110)
                    
                    btn3 = tk.Button(Err, text="Города Отправления", bg=color_knop, fg=color_text, bd=3,
                                font=("Arial", 12), height=1, width=18,
                                command=click3)
                    btn3.place(x=160, y=160)

                    btn4 = tk.Button(Err, text="Города прибытия", bg=color_knop, fg=color_text, bd=3,
                                font=("Arial", 12), height=1, width=18,
                                command=click4)
                    btn4.place(x=160, y=210)

                    btn5 = tk.Button(Err, text="Терминалы", bg=color_knop, fg=color_text, bd=3,
                                font=("Arial", 12), height=1, width=18,
                                command=click5)
                    btn5.place(x=160, y=260)                    

                def click_8():
                    """
                    Функция закрытия окна отчётов
                    """
                    new.destroy()
                    
                def PivotTables():
                    """
                    Функция открытия окна сводных таблиц
                    """
                    
                    def export():
                        """
                        Функция экспорта св.таблицы в эксель
                        """
                        A1=Atr1.get()
                        A2=Atr2.get()
                        Ag=Agg.get()
                        df = base.table_n1.pivot_table(index=A1, columns=A2, aggfunc=Ag)
                        writer = pd.ExcelWriter(r'output\pivottable.xlsx', engine='xlsxwriter')
                        df.to_excel(writer, 'Sheet1')
                        writer.save()
                        
                    def clicks():
                        """
                        Функция закрытия окна св.таблиц
                        """
                        Err.destroy()
                        
                    Err = Toplevel(new)
                    Err.geometry("200x200")
                    Err.config(bg=color_main)
                    x = 400
                    y = 200
                    Err.wm_geometry("+%d+%d" % (x, y))
                    Atr1 = ttk.Combobox(Err, state="readonly",width=27, values=("Код авиакомпании","Время","Назначение","Отправление","Выход"
                                                                                , "Терминал"))
                    Atr1.grid(column=2, row=6)

                    Atr2 = ttk.Combobox(Err, state="readonly" ,width=27, values=("Код авиакомпании","Время","Назначение",
                                                                                 "Отправление","Выход", "Терминал"))
                    Atr2.grid(column=2, row=7)

                    Agg = ttk.Combobox(Err,state="readonly",width=27, values=('mean', 'sum', 'count', 'min',
                                                          'max'))
                    Agg.grid(column=2, row=8)
                    
                    btns = tk.Button(Err, text="Экспорт", bg=color_knop, fg=color_text, bd=3,
                                font=("Arial", 14), height=1, width=15,
                                command=export)
                    btns.grid(column=2, row=10)
                    btns2 = tk.Button(Err, text="Закрыть", bg=color_knop, fg=color_text, bd=3,
                                font=("Arial", 14), height=1, width=15,
                                command=clicks)
                    btns2.grid(column=2, row=12)
                        


                lbl = tk.Label(new, text="Текстовые \n отчеты: ", bg=color_main, fg=color_text, bd=3,
                               font=("Arial", 15), height=2, width=18)
                lbl.place(x=50, y=20)

                btn = tk.Button(new, text="Отчет", bg=color_knop, fg=color_text, bd=3,
                                font=("Arial", 14), height=1, width=15,
                                command=click)
                btn.place(x=60, y=100)
                
                btn2 = tk.Button(new, text="Сводная таблица", bg=color_knop, fg=color_text, bd=3,
                                font=("Arial", 14), height=1, width=15,
                                command=PivotTables)
                btn2.place(x=60, y=150)

                btn8 = tk.Button(new, text="Назад", bg=color_knop, fg=color_text, bd=3,
                                 font=("Arial", 14), height=1, width=15,
                                 command=click_8)
                btn8.place(x=60, y=200)                   

                
            def IFDel_row(index):
                """
                Функция удаления строки
                """
                Err = Toplevel(labelframe)
                Err.geometry("320x200")
                Err.config(bg=color_main)
                x = 400
                y = 200
                Err.wm_geometry("+%d+%d" % (x, y))
                btn2 = tk.Button(Err, text="Точно хотите удалить?", 
                                                 bg=color_knop,fg=color_text, font=('Arial', 12), bd=1, width=35, height=2)
                btn2.place(x=0, y=0)

                def deln():
                    """
                    Функция открытия окна с подтверждением обновления
                    """ 
                    Err = Toplevel(labelframe)
                    Err.geometry("320x200")
                    Err.config(bg=color_main)
                    x = 400
                    y = 200
                    Err.wm_geometry("+%d+%d" % (x, y))
                    btn2 = tk.Button(Err, text="Обновите таблицу", 
                                                 bg=color_knop,fg=color_text, font=('Arial', 12), bd=1, width=35, height=2)
                    btn2.place(x=0, y=0)
                    def update_btn():
                        """
                        Функция обновления окна таблицы
                        """
                
                        root.destroy()
                        Show_table_n1()

                    btn = tk.Button(Err, text="Обновить", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1, width=16, height=2, command=update_btn)
                    btn.place(x=80,y=125)
                    ms.Del_row(index)
                    
                def deln2():
                    """
                    Функция закрытия окна
                    """ 
                    Err.destroy()

                btn = tk.Button(Err, text="Да", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1, width=8, height=2, command=deln)
                btn2 = tk.Button(Err, text="Нет", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1, width=8, height=2, command=deln2)
                btn.place(x=40,y=125)
                btn2.place(x=190,y=125)
                Err.mainloop()
    
                

            def click_close():
                """
                Функция закрытия окна
                """ 
                
                root.destroy()

            def update_btn():
                """
                Функция обновления таблицы
                """ 
                
                root.destroy()
                Show_table_n1()
            
            def export_to_txt():
                """
                Функция вывода текстовых отчётов
                """ 
                Err = Toplevel(labelframe)
                Err.geometry("480x280")
                Err.config(bg=color_main)
                x = 400
                y = 200
                Err.wm_geometry("+%d+%d" % (x, y))
                
                lblh = tk.Label(Err, text="Выберите параметры для вывода в текстовый файл", 
                               bg=color_main, fg=color_text, bd=2, font=('Arial', 14))
                lblh.place(x=5, y=10)
      
                btn1 = tk.Button(Err, text="Рейс - время", bg=color_knop,fg=color_text, font=('Arial', 10), 
                                bd=1, width=25, height=1, command=rp.exp1)
                btn1.place(x=5, y=50)   
                
                btn14 = tk.Button(Err, text="Рейс - статус", bg=color_knop,fg=color_text, font=('Arial', 10), 
                                bd=1, width=25, height=1, command=rp.exp14)
                btn14.place(x=5, y=75)  
                
                btn2 = tk.Button(Err, text="Код авиакомпании - рейс", bg=color_knop,fg=color_text, font=('Arial', 10), 
                                bd=1, width=25, height=1, command=rp.exp2)
                btn2.place(x=5, y=100)   
                
                btn7 = tk.Button(Err, text="Код авиакомпании - самолёт", bg=color_knop,fg=color_text, font=('Arial', 10), 
                                bd=1, width=25, height=1, command=rp.exp7)
                btn7.place(x=5, y=125)
                
                btn3 = tk.Button(Err, text="Код авиакомпании - рейс - время", bg=color_knop,fg=color_text, font=('Arial', 10), 
                                bd=1, width=30, height=1, command=rp.exp3)
                btn3.place(x=5, y=150)
                   
                btn4 = tk.Button(Err, text="Код авиакомпании - рейс - самолёт", bg=color_knop,fg=color_text, font=('Arial', 10), 
                                bd=1, width=30, height=1, command=rp.exp4)
                btn4.place(x=5, y=175) 
                
                btn5 = tk.Button(Err, text="Рейс - отправление - назначение", bg=color_knop,fg=color_text, font=('Arial', 10), 
                                bd=1, width=30, height=1, command=rp.exp5)
                btn5.place(x=5, y=200)
                   
                btn8 = tk.Button(Err, text="Рейс - терминал - выход", bg=color_knop,fg=color_text, font=('Arial', 10), 
                                bd=1, width=30, height=1, command=rp.exp8)
                btn8.place(x=5, y=225)
                    
                btn6 = tk.Button(Err, text="Код - рейс - отправление - назначение", bg=color_knop,fg=color_text, font=('Arial', 10), 
                                bd=1, width=30, height=1, command=rp.exp6)
                btn6.place(x=5, y=250)
                    
                btn9 = tk.Button(Err, text="Рейс ", bg=color_knop,fg=color_text, font=('Arial', 10), 
                                bd=1, width=12, height=1, command=rp.exp9)
                btn9.place(x=369, y=50)
                    
                btn10 = tk.Button(Err, text="Код", bg=color_knop,fg=color_text, font=('Arial', 10), 
                                bd=1, width=12, height=1, command=rp.exp10)
                btn10.place(x=369, y=75)
                   
                btn11 = tk.Button(Err, text="Самолёт", bg=color_knop,fg=color_text, font=('Arial', 10), 
                                bd=1, width=12, height=1, command=rp.exp11)
                btn11.place(x=265, y=50)
                   
                btn12 = tk.Button(Err, text="Время", bg=color_knop,fg=color_text, font=('Arial', 10), 
                                bd=1, width=12, height=1, command=rp.exp12)
                btn12.place(x=265, y=75)
                
                btn13 = tk.Button(Err, text="Общая\nтаблица", bg=color_knop,fg=color_text, font=('Arial', 10), 
                                bd=1, width=25, height=2, command=rp.exp13)
                btn13.place(x=265, y=105)
            
                def export_close():
                    Err.destroy()
            
                close = tk.Button(Err, text="Назад", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                              width=15, height=2, command=export_close)
                close.place(x=325, y=225)
            
                lbl = tk.Label(Err, text="После нажатия на кнопку\nотчёт будет сформирован\nи сохранён в output", 
                               bg=color_main, fg=color_text, bd=2, font=('Arial', 13))
                lbl.place(x=265, y=150)
               
            def export_to_excel():
                """
                Функция вывода общей таблицы рейсов
                """ 
                rp.export_excel()
                
                Err = Toplevel(labelframe)
                Err.geometry("300x170")
                Err.config(bg=color_main)
                x = 400
                y = 200
                Err.wm_geometry("+%d+%d" % (x, y))
                btn2 = tk.Button(Err, text="Общая таблица рейсов \nбыла сохранена в папке output",
                                 bg=color_knop,fg=color_text, font=('Arial', 12), bd=1, width=35, height=2)
                btn2.place(x=0, y=10)
                
                def close_export_txt():
                    """
                    Функция закрытия окна
                    """ 
                    Err.destroy()
                
                close = tk.Button(Err, text="Назад", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                              width=15, height=2, command=close_export_txt)
                close.place(x=150, y=115)
                
            
            def IFMod_row(index):
                """
                Функция изменения строки
                """ 

                def check(k, kn):
                    """
                    Функция проверки измененных данных
                    """ 
                    
                    if (k == 'Рейс'):
                        if (kn.isdigit() == False):
                            return 0
                        else:
                            return 1
                    else:
                        if (k == "Отправление"):
                            if (kn.isupper() == True):
                                return 1
                            else:
                                return 0
                        else:
                            if (k == "Назначение"):
                              if (kn.isupper() == True):
                                 return 1
                              else:
                                 return 0
                            else:  return 1

                
                def take():
                    """
                    Функция изменений строки
                    """ 
                    def foo_time(s):
                        """
                        Функция проверки временной строки
                        """                    
                        try:
                            s = str(datetime.time(int(s[:2]), int(s[3:5])))
                            print(s)
                            return True
                        except:
                            return False
                    def data_format_time(event):
                        """
                        Функция преобразования временной строки
                        """
                        if len(cr.get()) is 2:
                            cr.insert(END,":")
                        elif len(cr.get()) is 6:
                                cr.delete(5, END)
                        if not foo_time(cr.get()) and (len(cr.get()) is 5):
                                mb.showerror('Ошибка', 'Неверный ввод данных\nПовторите ввод')
                                cr.delete(0, END)   
                    def polu():
                        """
                        Функция получения значений и изменения строки
                        """                                         
                        
                        kn = cr.get()
                        k = en.get()
                        s = check(k, kn)
                        if (s == 1):
                            sran = ms.Modification(index, k, kn)
                            print(sran)
                            if (sran == 0):
                                Err = Toplevel(mag)
                                Err.geometry("300x200")
                                Err.config(bg=color_main)
                                x = 400
                                y = 200
                                Err.wm_geometry("+%d+%d" % (x, y))
                                btn2 = tk.Button(Err, text="Строка успешно изменена!\nОбновить таблицу?", 
                                                 bg=color_knop,fg=color_text, font=('Arial', 12), bd=1, width=35, height=2)
                                btn2.place(x=0, y=0)

                                def deln():
                                    """
                                   Функция закрытия окон изменения и обновления таблицы
                                    """ 
                                    
                                    Err.destroy()
                                    mag.destroy()
                                    root.destroy()
                                    Show_table_n1()

                                def deln2():
                                    """
                                   Функция закрытия окон изменения без обновления
                                    """ 
                                    
                                    Err.destroy()
                                    mag.destroy()

                                btn = tk.Button(Err, text="Да", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1, width=8, height=2, command=deln)
                                btn2 = tk.Button(Err, text="Нет", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1, width=8, height=2, command=deln2)
                                btn.place(x=40,y=125)
                                btn2.place(x=190,y=125)
                                Err.mainloop()
                            else:
                                if (sran == 1):
                                    Err = Toplevel(mag)
                                    Err.geometry("180x120")
                                    Err.config(bg=color_main)
                                    x = 400
                                    y = 200
                                    Err.wm_geometry("+%d+%d" % (x, y))
                                    lbl = tk.Label(Err, text="Строка не изменена, \nсуществует дубликат.", bg=color_main,
                                                   fg=color_text, bd=2,
                                                   font=('Arial', 13))
                                    lbl.grid(column=1, row=1)

                                    def deln():
                                        """
                                        Функция закрытия окона с ошибкой
                                        """ 
                                        
                                        Err.destroy()

                                    btn = tk.Button(Err, text="Ок", bg=color_knop, fg=color_text, bd=2,
                                                    font=('Arial', 13), command=deln)
                                    btn.grid(column=1, row=2)
                                    Err.mainloop()
                        else:
                            Err = Toplevel(mag)
                            Err.geometry("290x60")
                            Err.config(bg="#D1B8F4")
                            x = 400
                            y = 200
                            Err.wm_geometry("+%d+%d" % (x, y))
                            lbl = tk.Label(Err, text="Вы ввели неверные данные! \nПовторите попытку.", bg=color_knop,
                                           fg=color_main, bd=2,
                                           font=("Times", 18, "italic"))
                            lbl.grid(column=1, row=1)

                    btn2 = tk.Button(mag, text="Изменить", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,width=15, height=2,
                                      command=polu)
                    btn2.place(x=50, y=175)

                    if (en.get() == "Терминал"):
                        cr = ttk.Combobox(mag,state="readonly", width=18,font=('Arial', 13), values=("A", "B","C","D","E","F"))
                        cr.place(x=29, y=144)
                        print(cr.get())
                    else:
                        if (en.get() == "Выход"):
                            cr = ttk.Combobox(mag,state="readonly",width=18,font=('Arial', 13),
                                              values=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"))
                            cr.place(x=29, y=144)
                        else:
                             if (en.get() == "Статус"):
                                 cr = ttk.Combobox(mag,state="readonly",width=18,font=('Arial', 13),
                                                   values=('ожидается', 'регистрация', 'посадка', 'задерживается',
                                                               'отменён', 'улетел'))
                                 cr.place(x=29, y=144)        
                             else:
                                 if (en.get()=="Время"):
                                   cr = tk.Entry(mag, bg=color_dop,font=('Arial', 13), width=20)
                                   cr.bind('<KeyRelease>', data_format_time) # entry_time - поле ввода        
                                   cr.place(x=30, y=145)
                                 else:
                                  cr = tk.Entry(mag, bg=color_dop,font=('Arial', 13), width=20)
                                  cr.place(x=30, y=145)

                mag = Toplevel(root)
                mag.geometry("250x250")
                x = 200
                y = 200
                mag.wm_geometry("+%d+%d" % (x, y))
                mag.config(bg=color_main)
                
                lb = tk.Label(mag, text="Параметр:", bg=color_knop, fg=color_text, font=('Arial', 13), bd=1,
                                  relief=tk.SUNKEN, width=20, height=1)
                lb.place(x=35, y=20)           
                           
                en = ttk.Combobox(mag,state="readonly", width=20,font=('Arial', 13), values=(
                    "Время", "Рейс", "Код авиакомпании", "Самолёт", "Отправление", "Назначение", "Терминал",
                    "Выход", "Статус"))
                en.place(x=25, y=55)

                btn3 = tk.Button(mag, text="Выбрать", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,width=15, height=2, command=take)
                btn3.place(x=50, y=85)

            root = tk.Tk()
            root.grid_rowconfigure(0, weight=1)
            root.columnconfigure(0, weight=1)
            root.title("Рейсы")
            w, h = root.winfo_screenwidth(), root.winfo_screenheight() - 38
            root.geometry("%dx%d+0+0" % (w, h))

            mainframe = tk.Frame(root)
            mainframe.grid(sticky='news')
            labelframe = tk.Frame(mainframe, bg=color_dop, width=w, height=125)
            baseframe = tk.Frame(mainframe, bg=color_dop, width=w - 10, height=h - 125) 
                                                  
                                 
            btn_update = tk.Button(labelframe, text="Обновить", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                            width=15, height=4, command=update_btn)
            btn_update.place(x=10, y=7)

            add_row_button = tk.Button(labelframe, text="Добавить", bg=color_knop,fg=color_text,  font=('Arial', 13), bd=1,
                                       width=15, height=4, command=IFadd_row)
            add_row_button.place(x=190, y=7)

            btn_export_to_excel = tk.Button(labelframe, text="Экспорт в .xlsx", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                              width=15, height=2, command=export_to_excel)
            btn_export_to_excel.place(x=370, y=2)  

            btn_export_to_txt = tk.Button(labelframe, text="Экспорт в .txt", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                              width=15, height=2, command=export_to_txt)
            btn_export_to_txt.place(x=370, y=52) 

            otch1 = tk.Button(labelframe, text="Графические отчёты", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                              width=20, height=2, command=otch)
            otch1.place(x=560, y=2)    

            otch2 = tk.Button(labelframe, text="Текстовые отчёты", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                              width=20, height=2, command=otchTXT)
            otch2.place(x=560, y=52)                     

            Close = tk.Button(labelframe, text="Назад", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                              width=15, height=4, command=click_close)
            Close.place(x=1100, y=5)
            
            def filter0():
                FilterMenu = Toplevel(labelframe)
                FilterMenu.geometry("505x325")
                FilterMenu.config(bg=color_main)
                x = 400
                y = 200
                FilterMenu.wm_geometry("+%d+%d" % (x, y))  
                
                lb = tk.Label(FilterMenu, text="Рейс (больше чем):", bg=color_knop, fg=color_text, font=('Arial', 13), bd=1,
                                  relief=tk.SUNKEN, width=50, height=1)
                lb.place(x=20, y=15)

                lb = tk.Label(FilterMenu, text="Рейс (меньше чем):", bg=color_knop, fg=color_text, font=('Arial', 13), bd=1,
                                  relief=tk.SUNKEN, width=50, height=1)
                lb.place(x=20, y=75)  
    
                lb = tk.Label(FilterMenu, text="Выход (больше чем):", bg=color_knop, fg=color_text, font=('Arial', 13), bd=1,
                                  relief=tk.SUNKEN, width=50, height=1)
                lb.place(x=20, y=135)                     
                
                lb = tk.Label(FilterMenu, text="Выход (меньше чем):", bg=color_knop, fg=color_text, font=('Arial', 13), bd=1,
                                  relief=tk.SUNKEN, width=50, height=1)
                lb.place(x=20, y=195)     
                
                cr1 = tk.Entry(FilterMenu, bg=color_dop,font=('Arial', 13), width=20)
                cr1.place(x=30, y=45) 
                
                cr2 = tk.Entry(FilterMenu, bg=color_dop,font=('Arial', 13), width=20)
                cr2.place(x=30, y=105) 
                
                cr3 = tk.Entry(FilterMenu, bg=color_dop,font=('Arial', 13), width=20)
                cr3.place(x=30, y=165) 
            
                cr4 = tk.Entry(FilterMenu, bg=color_dop,font=('Arial', 13), width=20)
                cr4.place(x=30, y=225) 
                
                def filter1():
                        base.table_n1 = newtable
                        k = int(cr1.get())
                        base.table_n1 = base.table_n1[base.table_n1["Рейс"] > k]
                        root.destroy()
                        Show_table_n1()
                        
                def filter2():
                        base.table_n1 = newtable
                        k = int(cr2.get())
                        base.table_n1 = base.table_n1[base.table_n1["Рейс"] < k]
                        root.destroy()
                        Show_table_n1()
                
                def filter3():
                        base.table_n1 = newtable
                        k = int(cr3.get())
                        base.table_n1 = base.table_n1[base.table_n1["Выход"] > k]
                        root.destroy()
                        Show_table_n1()
                
                def filter4():
                        base.table_n1 = newtable
                        k = int(cr4.get())
                        base.table_n1 = base.table_n1[base.table_n1["Выход"] < k]
                        root.destroy()
                        Show_table_n1()
                        
                def otmena():
                        base.table_n1 = newtable
                        root.destroy()
                        Show_table_n1()
                        
                btn_update0 = tk.Button(FilterMenu, text="Отменить фильтры", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                            width=20, height=1, command=otmena)
                btn_update0.place(x=20, y=280)
                
                btn_update1 = tk.Button(FilterMenu, text="Обновить", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                            width=15, height=1, command=filter1)
                btn_update1.place(x=250, y=40)
                
                btn_update2 = tk.Button(FilterMenu, text="Обновить", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                            width=15, height=1, command=filter2)
                btn_update2.place(x=250, y=100)
                
                btn_update3 = tk.Button(FilterMenu, text="Обновить", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                            width=15, height=1, command=filter3)
                btn_update3.place(x=250, y=160)
                
                btn_update4 = tk.Button(FilterMenu, text="Обновить", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                            width=15, height=1, command=filter4)
                btn_update4.place(x=250, y=220)
                
            def sort():
                SortMenu = Toplevel(labelframe)
                SortMenu.geometry("500x400")
                SortMenu.config(bg=color_main)
                x = 400
                y = 200
                SortMenu.wm_geometry("+%d+%d" % (x, y)) 
                
                def command_time():
                    base.table_n1=base.table_n1.sort_values(by='Время') 
                    
                def command_kod():
                    base.table_n1=base.table_n1.sort_values(by='Код авиакомпании')  
                    
                def command_flight():
                    base.table_n1=base.table_n1.sort_values(by='Рейс')   
                    
                def command_plane():
                    base.table_n1=base.table_n1.sort_values(by='Самолёт')
                    
                def command_otpr():
                    base.table_n1=base.table_n1.sort_values(by='Отправление') 
                    
                def command_nazn():
                    base.table_n1=base.table_n1.sort_values(by='Назначение')
                
                def command_terminal():
                    base.table_n1=base.table_n1.sort_values(by='Терминал')  
                    
                def command_gate():
                    base.table_n1=base.table_n1.sort_values(by='Выход')  
                
                def command_status():
                    base.table_n1=base.table_n1.sort_values(by='Статус')  
                    
                def update():
                    root.destroy()
                    Show_table_n1()
                    
                sort_time = tk.Button(SortMenu, text="По времени", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                            width=20, height=2, command=command_time)
                sort_time.place(x=50, y=5)
                
                sort_kod = tk.Button(SortMenu, text="По коду авиакомпании", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                            width=20, height=2, command=command_kod)
                sort_kod.place(x=260, y=5)
                
                sort_flight = tk.Button(SortMenu, text="По рейсу", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                            width=20, height=2, command=command_flight)
                sort_flight.place(x=50, y=65)

                sort_plane = tk.Button(SortMenu, text="По самолёту", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                            width=20, height=2, command=command_plane)
                sort_plane.place(x=260, y=65)
                
                sort_otpr = tk.Button(SortMenu, text="По отправлению", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                            width=20, height=2, command=command_otpr)
                sort_otpr.place(x=50, y=125)
                
                sort_nazn = tk.Button(SortMenu, text="По назначению", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                            width=20, height=2, command=command_nazn)
                sort_nazn.place(x=260, y=125)
                
                sort_terminal = tk.Button(SortMenu, text="По терминалу", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                            width=20, height=2, command=command_terminal)
                sort_terminal.place(x=50, y=185)
                
                sort_gate = tk.Button(SortMenu, text="По выходу", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                            width=20, height=2, command=command_gate)
                sort_gate.place(x=260, y=185)
                
                sort_status = tk.Button(SortMenu, text="По статусу", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                            width=20, height=2, command=command_status)
                sort_status.place(x=155, y=245)

                btn_update = tk.Button(SortMenu, text="Обновить", bg=color_knop,fg=color_text, font=('Arial', 15), bd=2,
                            width=20, height=2, command=update)
                btn_update.place(x=135, y=330)
                
                
            sortirovka = tk.Button(labelframe, text="Сортировать", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1, 
                            width=20, height=2, command=sort) 
            sortirovka.place(x=800, y=52)
            
            filtr = tk.Button(labelframe, text="Фильтр", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1, 
                            width=20, height=2, command=filter0) 
            filtr.place(x=800, y=2)
            
           
                
                
            labelframe.grid()
            baseframe.grid(sticky='nws')
            baseframe.grid_rowconfigure(0, weight=1)
            baseframe.grid_columnconfigure(0, weight=1)
            baseframe.grid_propagate(False)
            cv = tk.Canvas(baseframe, bg="black")
            cv.grid(row=0, column=0, sticky="news")
            scrollframe = tk.Frame(cv, bg=color_main)
            k = base.table_n1
            scrollbar = tk.Scrollbar(baseframe, orient="vertical", command=cv.yview)
            cv.configure(yscrollcommand=scrollbar.set)
            cv.create_window((0, 0), window=scrollframe, width=w - 10, anchor='nw')

            # заголовок в таблице Эксель
            xt = 2
            yt = 105
            for i in list(k):
                cellname = tk.Label(labelframe, text=i, bg=color_knop, fg=color_text, bd=1, relief=tk.SUNKEN, width=18)
                cellname.place(x=xt, y=yt)
                xt += 132

            # данные в таблице Эксель
            rw = 1
            cl = 0
            for i in k:
                for p in k[i]:
                    lb = tk.Label(scrollframe, text=p, bg=color_dop, fg=color_text, font=('Arial', 10), bd=1,
                                  relief=tk.SUNKEN, width=16)
                    lb.grid(row=rw, column=cl, pady=2, sticky="W" + "S")
                    rw += 1
                cl += 1
                rw = 1

            # кнопочки удалить справа у экрана
            xt = 1190
            yt = 0
            for i in range(base.table_n1.index.argmax() + 1):
                mod_button = tk.Button(scrollframe, text="✐", bg=color_dop, fg="black", font=('Arial', 8), bd=1,
                                       relief=tk.SUNKEN, command=lambda x=i: IFMod_row(x))
                mod_button.place(x=xt, y=yt)
                xt += 20
                del_button = tk.Button(scrollframe, text="✖", bg=color_dop, fg="black", font=('Arial', 8), bd=1,
                                       relief=tk.SUNKEN, command=lambda x=i: IFDel_row(x))
                del_button.place(x=xt, y=yt)
                yt += 24
                xt = 1190

            scrollframe.update_idletasks()
            scrollbar.grid(row=0, column=2, sticky="ns")
            cv.config(scrollregion=cv.bbox("all"))
            baseframe.config(width=w - 10, height=h - 160)
            root.mainloop()

        Show_table_n1()

    def click2():
        """
        Функция открытия таблицы с названиями аэропортов и их кодами
        """ 
        
        root3 = Toplevel(root2)
        root3.geometry("342x615")
        root3.config(bg=color_main)
        x = 450
        y = 10
        root3.wm_geometry("+%d+%d" % (x, y))

        def click_8():
            """
            Функция закрытия окна
            """ 
            
            root3.destroy()

        mainframe = tk.Frame(root3)
        mainframe.grid(sticky='news')
        w, h = 350, root3.winfo_screenheight() - 77
        labelframe = tk.Frame(mainframe, bg=color_dop, width=w, height=125)
        baseframe = tk.Frame(mainframe, bg=color_dop, width=w - 10, height=h - 125)
        labelframe.grid()
        baseframe.grid(sticky='nws')
        baseframe.grid_rowconfigure(0, weight=1)
        baseframe.grid_columnconfigure(0, weight=1)
        baseframe.grid_propagate(False)
        cv = tk.Canvas(baseframe, bg=color_main)
        cv.grid(row=0, column=0, sticky="news")
        scrollframe = tk.Frame(cv, bg=color_main)

        Close = tk.Button(labelframe, text="Назад", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                              width=15, height=2, command=click_8)
        Close.place(x=170, y=25)

        k = base.table_n2
        scrollbar = tk.Scrollbar(baseframe, orient="vertical", command=cv.yview)
        cv.configure(yscrollcommand=scrollbar.set)
        cv.create_window((0, 0), window=scrollframe, width=w - 10, anchor='nw')
        
        xt = 1
        yt = 103
        for i in list(k):
            cellname = tk.Label(labelframe, text=i, bg=color_knop, fg=color_text, bd=1, relief=tk.SUNKEN, width=25)
            cellname.place(x=xt, y=yt)
            xt += 136
        
        rw = 1
        cl = 0
        for i in k:
            for p in k[i]:
                lb = tk.Label(scrollframe, text=p, bg=color_dop, fg=color_text, font=('Arial', 10), bd=1,
                                  relief=tk.SUNKEN, width=19)
                lb.grid(row=rw, column=cl, pady=3, sticky="W" + "S")
                rw += 1
            cl += 1
            rw = 1

        xt = 1240
        yt = 4
        scrollframe.update_idletasks()
        scrollbar.grid(row=0, column=2, sticky="ns")
        cv.config(scrollregion=cv.bbox("all"))
        baseframe.config(width=w - 10, height=h - 160)
        root3.mainloop()

    def click3():
        """
        Функция открытия таблицы с вместимостью самолётов
        """ 
        
        root3 = Toplevel(root2)
        root3.geometry("442x610")
        root3.config(bg=color_main)
        x = 450
        y = 10
        root3.wm_geometry("+%d+%d" % (x, y))

        def click_8():
            """
            Функция закрытия окна
            """ 
            #report1
            root3.destroy()

        mainframe = tk.Frame(root3)
        mainframe.grid(sticky='news')
        w, h = 450, root3.winfo_screenheight() - 77
        labelframe = tk.Frame(mainframe, bg=color_dop, width=w, height=125)
        baseframe = tk.Frame(mainframe, bg=color_dop, width=w - 10, height=h - 125)
        labelframe.grid()
        baseframe.grid(sticky='nws')
        baseframe.grid_rowconfigure(0, weight=1)
        baseframe.grid_columnconfigure(0, weight=1)
        baseframe.grid_propagate(False)
        cv = tk.Canvas(baseframe, bg=color_main)
        cv.grid(row=0, column=0, sticky="news")
        scrollframe = tk.Frame(cv, bg=color_main)

        Close = tk.Button(labelframe, text="Назад", bg=color_knop,fg=color_text, font=('Arial', 13), bd=1,
                              width=15, height=2, command=click_8)
        Close.place(x=280, y=25)

        k = base.table_n3
        scrollbar = tk.Scrollbar(baseframe, orient="vertical", command=cv.yview)
        cv.configure(yscrollcommand=scrollbar.set)
        cv.create_window((0, 0), window=scrollframe, width=w - 10, anchor='nw')
        xt = 1
        yt = 103
        for i in list(k):
            cellname = tk.Label(labelframe, text=i, bg=color_knop, fg=color_text, bd=1, relief=tk.SUNKEN, width=21)
            cellname.place(x=xt, y=yt)
            xt += 136
        
        rw = 1
        cl = 0
        for i in k:
            for p in k[i]:
                lb = tk.Label(scrollframe, text=p, bg=color_dop, fg=color_text, font=('Arial', 10), bd=1,
                                  relief=tk.SUNKEN, width=17)
                lb.grid(row=rw, column=cl, pady=3, sticky="W" + "S")
                rw += 1
            cl += 1
            rw = 1

        xt = 1240
        yt = 4

        scrollframe.update_idletasks()
        scrollbar.grid(row=0, column=3, sticky="ns")
        cv.config(scrollregion=cv.bbox("all"))
        baseframe.config(width=w - 10, height=h - 160)
        root3.mainloop()

    def click6():
        """
        Функция открытия окна смены интерфейса
        """
       
        root3 = Toplevel(root2)
        root3.geometry("600x400")
        root3.config(bg=color_main)
        x = 450
        y = 10
        root3.wm_geometry("+%d+%d" % (x, y))
        
        with open('library/colors.py', 'r', encoding = 'utf-8') as f:
                array = f.readlines()
            
        def func1():
            """
            Функция смены цвета фона
            """
            color_main = colorchooser.askcolor()[1]
            if color_main == None:
                color_main = "#EEEEC2" 
            with open('library/colors.py', 'w', encoding = 'utf-8') as f:
                    array[0]= 'color_main = "' + color_main +'"\n'
                    f.writelines(array)
        def func2():
            """
            Функция смены дополнительного цвета
            """
            color_dop = colorchooser.askcolor()[1]
            if color_dop == None:
                color_dop = "#EEEEB2"             
            with open('library/colors.py', 'w', encoding = 'utf-8') as f:
                    array[1]= 'color_dop = "' + color_dop +'"\n'
                    f.writelines(array)
        def func3():
            """
            Функция смены цвета кнопок
            """
            color_knop = colorchooser.askcolor()[1]
            if color_knop == None:
                color_knop = "#A5A57C"             
            with open('library/colors.py', 'w', encoding = 'utf-8') as f:
                    array[2]= 'color_knop = "' + color_knop +'"\n'
                    f.writelines(array)
        def func4():
            """
            Функция смены цвета текста
            """
            color_text = colorchooser.askcolor()[1]
            if color_text == None:
                color_text = "#322363"             
            with open('library/colors.py', 'w', encoding = 'utf-8') as f:
                    array[3]= 'color_text = "' + color_text +'"\n'
                    f.writelines(array)

        lbls = tk.Label(root3, text="Изменение цветовой палитры",fg=color_text, bg=color_main,
                    bd=2, font=("Arial", 18), height=4, width=42)
        lbls.place(x=10, y=-20)    
        
        lbls = tk.Label(root3, text="Основной цвет:", fg=color_text, bg=color_main,
                    bd=2, font=("Arial", 15))
        lbls.place(x=15, y=70) 
        
        btn1 = tk.Button(root3, text="Изменить", bg=color_knop, fg=color_text, bd=2,
                     font=("Arial", 12), height=1, width=15,
                     command=func1)
        btn1.place(x=275, y=70)

        lbls = tk.Label(root3, text="Дополнительный цвет:", fg=color_text, bg=color_main,
                    bd=2, font=("Arial", 15))
        lbls.place(x=15, y=110) 
        
        btn2 = tk.Button(root3, text="Изменить", bg=color_knop, fg=color_text, bd=2,
                     font=("Arial", 12), height=1, width=15,
                     command=func2)
        btn2.place(x=275, y=110)

        lbls = tk.Label(root3, text="Цвет кнопок:", fg=color_text, bg=color_main,
                    bd=2, font=("Arial", 15))
        lbls.place(x=15, y=150) 
        
        btn3 = tk.Button(root3, text="Изменить", bg=color_knop, fg=color_text, bd=2,
                     font=("Arial", 12), height=1, width=15,
                     command=func3)
        btn3.place(x=275, y=150)
        
        lbls = tk.Label(root3, text="Цвет текста:", fg=color_text, bg=color_main,
                    bd=2, font=("Arial", 15))
        lbls.place(x=15, y=190) 
        
        btn4 = tk.Button(root3, text="Изменить", bg=color_knop, fg=color_text, bd=2,
                     font=("Arial", 12), height=1, width=15,
                     command=func4)
        btn4.place(x=275, y=190)
        
        
        def click_cl():
            """
            Функция закрытия окна
            """ 
            root3.destroy()
            
        btn0 = tk.Button(root3, text="Назад", bg=color_knop, fg=color_text, bd=2,
                     font=("Arial", 15), height=2, width=15,
                     command=click_cl)
        btn0.place(x=410, y=320)
        
        lbls = tk.Label(root3, text="Внимание! Для того, чтобы изменения вступили в силу корректно,", fg=color_text, bg=color_main,
                    bd=2, font=("Arial", 12))
        lbls.place(x=15, y=235)
        lbls = tk.Label(root3, text="пожалуйста, перезапустите программу.", fg=color_text, bg=color_main,
                    bd=2, font=("Arial", 12))
        lbls.place(x=15, y=255)
        
    def click5():
        """
        Функция закрытия окна
        """ 
        
        root2.destroy()
        
    
        
    lbls = tk.Label(root2, text="Электронное табло аэропорта",fg=color_text, bg=color_main,
                    bd=2, font=("Arial", 18), height=4, width=42)
    lbls.place(x=10, y=-20)    
        
    btn = tk.Button(root2, text="Рейсы", bg=color_knop, fg=color_text, bd=2,
                    font=("Arial", 15), height=2, width=52,
                    command=click)
    btn.place(x=10, y=80)

    btn2 = tk.Button(root2, text="Аэропорты", bg=color_knop, fg=color_text, bd=2,
                     font=("Arial", 15), height=2, width=24,
                     command=click2)
    btn2.place(x=10, y=150)

    btn3 = tk.Button(root2, text="Самолёты", bg=color_knop, fg=color_text, bd=2,
                     font=("Arial", 15), height=2, width=24,
                     command=click3)
    btn3.place(x=317, y=150)
    
    btn5 = tk.Button(root2, text="Выход", bg=color_knop, fg=color_text, bd=2,
                     font=("Arial", 15), height=2, width=15,
                     command=click5)
    btn5.place(x=410, y=320)
    
    btn6 = tk.Button(root2, text="Смена интерфейса", bg=color_knop, fg=color_text, bd=2,
                   font=("Arial", 15), height=2, width=20,
                   command=click6)
    btn6.place(x=10, y=320)
 

    root2.mainloop()
    

    return 0

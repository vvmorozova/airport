import os
import sys
import numpy as np
import pandas as pd

import library.base as base

def Del_row(index):
    
    revenue1 = int(base.table_n1.iloc[index]["Рейс"])
    base.table_n1 = base.table_n1.drop(index, axis = 'rows')
    base.table_n1 = base.table_n1.reset_index(drop = True) #Модифицированная таблица 1 с удалённой строкой.
    data = list(base.table_n1["Рейс"])



def Add_row(time, airline,flight,plane,departure,destination,terminal,gate,status):
    
    values = [time, airline,flight,plane,departure,destination,terminal,gate,status]
    index = base.table_n1.index.argmax() + 1
    base.table_n1.loc[index] = values
    if Dublicates(base.table_n1):
        Del_row(index - 1)
        return 1
    else:
        revenue1 = int(base.table_n1.iloc[index]["Рейс"])
        index = base.table_n2.index.argmax() + 1
        base.table_n2.loc[index] = [revenue1, revenue1 * 12]
        if Dublicates(base.table_n2):
            base.table_n2 = base.table_n2.drop_duplicates()
        return 0


def Denormalization():
    
    base.table_dn = pd.merge(base.table_n1, base.table_n2, left_on = "Отправление", right_on = "Код аэропорта")
    base.table_dn = pd.merge(base.table_dn, base.table_n2, left_on = "Назначение", right_on = "Код аэропорта")
    base.table_dn.rename(columns={'Название города_x': 'Город назначения'}, inplace=True)
    base.table_dn.rename(columns={'Название города_y': 'Город отправления'}, inplace=True)
    base.table_dn = pd.merge(base.table_dn, base.table_n3, on = "Самолёт")
    del base.table_dn['Код аэропорта_x']
    del base.table_dn['Код аэропорта_y']
    return base.table_dn

def Modification(index, column, value):
   
    buffer = base.table_n1.iloc[index][column]
    base.table_n1.at[index, column]= value
    if Dublicates(base.table_n1):
        base.table_n1.at[index, column] = buffer
        return 1
    else:
        base.table_n1.at[index, column] = value
        return 0

def Dublicates(data):
    
    data = data[data.duplicated()]
    if data.empty:
        return False
    else:
        return True

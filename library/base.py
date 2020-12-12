import os
import pandas as pd

excel_input = pd.ExcelFile("data/board.xlsx")

table_dn = pd.read_excel(excel_input, 'Лист1') #Ненормализированная таблица.
table_n1 = pd.read_excel(excel_input, 'Main') #Нормализированная таблица 1.
table_n2 = pd.read_excel(excel_input, 'Airport') #Нормализированная таблица 2.
table_n3 = pd.read_excel(excel_input, 'Plane') #Нормализированная таблица 3.

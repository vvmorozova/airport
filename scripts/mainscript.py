import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import pandas as pd
from tkinter import *
import os
import sys
from tkinter import messagebox

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import library.script as ms
import library.base
import library.interface as IF

IF.window()
# https://colorscheme.ru/#3Z11TaLrGw0w0 - цветовая тема
import openpyxl
from openpyxl import load_workbook
import sympy as sp
import os
import matplotlib.pyplot as plt
import numpy as np
if __name__ == '__main__':
    excelPath = os.path.abspath('../..') + '\\doc\\DataAnalysis.xlsx'
    workbook=load_workbook(excelPath)
    sheet=workbook.active
    cols2 = []
    cols1 = []
    for cell in list(sheet.columns)[0]:
        cols1.append(cell.value)
    for cell in list(sheet.columns)[1]:
        cols2.append(cell.value)
    n = 250
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s6 = 0
    s7 = 0
    for i in range(n):
        s1 = s1 + cols2[i]
        s2 = s2 + cols1[i]
        s3 = s3 + cols1[i] * cols1[i]
        s4 = s4 + cols1[i] * cols2[i]
        s5 = s5 + cols1[i] * cols1[i] * cols1[i]
        s6 = s6 + cols1[i] * cols1[i] * cols2[i]
        s7 = s7 + cols1[i] * cols1[i] * cols1[i] * cols1[i]
    b0 = sp.Symbol('b0')
    b1 = sp.Symbol('b1')
    b2 = sp.Symbol('b2')
    f1 = ((s1 - b1 * s2 - b2 * s3) / 250) - b0
    f2 = ((s4 - b0 * s2 - b2 * s5) / s3) - b1
    f3 = ((s6 - b0 * s3 - b1 * s5) / s7) - b2
    result = sp.solve([f1, f2, f3], [b0, b1, b2])

    # {b0: 5.54334244651814, b1: 0.458746450400443, b2: 0.960930395945233}

    # b0=sp.Symbol('b0')
    # b1=sp.Symbol('b1')
    # b2=sp.Symbol('b2')
    # sp.solve([((s1-b1*s2-b2*s3)/100)-b0,((s4-b0*s2-b2*s5)/s3)-b1,((s6-b0*s3-b1*s5)/s7)-b2],[b0,b1,b2])
    a = result[b0]
    b = result[b1]
    c = result[b2]
    plt.scatter(cols1, cols2, color='blue')
    x = np.linspace(0, 200, 250)
    y = a + b * x + c * x * x
    plt.title("y=-0.0005x^2+0.0047x+1.2711")
    plt.plot(x, y, color="red")
    plt.show()
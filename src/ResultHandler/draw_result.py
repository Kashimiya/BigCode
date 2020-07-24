import csv
import os
import numpy as np
from scipy.interpolate import spline
from matplotlib import pyplot as plt


def draw_result():
    path = os.path.abspath('..\\..') + '\\doc\\typed_by_time.csv'
    lines = list(csv.reader(open(path, 'r')))
    X = []
    Y = []
    for line in lines:
        X.append(int(line[0]))
        Y.append(float(line[1]))
    X = np.array(X)
    Y = np.array(Y)
    # 散点图
    plt.scatter(X, Y)
    plt.title("scatter plot for result")
    plt.savefig(os.path.abspath('..\\..') + '\\img\\scatter plot for result.png')
    plt.show()
    # 平滑曲线
    plt.figure()
    newX = np.linspace(X.min(), X.max(), 300)
    newY = spline(X, Y, newX)
    plt.plot(newX, newY)
    plt.title("smooth curve for result")
    plt.savefig(os.path.abspath('..\\..') + '\\img\\smooth curve for result.png')
    plt.show()


if __name__ == '__main__':
    draw_result()

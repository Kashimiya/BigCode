import csv
import os
import numpy as np
from sklearn.cluster import k_means
from sklearn.metrics import silhouette_score
from scipy.interpolate import spline
from matplotlib import pyplot as plt


# 为结果进行聚类
def choose_clusters(nums):
    data = []
    for num in nums:
        data.append([float(num), 0])
    scores = []
    for i in range(len(nums) - 2):
        model = k_means(data, n_clusters=i + 2)
        scores.append(silhouette_score(data, model[1]))
    max_score = max(scores)
    cluster = 0
    for i in range(len(scores)):
        if scores[i] == max_score:
            cluster = i + 2
            break
    return k_means(data, cluster)


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
    model = choose_clusters(Y)
    # 散点图
    # 用颜色区分结果
    plt.scatter(X, Y, c=model[1])
    plt.title("scatter plot for result")
    # plt.savefig(os.path.abspath('..\\..') + '\\img\\scatter plot for result.png')
    plt.show()
    # 平滑曲线
    plt.figure()
    newX = np.linspace(X.min(), X.max(), 300)
    newY = spline(X, Y, newX)
    plt.plot(newX, newY)
    plt.title("smooth curve for result")
    # plt.savefig(os.path.abspath('..\\..') + '\\img\\smooth curve for result.png')
    plt.show()


if __name__ == '__main__':
    draw_result()

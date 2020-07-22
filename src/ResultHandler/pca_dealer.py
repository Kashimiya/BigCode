import os
import sys
import numpy as np
import json


# 加载codeinfo.json文件为矩阵
def make_matrix():
    path = os.path.abspath('..\\..') + '\\doc\\codeiinfo.json'
    file = open(path, encoding='utf-8')
    code_info_all = json.load(file)

    mat = []
    for code_info in code_info_all:
        mat.append([code_info['CodeLine'], code_info['cyclomatic_complexity'], code_info['pylint_score'],
                    code_info['commit_times']])
    return np.array(mat, dtype='float64')


# 选择主成分
def index_lst(lst, component=0, rate=0):
    if component and rate:
        print('Component and rate must choose only one!')
        sys.exit(0)
    if not component and not rate:
        print('Invalid parameter for numbers of components!')
        sys.exit(0)
    elif component:
        # 根据需要的主成分的数量来选择主成分
        return component
    else:
        # 根据信息利用率选择主成分
        for i in range(1, len(lst)):
            if sum(lst[:i]) / sum(lst) >= rate:
                return i
        return 0


def pca():
    code_info_matrix = make_matrix()
    p, n = np.shape(code_info_matrix)
    # 每一列的平均数
    t = np.mean(code_info_matrix, 0)
    # 标准化矩阵
    for i in range(p):
        for j in range(n):
            code_info_matrix[i, j] = float(code_info_matrix[i, j] - t[j])
    # 计算协方差矩阵(相关系数矩阵)
    cov_mat = np.dot(code_info_matrix.T, code_info_matrix) / (p - 1)
    # 协方差矩阵的特征值（矩阵）和特征向量（矩阵）
    U, V = np.linalg.eigh(cov_mat)
    # 重新排列特征值（矩阵）和特征向量（矩阵）
    U = U[::-1]
    for i in range(n):
        V[i, :] = V[i, :][::-1]
    # 要降成一维
    index = index_lst(U, component=1)
    if index:
        # 取特征向量矩阵的子矩阵
        v = V[:, :index]
        res = np.dot(code_info_matrix, v)
    else:
        # 由于选择了过大的rate（信息利用率）而导致无法得到合适的主成分
        print('Invalid rate choice.\nPlease adjust the rate.')
        print('Rate distribute follows:')
        print([sum(U[:i]) / sum(U) for i in range(1, len(U) + 1)])
        sys.exit(0)

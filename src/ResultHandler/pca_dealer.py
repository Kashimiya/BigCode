import os
import sys
import numpy as np
import json


class PcaDealer:
    __code_order = []

    # 加载codeinfo.json文件为矩阵
    def __make_matrix(self):
        path = os.path.abspath('..\\..') + '\\doc\\codeinfo.json'
        file = open(path, encoding='utf-8')
        code_info_all = json.load(file)['1']
        file.close()
        mat = []
        for code_info in code_info_all:
            mat.append([code_info['code_line'], code_info['cyclomatic_complexity']])
            self.__code_order.append(code_info['time_category'])
        return np.array(mat, dtype='float64')

    # 选择主成分
    def __index_lst(self, lst, component=0, rate=0):
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

    # @param: component 需要的主成分的数量，默认为1
    # @param: rate 信息利用率，默认无
    # @param: student_id 学生编号
    # 返回降维之后的矩阵
    def pca(self, component=1, rate=0):
        code_info_matrix = self.__make_matrix()
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
        index = self.__index_lst(U, component=component, rate=rate)
        if index:
            # 取特征向量矩阵的子矩阵
            v = V[:, :index]
            return np.dot(code_info_matrix, v)
        else:
            # 由于选择了过大的rate（信息利用率）而导致无法得到合适的主成分
            print('Invalid rate choice.\nPlease adjust the rate.')
            print('Rate distribute follows:')
            print([sum(U[:i]) / sum(U) for i in range(1, len(U) + 1)])
            sys.exit(0)

    def get_code_order(self):
        return self.__code_order


# 输出pca后的结果
# 直接运行该程序即可输出pca后的结果到csv文件
if __name__ == '__main__':
    pca_dealer = PcaDealer()
    matrix = pca_dealer.pca()
    order = pca_dealer.get_code_order()
    Path = os.path.abspath('..\\..') + '\\doc\\after_pca.csv'
    doc = open(Path, 'a')
    for i in range(len(order)):
        print(str(order[i]) + ',' + str(matrix[i][0]), file=doc)
    doc.close()

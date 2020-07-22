import os
import sys
import numpy as np
import json
from matplotlib import pyplot as plt


class PcaDealer:
    __code_order = []

    # 加载codeinfo.json文件为矩阵
    # @param: student_id 学生编号
    def __make_matrix(self, student_id):
        path = os.path.abspath('..\\..') + '\\doc\\codeinfo.json'
        file = open(path, encoding='utf-8')
        code_info_all = json.load(file)
        file.close()
        mat = []
        for code_info in code_info_all:
            if code_info['student_id'] == student_id:
                mat.append([code_info['CodeLine'], code_info['cyclomatic_complexity'],
                            code_info['commit_times']])
                self.__code_order.append(code_info['case_id'])
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

    # @param: component 需要的主成分的数量，默认为2
    # @param: rate 信息利用率，默认无
    # @param: student_id 学生编号
    def pca(self, student_id, component=2, rate=0):
        code_info_matrix = self.__make_matrix(student_id)
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

    # 根据得到的降维后的二维矩阵绘制散点图
    # 其中：蓝色代表平滑时期的代码，黄色代表赶作业时期的代码
    def draw_pca_matrix(self, student_id):
        matrix = self.pca(student_id, component=2, rate=0)
        smoothX, smoothY, hardX, hardY = [], [], [], []
        path = os.path.abspath('..\\..') + '\\doc\\ChoosenQuestions.json'
        file = open(path, encoding='utf-8')
        student_info = json.load(file)[student_id]
        file.close()
        for i in range(len(self.__code_order)):
            if self.__code_order[i] in student_info['smoothset']:
                smoothX.append(matrix[i, 0])
                smoothY.append(matrix[i, 1])
            else:
                hardX.append(matrix[i, 0])
                hardY.append(matrix[i, 1])
        plt.scatter(smoothX, smoothY, c='b')
        plt.scatter(hardX, hardY, c='y')
        plt.title("Code Info After PCA for : " + student_id)
        plt.show()


if __name__ == '__main__':
    pca_dealer = PcaDealer()
    Path = os.path.abspath('..\\..') + '\\doc\\ChoosenQuestions.json'
    File = open(Path, encoding='utf-8')
    student_infos = json.load(File)
    File.close()
    for studentId in student_infos:
        pca_dealer.draw_pca_matrix(studentId)

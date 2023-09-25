import numpy as np
import math
from data import train_data

class Discriminator:
    def __init__(self, dataset, prepossibility) -> None:
        # dataset is a n rows m cols matrix
        # n rows represent the amount of data points
        # m cols represent the number of features per data point
        dataset = np.matrix(dataset)

        # print(np.matrix(dataset))

        self.dataset = dataset
        self.prepossibility = prepossibility

        self.mu = np.mean(self.dataset, axis = 0)

        # 此处计算的是样本协方差矩阵，因此除以的数为 N
        self.sigma = ((self.dataset - self.mu).T @ (self.dataset - self.mu)) / len(self.dataset)

        # np.cov计算的是在无偏估计下的协方差举证 除以的数为 N-1 而不是 N
        # self.sigma = np.cov(self.dataset, rowvar = False) * (len(self.dataset) - 1) / len(self.dataset)


    def show_dataset(self):
        print(self.dataset)

    def show_mu(self):
        print(self.mu)

    def show_sigma(self):
        print(self.sigma)

    def g(self, x):
        d = len(self.dataset)
        return -1 / 2 * (x - self.mu) * self.sigma.I * (x - self.mu).T - d / 2 * np.log(2 * np.pi) - 1 / 2 * np.log(np.linalg.det(self.sigma)) + np.log(self.prepossibility)

    def mahalanobis_distance(self, x):
        r = np.sqrt((x - self.mu) * self.sigma.I * (x - self.mu).T)
        if np.size(r) != 1:
            exit("马氏距离肯定算错了!!!!")

        return np.linalg.det(r)

if __name__ == '__main__':
    tmp = Discriminator(train_data[0, :, :], 1 / 2)

    tmp.show_dataset()
    tmp.show_mu()
    tmp.show_sigma()

    # print(tmp.g(x[0, 0, :]))

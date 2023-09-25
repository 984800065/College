import numpy as np
from Discriminator import Discriminator
from data import train_data, test_data
from typing import List

class Classifier:
    def __init__(self, categories_amount, characteristic_amount, train_data, possibility_set) -> None:
        self.categories: List[Discriminator] = []
        self.categories_amount = categories_amount
        self.characteristic_amount = characteristic_amount
        self.train_data = train_data
        self.possibility_set = possibility_set

        for i in range(categories_amount):
            # for ndarray self.train_data
            # first dimension represents categorie
            # second dimension represents size of the training data set
            # third dimension represents characteristic_amount
            self.categories.append(Discriminator(self.train_data[i, :, : characteristic_amount], self.possibility_set[i]))
        
    def classify(self, data_set, true_categories, show_cls_ans: int = 0):
        total_amount = len(data_set)
        true_amount = 0
        real_categories = []

        for i, data in enumerate(data_set):
            tc = true_categories[i]
            max_idx = self.get_max_g_idx(data)

            real_categories.append(max_idx)

            if max_idx == tc:
                true_amount += 1

        exp_training_error = (total_amount - true_amount) / total_amount * 100

        if show_cls_ans == 1:
            print(np.vstack([real_categories, true_categories]))
        elif show_cls_ans == 2:
            print(np.array(real_categories))

        return exp_training_error
    
    def get_max_g_idx(self, data):
        g = []

        for j in self.categories:
                g.append(j.g(data))

        return np.argmax(g)
    
    def get_characteristic_amount(self):
        return self.characteristic_amount
    
    def get_mahalanobis_distance_matrix(self, test_data):
        md_matrix = []
        for i, data in enumerate(test_data):
            md_matrix.append([])
            
            for j in self.categories:
                md_matrix[i].append(j.mahalanobis_distance(data))

        md_matrix = np.array(md_matrix)

        return md_matrix
    
if __name__ == '__main__':
    
    # print(np.concatenate(train_data, axis = 0))

    data = np.concatenate(train_data, axis = 0)
    true_categories = np.arange(30)
    true_categories = (true_categories / 10).astype(int)
    print(true_categories)

    possibility_set_1 = [1 / 2, 1 / 2, 0]

    classifier_1_1 = Classifier(3, 1, train_data, possibility_set_1)
    exp_training_error_1_1 = classifier_1_1.classify(data[:, : classifier_1_1.get_characteristic_amount()], true_categories)
    print(exp_training_error_1_1)

    classifier_1_2 = Classifier(3, 2, train_data, possibility_set_1)
    exp_training_error_1_2 = classifier_1_2.classify(data[:, : classifier_1_2.get_characteristic_amount()], true_categories)
    print(exp_training_error_1_2)

    classifier_1_3 = Classifier(3, 3, train_data, possibility_set_1)
    exp_training_error_1_3 = classifier_1_3.classify(data[:, : classifier_1_3.get_characteristic_amount()], true_categories)
    print(exp_training_error_1_3)

    
    possibility_set_2_1 = [1 / 3, 1 / 3, 1 / 3]
    classifier_2_1 = Classifier(3, 3, train_data, possibility_set_2_1)
    md_matrix = classifier_2_1.get_mahalanobis_distance_matrix(test_data)
    print(md_matrix)

    exp_training_error_2_1 = classifier_2_1.classify(test_data[:, : classifier_2_1.get_characteristic_amount()], np.zeros(len(test_data)))
    print(exp_training_error_2_1)

    possibility_set_2_2 = [0.8, 0.1, 0.1]
    classifier_2_2 = Classifier(3, 3, train_data, possibility_set_2_2)
    exp_training_error_2_2 = classifier_2_2.classify(test_data[:, : classifier_2_2.get_characteristic_amount()], np.zeros(len(test_data)))
    print(exp_training_error_2_2)
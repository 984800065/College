import numpy as np
from Classifier import Classifier
from data import train_data, test_data
from typing import List

if __name__ == '__main__':
    
    # print(np.concatenate(train_data, axis = 0))

    data = np.concatenate(train_data, axis = 0)
    true_categories = np.arange(30)
    true_categories = (true_categories / 10).astype(int)
    # print(true_categories)
    
    possibility_set_2_1 = [1 / 3, 1 / 3, 1 / 3]
    classifier_2_1 = Classifier(3, 3, train_data, possibility_set_2_1)
    md_matrix = classifier_2_1.get_mahalanobis_distance_matrix(test_data)
    print(md_matrix)

    # print('\n\n\n')

    exp_training_error_2_1 = classifier_2_1.classify(test_data[:, : classifier_2_1.get_characteristic_amount()], np.zeros(len(test_data)), show_cls_ans = 2)

    possibility_set_2_2 = [0.8, 0.1, 0.1]
    classifier_2_2 = Classifier(3, 3, train_data, possibility_set_2_2)
    exp_training_error_2_2 = classifier_2_2.classify(test_data[:, : classifier_2_2.get_characteristic_amount()], np.zeros(len(test_data)), show_cls_ans = 2)
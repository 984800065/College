import numpy as np
from Classifier import Classifier
from data import train_data, test_data
from typing import List

if __name__ == '__main__':

    data = np.concatenate(train_data, axis = 0)
    true_categories = np.arange(30)
    true_categories = (true_categories / 10).astype(int)
    # print(true_categories)

    possibility_set_1 = [1 / 2, 1 / 2, 0]

    classifier_1_1 = Classifier(3, 1, train_data, possibility_set_1)
    exp_training_error_1_1 = classifier_1_1.classify(data[:, : classifier_1_1.get_characteristic_amount()], true_categories, show_cls_ans = 1)
    print(exp_training_error_1_1)

    classifier_1_2 = Classifier(3, 2, train_data, possibility_set_1)
    exp_training_error_1_2 = classifier_1_2.classify(data[:, : classifier_1_2.get_characteristic_amount()], true_categories, show_cls_ans = 1)
    print(exp_training_error_1_2)

    classifier_1_3 = Classifier(3, 3, train_data, possibility_set_1)
    exp_training_error_1_3 = classifier_1_3.classify(data[:, : classifier_1_3.get_characteristic_amount()], true_categories, show_cls_ans = 1)
    print(exp_training_error_1_3)
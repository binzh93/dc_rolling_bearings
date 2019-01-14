# -*- coding: utf-8 -*-
import pandas as pd
import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
import os


def train_csv_to_mat(train_csv_file, mat_save_path):
    if not os.path.exists(mat_save_path):
        os.makedirs(mat_save_path)
    train = pd.read_csv(train_csv_file, index_col=0, header=0)
    train.sort_values("label", inplace=True)
    label = train["label"].tolist()
    train.drop("label", axis=1,inplace=True)
    train_data = train.as_matrix()

    num = 0
    mat_list = []
    for it, val in enumerate(label):
        if val == num:
           mat_list.append(train_data[it])
           if it == len(label)-1:
               sio.savemat(os.path.join(mat_save_path, str(num)), {"data_"+str(num): np.array(mat_list)})
        else:
            sio.savemat(os.path.join(mat_save_path, str(num)), {"data_"+str(num): np.array(mat_list)})
            mat_list.clear()
            num += 1
            mat_list.append(train_data[it])

def test_csv_to_mat(test_csv_file, mat_save_path):
    if not os.path.exists(mat_save_path):
        os.makedirs(mat_save_path)
    train = pd.read_csv(test_csv_file, index_col=0, header=0)
    train_data = train.as_matrix()
    sio.savemat(os.path.join(mat_save_path, "test.mat"), {"data_test": train_data})
    

if __name__ == "__main__":
    train_csv_file = "/Users/zhubin/Desktop/dc_competition/train.csv"
    test_csv_file = "/Users/zhubin/Desktop/dc_competition/test_data.csv"

    train_mat_save_path = "/Users/zhubin/Desktop/dc_competition/train_file/"
    test_mat_save_path = "/Users/zhubin/Desktop/dc_competition/test_file/"
    train_csv_to_mat(train_csv_file, train_mat_save_path)
    # test_csv_to_mat(test_csv_file, test_mat_save_path)

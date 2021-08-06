import torch
import numpy as np
# import pandas as pd
# import torch.optim as optim
# import torch.nn.functional as F

def load_training_data(path = "training_label.txt"):
    # 把 training 時需要的 data 讀進來
    # 如果是 'training_label.txt'，需要讀取 label，如果是 'training_nolabel.txt'，不需要讀取 label
    if 'training_label' in path:
        with open(path, 'r', encoding= 'utf-8') as f:
            lines = f.readlines()
            lines = [line.strip('\n').split(' ') for line in lines]
        x = [line[2:] for line in lines]
        y = [line[0] for line in lines]
        return x, y
    else:
        with open(path, 'r', encoding= 'utf-8') as f:
            lines = f.readlines()
            x = [line.strip('\n').split(' ') for line in lines]
        return x


def load_testing_data(path = 'testing_data'):
    # 把 testing 時需要的 data 讀進來
    with open(path, 'r', encoding= 'utf-8') as f:
        lines = f.readlines()
        X = ["".join(line.strip('\n').split(",")[1:]).strip() for line in lines[1:]]
        X = [sen.split(' ') for sen in X]
    return X


def evaluation(outputs, labels):
    '''
    outputs: probability (float)
    labels: labels
    '''
    outputs[outputs>=0.5] = 1 # 大於等於 0.5 為正面
    outputs[outputs<0.5] = 0 # 小於 0.5 為負面
    correct = torch.sum(torch.eq(outputs, labels)).item()
    return correct


TRAIN_DATA_PATH = r"E:\Download\dataset\TextSentimentClassification\training_label.txt"
TRAIN_NOLABEL_DATA_PATH = r"E:\Download\dataset\TextSentimentClassification\training_nolabel.txt"
TEST_DATA_PATH = r"E:\Download\dataset\TextSentimentClassification\testing_data.txt"


if __name__ == '__main__':
    
    # with open(TRAIN_DATA_PATH, 'r', encoding= 'utf-8') as file:
    #     lines = file.readlines()
    #     func = lambda x: x.strip("\n").split(" ")
    #     lines = list(map(func, lines))
    #     x = [line[2:] for line in lines]
    #     y = [line[0] for line in lines]
        
    #     print(lines[0:100])
    #     print(x[0:100])
    #     print(y[0:100])

    
    # with open(TEST_DATA_PATH, 'r', encoding= 'utf-8') as file:
    #     lines = file.readlines()
    #     func = lambda x: ''.join(x.strip("\n").split(",")[1:]).strip()
    #     lines = list(map(func, lines))[1:]
    #     lines = list(map(lambda x: x.split(' '), lines))
    #     print(lines[0:100])


    random_number = np.random.randint(10000)
    print('Randomly choose a data, index: ', random_number)
    print(load_training_data(TRAIN_DATA_PATH)[0][random_number], load_training_data(TRAIN_DATA_PATH)[1][random_number])
    print(load_testing_data(TEST_DATA_PATH)[random_number])
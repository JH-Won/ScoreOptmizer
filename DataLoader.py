import numpy as np
import pandas as pd
import math
import os

path = './data/'

def list_all_files():
    ret = []
    files = os.listdir(path)
    for file in files:
        if file.endswith('.csv'):
            ret.append(file)
    return ret

def convert_str(number):
    try:
        return float(number)
    except ValueError:
        return math.nan

def preprocess_file(file):
    assert type(file) is str and file.endswith('.csv'), "invalid file."
    df = pd.read_csv(file, dtype = str)
    
    header = list(df.values[1:, 0])
    mat = df.values[:,1:]

    length = mat.shape[0]
    score_mat = []
    for i in length:
        row = []
        for j in length:
            row.append(convert_str(mat[i ,j]))
        score_mat.append(row)
    score_mat = np.asfarray(score_mat)
    return header, score_mat
import numpy as np
import pandas as pd
import math
import os


def list_all_files(path = './data/'):
    ret = []
    files = os.listdir(path)
    for file in files:
        if file.endswith('.csv'):
            ret.append(os.path.join(path,file))
    return ret

def convert_str(number):
    try:
        return float(number)
    except ValueError:
        return math.nan

def preprocess_file(file, not_include = None):
    assert type(file) is str and file.endswith('.csv'), "invalid file."
    df = pd.read_csv(file, dtype = str)
    
    mat = df.values[0:,1:]

    length = mat.shape[0]
    header = []
    score_mat = []
    for i in range(length):
        if not_include != None and i in not_include:
            continue
        header.append(df.values[i, 0])
        col = []
        for j in range(length):
            if not_include != None and j in not_include:
                continue
            col.append(convert_str(mat[j ,i]))
        score_mat.append(col)
    score_mat = np.asfarray(score_mat).T

    return header, score_mat
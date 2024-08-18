import numpy as np
import copy
import math
import pandas as pd
from pandas import plotting 
import matplotlib.pyplot as plt
import sklearn
from sklearn.decomposition import PCA 
import json
import matplotlib.ticker as ticker

from utils import commindline

def get_PCA_data_by_face_ratio():
    [input_path, output_path] = commindline.get_args()
    _face_ratio_dict = json.load(open(input_path, 'r'))
    face_ratio_dict = copy.deepcopy(_face_ratio_dict)

    for key, value in _face_ratio_dict.items():
        face_ratio_dict[key]['face_height'] = math.ceil(value['face_height']/value['face_width']*100)/100
        face_ratio_dict[key]['face_width'] = math.ceil(value['face_width']/value['face_height']*100)/100

    face_ratio_data_for_pandas = {}

    print('create face_ratio_data_for_pandas for pandas')
    for k in list(face_ratio_dict.values())[0]:
        face_ratio_data_for_pandas[k] =[]

    for k,v in face_ratio_dict.items():
        for _k, _v in v.items():
            face_ratio_data_for_pandas[_k].append(_v)

    for k, _list in face_ratio_data_for_pandas.items():
        print(k, len(_list))

    _face_ratio_df = pd.DataFrame(face_ratio_data_for_pandas)
    # face_width, face_height, eye_count, eye_height, eye_width, eye_to_eye, eye_to_side, eye_to_jaw, eye_to_forehead
    face_ratio_df = _face_ratio_df[['eye_height', 'eye_width', 'eye_to_jaw', 'eye_to_forehead', 'eye_to_side']]
    print(face_ratio_df)

    # 行列の標準化
    dfs = face_ratio_df.iloc[:, 1:].apply(lambda x: (x-x.mean())/x.std(), axis=0)

    pca = PCA()
    pca.fit(dfs)
    feature = pca.transform(dfs)

    # 第一、第二主成分で散布図作成
    plt.clf()
    plt.figure(figsize=(10, 10))
    plt.scatter(feature[:, 0], feature[:, 1], alpha=0.8, c=list(face_ratio_df.iloc[:, 0]))
    plt.grid()
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.savefig(output_path+'/scatter_plot.png')

    # 寄与率出力
    contribution_rate = pd.DataFrame(pca.explained_variance_ratio_, index=["PC{}".format(x + 1) for x in range(len(dfs.columns))])
    with open(output_path+'/contribution_rate.json', 'w', encoding="utf-8") as f:
        print('save contribution_rate')
        json.dump(contribution_rate.to_dict(), f, ensure_ascii=False)
    print(contribution_rate)

    plt.clf()
    plt.gca().get_xaxis().set_major_locator(ticker.MaxNLocator(integer=True))
    plt.plot([0] + list( np.cumsum(pca.explained_variance_ratio_)), "-o")
    plt.xlabel("Number of principal components")
    plt.ylabel("Cumulative contribution rate")
    plt.grid()
    plt.savefig(output_path+'/contribution_rate.png')

    # 観測変数の寄与度
    plt.clf()
    plt.figure(figsize=(6, 6))
    for x, y, name in zip(pca.components_[0], pca.components_[1], face_ratio_df.columns[1:]):
        plt.text(x, y, name)
    plt.scatter(pca.components_[0], pca.components_[1], alpha=0.8)
    plt.grid()
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.savefig(output_path+'/contribution_of_observed_variables.png')

get_PCA_data_by_face_ratio()
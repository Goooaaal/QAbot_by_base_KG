import os
import numpy as np
import pandas
from nltk.corpus import treebank
import matplotlib.pyplot as plt

t = treebank.parsed_sents('wsj_0001.mrg')[0]
mu, sigma = 2, 0.5
v = np.random.normal(mu, sigma, 10000)
plt.hist(v, bins=50, density=1)
(n, bins) = np.histogram(v, bins=50, density=True)
plt.plot(0.5 * (bins[1:] + bins[:-1]), n)
def input_file(file_path):
    QA_sequence = dict()
    # dict2 = dict()
    with open(file_path, 'r', encoding='utf-8', newline='') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(' ')
            key = ''.join(line[0])
            value = ''.join(line[1:])
            # dict2 = {key: value}
            QA_sequence[key] = value
            # print(QA_sequence)
    return QA_sequence

# sequence = input_file('crawler.csv')




#encoding=utf-8

import numpy as np
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet

net = buildNetwork(2, 3, 1)


a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
data = []
data_1 = []
for i in range(100):
    with open("./data./raw_text./novel/{0}.txt".format(i), "r", encoding="windows-1251") as f:
        raw = f.read()
    with open("./data./encrypted_text./visiner./novel/{0}.txt".format(i), "r") as f1:
        raw1 = f1.read()
    text = []
    text1 = []
    j = 0
    while len(text) != 33:
        if raw[j].lower() in a:
            text.append((ord(raw[j]) - 1072) / 33)
            text1.append((ord(raw1[j]) - 1072) / 33)
        j += 1
    data_1.append(text1)
    data.append(text)

X = np.array(data)

# выходные данные
y = np.array(data_1)

DS = SupervisedDataSet( 100, 100 )

DS.appendLinked( data, data_1 )
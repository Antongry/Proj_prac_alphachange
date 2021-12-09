#encoding=utf-8

import numpy as np


# Сигмоида
def nonlin(x, deriv=False):
    if deriv == True:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


# набор входных данных
a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
data = []
data_1 = []
for i in range(100):
    with open("./data./raw_text./novel/{0}.txt".format(i), "r") as f:
        raw = f.read()
    with open("./data./encrypted_text./visiner./novel/{0}.txt".format(i), "r") as f1:
        enc = f1.read()
    text = []
    text1 = []
    j = 0
    while len(text) != 33:
        if raw[j].lower() in a:
            text.append((ord(raw[j]) - 1072) / 33)
            text1.append((ord(enc[j]) - 1072) / 33)
        j += 1
    data_1.append(text1)
    data.append(text)

X = np.array(data)

# выходные данные
y = np.array(data_1)

# сделаем случайные числа более определёнными
np.random.seed(1)

# инициализируем веса случайным образом со средним 0
syn0 = 2 * np.random.random((33, 33)) - 1

for iter in range(10000):
    # прямое распространение
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))

    # насколько мы ошиблись?
    l1_error = y - l1

    # перемножим это с наклоном сигмоиды
    # на основе значений в l1
    l1_delta = l1_error * nonlin(l1, True)  # !!!

    # обновим веса
    syn0 += np.dot(l0.T, l1_delta)  # !!!


print("Выходные данные после тренировки:")
#print(l1)
ans = []
for i in range(50):
    text = []
    for j in range(len(l1[i])):
        #text.append((l1[i][j] * 33 + 1072).round())
        data_1[i][j] = chr(int(data_1[i][j] * 33 + 1072))
        text.append(chr(int((l1[i][j] * 33 + 1072).round())))
    ans.append(text)

print(ans)
print('-----------------------------------------------')
print(data_1)

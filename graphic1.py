import matplotlib.pyplot as plt

a = ''
b = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
ch_raw = [0] * 33
ch_enc = [0] * 33

for i in sorted(b):
    a += i


for i in range(0, 40): #diapazon textov
    with open("./encrypted_text/{0}.txt".format(i), "r") as f:
        text = f.read()
    with open("./raw_text/{0}.txt".format(i), "r") as f1:
        text1 = f1.read()

    for j in range(len(a)):
        chance_raw = text1.count(a[j])/len(text1)
        chance_enc = text.count(a[j])/len(text)
        ch_raw[j] += chance_raw
        ch_enc[j] += chance_enc

fig, ax = plt.subplots()

a*=3
print(len(a))
for i in range(33):
    x = a[i]
    y = ch_enc[i] / 40   # encrypt or raw
 #   ax.bar(x, y)
  #  x = a[i * 2 + 1]
  #  y = ch_raw[i // 2] / 40

    ax.bar(x, y)

    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(11)  # ширина Figure
    fig.set_figheight(6)  # высота Figure

plt.show()

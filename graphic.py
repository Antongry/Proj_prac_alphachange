import matplotlib.pyplot as plt

def mkgraph(raw, enc, n, fname, e=1):
    a = ''
    b = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
    ch_raw = [0] * 33
    ch_enc = [0] * 33

    for i in sorted(b):
        a += i

    for i in range(n): #diapazon textov
        with open("./data./encrypted_text" + enc + "/{0}.txt".format(i), "r") as f:
            text = f.read()
        with open("./data./raw_text" + raw + "/{0}.txt".format(i), "r") as f1:
            text1 = f1.read()

        for j in range(len(a)):
            chance_raw = text1.count(a[j])/len(text1)
            chance_enc = text.count(a[j])/len(text)
            ch_raw[j] += chance_raw
            ch_enc[j] += chance_enc

    fig, ax = plt.subplots()

    for i in range(33):
        x = a[i]
        if e:
            y = ch_enc[i] / n   # encrypt or raw
        else:
            y = ch_raw[i] / n

        ax.bar(x, y)

        ax.set_facecolor('seashell')
        fig.set_facecolor('floralwhite')
        fig.set_figwidth(11)  # ширина Figure
        fig.set_figheight(6)  # высота Figure

    plt.savefig("./data./statistics./graphic./" + fname)
    #print(fname)


mkgraph("./novel", "./visiner./novel", 100, "novel_visiner.png")
mkgraph("./poem", "./visiner./poem", 100, "poem_visiner.png")
mkgraph("./random", "./visiner./random", 50, "random_visiner.png")
mkgraph("./novel", "./tritemius./novel", 100, "novel_tritemius.png")
mkgraph("./poem", "./tritemius./poem", 100, "poem_tritemius.png")
mkgraph("./random", "./tritemius./random", 50, "random_tritemius.png")

mkgraph("./novel", "./visiner./novel", 100, "novel.png", 0)
mkgraph("./poem", "./visiner./poem", 100, "poem.png", 0)
mkgraph("./random", "./visiner./random", 50, "random.png", 0)
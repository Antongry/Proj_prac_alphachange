import matplotlib.pyplot as plt

def mkgraph(raw, enc, n, fname):
    a = ''
    b = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
    ch_raw = [0] * 33
    ch_enc = [0] * 33

    for i in sorted(b):
        a += i


    for i in range(n): #diapazon textov
        with open("./data./encrypted_text" + enc + "/{0}.txt".format(i), "r") as f:
            text = f.read()
        with open("./data./raw_text" + raw + "/{0}.txt".format(i), "r") as f:
            text1 = f.read()

        for j in range(len(a)):
            chance_raw = text1.count(a[j])/len(text1)
            chance_enc = text.count(a[j])/len(text)
            ch_raw[j] += chance_raw
            ch_enc[j] += chance_enc

    fig, ax = plt.subplots()

    a *= 2
    #print(len(a))
    for i in range(33 * 2):
        if i % 2:
            x = a[i // 2].upper()
            y = ch_enc[i // 2] / 40   # encrypt or raw
            ax.bar(x, y, color='lightsteelblue')
        else:
            x = a[i // 2]
            y = ch_raw[i // 2] / 40
            ax.bar(x, y, color='burlywood')

        ax.set_facecolor('seashell')
        fig.set_facecolor('floralwhite')
        fig.set_figwidth(11)  # ширина Figure
        fig.set_figheight(6)  # высота Figure

    plt.savefig("./data./statistics./graphic./cmp_stats/" + fname)
    #plt.show()

mkgraph("./novel", "./visiner./novel", 100, "novel_visiner.png")
mkgraph("./poem", "./visiner./poem", 100, "poem_visiner.png")
mkgraph("./random", "./visiner./random", 50, "random_visiner.png")

mkgraph("./novel", "./tritemius./novel", 100, "novel_tritemius.png")
mkgraph("./poem", "./tritemius./poem", 100, "poem_tritemius.png")
mkgraph("./random", "./tritemius./random", 50, "random_tritemius.png")

mkgraph("./novel", "./visiner1./novel", 100, "novel_visiner1.png")
mkgraph("./poem", "./visiner1./poem", 100, "poem_visiner1.png")
mkgraph("./random", "./visiner1./random", 50, "random_visiner1.png")
import matplotlib.pyplot as plt

def mkgraph(e, adress, n, fname):
    a = ''
    b = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
    ch = [0] * 33

    for i in sorted(b):
        a += i

    for i in range(n): #diapazon textov
        if e:
            with open("./data./encrypted_text" + adress + "/{0}.txt".format(i), "r") as f:
                text = f.read()
        else:
            with open("./data./raw_text" + adress + "/{0}.txt".format(i), "r") as f:
                text = f.read()

        for j in range(len(a)):
            chance = text.count(a[j])/len(text)
            ch[j] += chance

    fig, ax = plt.subplots()

    for i in range(33):
        x = a[i]
        y = ch[i] / n

        ax.bar(x, y)

        ax.set_facecolor('seashell')
        fig.set_facecolor('floralwhite')
        fig.set_figwidth(11)  # ширина Figure
        fig.set_figheight(6)  # высота Figure

    plt.savefig("./data./statistics./graphic./" + fname)
    #print(fname)


mkgraph(1, "./visiner./novel", 100, "novel_visiner.png")
mkgraph(1, "./visiner./poem", 100, "poem_visiner.png")
mkgraph(1, "./visiner./random", 50, "random_visiner.png")

mkgraph(1, "./tritemius./novel", 100, "novel_tritemius.png")
mkgraph(1, "./tritemius./poem", 100, "poem_tritemius.png")
mkgraph(1, "./tritemius./random", 50, "random_tritemius.png")

mkgraph(0, "./novel", 100, "novel.png")
mkgraph(0, "./poem", 100, "poem.png")
mkgraph(0, "./random", 50, "random.png")

mkgraph(1, "./visiner1./novel", 100, "novel_visiner1.png")
mkgraph(1, "./visiner1./poem", 100, "poem_visiner1.png")
mkgraph(1, "./visiner1./random", 50, "random_visiner1.png")
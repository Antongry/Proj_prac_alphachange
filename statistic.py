# 0 - 39: jane_eyre
# 40 - 86: onegin
# 87 - 99 random
def mkstat(raw, enc, n):
    a = ''
    b = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
    ch_raw = [0] * 33
    ch_enc = [0] * 33

    for i in sorted(b):
        a += i

    for i in range(n):
        with open("./data./encrypted_text" + enc + "/{0}.txt".format(i), "r") as f:
            text = f.read()
        with open("./data./raw_text" + raw + "/{0}.txt".format(i), "r") as f:
            text1 = f.read()

        data = 'буква       raw    |   enc\n'

        for j in range(len(a)):
            chance_raw = text1.count(a[j])/len(text1)
            chance_enc = text.count(a[j])/len(text)
            ch_raw[j] += chance_raw
            ch_enc[j] += chance_enc

            data += '  {0}:       '.format(a[j])
            data += '{0}  |  {1}\n'.format("%.4f" % (chance_raw), "%.4f" % (chance_enc))

        with open("./data./statistics./text./" + enc + "/{0}.txt".format(i), "w") as f2:
            f2.write(data)


mkstat("./novel", "./visiner./novel", 200)
mkstat("./poem", "./visiner./poem", 100)
mkstat("./random", "./visiner./random", 50)

mkstat("./novel", "./tritemius./novel", 200)
mkstat("./poem", "./tritemius./poem", 100)
mkstat("./random", "./tritemius./random", 50)

mkstat("./novel", "./visiner1./novel", 200)
mkstat("./poem", "./visiner1./poem", 100)
mkstat("./random", "./visiner1./random", 50)
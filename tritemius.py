def tritemius(s, alphabet):
    data = []
    for i in range(len(a)):
        data.append([])
        for k in (a[i::] + a[0:i]):
            data[i].append(k)

    ans = ''
    counter = 0
    for j in range(len(s)):
        if s[j] in a:
            ans += data[counter % len(a)][a.find(s[j])]
            counter += 1
        else:
            ans += s[j]
    return ans

a = 'ёйцукенгшщзхъфывапролджэячсмитьбю'

#novel
for i in range(100):
    with open("./data./raw_text./novel/{0}.txt".format(i), "r") as in_:
        text = in_.read()

    with open("./data./encrypted_text./tritemius./novel/{0}.txt".format(i), "w") as out_:
        out_.write(tritemius(text, a))

#poem
for i in range(100):
    with open("./data./raw_text./poem/{0}.txt".format(i), "r") as in_:
        text = in_.read()

    with open("./data./encrypted_text./tritemius./poem/{0}.txt".format(i), "w") as out_:
        out_.write(tritemius(text, a))

#random
for i in range(50):
    with open("./data./raw_text./random/{0}.txt".format(i), "r") as in_:
        text = in_.read()

    with open("./data./encrypted_text./tritemius./random/{0}.txt".format(i), "w") as out_:
        out_.write(tritemius(text, a))

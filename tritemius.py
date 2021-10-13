a = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
data = []
for i in range(len(a)):
    data.append([])
    for k in (a[i::] + a[0:i]):
        data[i].append(k)

for i in range(100):
    with open("./data./raw_text./novel/{0}.txt".format(i), "r") as in_:
        text = in_.read()
    ans = ''
    counter = 0
    for j in range(len(text)):
        if text[j] in a:
            ans += data[counter % len(a)][a.find(text[j])]
            counter += 1
        else:
            ans += text[j]

    with open("./data./encrypted_text./tritemius./novel/{0}.txt".format(i), "w") as out_:
        out_.write(ans)

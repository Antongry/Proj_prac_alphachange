a = ''
b = 'ёйцукенгшщзхъфывапролджэячсмитьбю'

for i in sorted(b):
    a += i

for i in range(100):
    with open("./encrypted_text/{0}.txt".format(i), "r") as f:
        text = f.read()
    with open("./raw_text/{0}.txt".format(i), "r") as f1:
        text1 = f1.read()

    data = 'буква     enc | raw\n'
    for j in range(len(a)):
        data += '  {0}:       '.format(a[j])
        data += '{0}  |  {1}\n'.format(text.count(a[j]), text1.count(a[j]))
    with open("./statistics/{0}.txt", "w") as f2:
        f2.write(data)

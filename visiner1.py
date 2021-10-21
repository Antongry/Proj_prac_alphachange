#a = 'ёйцукенгшщзхъфывапролджэячсмитьбю'

def visiner1(text ,key, a):
    data = []
    for i in range(len(a)):
        data.append([])
        for k in (a[i::] + a[0:i]):
            data[i].append(k)

    ans = ''
    counter = 0
    for j in range(len(text)):
        if text[j] in a:
            ans += data[a.find(key[counter % len(key)])][a.find(text[j])]
            counter += 1
        else:
            ans += text[j]
    return ans

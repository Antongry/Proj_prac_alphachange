a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
data = []
for i in range(len(a)):
    data.append([])
    for k in (a[i::] + a[0:i]):
        data[i].append(k)

key = 'можноиспользовать'
for i in range(1):
    with open("./raw_text/{0}.txt".format(i), "r") as in_:
        text = in_.read()
    text = text.lower()
    ans = ''
    counter = 0
    for j in range(len(text)):
        if text[j] in a:
            ans += data[a.find(key[counter % len(key)])][a.find(text[j])]
            counter += 1
        else:
            ans += text[j]
    with open("./encrypted_text/{0}.txt".format(i), "w") as out_:
        out_.write(ans)

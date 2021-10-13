# coding= utf-8


def find_pos(symbol, alphabet):
    for i in range(len(alphabet)):
        if alphabet[i] == symbol:
            return i
    return -1


def visiner(s, key, side, alphabet):
    ans = ''

    # make table

    table = [alphabet]
    for i in range(len(alphabet) - 1):
        alphabet = alphabet[1::] + alphabet[0]
        table.append(alphabet)
    alphabet = alphabet[1::] + alphabet[0]

    # convert key
    k = []
    for i in range(len(key)):
        a = find_pos(key[i], alphabet)
        if a != -1:
            k.append(a)

    # crypt
    last_line = 0
    line = last_line
    j = 0  # current sdvig

    for i in range(len(s)):
        a = find_pos(s[i], table[last_line])
        if a != -1:
            # find line
            line = last_line + side * k[j]

            if line >= len(alphabet):
                line -= len(alphabet)
            if line < 0:
                line += len(alphabet)

            if j >= len(k):
                j -= len(k)
            if j < 0:
                j += len(k)

                # samo koldynstvo

            ans += table[line][a]
            last_line = line
        else:
            ans += s[i]
    return ans


al = ''
for i in range(ord('а'), ord('я')+1):
    al += chr(i)
    #print(al)

#novel
for i in range(100):
    with open("./data./raw_text./novel/{0}.txt".format(i), "r") as in_:
        text = in_.read()

    with open("./data./encrypted_text./visiner./novel/{0}.txt".format(i), "w") as out_:
        out_.write(visiner(text, "некий ключ", 1, al))

#poem
for i in range(100):
    with open("./data./raw_text./poem/{0}.txt".format(i), "r") as in_:
        text = in_.read()

    with open("./data./encrypted_text./visiner./poem/{0}.txt".format(i), "w") as out_:
        out_.write(visiner(text, "некий ключ", 1, al))

#random
for i in range(50):
    with open("./data./raw_text./random/{0}.txt".format(i), "r") as in_:
        text = in_.read()

    with open("./data./encrypted_text./visiner./random/{0}.txt".format(i), "w") as out_:
        out_.write(visiner(text, "некий ключ", 1, al))

#encoding=utf-8

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
        a = alphabet.find(key[i])
        if a != -1:
            k.append(a)
    #print(k)
    # crypt
    line = 0
    j = 0  # current sdvig

    for i in range(len(s)):
        a = table[last_line].find(s[i])       
        if a != -1:
            # find line
            line += side * k[j]
            j+=1

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
        else:
            ans += s[i]
    return ans

#print(visiner("pupa i lupa polucali", "chupa", 1, "abcdefghijklmnopqrstuvwxyz"))

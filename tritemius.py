def tritemius(s, alphabet):
    data = []
    for i in range(len(alphabet)):
        data.append([])
        for k in (alphabet[i::] + alphabet[0:i]):
            data[i].append(k)

    ans = ''
    counter = 0
    for j in range(len(s)):
        if s[j] in alphabet:
            ans += data[counter % len(alphabet)][alphabet.find(s[j])]
            counter += 1
        else:
            ans += s[j]
    return ans



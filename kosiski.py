
l=[]

nods=[0] * 500

nl = 0

def nod(a, b):
    for i in range(a,1,-1):
        if (a % i == 0) and (b % i == 0):
            return i
    return 1

n = 0

with open("./data./encrypted_text" + "./visiner./novel" + "/{0}.txt".format(0), "r") as f:
    s = f.read()



for i in range(int(len(s)/4)-2):
    str1 = s[i: i+2]

    for j in range(i+1, int(len(s)/4)-2):
        str2 = s[j:  j+2]

        if str1 != str2:
            l.append(j - i)
            nl += 1
    #print(i, nl)


for i in range(nl):
    for j in range(i+1, nl):
        nods[nod(l[i], l[j])] += 1
    print(i, nl)

keylen = 0
for i in range (2, 500):
    if (nods[keylen] < nods[i]):
        keylen = i

print(keylen)


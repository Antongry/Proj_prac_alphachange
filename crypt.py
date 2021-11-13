#encoding=utf-8
from tritemius import tritemius
from visiner import visiner
from visiner1 import visiner1

al = ''
for i in range(ord('а'), ord('я')+1):
    al += chr(i)
    #print(al)


#tritemius

#novel
for i in range(100):
    with open("./data./raw_text./novel/{0}.txt".format(i), "r") as in_:
        text = in_.read()

    with open("./data./encrypted_text./tritemius./novel/{0}.txt".format(i), "w") as out_:
        out_.write(tritemius(text, al))

#poem
for i in range(100):
    with open("./data./raw_text./poem/{0}.txt".format(i), "r") as in_:
        text = in_.read()

    with open("./data./encrypted_text./tritemius./poem/{0}.txt".format(i), "w") as out_:
        out_.write(tritemius(text, al))

#random
for i in range(50):
    with open("./data./raw_text./random/{0}.txt".format(i), "r") as in_:
        text = in_.read()

    with open("./data./encrypted_text./tritemius./random/{0}.txt".format(i), "w") as out_:
        out_.write(tritemius(text, al))




#visiner

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



#visiner1

#novel
for i in range(100):
    with open("./data./raw_text./novel/{0}.txt".format(i), "r") as in_:
        text = in_.read()

    with open("./data./encrypted_text./visiner1./novel/{0}.txt".format(i), "w") as out_:
        out_.write(visiner1(text, "некийключ", al))

#poem
for i in range(100):
    with open("./data./raw_text./poem/{0}.txt".format(i), "r") as in_:
        text = in_.read()

    with open("./data./encrypted_text./visiner1./poem/{0}.txt".format(i), "w") as out_:
        out_.write(visiner1(text, "некийключ", al))

#random
for i in range(50):
    with open("./data./raw_text./random/{0}.txt".format(i), "r") as in_:
        text = in_.read()

    with open("./data./encrypted_text./visiner1./random/{0}.txt".format(i), "w") as out_:
        out_.write(visiner1(text, "некийключ", al))
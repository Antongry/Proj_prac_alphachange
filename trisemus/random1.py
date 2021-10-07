import random


def generate_random_string(length):
    letters = "ёйцукенгшщзхъфывапролджэячсмитьбю"
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

with open("rand.txt", "w") as f:
    f.write(generate_random_string(2844))

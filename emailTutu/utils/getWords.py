import random

with open("lover_words.txt", "r") as f:
    lines = f.readlines()


def get_words():
    return random.choice(lines)

if __name__ == '__main__':
    print(get_words())
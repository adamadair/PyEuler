import os
from math import log10


class P099:
    def run_me(self):
        largest = [0, 0]
        for i, line in enumerate(open(os.path.join(os.path.dirname(__file__), '..\data\p099_base_exp.txt'))):
            a, x = list(map(int, line.split(',')))
            if x * log10(a) > largest[0]:
                largest = [x * log10(a), i + 1]
        print(largest[1])
        return largest[1]

if __name__ == '__main__':
    P099().run_me()
"""
Project Euler problem 001 solution.

Prints the sum of all the multiples of 3 or 5 below 1000
"""


class P001:
    def run_me(self):
        print((self.sum_divisible_by(999, 3) + self.sum_divisible_by(999, 5)) - self.sum_divisible_by(999, 15))

    @staticmethod
    def sum_divisible_by(target: int, number: int) -> int:
        p = target // number
        return number * ((p * (p + 1)) // 2)


if __name__ == '__main__':
    P001().run_me()

class P371:
    def run_me(self):
        t, e0, e1 = 1000, 0, 0

        for i in range((t // 4), -1, -1):
            e1 = (t + ((t - 2.) - 2 * i) * e1) / (t - i - 1)
            e0 = (t + ((t - 2.) - 2 * i) * e0 + e1) / (t - i - 1)
        ans = "%.8f" % e0
        print(ans)
        return ans


if __name__ == '__main__':
    P371().run_me()

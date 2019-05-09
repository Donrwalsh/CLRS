def run_time_01(n):
    return 100 * n ** 2


def run_time_02(n):
    return 2 ** n


n = 2
while True:
    if run_time_01(n) < run_time_02(n):
        print("Lowest value of n is " + str(n))
        break
    else:
        n += 1
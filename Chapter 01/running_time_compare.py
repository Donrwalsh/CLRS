import math


def generate_time_array():
    second = 1000000
    minute = 60 * second
    hour = 60 * minute
    day = 24 * hour
    month = 30 * day
    year = 365 * day
    century = 100 * year
    return [second, minute, hour, day, month, year, century]


def sqrt_n(time):
    return time ** 2


def n(time):
    return time


def n_lg_n(time):
    time_taken, n = 0, 0
    initial_n = 1
    # overshoot the first n
    while time_taken <= time:
        initial_n *= 10
        time_taken = (initial_n * math.log(initial_n, 2))
    # now double back iteratively and determine the specific location
    n = 0
    for x in range(len(str(initial_n))):
        o = initial_n // 10 ** x
        n = n_lg_n_helper(time, o, n)
    return n


def n_lg_n_helper(time, o, n_so_far):
    time_taken = 0
    n = n_so_far
    while time_taken < time:
        n += o
        time_taken = (n * math.log(n, 2))
    return n - o


def n_squared(time):
    time_taken, n = 0, 0
    while time_taken <= time:
        n += 1
        time_taken = n ** 2
    return n-1


def n_cubed(time):
    time_taken, n = 0, 0
    while time_taken <= time:
        n += 1
        time_taken = n ** 3
    return n-1


def two_to_the_n(time):
    time_taken, n = 0, 0
    while time_taken <= time:
        n += 1
        time_taken = 2 ** n
    return n-1


def n_factorial(time):
    time_taken, n = 0, 0
    while time_taken <= time:
        n += 1
        time_taken = math.factorial(n)
    return n-1


time_array = generate_time_array()
time_array_names = ["second", "minute", "hour", "day", "month", "year", "century"]

print("lg(n)")
for i in range(len(time_array_names)):
    print(time_array_names[i] + ": 2^" + str(time_array[i]))

print("sqrt(n)")
for i in range(len(time_array_names)):
    print(time_array_names[i] + ": " + str(sqrt_n(time_array[i])))

print("n")
for i in range(len(time_array_names)):
    print(time_array_names[i] + ": " + str(n(time_array[i])))

print("n lg(n)")
for i in range(len(time_array_names)):
    print(time_array_names[i] + ": " + str(n_lg_n(time_array[i])))

print("n^2")
for i in range(len(time_array_names)):
    print(time_array_names[i] + ": " + str(n_squared(time_array[i])))

print("n^3")
for i in range(len(time_array_names)):
    print(time_array_names[i] + ": " + str(n_cubed(time_array[i])))

print("2^n")
for i in range(len(time_array_names)):
    print(time_array_names[i] + ": " + str(two_to_the_n(time_array[i])))

print("n!")
for i in range(len(time_array_names)):
    print(time_array_names[i] + ": " + str(n_factorial(time_array[i])))



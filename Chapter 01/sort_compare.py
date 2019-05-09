import math

n = 2
while True:
    if n < 8 * math.log2(n):
        print("for n = " + str(n) + ", merge sort beats insertion sort")
    else:
        print("for n = " + str(n) + ", insertion sort wins!")
        break
    n += 1

n = 5

for i in range(n):
    j = 0

    while j < n-i-1:
        print(" ", end="")
        j += 1

    j = 0

    while j < 2*i+1:
        print("*", end="")
        j += 1

    print()
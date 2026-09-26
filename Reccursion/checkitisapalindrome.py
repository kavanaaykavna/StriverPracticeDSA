L = "madan"
n = len(L)

def f(i):
    if i >= (n // 2):
        return True

    if L[i] != L[n-i-1]:
        return False

    return f(i + 1)

print(f(0))
def sumnum(n):
    if n <= 0:
        return 0
    return n + sumnum(n - 1)


sumnum(3)

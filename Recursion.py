def recur(n, m):
    if n > 0:
        m = n + m
        n = n - 1
        recur(n, m)
    else:
        print(m)


if __name__ == "__main__":
    recur(5, 0)

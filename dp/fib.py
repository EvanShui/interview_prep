def fib_rec(n):
    if n <= 1:
        return 1 
    return fib_rec(n-1) + fib_rec(n-2)

def fib_dp(n):
    if n <= 1:
        return 1
    lst = [0] * n
    lst[0] = 1
    lst[1] = 1
    for i in range(2, n):
        lst[i] = lst[i-1] + lst[i-2]
    return lst[-1]

def main():
    print(fib_dp(6))

if __name__ == '__main__':
    main()

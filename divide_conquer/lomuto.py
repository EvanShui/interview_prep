def partition(A):
    p = A[0]
    s = 0
    for i in range(1, len(A)):
        if A[i] < p:
            s += 1
            A[s], A[i] = A[i], A[s]
    A[0],A[s] = A[s],A[0]
    return s

def main():
    A = [4,1,10,8,7,12,9,2,15]
    A = partition(A)
    assert(A == 2)

if __name__ == '__main__':
    main()

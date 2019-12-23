from lomuto import partition

def quickSelect(A, k):
    print('calling quickselect on A: {} key: {}'.format(A, k))
    s = partition(A)
    print('partition is: ', s)
    if s == k-1:
        return A[s]
    elif s > k-1:
        return quickSelect(A[:s+1], k)
    else:
        return quickSelect(A[s+1:], k-s-1)

def main():
    A = [4,1,10,8,7,12,9,2,15]
    assert(quickSelect(A, 5) == 8)
    assert(quickSelect(A, 7) == 10)

if __name__ == '__main__':
    main()

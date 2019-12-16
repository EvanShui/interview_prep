def selection_sort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        print("swapping [idx: {}, val: {}] with [idx: {}, val: {}]".format(i,
            A[i], min_idx, A[min_idx]))
        A[i], A[min_idx] = A[min_idx], A[i]

def main():
    A = [2, 42, 1, 94, 4, 3, 321]
    selection_sort(A)
    assert(A == [1, 2, 3, 4, 42, 94, 321])

if __name__ == '__main__':
    main()

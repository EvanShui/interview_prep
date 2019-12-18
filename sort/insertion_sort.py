def insertion_sort(A):
    for i in range(1, len(A)):
        # it's important that we store A[i] into a key variable. The value in
        # the ith position can change as we swap values as we head towards idx:
        # 0
        #
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        print("swapping: [idx: {} val: {}] with [idx: {} val: {}]".format(j,
            A[j], i, A[i]))
        # A[i] on line 3 != A[i] at this point of the code
        A[j+1] = key
        
def main():
    A = [2, 42, 1, 94, 4, 3, 321]
    insertion_sort(A)
    print(A)
    assert(A == [1, 2, 3, 4, 42, 94, 321])

if __name__ == '__main__':
    main()

import random
random.seed(123)

def partition(A):
    A = median3(A)
    pivot = A[-2]
    i = 0
    j = len(A) - 3
    print('i: ', i)
    print('j: ', j)
    print(A)
    while i < j:
        while A[i] < pivot:
            i += 1
            print('i: ', i)
            print(A)
        while A[j] > pivot:
            j -= 1
            print('j: ', j)
            print(A)

        if i < j:
            print('swapping: [idx: {} val: {}] [idx:{} val: {}]'.format(i, A[i],
                j, A[j]))
            A[i], A[j] = A[j], A[i]
            print(A)
    A[j+1], A[len(A) - 2] = A[len(A) - 2], A[j+1]
    print('after resetting pivot: ',A)
    return A

def median3(A):
    max_ind = A.index(max(A))
    min_ind = A.index(min(A))
    potential_indices = []
    for ind,val in enumerate(range(len(A))):
        if ind != max_ind and ind != min_ind:
            potential_indices.append(ind)
    rand_ind = potential_indices[random.randint(0, len(potential_indices)-1)]
    rand_val = A[rand_ind]
    max_val = A[max_ind]
    print('pivot: ', A[rand_ind])
    A[0], A[min_ind] = A[min_ind], A[0]
    A.remove(rand_val)
    A.remove(max_val)
    A.append(rand_val)
    A.append(max_val)
    return A

def main():
    A = [4,1,10,8,7,12,9,2,15]
    A = partition(A)
    assert(A == [1,2,4,7,12,9,10,8,15])
if __name__ == '__main__':
    main()

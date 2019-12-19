def merge_sort(A):
    print("in merge sort: ", A)
    if len(A) <= 1:
        return A
    mid_ind = len(A) // 2
    left_arr = merge_sort(A[:mid_ind])
    print("left arr: ", left_arr)
    right_arr = merge_sort(A[mid_ind:])
    print("right arr: ", right_arr)
    return merge(left_arr, right_arr)

def merge(left, right):
    print('---------enter merge subroutine---------')
    print('left: ', left)
    print('right: ', right)
    ret_arr = []
    left_idx = 0
    right_idx = 0
    left_val = 0
    right_val = 0
    while left_idx < len(left) or right_idx < len(right):
        if left_idx >= len(left):
            left_val = float('inf')
        else:
            left_val = left[left_idx]

        if right_idx >= len(right):
            right_val = float('inf')
        else:
            right_val = right[right_idx]
        print('left: [idx: {} val: {}] right: [idx: {} val: {}]'.format(left_idx, left_val, right_idx, right_val))

        if left_val < right_val:
            ret_arr.append(left_val)
            left_idx += 1
        else:
            ret_arr.append(right_val)
            right_idx += 1
    print('popping out merge: ', ret_arr)
    print('---------exit merge subroutine---------')
    return ret_arr

def main():
    A = [2, 42, 1, 94, 4, 3, 321]
    A = merge_sort(A)
    assert(A == [1, 2, 3, 4, 42, 94, 321])

if __name__ == '__main__':
    main()

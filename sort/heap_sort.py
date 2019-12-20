import sys
sys.path.append('/home/eshui/interview_prep/ds')
from heap import Heap

def heap_sort(A):
    ret_arr = []
    heap = Heap(len(A)+1)
    heap.buildHeap(A)
    for i in range(len(A)):
        ret_arr.append(heap.deleteMax())
    return ret_arr[::-1]

def main():
    A = [2, 42, 1, 94, 4, 3, 321]
    A = heap_sort(A)
    assert(A == [1, 2, 3, 4, 42, 94, 321])

if __name__ == '__main__':
    main()

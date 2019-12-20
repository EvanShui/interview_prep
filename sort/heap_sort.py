import sys
sys.path.append('/home/eshui/interview_prep/ds')
from heap import Heap

def heap_sort(A):
    heap = Heap(len(A)+1)
    # stage 1
    heap.buildHeap(A)
    # stage 2
    for ind, val in enumerate(range(len(A))):
        val = heap.deleteMax()
        heap.heap[heap.capacity-ind-1] = val
    return heap.heap[1:]

def main():
    A = [2, 42, 1, 94, 4, 3, 321]
    A = heap_sort(A)
    assert(A == [1, 2, 3, 4, 42, 94, 321])

if __name__ == '__main__':
    main()

class Heap(object):

    def __init__(self, capacity):
        # max heap
        self.capacity = capacity;
        self.heap_length = 0;
        self.heap = [0] * self.capacity

    def driftDown(self, pos):
        tmp = self.heap[pos]
        while pos * 2 <= self.heap_length:
            child = pos * 2
            if child != self.heap_length and (self.heap[child + 1] > self.heap[child]):
                child += 1
            if self.heap[child] > tmp:
                # alter > to < to change from max heap to min heap
                self.heap[pos] = self.heap[child]
                pos = child
            else:
                break
        self.heap[pos] = tmp

    def driftUp(self, pos):
        if pos > self.heap_length:
            return False
        parent_ind = pos // 2
        while parent_ind > 0:
            if self.heap[parent_ind] < self.heap[pos]:
                # alter < to > to change from max heap to min heap
                # swap them
                temp = self.heap[parent_ind]
                self.heap[parent_ind] = self.heap[pos]
                self.heap[pos] = temp
            else:
                return False
            pos = parent_ind
            parent_ind //= 2
        return True

    def buildHeap(self, inp_arr):
        if len(inp_arr) > self.capacity:
            return False
        self.heap_length = len(inp_arr)
        for i in range(1, self.heap_length + 1):
            self.heap[i] = inp_arr[i-1]
        for i in range(int(self.heap_length/2), 0, -1):
            self.driftDown(i)
        return True

    def insert(self, val):
        if self.heap_length == self.capacity:
            return False
        self.heap_length += 1
        self.heap[self.heap_length] = val
        self.driftUp(self.heap_length)
        return True

    def verify(self):
        index = self.heap_length
        while index > 1:
            if (self.heap[index] > self.heap[index//2]):
                return False
            index -= 1
        return True
    
    def deleteMax(self):
        temp = self.heap[1]
        self.heap[1] = self.heap[self.heap_length]
        self.heap[self.heap_length] = 0
        self.heap_length -= 1
        self.driftDown(1)
        return temp

    def isFull(self):
        if self.heap_length == self.capacity - 1:
            return True
        return False

def main():
    heap = Heap(10)
    test1 = [1,2,3,4,5]
    test2 = [9, 3, 5, 10, 2, 6, 34]
    test3 = [20, 15, 13, 12, 11 ,10, 9]
    heap.buildHeap(test1)
    assert(heap.heap == [0, 5, 4, 3, 1, 2, 0, 0, 0, 0])
    heap.buildHeap(test2)
    assert(heap.heap == [0, 34, 10, 9, 3, 2, 6, 5, 0, 0])
    heap.buildHeap(test3)
    assert(heap.heap == [0, 20, 15, 13, 12, 11, 10, 9, 0, 0])
    heap.insert(32)
    assert(heap.heap == [0, 32, 20, 13, 15, 11, 10, 9, 12, 0])
    heap.insert(18)
    assert(heap.heap == [0, 32, 20, 13, 18, 11, 10, 9, 12, 15])
    assert(heap.isFull() == True)
    assert(heap.deleteMax() == 32)
    assert(heap.heap == [0, 20, 18, 13, 15, 11, 10, 9, 12, 0])
    assert(heap.isFull() == False)

if __name__ == '__main__':
    main()

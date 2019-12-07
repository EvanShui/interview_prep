class Heap(object):

    def __init__(self, capacity):
        self.heap_length = capacity + 1;
        self.capacity = capacity;
        self.heap = [0] * self.heal_length

    def driftDown(index):
        left_child = index*2
        right_child = index*2 + 1
        min_child = left_child
        temp = self.heap[index]
        while min_child <= self.capacity:
            if self.heap[left_child] > self.heap[right_child]:
                min_child = right_child
            else:
                min_child = left_child
            if self.heap[min_child] < self.heap[index]:
                temp = self.heap[index]
                self.heap[index] = self.heap[min_child]
                self.heap[min_child] = temp
            else:
                return
            index = min_child
            min_child *= 2

    def driftDownTest():

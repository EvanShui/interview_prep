class Heap(object):

    def __init__(self, capacity):
        self.heap_length = capacity + 1;
        self.capacity = capacity;
        self.heap = [0] * self.heal_length

    def driftDown(index):
        child_ind = index*2
        right_child = child_ind + 1
        left_child = child_ind
        temp = self.heap[index]
        while child_ind <= self.capacity:
            if self.heap[left_child] > self.heap[right_child]:
                child_ind = right_child
            else:
                child_ind = left_child
                

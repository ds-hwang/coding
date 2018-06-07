class Heap(object):
    def __init__(self, root):
        self.array = [root]
    
    def insert(self, value):
        i = len(self.array)
        self.array.append(value)
        self.heapify(i)
    
    def heapify(self, i):
        current = i
        parent = self.parent(current)
        while current and self.array[parent] < self.array[current]:
            (self.array[parent], self.array[current]) = (self.array[current], self.array[parent])
            current = parent
            parent = self.parent(current)
    
    def pop(self):
        if not self.array:
            return None
        result = self.array[0]
        current = 0
        left = self.left(current)
        right = self.right(current)
        while left:
            if not right:
                self.array[current] = self.array[left]
                del self.array[left]
                return result
            if self.array[left] > self.array[right]:
                self.array[current] = self.array[left]
                current = left
            else:
                self.array[current] = self.array[right]
                current = right
            left = self.left(current)
            right = self.right(current)
        if (current + 1) == len(self.array):
            self.array.pop()
            return result
        self.array[current] = self.array.pop()
        self.heapify(current)
        return result
                
    # [1,2,3,4,5,6,7,8,9]
    def level(self, i):
        hi = i + 1
        l = 1
        c = hi >> 1
        while c:
            c = c >> 1
            l += 1
        return l

    def parent(self, i):
        hi = i + 1
        return (hi // 2) - 1
    
    def left(self, i):
        hi = i + 1
        l = (hi * 2) - 1
        if len(self.array) <= l:
            return None
        return l
    
    def right(self, i):
        l = self.left(i)
        if not l:
            return None
        r = l + 1
        if len(self.array) <= r:
            return None
        return r

heap = Heap(5)
heap.insert(6)
heap.insert(3)
heap.insert(56)
heap.insert(7)
heap.insert(26)
heap.insert(1)
heap.insert(98)
heap.insert(65)
heap.insert(36)
heap.insert(66)

max_value = heap.pop()
while max_value:
    print(max_value)
    max_value = heap.pop()
    
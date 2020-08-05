class RingBuffer:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
        self.indexOfOldestItem = 0

    def append(self, item):
        if len(self.queue) < self.capacity:
            self.queue.append(item)
        else:
            self.queue[self.indexOfOldestItem] = item
            shouldReset = True if self.indexOfOldestItem == self.capacity else False
            self.indexOfOldestItem = 0 if shouldReset else self.indexOfOldestItem + 1

    def get(self):
        return self.queue
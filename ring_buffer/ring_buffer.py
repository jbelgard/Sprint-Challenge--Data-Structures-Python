class RingBuffer:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
        self.indexToOverwrite = 0

    def append(self, item):
        queueSize = len(self.queue)
        if queueSize < self.capacity:
            self.queue.append(item)
        else:
            self.queue[self.indexToOverwrite] = item
            self.indexToOverwrite += 1

        if self.indexToOverwrite == self.capacity:
            self.indexToOverwrite = 0

    def get(self):
        return self.queue
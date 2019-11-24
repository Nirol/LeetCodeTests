import sys
class FullQueue(Exception):
    def __str__(self):
        return ("Cant insert items to a full queue")


class EmptyQueue(Exception):
    def __str__(self):
        return ("Cant remove items from an empty queue")

class Queue:
    def __init__(self, max_size=15):
        self.max_size = max_size
        self.queue_list = []
        self.size = 0

    def enqueue(self, item):
        if (self.size == self.max_size):
            raise FullQueue
            return -1
        else:
            self.queue_list.append(item)
            self.size+=1
            return 0

    def dequeue(self):
        if (self.size == 0):
            raise EmptyQueue
            return -1
        else:
            item = self.queue_list.pop(0)
            self.size-=1
            return item

    def size(self):
        return self.size

    def is_full(self):
        return self.size == self.max_size



if(__name__ == "__main__"):
    x = Queue()
    x.enqueue(5)
    x.enqueue(13)
    x.enqueue(12)
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())



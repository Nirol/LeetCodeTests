import sys
class Stack:
    def __init__(self, max_size=15):
        self.max_size = max_size
        self.stack_list = []
        self.size = 0
        self.min = sys.maxsize

    def push(self, item):
        if len(self.stack_list) == 0:
            min = item
            self.stack_list.insert(0,"bottom")
        else:
            to_push = item - self.min
            self.stack_list.insert(0, to_push)
            if to_push < 0:
                self.min = item

    def pop(self):
        poped_item = self.stack_list.pop(0)
        to_return = poped_item
        if poped_item < 0:
            #return min to earlier min value
            to_return = self.min
            self.min = self.min - poped_item
        return to_return







    def is_full(self):
        return self.size == self.max_size



if(__name__ == "__main__"):
    x = Stack()
    x.enqueue(5)
    x.enqueue(13)
    x.enqueue(12)
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())
    print(x.dequeue())


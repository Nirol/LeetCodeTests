from heapq import heappush, heappop
class DinnerPlates:

    def __init__(self, capacity: int):
        self.list_stacks = []
        self.cap = capacity
        self.list_stacks.insert([])
        self.min_open_stack = 0
        self.heap=[]
        heappush(self.heap, 0)

    def find_next_min_stack(self):
        new_min = None
        try:
            new_min = self.min_open_stack=heappop(self.heap)
        except IndexError:
            new_min = -1
        finally:
            self.min_open_stack = new_min

    def push(self, val: int) -> None:
        if self.min_open_stack == -1:
            new_stack = [val]
            self.list_stacks.append(new_stack)
            self.min_open_stack = len(self.list_stacks) - 1
        else:
            self.list_stacks[self.min_open_stack].insert(0,val)
            if len(self.list_stack[self.min_open_stack] == self.cap):
                self.find_next_min_stack()

    def pop(self) -> int:
        to_return = self.list_stacks[-1].pop()
        if len(self.list_stacks[-1]) == 0:
            if self.min_open_stack == len(self.list_stacks) -1:
                self.find_next_min_stack()
            self.list_stacks.remove(-1)

        elif len(self.list_stacks[-1]) == self.cap -1:
            heappush(self.heap, len(self.list_stacks) - 1)
        return to_return

    def update_min_Stack(self, index):
        if index < self.min_open_stack:
            self.min_open_stack=index
        else:
            heappush(self.heap, index)

    def popAtStack(self, index: int) -> int:
        to_return = self.list_stacks[index].pop()
        self.update_min_stack(index)
        return to_return


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_list = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_list.insert(0, x)

    def pop(self):
        """
        :rtype: None
        """
        return self.stack_list.pop(0)

    def top(self):
        """
        :rtype: int
        """
        to_return = self.stack_list[0]
        return to_return

    def getMin(self):
        """
        :rtype: int
        """
        min_item = min(self.stack_list)
        return min_item


if __name__ == "__main__":
    x =  MinStack()
    x.push(5)
    x.push(6)
    x.push(7)
    print(x.getMin())
    print(x.top())
    print(x.pop())
    print(x.pop())
    print(x.pop())

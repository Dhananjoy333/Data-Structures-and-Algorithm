#Q.Leetcode-155 : create functions push,pop,top and getmin
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        if len(self.stack) == 0:
            self.stack.append([val,val])
        else:
            mini = min(self.stack[-1][1],val)
            self.stack.append([val,mini])

    def pop(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack[-1][0]

    def getMin(self):
        if len(self.stack) == 0:
            return 0
        return self.stack[-1][1]
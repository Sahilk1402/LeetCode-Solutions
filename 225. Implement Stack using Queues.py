from collections import deque
class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self.curr_top = None

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.curr_top = x

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.curr_top = self.queue1.popleft()
            self.queue2.append(self.curr_top)
        popped_element = self.queue1.popleft()
        self.queue1 , self.queue2 = self.queue2, self.queue1
        return popped_element
    def top(self) -> int:
        return self.curr_top

    def empty(self) -> bool:
        return len(self.queue1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

#큐를 이용한 스택 구현.

'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
'''

#풀이 방법

'''
1.스택 구조 이용
'''

# # # # # # # # # # # # # # # # # # # # # 재귀함수

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q)==0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

'''Implement Queue using Stacks

    William Ikenna-Nwosu (wiknwo)

    Implement a first in first out (FIFO) queue using only 
    two stacks. The implemented queue should support all the 
    functions of a normal queue (push, peek, pop, and empty).

    Implement the MyQueue class:

    - void push(int x) Pushes element x to the back of the 
    queue.

    - int pop() Removes the element from the front of the 
    queue and returns it.

    - int peek() Returns the element at the front of the queue.

    - boolean empty() Returns true if the queue is empty, 
    false otherwise.
'''
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.queue


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
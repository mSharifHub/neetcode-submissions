
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class MyStack:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __index_error(self):
      if self.head is None:
            raise IndexError("Cannot dequeue from an empty queue")


    def enqueue(self,value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node 
        self._size +=1

    def dequeue(self):
        self.__index_error()

        popped_value = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tai = None

        self._size -= 1

        return popped_value

    def peek(self):
       self._MyStack__index_error()
       return self.head.value
        
    
    def push(self, x: int) -> None:
        self.enqueue(x)
        

    def pop(self) -> int:
        return self.dequeue()
        

    def top(self) -> int:
        return self.peek()
        

    def empty(self) -> bool:
        return self._size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
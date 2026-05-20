class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    #push element to the back of the queue
    def push(self,x:int) -> None:
        self.stack1.append(x)
        
    #remove element from the front of the queue
    def pop(self) -> int:
        self._transfer_if_needed()
        return self.stack2.pop()
    
    
    #get front element
    def peek(self) ->int:
        self._transfer_if_needed()
        return self.stack2[-1]
    
    #check if queue is empty
    def empty(self) ->bool:
        return len(self.stack1) ==0 and len(self.stack2) ==0
    
    # transfer elements only when needed
    def _transfer_if_needed(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())


if __name__=="__main__":
    q=Solution()
    q.push(10)
    q.push(20)
    q.push(30)
    print(q.peek()) # peek dont remove the value
    print(q.pop())
from collections import deque
class Queue:
    def __init__(self):
        self.q = deque()
    def enqueue(self,val):
        if len(self.q) == 5:
            return "Queue Overflow"
        else:
            self.q.append(val)
            return ("Enqueued Element",val)
    def dequeue(self):
        if not self.q:
            return "Queue Underflow"
        else:
            return self.q.popleft()
    def top(self):
        if not self.queue:
            return "Queue Underflow"
        else:
            return self.stack[-1]
    def peek(self):
        if not self.q:
            return "Queue Underflow"
        else:
            return self.stack[-1]
qObj = Queue()
ele = [5,10,20,30,40,50]
for i in ele:
    print(qObj.enqueue(i))
    print(qObj.q)
print(qObj.dequeue())

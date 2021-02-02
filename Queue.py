class Queue:
  def __init__(self): # constructor
    self.contents = []
  def isEmpty(self): # predicate to test contents 
    return self.contents == []
  def front(self): # lookup function 
    return self.contents[0]
  def enqueue(self, element): # add elements 
    self.contents = self.contents + [ element ]
  def dequeue(self): # take elements out 
    item = self.front()
    self.contents = self.contents[1:]
    return item
  def __str__(self): # functions to simplify viewing 
    return str(self.contents)
  def __repr__(self):
    return str(self.contents)

def main():
  a = Queue()            # creates an empty queue 
  print(a)               # prints [] 
  print(a.isEmpty())     # prints True 
  a.enqueue(1)           # prints nothing but adds 1 to the queue 
  print(a)               # prints [1]
  print(a.front())       # prints 1
  print(a)               # prints [1]
  a.enqueue(5)           # prints nothing the queue is now [1, 5]
  a.enqueue(8)           # prints nothing the queue is now [1, 5, 8]
  a.enqueue(10)          # prints nothing the queue is now [1, 5, 8, 10]
  print(a.isEmpty())     # prints False  
  print(a)               # prints [1, 5, 8, 10]
  print(a.dequeue())     # prints 1 and the queue is now [5, 8, 10]
  print(a)               # prints [5, 8, 10]

if __name__=="__main__":
  main()
  

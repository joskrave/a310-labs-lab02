# cons, first, rest, isEmpty, length 

class MTList:
  def __init__(self):
    pass
  def isEmpty(self):
    return True
  def cons(self, item):
    return NEList(item)
  def __str__(self):
    return " MT "
  def length(self):
    return 0
  def append(self, other):
    return other

class NEList:
  def __init__(self, item):
    self.item = item
    self.next = MTList()
  def first(self):
    return self.item
  def rest(self):
    return self.next
  def cons(self, item):
    a = NEList(item)
    a.next = self
    return a
  def isEmpty(self):
    return False
  def __str__(self):
    return str(self.item) + " " + str(self.next)
  def length(self):
    return 1 + self.next.length()
  def append(self, other):
    if other.isEmpty():
      return self
    else:
      a = self.rest().append(other)
      return a.cons(self.first())

def main():
  a = MTList()
  print( "Empty list: " + str(a) )
  print( "Is the list empty at this stage? Answer: " + str(a.isEmpty()) )
  print( "How long is the list at this stage? Answer: " + str(a.length()) )
  a = a.cons(3)
  print( "Adding 3 list becomes: " + str(a) )
  print( "Is the list empty at this stage? Answer: " + str(a.isEmpty()) )
  a = a.cons(5)
  print( "Adding 5 list becomes: " + str(a) )
  a = a.cons(1)
  print( "Adding 1 list becomes: " + str(a) )
  print( "How long is the list at this stage? Answer: " + str(a.length()) )
  a = a.rest().rest().cons(1)
  print( "Taking out the 5 the list becomes: " + str(a) )
  print( "Is the list empty at this stage? Answer: " + str(a.isEmpty()) )
  b = MTList()
  b = b.cons(9)
  c = a.append(b)
  print( str(a) + " append " + str(b) + " produces " + str(c) )

if __name__=="__main__":
  main()

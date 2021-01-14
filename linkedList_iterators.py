from linkedList import LinkedList

class IterableLinkedList(LinkedList):

  def __iter__(self):
    def value_generator():
      current = self.head
      while current:
        yield current.value
        current = current.next
    return value_generator()

ill = IterableLinkedList([0,5,4,2])

sum = 0 
for number in ill :
  sum += number if number % 2 else 0

print(sum)
# 5
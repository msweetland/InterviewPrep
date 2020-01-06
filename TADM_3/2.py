class Node(object):
  def __init__(self, item, next_node=None):
    self.item = item
    self.next = next_node

  def get_data(self):
    return self.item
  
  def get_next(self):
    return self.next

  def set_next(self, new_next):
    self.next = new_next


def create_linked_list(arr):
  assert len(arr) is not 0, 'make sure array is not zero'
  Head = Node(arr[0])
  Last = Head
  for item in arr[1:]:
    temp_node = Node(item)
    Last.set_next(temp_node)
    Last = temp_node
  return Head


def linked_to_arr(linked_list):
  arr = []
  current_node = linked_list
  while current_node:
    arr.append(current_node.get_data())
    current_node = current_node.get_next()
  return arr

# Write a program to reverse the direction of a given singly-linked list.
# In other words, after the reversal all pointers should now point backwards.
# your algorithm should take linear time

def reverse_linked_list(linked_list: Node):
  stack: List[Node] = []
  current_node = linked_list
  while current_node:
    stack.append(current_node)
    current_node = current_node.get_next()

  Head = stack.pop()
  Current = Head
  while len(stack) > 0:
    next_node = stack.pop()
    next_node.set_next(None) # remove previous reference
    Current.set_next(next_node)
    Current = Current.get_next()

  return Head


if __name__ == "__main__":
  test_arr = [1,2,3,4]
  linked_list = create_linked_list(test_arr)
  rev_linked_list = reverse_linked_list(linked_list)
  rev_arr = linked_to_arr(rev_linked_list)
  assert rev_arr == test_arr[::-1]


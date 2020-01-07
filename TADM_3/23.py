class LinkedNode(object):
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
  Head = LinkedNode(arr[0])
  Last = Head
  for item in arr[1:]:
    temp_node = LinkedNode(item)
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


# Implement an algorithm to reverse a linked list
def iterative_reverse_linked(linked_list: LinkedNode):
  # Use second list as stack data structure
  Head = None
  while linked_list:
    split_node = linked_list.get_next()
    linked_list.set_next(Head)
    Head = linked_list 
    linked_list = split_node
  return Head


# Now do it without recursion.
def recursive_reverse_linked(linked_list: LinkedNode):
  # use call stack to reverse
  if not linked_list or not linked_list.get_next():
    return linked_list
  else:
    split_node = linked_list.get_next()
    linked_list.set_next(None)
    Head = recursive_reverse_linked(split_node)
    split_node.set_next(linked_list)
    return Head


if __name__ == "__main__":
  test_arr = [1, 2, 3, 4, 5]
  linked_list = create_linked_list(test_arr)

  reverse_iterative = iterative_reverse_linked(linked_list)
  reverse_iterative_arr = linked_to_arr(reverse_iterative)
  assert reverse_iterative_arr == test_arr[::-1]

  reverse_recursive = recursive_reverse_linked(linked_list)
  reverse_recursive_arr = linked_to_arr(reverse_iterative)
  assert reverse_recursive_arr == test_arr[::-1]
  

from inspect import isfunction

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


class BinaryNode(object):
  def __init__(self, item, comparator, next_node_left=None, next_node_right=None):
    assert isfunction(comparator), 'Comparator must be a function'
    self.item = item
    self.comparator = comparator
    self.next_node_left: BinaryNode = next_node_left
    self.next_node_right: BinaryNode = next_node_right

  def get_data(self):
    return self.item

  def get_next_left(self):
    return self.next_node_left

  def get_next_right(self):
    return self.next_node_right

  def set_next_left(self, new_node_left):
    self.next_node_left = new_node_left

  def set_next_right(self, new_node_right):
    self.next_node_right = new_node_right

  def insert(self, value):
    if self.comparator(value, self.item):
      if self.next_node_left:
        self.next_node_left.insert(value)
      else:
        new_node = BinaryNode(value, self.comparator)
        self.set_next_left(new_node)
    else:
      if self.next_node_right:
        self.next_node_right.insert(value)
      else:
        new_node = BinaryNode(value, self.comparator)
        self.set_next_right(new_node)


def create_binary_tree(arr, comparator):
  assert len(arr) > 0, 'Array must not be empty'
  Tree = BinaryNode(arr[0], comparator)
  for value in arr[1:]:
    Tree.insert(value)
  return Tree

def linked_to_arr(linked_list):
  arr = []
  current_node = linked_list
  while current_node:
    arr.append(current_node.get_data())
    current_node = current_node.get_next()
  return arr

# Write a program to convert a binary search tree into a linked list.

def tree_to_linked_list(binary_tree: BinaryNode) -> LinkedNode:
  middle_node = LinkedNode(binary_tree.get_data())
  left_linked = None
  right_linked = None
  Head = None
  if binary_tree.get_next_left():
    left_linked = tree_to_linked_list(binary_tree.get_next_left())
  if binary_tree.get_next_right():
    right_linked = tree_to_linked_list(binary_tree.get_next_right())
  if right_linked:
    middle_node.set_next(right_linked)
  if left_linked:
    Head = left_linked
    current_node = Head
    while current_node:
      next_node = current_node.get_next()
      if not next_node:
        current_node.set_next(middle_node)
        break
      else:
        current_node = next_node
  else:
    Head = middle_node
  return Head



if __name__ == "__main__":
  def compare(a, b): return a < b
  test_arr = [1, 6, 3, 6, 3, 10, 7, 8]
  binary_tree = create_binary_tree(test_arr, compare)
  linked_binary = tree_to_linked_list(binary_tree)
  arr = linked_to_arr(linked_binary)
  assert arr == sorted(test_arr)

  # assert compare_tree(create_binary_tree_a, create_binary_tree_b) == False

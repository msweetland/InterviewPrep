from inspect import isfunction

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


# Write a function to compare whether two binary trees are identical. 
# Identical trees have the same key value at each position and the same structure.
def compare_tree(tree_a: BinaryNode, tree_b: BinaryNode):
  # in order traversal
  if not tree_a and not tree_b:
    return True
  elif (tree_a and not tree_b) or (tree_b and not tree_a):
    return False
  else:
    return (
      tree_a.get_data() == tree_b.get_data() and 
      compare_tree(tree_a.get_next_left(), tree_b.get_next_left()) and
      compare_tree(tree_a.get_next_right(), tree_b.get_next_right())
    )

if __name__ == "__main__":
  compare = lambda a, b : a < b
  test_arr_a = [1, 6, 3, 4, 5, 7, 9, 2, 3, 8]
  test_arr_b = [1, 6, 3, 4, 5, 7, 9, 2, 3, 9]
  binary_tree_a = create_binary_tree(test_arr_a, compare)
  binary_tree_b = create_binary_tree(test_arr_b, compare)
  binary_tree_c = create_binary_tree(test_arr_b, compare)
  assert compare_tree(binary_tree_a, binary_tree_b) == False
  assert compare_tree(binary_tree_b, binary_tree_c) == True



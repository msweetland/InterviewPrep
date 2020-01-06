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


# Write a function to find the middle node of a singly-linked list.
def find_middle_linked(linked_list):
  # calculate size of list, divide by tow loop through gain and get
  current_node = linked_list
  length = 0
  while current_node:
    length += 1
    current_node = current_node.get_next()
  return length // 2

if __name__ == "__main__":
  arr = [1,2,3,4,5,6,7,8, 9]
  ll = create_linked_list(arr)
  middle = find_middle_linked(ll)
  assert middle == 4

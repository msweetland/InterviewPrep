# Design a dictionary data structure in which search, insertion, and deletion can all be processed in O(1) time in the worst case.
# You may assume the set elements are integers drawn from a finite set {1,2,..,n}, and initialization can take $ O(n) $ time.

class Finite_Lookup(object):
  def __init__(self, length):
    self.bit_array = [False for i in range(length)]

  def insert(self, idx):
    assert idx < len(self.bit_array)
    self.bit_array[idx] = True

  def search(self, idx):
    assert idx < len(self.bit_array)
    return self.bit_array[idx]
  
  def delete(self, idx):
    assert idx < len(self.bit_array)
    self.bit_array[idx] = False

if __name__ == "__main__":
    dic = Finite_Lookup(100)
    dic.insert(0)
    assert dic.search(0) == True
    dic.delete(0)
    assert dic.search(0) == False

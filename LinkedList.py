class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None


  def __eq__(self, other):
    return True if self.value == other.value else False


class LinkedList:
  def __init__(self, head=None):
    self.head = head


  def append(self, node):
    if not self.head:
      self.head = node
      return
    cursor_node = self.head
    while cursor_node.next_node:
      cursor_node = cursor_node.next_node
    cursor_node.next_node = node


  def insert(self, flag_node, node):
    if self.head == flag_node:
      node.next_node = self.head
      self.head = node
    else:
      _node = self.head
      while _node.next_node:
        if _node.next_node == flag_node:
          break
        _node = _node.next_node
      node.next_node = _node.next_node
      _node.next_node = node


  def delete(self, node):
    if self.head:
      if self.head.value == node.value:
        self.head = self.head.next_node
        return
      prev_node = self.head
      while prev_node.next_node:
        if prev_node.next_node == node:
          break
        prev_node = prev_node.next_node
      _node = prev_node.next_node
      prev_node.next_node = _node.next_node


  def print_list(self):
    cursor_node = self.head
    while cursor_node:
      print(cursor_node.value)
      cursor_node = cursor_node.next_node

class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None


  def __eq__(self, other):
    return True if self.value == other.value else False


class LinkedList:
  def __init__(self):
    self.head = None


  def __contains__(self, node):
    found = False
    if self.head:
      cursor = self.head
      while cursor:
        if cursor == node:
          found = True
          break
        cursor = cursor.next_node
    return found


  def __len__(self):
    cnt = 0
    if self.head:
      cursor = self.head
      while cursor:
        cnt += 1
        cursor = cursor.next_node
    return cnt


  def append(self, node):
    if not self.head:
      self.head = node
      return
    cursor = self.head
    while cursor.next_node:
      cursor = cursor.next_node
    cursor.next_node = node


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


  def remove_duplicates(self):
    # (i/o/p)c -> (inner/outer/prev) curosr
    oc = self.head
    while oc.next_node:
      pc, ic = oc, oc.next_node
      while ic:
        if ic == oc:
          pc.next_node = ic.next_node
        else:
          pc = pc.next_node
        ic = ic.next_node
      oc = oc.next_node


  def reverse(self):
    if not self.head or not self.head.next_node:
      return

    cursor = self.head.next_node
    self.head.next_node = None

    while cursor:
      next_cursor = cursor.next_node
      cursor.next_node = self.head
      self.head = cursor
      cursor = next_cursor


  def print_list(self):
    cursor = self.head
    while cursor:
      print(cursor.value)
      cursor = cursor.next_node

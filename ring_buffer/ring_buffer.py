class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # check if the storage contains any Nones and replace first available None
    if None in self.storage:
      # get index of first None
      append_index = self.storage.index(None)
      # add new item at the append_index
      self.storage[append_index] = item
    # if there are no Nones, find the oldest item and replace it
    else:
      # initialize the oldest item as the start of the list
      oldest_item = self.storage[0]
      # loop through the list to find the oldest item
      for item_i in self.storage:
        if item_i < oldest_item:
          oldest_item = item_i
      # get the index of the oldest item
      append_index = self.storage.index(oldest_item)
      # add new item at the append_index
      self.storage[append_index] = item
    
  def get(self):
    # return the storage without any None items
    return [item for item in self.storage if item != None]
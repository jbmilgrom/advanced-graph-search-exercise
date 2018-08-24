class PriorityQueue:

  def __init__(self, is_higher_priority = lambda subject, target: subject[0] < target[0]):
    self._high_to_low = [] # ordered from high to low so easier to pop off low from end
    self._is_higher_priority = is_higher_priority

  def insert(self, item):
    i = 0
    # TODO: divide and conquer to improve perforamce
    while i < len(self._high_to_low):
      if not self._is_higher_priority(item, self._high_to_low[i]):
        self._high_to_low.insert(i, item)
        return
      i += 1
    self._high_to_low.append(item)

  def next(self):
    return self._high_to_low.pop()

  def is_empty(self):
    return len(self._high_to_low) == 0
class PriorityQueue:

  def __init__(self):
    self._high_to_low = [] # ordered from high to low so easier to pop off low from end

  def insert(self, pair):
    i = 0
    # TODO: divide and conquer to improve perforamce
    while i < len(self._high_to_low):
      if pair[0] > self._high_to_low[i][0]:
        self._high_to_low.insert(i, pair)
        return
      i += 1
    self._high_to_low.append(pair)

  def next(self):
    return self._high_to_low.pop()

  def is_empty(self):
    return len(self._high_to_low) == 0
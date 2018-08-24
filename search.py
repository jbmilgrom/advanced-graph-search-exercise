import collections
from constants import G, S, COSTS
from priority_queue import PriorityQueue


# Understanding:
#   Find the shortest number of hops between S and G on a nxn grid
#   return the path in the form of a dictionary {
#     (S): None,
#     (A): (S),
#     (B): (A),
#     ...
#     (G): (G-1)
#   }
#   Neighbors are N,S,E,W of every node
#   Breadth first search of neighbors, until G is found
#     tracking visited nodes by whether or not dest:source combination has occured before
def bfs(grid, start, goal):
  queue = collections.deque()
  return no_cost_search(
    grid,
    start,
    goal,
    lambda node: queue.append(node),
    lambda: queue.popleft(),
    lambda: len(queue) == 0
  )

def dfs(grid, start, goal):
  stack = collections.deque()
  return no_cost_search(
    grid,
    start,
    goal,
    lambda node: stack.append(node),
    lambda: stack.pop(),
    lambda: len(stack) == 0
  )

def ucs(grid, start, goal):
  length = len(grid)
  visited = { start: 'START' }
  pqueue = PriorityQueue()
  pqueue.insert((0, start))
  while not pqueue.is_empty():
    cost, current = pqueue.next()
    if grid[current[0]][current[1]] == G:
        return visited
    for next in neighbors(current, -1, length):
      if visited.get(next):
        continue
      pqueue.insert((cost + COSTS[grid[next[0]][next[1]]], next))
      visited[next] = current

def a_star(grid, start, goal):
  length = len(grid)
  visited = { start: 'START' }
  pqueue = PriorityQueue()
  pqueue.insert((0 + manhattan_distance_heuristic(start, goal), 0, start))
  while not pqueue.is_empty():
    _, cost, current = pqueue.next()
    if grid[current[0]][current[1]] == G:
        return visited
    for next in neighbors(current, -1, length):
      if visited.get(next):
        continue
      next_cost = cost + COSTS[grid[next[0]][next[1]]]
      pqueue.insert((next_cost + manhattan_distance_heuristic(next, goal), next_cost, next))
      visited[next] = current

def manhattan_distance_heuristic(current, goal):
   return abs(goal[0] - current[0]) + abs(goal[1] - current[1])

def no_cost_search(grid, start, goal, enter, exit, is_empty):
  length = len(grid)
  visited = { start: 'START' }
  enter(start)
  while not is_empty():
    current = exit()
    for next in neighbors(current, -1, length):
      if visited.get(next):
        continue
      enter(next)
      visited[next] = current
      if grid[next[0]][next[1]] == G:
        return visited

def neighbors(coordinate, low, high):
  x, y = coordinate
  delta = [ (0, 1), (1, 0), (-1, 0), (0, -1) ]
  return [ (x + i, y + j) for i, j in delta if x + i < high and x + i > low and y + j < high and y + j > low ]



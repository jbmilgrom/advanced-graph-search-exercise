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
  return _no_cost_search(
    grid,
    start,
    goal,
    False
  )

def dfs(grid, start, goal):
  return _no_cost_search(
    grid,
    start,
    goal,
    True
  )

def ucs(grid, start, goal):
  return _cost_search(
    grid,
    start,
    goal,
    lambda _, __: 0
  )

def a_star(grid, start, goal):
  return _cost_search(
    grid,
    start,
    goal,
    # manhattan distance heuristic
    lambda current, goal: abs(goal[0] - current[0]) + abs(goal[1] - current[1])
  )

def _no_cost_search(grid, start, goal, insert_item_at_top_of_queue = False):
  pqueue = PriorityQueue(lambda _, __: insert_item_at_top_of_queue)
  return _search(
    grid,
    start,
    goal,
    lambda node: pqueue.insert(node),
    lambda: pqueue.next(),
    lambda: pqueue.is_empty(),
    lambda coord: 1,
    lambda _, __: 0
  )

def _cost_search(grid, start, goal, future_cost_heuristic):
  pqueue = PriorityQueue()
  return _search(
    grid,
    start,
    goal,
    lambda node: pqueue.insert(node),
    lambda: pqueue.next(),
    lambda: pqueue.is_empty(),
    lambda coord: COSTS[grid[coord[0]][coord[1]]],
    future_cost_heuristic
  )

def _search(grid, start, goal, enter, exit, is_empty, step_cost, future_cost_heuristic):
  length = len(grid)
  visited = { start: 'START' }
  enter((0 + future_cost_heuristic(start, goal), 0, start))
  while not is_empty():
    _, cost, current = exit()
    if grid[current[0]][current[1]] == G:
        return visited
    for next in neighbors(current, -1, length):
      if visited.get(next):
        continue
      next_cost = cost + step_cost(next)
      heuristic = next_cost + future_cost_heuristic(next, goal)
      enter((heuristic, next_cost, next))
      visited[next] = current

def neighbors(coordinate, low, high):
  x, y = coordinate
  delta = [ (0, 1), (1, 0), (-1, 0), (0, -1) ]
  return [ (x + i, y + j) for i, j in delta if x + i < high and x + i > low and y + j < high and y + j > low ]



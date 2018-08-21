import collections
from constants import G, S


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
  length = len(grid)
  q = collections.deque()
  visited = { start: 'START' }
  q.append(start)
  while len(q) > 0:
    current = q.popleft()
    for next in neighbors(current, -1, length):
      if visited.get(next):
        continue
      q.append(next)
      visited[next] = current
      if grid[next[0]][next[1]] == G:
        return visited

def dfs():
  pass

def ucs():
  pass

def a_star():
  pass


def neighbors(coordinate, low, high):
  x, y = coordinate
  change = [ (0, 1), (1, 0), (-1, 0), (0, -1) ]
  return [ (x + i, y + j) for i, j in change if x + i < high and x + i > low and y + j < high and y + j > low ]


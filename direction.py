class Node:
def init(self, x, y, direction):
self.x = x
self.y = y
self.direction = direction

__left = { 'N' : 'W’,
'E' : 'N',
'S' : 'E',
'W' : 'S' }

__right = { 'N' : 'E',
'E' : 'S',
'S' : 'W',
'W' : 'N' }

__dx = { 'N' : 0,
'E' : 1,
'S' : 0,
'W' : -1 }

__dy = { 'N' : 1,
'E' : 0,
'S' : -1,
'W' : 0 }
def str(self):
return "<%d,%d,%s>" % (self.x, self.y, self.direction)

def _left(self):
return Node(self.x, self.y,
self.__left[self.direction])

def _right(self):
return Node(self.x, self.y,
self.__right[self.direction])

def _forward(self):
return Node(self.x + self.__dx[self.direction],
self.y + self.__dy[self.direction],
self.direction)

def children(self):
return [ ('left', self._left()),
('right', self._right()),
('forward', self._forward()),
]

def dfs(node, soughtValue, visitedNodes):
if node.x == soughtValue.x and node.y == soughtValue.y and node.direction == soughtValue.direction:
return []

newVisited = visitedNodes[:]
newVisited.append(node)
for action, adjNode in node.children():
if adjNode not in newVisited:
plan = dfs(adjNode, soughtValue, newVisited)
if plan is not None:
p = [action]
p.extend(plan)
return p
return None`

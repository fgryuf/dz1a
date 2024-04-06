from typing import TypeVar, Generic
from collections import deque

__all__ = ("Node", "Graph")


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root
        self.ans = []

    def dfs(self) -> list[Node]:
        self.ans.append(self._root)
        for i in self._root.outbound:
            if i not in self.ans: 
                self._root = i
                self.dfs()
        return self.ans

    def bfs(self) -> list[Node]:
        que = deque()
        que.append(self._root)
        while len(que) != 0:
            d = que[0]
            self.ans.append(d)
            que.popleft()
            for i in d.outbound:
                if i not in self.ans and i not in que:
                    que.append(i)
        anss = self.ans
        self.ans = []
        return anss
    
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
b.point_to(f)
f.point_to(e)

g = Graph(a)

print(g.bfs())
#dddd
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visited = {}

        def dfs(head):

            if not head:
                return None

            if head in visited:
                return visited[head]

            res = Node(head.val, [])
            visited[head] = res

            for n in head.neighbors:
                res.neighbors.append(dfs(n))

            return res


        return dfs(node)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict


class Solution(object):
    def cloneGraph(self, node):
        def dfs(node):
            if node in map: return map[node]
            clone = Node(node.val, [])
            map[node] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone

        if node == None: return None
        map = defaultdict(Node)  # Map OLD node to NEW node
        return dfs(node)

'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # key: memory id of original node
        # value: corresponding deep copy node
        mapping = {}
        # record of nodes whose neighbor list has been rebuilt
        rebuild = set()
        
        def dfs_copy(node):
            if id(node) in mapping:
                # current node has deep copy already
                return
            # create deep copy of current node
            mapping[id(node)] = Node(val=node.val, neighbors=[])
            for ori_neighbor in node.neighbors:
                # create deep copy for original neighbors
                dfs_copy( ori_neighbor )
        # -----------------------------------------------------------
        
        def dfs_rebuild_neighbor( node ):
            
            if node in rebuild:
                
                # neighbor list has been rebuilt already
                return
            
            for ori_neighbor in node.neighbors:
                # rebuild neighbor for deep-copy nodes
                mapping[id(node)].neighbors.append( mapping[id(ori_neighbor)] )
            
            # current node has been rebuilt with neighbors of deep-copy
            rebuild.add( node )
            
            for ori_neighbor in node.neighbors:
                # rebuild neighbor list in dfs
                dfs_rebuild_neighbor( ori_neighbor )
        
        # -----------------------------------------------------------
        
        if node:
            
            # non-empty node
			
			# create deep-copy and maintain mapping relation
            dfs_copy( node )
			
			# rebuild neighbor list
            dfs_rebuild_neighbor( node )
			
            return mapping[ id(node) ]
        
        else:
            
            # empty node (i.e., empty graph)
            return None
            
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def makeTree(self, tree, node):
        root = None
        if node:
            root = TreeNode(val=node)
            if node in tree:
                root.left = self.makeTree(tree, tree[node][0])
                root.right = self.makeTree(tree, tree[node][1])
        return root

    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        roots = set(d[0] for d in descriptions)
        tree = {}
        for p, c, left in descriptions:
            if p not in tree:
                tree[p] = [None, None]
            if left:
                tree[p][0] = c
            else:
                tree[p][1] = c
            if c in roots:
                roots.remove(c)
        root = list(roots)[0]
        return self.makeTree(tree, root)

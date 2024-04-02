"""
BST Level-Order Traversal
Day 23

-binary search trees
-


"""

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        if root is None:
            return
        #print(root)
        queue = []
        queue.append(root)
        
        while len(queue) != 0:
            p = queue.pop(0)
            print(p.data, end=' ')
            #print(p)
            if p.left is not None:
                print(p.left)
                queue.append(p.left)
            if p.right is not None:
                queue.append(p.right)
        
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

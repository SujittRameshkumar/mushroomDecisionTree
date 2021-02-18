import pandas as pd
import numpy as np

class decisionTree:
    children = []
    left = None
    right = None
    treeHeight = 0

    def __init__(self, left, right, children)

        self.children = children
        self.left = left
        self.right = right
        self.treeHeight = getHeight(self)


    def getHeight(rootNode):
        if node is None:
        return -1 ; 
 
        else :
 
            # Compute the depth of each subtree
            lDepth = maxDepth(node.left)
            rDepth = maxDepth(node.right)
    
            # Use the larger one
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    def dfs(node, targetSum):
        if not node:
            return 0
        
        # Count paths with sum == targetSum starting from the current node
        count = 1 if node.val == targetSum else 0
        count += dfs(node.left, targetSum - node.val)
        count += dfs(node.right, targetSum - node.val)
        return count

    if not root:
        return 0
    
    # Count paths starting from the root, then do the same for all nodes
    # as roots of their subtrees
    pathCount = dfs(root, targetSum)
    pathCount += pathSum(root.left, targetSum)
    pathCount += pathSum(root.right, targetSum)
    
    return pathCount

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        depth = {
            None: -1
        }
        def dfs(node, parent = None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
                
        dfs(root)
        max_depth = max(depth.values())
        
        def decide(node):
            if not node or depth[node] == max_depth:
                return node
            l, r = decide(node.left), decide(node.right)
            return node if l and r else l or r
        return decide(root)

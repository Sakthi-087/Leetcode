# Definition for a binary tree node.


class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        stack = []
        i = 0
        
        while i < len(traversal):
            level = 0
            # Calculate the depth of the current node by counting dashes
            while i < len(traversal) and traversal[i] == '-':
                level += 1
                i += 1
            
            # Read the value of the node
            value = 0
            while i < len(traversal) and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            
            # Create the new node
            node = TreeNode(value)
            
            # If the stack length is greater than the level, pop nodes to find the parent
            while len(stack) > level:
                stack.pop()
            
            # If there's a parent node in the stack, determine whether to add as left or right child
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            # Push the current node to the stack
            stack.append(node)
        
        # The first node in the stack is the root
        return stack[0]

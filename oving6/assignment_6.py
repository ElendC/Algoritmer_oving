# -*- coding: utf-8 -*-
"""Assignment#6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IfPWONRwANaTJg6-M0yj6Z-UulMXTLbw
"""

"""# Assignment #6

# Complete the given python code. There are six parts to be done!
Please follow the comments in the code
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# A utility function to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

# A utility function to insert a new node with given key in BST
def insert(node, key):           
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)
    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    # return the (unchanged) node pointer
    return node

def count_leaf_nodes(root):
    # Write Code here
    leafNodes = 0
    if root is not None: # Base case
        if root.left == None and root.right == None:
            print(f'{root.key}', end=' | ')
            return 1
        leafNodes += count_leaf_nodes(root.left)
        leafNodes += count_leaf_nodes(root.right)
    return leafNodes
    # End

    """ Let us take the following BST
          50
        / \
        30  70
        / \ / \
      20 40 60 80

      Then it is expected to print 4 by calling the function
    """

def preorder(root):
    nodeList = []
    if root is not None:
        print(root.key)
        preorder(root.left)
        preorder(root.right)

    """ Let us take following BST
          50
        / \
        30  70
        / \ / \
      20 40 60 80

      Then it is expected to print 50,30,20,40,70,60,80 by calling the function
    """
    # write your code here
    # end

def print_nodes_with_two_child(root):
    """ Let us take following BST
          50
        / \
        30  70
        / \ / \
      20 40 60 80

      Then it is expected to print 50,30,70 by calling the function
    """
    # write your code here

    if root is not None:
        if root.left and root.right:
            print(root.key)
        print_nodes_with_two_child(root.left)
        print_nodes_with_two_child(root.right)

    # end

def print_nodes_bylevel(root):
    """ Let us take following BST
          50
        / \
        30  70
        / \ / \
      20 40 60 80

      Then it is expected to print 50,30,70,20,40,60,80 by calling the function
    """
    # write your code here
    queue = [root]

    while queue:
        currentRoot = queue.pop(0)
        print(currentRoot.key)

        if currentRoot.left:
            queue.append(currentRoot.left)
        if currentRoot.right:
            queue.append(currentRoot.right)

    # end

def tree_height(root):
    # write your code here
    if root is None:
        return 0
    else:
        left_height = tree_height(root.left)
        right_height = tree_height(root.right)
        return max(left_height, right_height) + 1
    # end

# Driver Code
if __name__ == '__main__':
    
    # Q1:
    root = None
    # insert all nodes in the given order by calling insert function
    nodes = [50,30,20,40,70,60,80,71,25,85]

    for i in nodes:
        root = insert(root, i)



    # Q2:
    print(f"\n tree_height: {tree_height(root)-1}")

    # Q3:
    print('\n Leaf Nodes: ')
    print(f"\n Number of leaf nodes: {count_leaf_nodes(root)} ")

    # Q4:
    print(f"\n print nodes in level order: ")
    print_nodes_bylevel(root)
    # Q5:
    print(f"\n preorder traversal of tree:")
    preorder(root)
    # Q6:
    print("\n print_nodes_with_two_child:")
    print_nodes_with_two_child(root)

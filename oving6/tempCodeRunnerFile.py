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
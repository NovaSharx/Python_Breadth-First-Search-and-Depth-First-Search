from collections import deque
import math


def max_levels(array):
    # Transposed '(2 ** n) - 1'
    levels = int(int((math.log(len(array) + 1) / math.log(2))))
    return (levels)


class Node:
    def __init__(self, key):
        if key == "null":
            self.data = None
        else:
            self.data = key
            self.left = None
            self.right = None


example_list = [5, 3, 8, 2, 4, None, 9]

# Create basic binary tree
root = Node(example_list[0])
root.left = Node(example_list[1])
root.right = Node(example_list[2])
root.left.left = Node(example_list[3])
root.left.right = Node(example_list[4])
# root.right.left = Node(example_list[5]) (we skip this to avoid problems)
root.right.right = Node(example_list[6])


# Breadth-first Traversal
def max_values_each_level_BFS():

    max_values_array = []

    Q = deque()  # My Queue
    V = []  # My visited list
    M = set()  # My nodes that have been visited or that are marked to be visited

    Q.append(root)

    # Continues till the loop hits the end of the binary tree (The None values of the leaf nodes)
    while len(Q) != 0:
        largest = 0

        for _ in range(len(Q)):  # Repeat for each node at current level in binary tree
            current = Q.pop()
            V.append(current)

            # Find largest in current while loop iteration (or level in binary tree)
            if current.data > largest:
                largest = current.data

            # Add child nodes in upper level of binary tree to the Queue for the next while loop iteration
            for child in [current.left, current.right]:
                if child not in M and child != None:
                    Q.appendleft(child)
                M.add(child)
        # Add largest child node to list for current level in binary tree
        max_values_array.append(largest)

    return max_values_array


# Depth-first Traversal
def recursive_print_inorder_DFS(root):

    if root:
        recursive_print_inorder_DFS(root.left)
        print(root.data)
        recursive_print_inorder_DFS(root.right)

def recursive_print_preorder_DFS(root):

    if root:
        print(root.data)
        recursive_print_preorder_DFS(root.left)
        recursive_print_preorder_DFS(root.right)

def recursive_print_postorder_DFS(root):

    if root:
        recursive_print_postorder_DFS(root.left)
        recursive_print_postorder_DFS(root.right)
        print(root.data)



print(max_values_each_level_BFS())
print("-------------------------")
recursive_print_inorder_DFS(root)
print("-------------------------")
recursive_print_preorder_DFS(root)
print("-------------------------")
recursive_print_postorder_DFS(root)

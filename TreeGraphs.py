from DataStructures import Link

# Chapter 4 - Trees and Graphs

# ================== classes =================== #

class Tree():
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

    def __str__(self):
        return str(self.val) + '{ ' + str(self.children) + '} '

class DirectedGraph():
    def __init__(self, val=None, neighbors=[]):
        self.val = val
        self.neighbors = neighbors

    def addNeighbor(self, n):
        self.neighbors.append(n)
        # n.neighbors.append(self)

    def __str__(self):
        return str(self.val) + [str(c) for c in self.children]

class BinaryTree():
    def __init__(self, val=None, leftChild=None, rightChild=None):
        self.val = val
        self.leftChild = leftChild
        self.rightChild = rightChild

    def __str__(self):
        return str(self.val) + '{ ' + str(self.children) + '} '


# 4.1 is a Binary Tree Balanced - heights differ by no more than 1
def isBalanced(t):
    """
    a node is balanced if the height of its left subtree is within 1 of
    its right subtree
    calculate the heights of the trees with -1 reserved for balanced

    """
    return getSubtreeHeight(t) > -1

def getSubtreeHeight(t):
    """
    helper for isBalanced
    -1 for not balanced, otherwise return distance
    """
    if not t:
        return 0
    left = getSubtreeHeight(t.leftChild)
    if left == -1:
        return -1
    right = getSubtreeHeight(t.rightChild)
    if right == -1:
        return -1

    # check both
    if right > left + 1 or left > right + 1:
        return -1
    return 1 + max(left, right)


# 4.2 graphPath

def existsGraphPath(start, finish):
    """
    maintain a queue for BFS
    """
    fringe = [start]
    visited = set([start])
    while fringe:
        target = fringe[0]
        fringe = fringe[1:]

        if target == finish:
            return True

        visited.add(target)

        [fringe.append(c) for c in target.neighbors if c not in visited]

    return False


# 4.3 Build BST from array
def create_minimal_BST(nums):
    """
    :param nums:
    :return Tree:

    the middle element becomes the root
    recursively add small stuff to the leftsubtree, and big to the right
    """
    if not nums:
        return None
    m = len(nums) // 2
    middle = nums[m]
    root = BinaryTree(middle)
    root.leftChild = create_minimal_BST(nums[:m])
    root.rightChild = create_minimal_BST(nums[m+1:])
    return root

# 4.4 tree to D Linked Lists at height D
def create_linked_lists(t):
    """

    :param t:
    :return Linked List of Linked Lists:
    pass the level
    """

    def helper(tree_root, list_of_lists, level):

        if not tree_root:
            return

        level_list = Link(None)

        if len(list_of_lists) >= level:
            # too big! level is not in list
            level_list = Link(None)

            # we can sign off on the previous level
            list_of_lists.append(level_list)
        else:
            level_list = list_of_lists[level]

        level_list.append(tree_root)
        helper(tree_root.leftChild, list_of_lists, level + 1)
        helper(tree_root.rightChild, list_of_lists, level + 1)

    sol = []
    helper(t, sol, 0)
    return sol

# 5.1



# ================== utils =================== #


def test(call, result=True):
    if call != result:
        print("got: " + str(call))
        raise ValueError("test failed")

# ================== tests =================== #

# 4.1 - check if a binary tree is balanced

Tree = BinaryTree
t = Tree(5, Tree(3), Tree(8))
t2 = Tree(5, Tree(3), Tree(8, Tree(4)))
t3 = Tree(5, Tree(3), Tree(8, Tree(4), Tree(7)))
t4 = Tree(5, Tree(3), Tree(8, Tree(4), Tree(7, Tree(3))))
t5 = Tree(5, Tree(3, Tree(2)))
test(isBalanced(t), True)
test(isBalanced(t2), True)
test(isBalanced(t3), True)
test(isBalanced(t4), False)
test(isBalanced(t5), False)

# 4.2 - isGraphRoute (T/F)
Graph = DirectedGraph
g = Graph(1)
a = Graph(2)
b = Graph(3)
c = Graph(4)
g.addNeighbor(b)
g.addNeighbor(c)
b.addNeighbor(c)
a.addNeighbor(b)
test(existsGraphPath(g, b), True)
test(existsGraphPath(b, g), False)
test(existsGraphPath(g, a), False)
test(existsGraphPath(a, g), False)
test(existsGraphPath(g, c), True)
d = Graph(5)
e = Graph(6)
c.addNeighbor(d)
d.addNeighbor(e)
test(existsGraphPath(g, a), False)
test(existsGraphPath(g, e), True)
test(existsGraphPath(d, e), True)
test(existsGraphPath(d, g), False)

# 4.3 - build a Binary Search Tree of minimum height from a sorted list
nums = [1, 2 ,3]
small_tree = create_minimal_BST(nums)
test(small_tree.val, 2)
test(small_tree.leftChild.val, 1)
test(small_tree.rightChild.val, 3)
nums = [1, 2 ,3, 4]
small_tree = create_minimal_BST(nums)
test(small_tree.val, 3)
test(small_tree.leftChild.val, 2)
test(small_tree.leftChild.leftChild.val, 1)
test(small_tree.rightChild.val, 4)
nums = [n+1 for n in range(7)]
small_tree = create_minimal_BST(nums)
test(small_tree.val, 4)
test(small_tree.leftChild.val, 2)
test(small_tree.leftChild.leftChild.val, 1)
test(small_tree.leftChild.rightChild.val, 3)
test(small_tree.rightChild.val, 6)
test(small_tree.rightChild.leftChild.val, 5)
test(small_tree.rightChild.rightChild.val, 7)
nums = [n+1 for n in range(64)]
large_tree = create_minimal_BST(nums)
test(large_tree.val, 33)
test(large_tree.rightChild.val, 49)
test(large_tree.leftChild.val, 17)

# 4.4 - convert a binary tree to a set of D Linked Lists with all the elements at that height
# nums = [1]
# small_tree = create_minimal_BST(nums)
# linked_lists = create_linked_lists(small_tree)
# one = Link(1)
# test(Link.compare_to(linked_lists.val, one))
# nums = [1, 2 ,3]
# small_tree = create_minimal_BST(nums)
# linked_lists = create_linked_lists(small_tree)
# one = Link(1)
# children = Link(2, Link(3))
# test(Link.compare_to(linked_lists.val, one))
# test(linked_lists.next.val, children)
# nums = [n+1 for n in range(64)]
# large_tree = create_minimal_BST(nums)
# linked_lists = create_linked_lists(large_tree)
# test(linked_lists.val.len(), 1)
# test(linked_lists.next.val.len(), 2)
# test(linked_lists.next.next.val.len(), 4)
# test(linked_lists.next.next.next.val.len(), 8)


# 5.1 - bit insertion
N = int('10000000000', 2)
M = int('10011')
i = 2
j = 6
output = int('10001001100', 2)
test(bit_insertion(N, M, i, j), output)


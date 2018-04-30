from DataStructures import Link

# Chapter 4 - Trees and Graphs

# ================== classes =================== #

class Tree():
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

    def __str__(self):
        return str(self.val) + '{' + str(self.children) + '} '

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
        return str(self.val) + ' {' + str(self.leftChild) + ' | ' + str(self.rightChild) + '} '


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
    pass the level into the helper
    because BFS, hitting new stuff means always new
    """

    def helper(tree_root, list_of_lists, level):

        if not tree_root:
            return

        level_list = Link(None)
        # level is ever too high???? then we need to add a new list
        # and we are done with everything below

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

# 4.5 is BST

def isBST(tree):
    """
    :param tree:
    :return bool:

    you must be smaller than the min of your right child's tree
    you must be larger than the max of your left child's tree

       5
     3   7
    1   4 8

    call a helper, that bubbles up a tuple with max, min
    just return False if not balanced
    overall is call helper on the root
    """

    MAX_INT = float('inf')
    MIN_INT = -MAX_INT

    def max_min_bst(t):
        """

        :param t:
        :return (min, max):
        note - its ok for the root to be equal to the leftchild
        """
        if not t:
            return (MAX_INT, MIN_INT)

        left, right = None, None
        if t.leftChild:
            # check left side
            left_call = max_min_bst(t.leftChild)
            if left_call and t.val > t.leftChild.val and t.val > left_call[1]:
                left = (left_call[0], t.val)

        if t.rightChild:
            # check the right side
            right_call = max_min_bst(t.rightChild)
            if right_call and t.val < t.rightChild.val and t.val < right_call[0]:
                right = (t.val, right_call[1])

        if t.leftChild and not t.rightChild:
            return left

        if t.rightChild and not t.leftChild:
            return right

        if not t.leftChild and not t.rightChild:
            # leaf
            sol = (t.val, t.val)
            return sol

        else:
            # both children
            if left and right and left[1] <= right[0]:
                return (left[0], right[1])
            else:
                return None

    return bool(max_min_bst(tree))

# 4.6 next node in BST
def next_node(tree):
    """
    if you have a right child - go the smallest of that
    if you you don't?
        are you a left child?
            return your parent
        ... ur the biggest return None
    :param tree:
    :return BinaryTree:
    """
    return tree



def clean_is_BST(tree):

    def is_BST(t, min_val, max_val):
        """
        :param t:
        :param min_val:
        :param max_val:
        :return if everything is between min and max val:
        """
        if not t:
            return True
        if t.val >= max_val or t.val < min_val:
            return False
        left = is_BST(t.leftChild, min_val, t.val)
        right = is_BST(t.rightChild, t.val, max_val)
        if left and right:
            return True
        return False

    return is_BST(tree, -float('inf'), float('inf'))

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
# import pdb; pdb.set_trace()
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


# 4.5 is BST
t0 = BinaryTree(1)
t1 = BinaryTree(2)
t1.rightChild = BinaryTree(1)
t1.leftChild = BinaryTree(3)
t2 = BinaryTree(2)
t2.rightChild = BinaryTree(3)
t2.leftChild = BinaryTree(1)
t3 = BinaryTree(5)
t3.rightChild = BinaryTree(7)
t3.leftChild = BinaryTree(3)
t3.rightChild.rightChild = BinaryTree(8)
t3.rightChild.leftChild = BinaryTree(6)
t3.leftChild.leftChild = BinaryTree(2)
t3.leftChild.rightChild = BinaryTree(4)
t3.leftChild.leftChild.leftChild = BinaryTree(1)
t4 = BinaryTree(2)
t4.leftChild = BinaryTree(1)
t4.leftChild.leftChild = BinaryTree(0)
t4.leftChild.leftChild.rightChild = BinaryTree(4)
test(isBST(t0))
test(isBST(t1), False)
test(isBST(t2))
test(isBST(t3))
test(isBST(t4), False)

isBST = clean_is_BST
test(isBST(t0))
test(isBST(t1), False)
test(isBST(t2))
test(isBST(t3))
test(isBST(t4), False)

# 4.6 next node in BST
node = t3.leftChild
next = next_node(node)
nextnext = next_node(next)
nextnextnext = next_node(nextnext)
nextnextnextnext = next_node(nextnextnext)
test(node.val, 3)
test(next.val, 4)
test(nextnext.val, 5)
test(nextnextnext.val, 6)
test(nextnextnextnext.val, 7)

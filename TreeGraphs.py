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





    return True



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





# given a number and a list of numbers
    # total number of times numbers in the list sum to a given number

def count_sums(nums, k):
    """
    recursively - include vs don't include members of a set
    count_helper(nums (smaller set), k (could be smaller))
        add up all the nums ... equals k? then good
    """

    def rec_count(subset, g):
        """
        subset of the numbers, and a goal
        """
        if sum(subset) == g:
            return 1
        if not subset:
            return 0
        use_first = rec_count(subset[1:], g-subset[0])
        ignore_first = rec_count(subset[1:], g)

        return use_first + ignore_first

    return rec_count(nums, k)


def count_change(amount, coins):
    """
    two groups: use all the coins with amount-biggest
                use all the coins but the biggest
    assume coins are in descending order
    """
    if amount == 0:
        return 1
    if not coins:
        return 0
    if amount < 0:
        return 0
    return count_change(amount-coins[0], coins) + count_change(amount, coins[1:])



def hired_sentence_most_words(S):
    """
    goal: find the sentence with the largest number of words
    return the number of words in that sentence
    breakdown
        break down string into words 
        scan the words for ending puncuation
            ends in . or ? create a new sentence
        count the number of words per sentence
        math
    """
    new_S = ''
    i = 0
    while i < len(S)-1:
        j = i + 1
        if S[i] == ' ' and S[j] == ' ':
            # only copy one
            new_S += (S[i])
            i += 2
        else:
            new_S += (S[i])
            i += 1
    print(new_S)
    S = new_S

    words = S.split(" ")
    sentences = []  # array of word arrays
    current_sentence = []
    for word in words:
        if word:
            last_let = word[len(word)-1]
            if last_let == '.' or last_let == '?' or last_let == '!':
                # new sentence
                word_without_last = word[:len(word)-1]
                current_sentence.append(word_without_last)
                sentences.append(current_sentence)
                current_sentence = []
            else:
                # another word to the current sentence
                current_sentence.append(word)
    
    max_count = 0
    for sentence in sentences:
        max_count = max(max_count, len(sentence))


    return max_count, sentences


def perfect_squares_in_range(A, B):
    if B < 0:
        return 0
    A = max(A, 0)
    return pos_solution(A, B)


def pos_solution(A, B):
    """
    return the number of whole squares in the interval inclusive
    can't check all the numbers
    """
    count = 0
    for i in range(int(math.sqrt(A)), int(math.sqrt(B)+1)):
        square = i*i
        if square <= B and square >= A:
            # happy
            count += 1
    return count


# recursive tree representation of segment paths

class Node:
    """
    represent a Node in the tree hierarchy schema
    """
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return str(self.data)

    def display(self, spaces=2):
        """
        recursively build a string with the node's data and its children's data
        """
        children_str = ""
        for child in self.children:
            children_str += "\n" + spaces * ' ' + child.display(spaces + 2)
        return "<" + str(self.data) + ">" + children_str 


def generate_tree(paths):
    """
    Main function taking a list of path strings, and building a tree
    Assuming all segments are identifiable by unique strings
    Start with "segment tree" as the first root node of the full structure
    """

    seen = {}  # map name to Node
    head = Node("Segment Tree")

    for path in paths:
        node = head
        segs = path.split(" > ")
        for i in range(len(segs)):
            # if its a segment seen before, append to that one rather than a new one
            if segs[i] in seen:
                child = seen[segs[i]]
            else:
                child = Node(segs[i])
                seen[segs[i]] = child
                node.add_child(child)
            node = child
    return head
    

def tester(goal, words_set, test_str):
    """
    simple testing function
    """
    if goal == (words_set == test_str):
        print("success")
    else:
        print("failure")


def test_one():
    """
    ( test from interview )

        FunStore
            Clothing
                Likes clothes so much
                A Red Shirt
                    N
                    Y

    """
    segments = ["FunStore > Clothing > Likes clothes so much",
                "FunStore > Clothing > A Red Shirt > N",
                "FunStore > Clothing > A Red Shirt > Y"]
    tree = generate_tree(segments)

    print(tree.display(2))
    tester(True, tree.children[0].data, "FunStore")
    tester(True, tree.children[0].children[0].data, "Clothing")
    tester(True, tree.children[0].children[0].children[0].data, "Likes clothes so much")
    tester(True, tree.children[0].children[0].children[1].data, "A Red Shirt")
    tester(True, tree.children[0].children[0].children[1].children[0].data, "N")
    tester(True, tree.children[0].children[0].children[1].children[1].data, "Y")


def test_two():
    """
    ( new test )
    
    A
      B
        C
          D
            E
          F
            G
        H
          I
            J
      L
        M
          N
            O
              P
    Q
      R
    """
    segments = ["A > B > C > D",
                "A > B > C > D > E",
                "A > B > C > F > G",
                "A > B > H > I > J",
                "A > L > M > N > O > P",
                "Q > R"]
    tree = generate_tree(segments)

    print(tree.display(2))
    tester(True, tree.children[0].data, "A")
    tester(True, tree.children[0].children[0].data, "B")
    tester(True, tree.children[0].children[0].children[0].data, "C")
    tester(True, tree.children[0].children[0].children[0].children[0].data, "D")
    tester(True, tree.children[0].children[0].children[0].children[0].children[0].data, "E")
    tester(True, tree.children[0].children[0].children[0].children[1].data, "F")
    tester(True, tree.children[0].children[0].children[0].children[1].children[0].data, "G")
    tester(True, tree.children[0].children[0].children[1].data, "H")
    tester(True, tree.children[0].children[0].children[1].children[0].data, "I")
    tester(True, tree.children[0].children[0].children[1].children[0].children[0].data, "J")
    tester(True, tree.children[0].children[1].data, "L")
    tester(True, tree.children[0].children[1].children[0].data, "M")
    tester(True, tree.children[0].children[1].children[0].children[0].data, "N")
    tester(True, tree.children[0].children[1].children[0].children[0].children[0].data, "O")
    tester(True, tree.children[0].children[1].children[0].children[0].children[0].children[0].data, "P")

    tester(True, tree.children[1].data, "Q")
    tester(True, tree.children[1].children[0].data, "R")


def test_three():
    """
    misc. sanity tests
    """
    segments = []
    tree = generate_tree(segments)
    print(tree.display(2))
    tester(True, tree, tree)
    tester(False, tree.data, "BAD DATA")
    tester(True, tree.children, [])


# running tests
# test_one()
# test_two()
# test_three()

def build_words(d, s):
    """
    back to original problem - return the strings
    """
    
    memo = {}  # save results
    memo[''] = False  # can't do anything with an empty string

    def helper(sub_s):
        """
        process this smaller "sub_string"
        """
        # don't recompute unless neccessary

        if sub_s in d:
            memo[sub_s] = sub_s
            
        if sub_s in memo:
            return memo[sub_s]

        # through every possible binary split - working with the first part, then everything else
        for i in range(len(sub_s)):
            first = sub_s[:i]
            last = sub_s[i:]
            if first in d:
                memo[first] = first
                processed_last = helper(last)
                if processed_last:
                    return first + ' ' + processed_last # *** this line changed - return before and then processed after
        return None

    return helper(s)



# LRU
# Example is an HTTP cache that stores <URL : page content>
#
# 1. Please first design an API for our memory cache library
# 2. What should the Big-O time complexity be for each of the key operations?
# 3. What are some real world constraints our memory cache might have?



"""

get(key):
    >>> the value associated with the key if its in the cache
    or perform the actual lookup

set(key, value):
    maybe update
    >>> the old value
    or return None, and set that key to the new value

to_string()

SIZE
"""

"""
# option 1
        queue - eviction - doubly linked
        []
        
        
# option 2
        dictionary - 
        del
"""


class Node:
    
    def __init__(self, data, next_node, previous_node, key):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node
        self.key = key
    
    def __repr__(self):
        return str(self.data) + str(self.next_node)
    
    def __str__(self):
        return repr(self)
    

class Cache:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.length = 0
        self.map = {}
    
    def cache_set(self, key, value):
        # update the value
        
        if key in self.map:
            
            if self.head == self.map[key]:
                self.head = self.map[key].next_node
            
            self.map[key].data = value
            
            # pulls the target node out of the strcture
            
            after_target = self.map[key].next_node
            previous_target = self.map[key].previous_node
            if after_target:
                after_target.previous_node = previous_target
            if previous_target:
                previous_target.next_node = after_target
            
            old_tail = self.tail
            self.tail = self.map[key]
            self.map[key].previous_node = old_tail
            self.map[key].next_node = None
        
        else:
            
            if self.length >= self.capacity:
                # eviction
                del self.map[self.head.key] 
                self.head = self.head.next_node
                self.head.next_node.previous_node = None
                self.length -= 1
                
            new_node = Node(value, None, self.tail)
            self.map[key] = new_node
            self.tail = new_node
            if not self.head:
                self.head = new_node
            self.length += 1
            
            
                
                
        return value
            
    def __str__(self):
        return str(self.map)
    
        
def test_one():
    cache = Cache(10)
    print(cache)



"""
Roads and Bridges
"""
# variables here
n = 3
road_tups = [(0, 1), (0, 2), (1, 2)]
SIZE = n + len(road_tups)

class City:
    def __init__(self, num, neighbors):
        self.num = num
        self.neighbors = {}
        for neigh in neighbors:
            self.neighbors[neigh] = False  # no bridge to them
        self.library = False

    def append_neighbor(self, neighbor):
        if not neighbor in self.neighbors:
            self.neighbors[neighbor] = False

    def __str__(self):
        return "City " + str(self.num)

    def __repr__(self):
        return str(self) 
        

def has_library(city, seen):
    if city in seen:
        return False # we already tried this
    if city.library:
        return True

    to_search = []  # list of cities we need to check

    neighs = list(city.neighbors.keys())
    for n in neighs:
        if city.neighbors[n]:
            # this is a built bridge! valid!
            to_search.append(n)

    success = False
    for poss in to_search:
        new_seen = seen
        new_seen[city] = True
        success = has_library(poss, new_seen)
        if success:
            break

    return success
        

def to_bin(n):
    base = "{0:b}".format(n)
    while len(base) < SIZE:
        base = '0' + base
    return base



def toggle_bridge(start, finish, val):
    # start and finish are integers - val is a bool
    cities[start].neighbors[cities[finish]] = val 
    cities[finish].neighbors[cities[start]] = val 


def generate_setup(bitstr):
    for i in range(len(bitstr)):
        if i < len(cities):
            # set a city here
            if bitstr[i] == '1':
                cities[i].library = True
            else:
                cities[i].library = False 
        else:
            # set a road here
            if bitstr[i] == '1':
                road = road_tups[i-len(cities)]
                toggle_bridge(road[0], road[1], True)
            else:
                road = road_tups[i-len(cities)]
                toggle_bridge(road[0], road[1], False)


def recap():
    print("---")
    for city in cities:
        print(str(city) + " | " + str(city.library) + " | " + str(city.neighbors))


def has_lib_test(seed_num):
    """
        seed_num is the number from 0 to 2^n 
        where n is the number of cities + number of roads
        prints the booleans
    """
    print("\nSEED " + str(seed_num) + ' // ' + str(to_bin(seed_num)))
    generate_setup(to_bin(seed_num))
    results = []
    all_true = True 
    for i in range(n):
        res = has_library(cities[i], {})
        if not res:
            all_true = False
        results.append(res)
    recap()
    print(results)
    return all_true


cities = []
for i in range(n):
    my_city = City(i, [])
    cities.append(my_city)

for road in road_tups:
    start = road[0]
    finish = road[1]
    cities[start].append_neighbor( cities[finish] )
    cities[finish].append_neighbor( cities[start] )

print(cities)

solutions = []
for i in range(2**SIZE):
    all_true = has_lib_test(i)
    if all_true:
        solutions.append(i)
import pdb; pdb.set_trace()



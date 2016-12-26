# Data Structures questions - chapters 1-4

# ================== chapter 1 =================== #

def is_all_unique_chars(s):
    """
    returns if a string has all unique characters
    """
    # build hashset
    my_dict = {}
    for c in s:
        if c in my_dict:
            return False
        my_dict[c] = True
    return True


def is_all_unique_no_space(s):
    """
    returns if a string has all unique characters without data structs
    """
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True


def is_permutation(a, b):
    """
    returns whether string a is a permutation of string b
    """
    
    # strategy 1: sort both strings then compare them traditionally
    a_list, b_list = [c for c in a], [c for c in b]
    a_list.sort()
    b_list.sort()
    return a_list == b_list


def percent_20_replacements(s):
    """
    replace all instances of a space with a %20
    """

    # build a new string
    new_str = ''
    for c in s:
        if c == ' ':
            new_str += '%20'
        else:
            new_str += c
    return new_str


def percent_20_in_place(s, n):
    """
    replace all instances of a space with a %20 in place
    n refers to the length of the string (character array)
    """
    # make one pass to calculate the final size to allocate
    # then make a second pass to fill out the array
    # tbh excuse to work with arrays

    spaces = 0 
    for c in s:
        if c == ' ':
            spaces += 1

    # for each space - we gain 2 characters

    new_len = n + 2 * spaces 
    new_str = [' ' for _ in range(new_len)]

    j = 0  # counter for new_str
    for i in range(len(s)):
        if s[i] == ' ':
            new_str[j] = '%'
            new_str[j+1] = '2'
            new_str[j+2] = '0'
            j += 3 
        else:
            new_str[j] = s[i]
            j += 1
    ret_str = ''
    for c in new_str:
        ret_str += c
    return ret_str

        
def palindrome_perm(s):
    """
    for all permutations of a string s, determine if any are a palindrome
    """
    # populate a hashset - throw out duplicates
    # if remaining is one or zero characters - true

    my_dict = {}
    for c in s:
        if c in my_dict:
            del my_dict[c]
        else:
            my_dict[c] = True

    return len(my_dict) <= 1
    


# ================== chapter 2 =================== #

class Link:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def compare_to(a, target):
        if not a and not target:
            return True
        if (a and not target) or (a and not target):
            return False
        if a.val != target.val:
            return False
        return Link.compare_to(a.next, target.next)

    def len(self):
        c = 0
        while(self):
            self = self.next
            c += 1
        return c

    def append(self, target):
        self.next = target

    def __str__(self):
        return '(' + str(self.val) + ', ' + str(self.next) + ')'

    def __repr__(self):
        return str(self)


def rdl(head):
    """
    remove duplicate link - solved recursively
    keep track of previous (start None) and curr (start head)
    if current in seen? skip it by changing prev's next
        shift over
    """
    
    seen = {}
    prev = None
    curr = head
    while curr:
        if curr.val in seen:
            prev.next = curr.next
        else:
            seen[curr.val] = True
            prev = curr
        curr = curr.next
    return head
         


        
# ================== utils =================== #


def test(call, result):
    if call != result:
        raise ValueError("test failed")


# 1.1 - unique chars
test(is_all_unique_chars("abcde"), True)
test(is_all_unique_chars("thelazydog"), True)
test(is_all_unique_chars("hello"), False)
test(is_all_unique_no_space("abcde"), True)
test(is_all_unique_no_space("thelazydog"), True)
test(is_all_unique_no_space("hello"), False)

# 1.2 - permutations
test(is_permutation("lol", "lol"), True)
test(is_permutation("abcde", "abced"), True)
test(is_permutation("lol", "lolz"), False)
test(is_permutation("123456asdfasdf", "12313asdfasdf"), False)

# 1.3 - %20 replacements
test(percent_20_replacements("hello world test"), 
        "hello%20world%20test")
test(percent_20_in_place("hello world test", 16), 
        "hello%20world%20test")

# 1.4 - palindrome perm
test(palindrome_perm("tactcoa"), True)
test(palindrome_perm("lool"), True)
test(palindrome_perm("o"), True)
test(palindrome_perm("oo"), True)
test(palindrome_perm("abc"), False)
test(palindrome_perm("abbb"), False)

# 2.1 - remove duplicates from a linked list
empty = Link()
one = Link(1)
one_two = Link(1, Link(2))
one_one = Link(1, Link(1))
two_one = Link(2, Link(1))
one_one_one_one = Link(1, Link(1, one_one))
two_two_one_one = Link(2, Link(2, one_one))
test(Link.compare_to(one_one, Link(1, Link(1))), True)
test(Link.compare_to(rdl(one_two), rdl(one)), False)
test(Link.compare_to(rdl(one_two), rdl(one_two)), True)
test(Link.compare_to(rdl(one_two), rdl(one_one)), False)
test(Link.compare_to(rdl(one_one_one_one), one), True)
test(Link.compare_to(rdl(two_two_one_one), two_one), True)




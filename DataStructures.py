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


def one_away(a, b):
    """
    three options - insert, remove or replace
    """

    def replace_check(s1, s2):
        """
        check if replacing a single character in s1 becomes s2
        """
        if len(s1) != len(s2):
            return False
        found_diff = False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if found_diff:
                    return False
                found_diff = True
        return True

    
    def insert_check(s1, s2):
        """
        inserting a char into s1 becomes s2
        """
        m = len(s1)
        n = len(s2)
        if m + 1 != n:
            return False
        i, j = 0, 0
        inserted = False
        while i < m and j < n:
            if s1[i] != s2[j]:
                if inserted:
                    return False
                inserted = True
                j += 1
            i += 1
            j += 1
        return True

    m = len(a)
    n = len(b)
    if m == n:
        return replace_check(a, b)
    if m > n:
        return insert_check(b, a)
    return insert_check(a, b)


        




    


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
         
def kth_to_first(head, k):
    """
    alt helper...
    """
    if k == 0:
        return head
    else:
        return kth_to_first(head.next, k - 1)

def kth_to_last(head, k):
    """
    assumptions:
    1) k <= len of the list 
    2) k = 1 is the last element
    """
    list_len = head.len()
    while k < list_len:
        head = head.next
        k += 1
    return head

# make a ruler of length k (gap between two nodes)
# then slide both down till the end lol

def remove_mid_link(target):
    """
    take the target node, and make it grab its next's info
    """

    if not target or not target.next:
        # can't be at the end
        return False
    next = target.next
    target.val = next.val
    target.next = next.next

def partition_ll(head, target):
    """
    build a before list and an after list
    """
    val = target.val
    all_vals = []
    n = head
    while (n):
        all_vals.append(n.val)
        n = n.next
    all_vals.sort()
    if all_vals:
        new_head = Link(all_vals[0])
        new_tail = new_head
    for v in all_vals[1:]:
        new_tail.next = Link(v)
        new_tail = new_tail.next
    return new_head 

    
def sum_ll(a, b):
    """
    turn a linked list into a number, then conventionally add them
    """
    def link_to_num(link):
        """
        Link(7, Link(1, Link(6))) becomes 617
        """
        val = 0
        place = 1
        while link:
            val += (link.val * place)
            place *= 10
            link = link.next
        return val 

    def num_to_link(num):
        """
        617 becomes Link(7, Link(1, Link(6))) 
        gets the ones, then get the tens etc...
        """
        
        link = Link(num % 10)
        head = link
        while num >= 10:
            num = num // 10
            link.next = Link(num % 10)
            link = link.next
        return head 

    return num_to_link(link_to_num(a) + link_to_num(b)) 
        






        
# ================== utils =================== #


def test(call, result=True):
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

oa = one_away
# 1.5 - one away
test(oa("pale", "ple"))
test(oa("pales", "pale"))
test(oa("pale", "bale"))
test(oa("pale","bake"), False)

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

# 2.2 - return kth to last element from a linked list
one_one = Link(1, Link(1))
two_two_one_one = Link(2, Link(2, one_one))
ktl = kth_to_last 
test(Link.compare_to(ktl(two_two_one_one, 1), Link(1)), True)
test(Link.compare_to(ktl(two_two_one_one, 1), Link(2)), False)
test(Link.compare_to(ktl(two_two_one_one, 2), one_one), True)
test(Link.compare_to(ktl(two_two_one_one, 2), one_one_one_one), False)
test(Link.compare_to(ktl(two_two_one_one, 4), two_two_one_one), True)

# 2.3 - delete a middle mode from a linked list
the_list = Link(1, Link(2, Link(3)))
mid = the_list.next
ends = Link(1, Link(3))
second_list = Link(1, Link(2, Link(3, Link(4))))
second_mid = second_list.next
rest = Link(1, Link(3, Link(4)))
rml = remove_mid_link
rml(mid)
test(Link.compare_to(the_list, ends))
rml(second_mid)
test(Link.compare_to(second_list, rest))

# 2.4 partition a linked list around x

in_l =  Link(3, Link(5, Link(8, Link(5, Link(10, Link(2, Link(1)))))))
out_l = Link(1, Link(2, Link(3, Link(5, Link(5, Link(8, Link(10)))))))
test(Link.compare_to(partition_ll(in_l, in_l.next), out_l)) 

# 2.5 sum linked list representations of numbers
six_one_seven = Link(7, Link(1, Link(6)))
two_nine_five = Link(5, Link(9, Link(2)))
nine_one_two = Link(2, Link(1, Link(9)))
test(Link.compare_to(sum_ll(six_one_seven, two_nine_five), nine_one_two))



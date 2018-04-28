# 5.1 - bit insertion with masks
def bit_insertion(N, M, i, j):
    """
    :param N:
    :param M:
    :param i:
    :param j:
    :return integer:


    11 with 5 on M 2
    10000010000
    10011
    insert at index 2
    10000010000
        10011
    build right mask, and left mask
    1s on the left ... and 1s on the right
    11110000011
    and the mask, then or with the shifted small
    """
    all_ones = 0xffffffff
    right_mask = (1 << i) - 1
    left_mask = all_ones << (j + 1)
    mask = right_mask | left_mask
    clean_n = N & mask
    sol = clean_n | (M << i)
    return bin(sol)

# 5.2 - print the binary representation of a double
def bin_rep(double):
    """

    :param double:
    :return bin:
    build a string ... then convert
    double the number ... is >= 0.5

    0.125
    ... double it to .25 -- small? so no 0.5s - append 0
    0.25
    ... small so no 0.25s - append 0
    0.5
    ... yes so subtract 0.5 and continue

    break when double == 0
    keep a counter - counter gets too high return impossible
    """
    ctr = 0
    sol = ""
    EPSILON = 0.0001
    while ctr < 32:
        if double <= EPSILON:
            return sol
        if double >= 0.5:
            double -= 0.5
            sol += str(1)
        else:
            sol += str(0)
        double *= 2
        ctr += 1
    return sol + "ERROR"

# 5.3 same number of bits
def next_largest(n):
    """

    :param n (integer):
    :return bin:

    11010101
    11010110

    find 01 and swap it with 10

    10000000000000
    append a 0 to the beginning
    then
    100000000000000
    """
    if n <= 0:
        return 0

    bin_form = bin(n)
    bin_form = bin_form[0] + bin_form[2:]
    for j in range(1, len(bin_form)):
        i = len(bin_form) - j
        if bin_form[i] == '1' and bin_form[i - 1] == '0':
            # we found a 01
            bin_form = bin_form[:i - 1] + '10' + bin_form[i + 1:]
            break
    return int(bin_form, 2)

def next_smallest(n):
    if n <= 1:
        return 0

    bin_form = bin(n)
    bin_form = bin_form[0] + bin_form[2:]
    for j in range(1, len(bin_form)):
        i = len(bin_form) - j
        if bin_form[i] == '0' and bin_form[i - 1] == '1':
            # we found a 01
            bin_form = bin_form[:i - 1] + '01' + bin_form[i + 1:]
            break
    return int(bin_form, 2)

# 5.4 explain this number
# n & (n - 1) == 0 - power of 2

# 5.5 number of bis to convert a number into another
def num_bits_to_convert(x, y):
    count = 0
    while x > 0 or y > 0:
        x_one = x % 2
        y_one = y % 2
        if x_one != y_one:
            count += 1
        x = x // 2
        y = y // 2
    return count

# 5.6 - swap even and odd bits
def swap_even_odd(x):
    """

    all  = XXXXXXXX
    odd  = X.X.X.X.
    even = .X.X.X.X

    shift odd to the right
    shift even to the left




    :param x:
    :return:
    """

    odd = 0xAAAA & x
    even = 0x5555 & x
    return (odd >> 1) | (even << 1)

# 5.7 - find missing number
"""
even odd cases
0000
0001
0010
----
0100
0101
0110
0111
====
0433
last bit - more zeros than ones and should be balanced ... 1
remove bits that aren't relevant
    
next bit - more zeros than ones and should be balanced
Observation
equal or less 0s? add a 0
only add a 1 when more 0s than ones
"""
def find_missing(bin_nums):

    n = len(bin_nums) + 1
    k = len(bin_nums[-1])

    # everything is the same length now
    bin_strs = []
    for num in bin_nums:
        s = '0' * (k - len(num)) + num[2:]
        bin_strs.append(s)

    def find_missing_helper(sub_set, col):

        if col < 0:
            return ''

        zero_ending, one_ending = [], []

        for num in sub_set:
            if num[col] == '1':
                one_ending.append(num)
            else:
                zero_ending.append(num)

        s = None
        if len(zero_ending) <= len(one_ending):
            # we removed a zero
            s = find_missing_helper(zero_ending, col - 1) + '0'
        else:
            # we removed a one
            s = find_missing_helper(one_ending, col - 1) + '1'

        return s


    return int(find_missing_helper(bin_strs, k - 3), 2)

#5.8 Draw a horizontal line across screen
class Screen():

    # draw horizontal line
    def __init__(self, arr, width):
        """
        width in bytes
        """
        self.arr = arr
        self.width = width // 8 # in bytes

    def __str__(self):
        full_s = ''
        for i in range(len(self.arr) // self.width):
            s = ''
            for j in range(self.width):
                val = bin(self.arr[(self.width * i) + j])[2:]
                s += '0' * (8 - len(val)) + val + '  '
            full_s += s + '\n'

        return full_s
    """
    
    16 bytes
    width 16 bits
    00000000 00000000
    
    """



    def draw_horizontal_line(self, x1, x2, y):
        row_bit_width = self.width
        start = self.width * 8 * y
        i = start + x1
        print(i)
        while i < start + x2 + 1:
            curr = self.arr[i // 8]

            mask = '0' * (i % 8) + '1' + '0' * (7 - i % 8)
            self.arr[i // 8] = int(mask, 2) | self.arr[i // 8]

            print(x1, x2, y, i)
            print(self.arr)
            i += 1









# ================== utils =================== #


def test(call, result=True):
    if call != result:
        print("got: " + str(call))
        print("expected: " + str(result))
        raise ValueError("test failed")

# ================== tests =================== #

# 5.1 - bit insertion
N = int('10000000000', 2)
M = int('10011', 2)
i = 2
j = 6
output = bin(int('10001001100', 2))
test(bit_insertion(N, M, i, j), output)

# 5.2 - binary representation of double
test(bin_rep(0.5), "1")
test(bin_rep(0.125), "001")
test(bin_rep(0.25), "01")
test(bin_rep(0.75), "11")
test(bin_rep(0.875), "111")
test(bin_rep(0.875001), "111")
# test(bin_rep(0.875000000000000000000001), "ERROR")

# 5.3 -
test(next_largest(1), 2)
test(next_largest(4), 8)
test(next_largest(5), 6)
test(next_largest(7), 11)
test(next_largest(17), 18)

# 5.3 -
test(next_smallest(2), 1)
test(next_smallest(8), 4)
test(next_smallest(6), 5)
test(next_smallest(11), 7)
test(next_smallest(18), 17)

# 5.5
test(num_bits_to_convert(1, 0), 1)
test(num_bits_to_convert(5, 0), 2)
test(num_bits_to_convert(4, 0), 1)
test(num_bits_to_convert(7, 0), 3)
test(num_bits_to_convert(7, 4), 2)
test(num_bits_to_convert(7, 1), 2)
test(num_bits_to_convert(16, 1), 2)
test(num_bits_to_convert(274, 274), 0)
test(num_bits_to_convert(0, 0), 0)

# 5.6
test(swap_even_odd(3), 3)
test(swap_even_odd(1), 2)
test(swap_even_odd(2), 1)
test(swap_even_odd(8), 4)
test(swap_even_odd(4), 8)
test(swap_even_odd(7), 11)
test(swap_even_odd(9), 6)
test(swap_even_odd(6), 9)

# 5.7
nums = [0]
bin_nums = [bin(n) for n in nums]
test(find_missing(bin_nums), 1)
nums = [1]
bin_nums = [bin(n) for n in nums]
test(find_missing(bin_nums), 0)
nums = [1, 2, 3, 4, 5, 6]
bin_nums = [bin(n) for n in nums]
test(find_missing(bin_nums), 0)
nums = [0, 1, 2, 3, 5, 6]
bin_nums = [bin(n) for n in nums]
test(find_missing(bin_nums), 4)

# 5.8
arr = [0x00 for _ in range(16)]
width = 16
screen = Screen(arr, width) #  8 rows of 16 pixels
print(str(screen))
screen.draw_horizontal_line(1, 6, 1)
screen.draw_horizontal_line(3, 15, 4)
screen.draw_horizontal_line(1, 3, 5)
print(str(screen))



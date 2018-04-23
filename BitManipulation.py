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

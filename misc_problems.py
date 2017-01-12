

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


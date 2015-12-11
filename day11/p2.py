#!/usr/bin/env python

import timeit

def s2n(password):
    return [ord(x) for x in password]

def n2s(nums):
    return ''.join([chr(x) for x in nums])

def increment(nums):
    """
    >>> n2s(increment(s2n("xx")))
    'xy'
    >>> n2s(increment(s2n("xy")))
    'xz'
    >>> n2s(increment(s2n("xz")))
    'ya'
    >>> n2s(increment(s2n("ya")))
    'yb'
    """
    pos = len(nums)-1
    while True:
        nums[pos] = nums[pos] + 1
        if nums[pos] > ord('z'):
            nums[pos] = ord('a')
            pos = pos - 1
        else:
            break
    return nums

def increment_past_bad_letters(nums):
    """
    >>> n2s(increment_past_bad_letters(s2n('ghijklmn')))
    'ghjaaaaa'
    >>> n2s(increment_past_bad_letters(s2n('xx')))
    'xy'
    >>> n2s(increment_past_bad_letters(s2n('xz')))
    'ya'
    """
    fb = False
    for bc in [ord('i'), ord('o'), ord('l')]:
        if bc in nums:
            fb = True
            i = nums.index(bc)
            for p in range(i+1, len(nums)):
                nums[p] = ord('a')
            nums[i] = nums[i]+1
    if not fb:
        pos = len(nums)-1
        while True:
            nums[pos] = nums[pos] + 1
            if nums[pos] > ord('z'):
                nums[pos] = ord('a')
                pos = pos - 1
            else:
                break
    return nums

def has_increasing_straight(nums):
    """
    >>> has_increasing_straight(s2n("abc"))
    True
    >>> has_increasing_straight(s2n("xyz"))
    True
    >>> has_increasing_straight(s2n("abd"))
    False
    """
    for p in range(0, len(nums)-2):
        if nums[p] == nums[p+1]-1 and nums[p+1] == nums[p+2] - 1:
            return True
    return False

def has_no_bad_letters(nums):
    """
    >>> has_no_bad_letters(s2n("abcdefg"))
    True
    >>> has_no_bad_letters(s2n("nope"))
    False
    """
    for bc in [ord('i'), ord('o'), ord('l')]:
        if bc in nums:
            return False
    return True

def has_two_pair(nums):
    """
    >>> has_two_pair(s2n("aabcd"))
    False
    >>> has_two_pair(s2n("aabcdd"))
    True
    >>> has_two_pair(s2n("aaabcd"))
    False
    """
    count = 0
    p = 1
    while p < len(nums):
        if nums[p] == nums[p-1]:
            count = count + 1
            p = p + 1
        p = p + 1
        if count >= 2:
            return True
    return False

def is_good_password(nums):
    """
    >>> is_good_password(s2n("hijklmmn"))
    False
    >>> is_good_password(s2n("abbceffg"))
    False
    >>> is_good_password(s2n("abbcegjk"))
    False
    """
    return has_no_bad_letters(nums) and has_increasing_straight(nums) and has_two_pair(nums)

def find_next_password(password):
    """
    >>> find_next_password("abcdefgh")
    'abcdffaa'
    >>> find_next_password("ghijklmn")
    'ghjaabcc'
    """
    nums = s2n(password)
    while True:
        #nums = increment_past_bad_letters(nums)
        nums = increment(nums)
        if is_good_password(nums):
            break
    return n2s(nums)

def main2():
    npw = find_next_password('hepxcrrq')
    print npw
    npw = find_next_password(npw)
    print npw

def main():
    print 'Hello'
    time = timeit.timeit(main2, number=1)
    print "Elapsed time", time

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()


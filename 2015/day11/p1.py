#!/usr/bin/env python

import timeit

def increment(password):
    """
    >>> increment("xx")
    'xy'
    >>> increment("xy")
    'xz'
    >>> increment("xz")
    'ya'
    >>> increment("ya")
    'yb'
    """
    nums = [ord(x) for x in password]
    pos = len(nums)-1
    while True:
        nums[pos] = nums[pos] + 1
        if nums[pos] > ord('z'):
            nums[pos] = ord('a')
            pos = pos - 1
        else:
            break
    return ''.join([chr(x) for x in nums])

def increment_past_bad_letters(password):
    """
    >>> increment_past_bad_letters('ghijklmn')
    'ghjaaaaa'
    >>> increment_past_bad_letters('xx')
    'xy'
    >>> increment_past_bad_letters('xz')
    'ya'
    """
    nums = [ord(x) for x in password]
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
    return ''.join([chr(x) for x in nums])

def has_increasing_straight(password):
    """
    >>> has_increasing_straight("abc")
    True
    >>> has_increasing_straight("xyz")
    True
    >>> has_increasing_straight("abd")
    False
    """
    for p in range(0, len(password)-2):
        if ord(password[p]) == ord(password[p+1])-1 and ord(password[p+1]) == ord(password[p+2]) - 1:
            return True
    return False

def has_no_bad_letters(password):
    """
    >>> has_no_bad_letters("abcdefg")
    True
    >>> has_no_bad_letters("nope")
    False
    """
    c1 = password.count('i')
    c2 = password.count('o')
    c3 = password.count('l')
    return (c1+c2+c3) == 0

def has_two_pair(password):
    """
    >>> has_two_pair("aabcd")
    False
    >>> has_two_pair("aabcdd")
    True
    >>> has_two_pair("aaabcd")
    False
    """
    count = 0
    for c in range(ord('a'), ord('z')+1):
        pair = chr(c)+chr(c)
        count = count + password.count(pair)
        if count >= 2:
            return True
    return False

def is_good_password(password):
    """
    >>> is_good_password("hijklmmn")
    False
    >>> is_good_password("abbceffg")
    False
    >>> is_good_password("abbcegjk")
    False
    """
    return has_no_bad_letters(password) and has_increasing_straight(password) and has_two_pair(password)

def find_next_password(password):
    """
    >>> find_next_password("abcdefgh")
    'abcdffaa'
    >>> find_next_password("ghijklmn")
    'ghjaabcc'
    """
    while True:
        #password = increment_past_bad_letters(password)
        password = increment(password)
        if is_good_password(password):
            break
    return password

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


def is_vowel(c):
    return c == 'a' or c == 'i' or c == 'e' or c == 'o' or c == 'u'


def max_vowels(s, k):
    count = 0
    start = 0
    max_count = 0
    for end in range(len(s)):
        if is_vowel(s[end]):
            count += 1
        if end >= k:
            if is_vowel(s[start]):
                count -= 1
            start += 1
        max_count = max(max_count, count)
    return max_count


class Solution:
    pass


s1 = "abciiidef"
k1 = 3
print(max_vowels(s1, k1))


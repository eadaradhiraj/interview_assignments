#An anagram is a sequence of numbers that can be formed by rearranging the digits of a string.
#Given a string that consists of only digits,
#modify the first half of the string so that it is an anagram of the second half.
#Determine the minimum number of operations needed to complete the task.


from collections import Counter


def solution(s):
    l = len(s)
    if l % 2 != 0:
        return 0
    l2 = l // 2
    return sum((Counter(s[:l2]) - Counter(s[l2:])).values())


print(solution("122123"))
print(solution("123456"))
print(solution("0003187671"))

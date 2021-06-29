class Solution:
    """
    @param friends: people's friends
    @param user: the user's id
    @return: the person who most likely to know
    """

    def recommendFriends(self, friends, user):
        # Write your code here
        friend = set(friends[user])
        m = 0
        result = 0 if user != 0 else 1
        for i in range(len(friends)):
            if i != user and i not in friend:
                length = len(friend & set(friends[i]))
                if length > m:
                    m = length
                    result = i
        return result


s = Solution()
a = [[1, 2, 3], [0, 4], [0, 4], [0, 4], [1, 2, 3]]
b = 0
print(s.recommendFriends(a, b))


class Solution:
    """
    @param A:
    @return: nothing
    """

    def playGames(self, A):
        # Write your code here
        result = 0
        length = len(A)
        while set(A) != {0}:
            A.sort()
            for i in range(1, length):
                A[i] -= 1
                result += 1
        return result


s = Solution()
print(s.playGames([4, 5]))

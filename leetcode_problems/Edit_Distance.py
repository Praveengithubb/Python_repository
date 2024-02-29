class EditDistance:
    def min_distance(self, word1, word2):
        dp = [[-1] * len(word2) for _ in range(len(word1))]
        return self.min_distance_recursive(0, 0, word1, word2, dp)

    def min_distance_recursive(self, ind1, ind2, word1, word2, dp):
        if ind1 > len(word1) - 1:
            return len(word2) - ind2

        if ind2 > len(word2) - 1:
            return len(word1) - ind1

        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        if word1[ind1] == word2[ind2]:
            dp[ind1][ind2] = self.min_distance_recursive(ind1 + 1, ind2 + 1, word1, word2, dp)
        else:
            a = 1 + self.min_distance_recursive(ind1 + 1, ind2, word1, word2, dp)
            b = 1 + self.min_distance_recursive(ind1 + 1, ind2 + 1, word1, word2, dp)
            c = 1 + self.min_distance_recursive(ind1, ind2 + 1, word1, word2, dp)
            dp[ind1][ind2] = min(a, b, c)

        return dp[ind1][ind2]


edit_distance = EditDistance()
print(edit_distance.min_distance("horse", "ros"))

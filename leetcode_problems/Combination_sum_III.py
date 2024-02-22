class CombinationSumIII:
    @staticmethod
    def combinationSum3(k, n):
        combinations = []
        CombinationSumIII.backtracking(combinations, [], k, n, 1)
        return combinations

    @staticmethod
    def backtracking(result, current, k, n, start):
        if len(current) == k and n == 0:
            result.append(list(current))
            return
        for i in range(start, 10):
            current.append(i)
            CombinationSumIII.backtracking(result, current, k, n - i, i + 1)
            current.pop()


if __name__ == "__main__":
    k = 3
    n = 7
    print(CombinationSumIII.combinationSum3(k, n))

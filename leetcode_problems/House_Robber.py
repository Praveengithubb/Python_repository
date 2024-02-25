class HouseRobber:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_money = [0] * len(nums)
        max_money[0] = nums[0]
        max_money[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            max_money[i] = max(nums[i] + max_money[i - 2], max_money[i - 1])
        return max_money[-1]


h = HouseRobber()
numss = [1, 2, 3, 1]
print(h.rob(numss))

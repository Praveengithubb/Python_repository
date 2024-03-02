class SingleNumber:
    def singleNumber(self, nums):
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        return ans


s = SingleNumber()
nums = [2, 2, 1]
print(s.singleNumber(nums))

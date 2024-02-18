class PeakElement:
    def findPeakElement(self, arr):
        i = 0
        j = len(arr) - 1
        index = 0
        while i < j:
            if arr[i] < arr[j]:
                index = j
                i += 1
            elif arr[i] > arr[j]:
                index = i
                j -= 1
            else:
                i += 1
        return index


p = PeakElement()
nums = [1]
p.findPeakElement(nums)

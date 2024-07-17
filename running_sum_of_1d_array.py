class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numer = nums[0]
        newnums = [numer]
        nums.pop(0)
        
        for number in nums:
            numer += number
            newnums.append(numer)

        return newnums

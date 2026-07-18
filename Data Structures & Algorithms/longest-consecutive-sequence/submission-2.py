class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0
        for num in nums_set:
            count=0
            l=num
            if l-1 not in nums_set:
                while(l in nums_set):
                    count+=1
                    l+=1
                if(max_count<count):
                    max_count=count
        return max_count
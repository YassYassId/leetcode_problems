class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        consecutive_dict = defaultdict(list)
        max_count = 0
        for num in nums_set:
            count=0
            l=num-1
            while(l in nums_set):
                count+=1
                l-=1
            if(max_count<count+1):
                max_count=count+1
        return max_count
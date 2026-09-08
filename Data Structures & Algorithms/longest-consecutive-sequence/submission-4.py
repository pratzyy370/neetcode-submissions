class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setss=set()
        for val in nums:
            if val in setss:
                continue
            setss.add(val)
        longest=0
        for val in setss:
            if val-1 not in setss:
                count=1
                while val + count in setss:
                    count += 1

                longest = max(longest, count)

        return longest


        
        
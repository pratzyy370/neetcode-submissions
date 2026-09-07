class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dixtt={}
        for val in nums:
            if val in dixtt:
                dixtt[val]+=1
            else:
                dixtt[val]=1
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, val in dixtt.items():
            buckets[val].append(key)

        # Step 3: Take elements from highest frequency
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

        

        
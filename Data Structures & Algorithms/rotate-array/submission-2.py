class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums1 = nums[-k:]
        nums2 = nums[:-k]

        nums[:] = nums1 + nums2


            





            












        
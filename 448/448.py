class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        not_nums = set()
        nums_set = set(nums)
        
        for i, num in enumerate(nums):
            print(i + 1)
            not_nums.add(i + 1)
                
        return not_nums - nums_set
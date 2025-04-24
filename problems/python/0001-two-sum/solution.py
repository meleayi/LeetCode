class Solution:
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

# Test case (optional)
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
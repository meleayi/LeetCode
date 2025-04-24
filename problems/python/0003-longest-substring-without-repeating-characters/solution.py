class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # To store characters in the current window
        left = 0  # Left pointer of the sliding window
        max_length = 0  # To track the maximum length of substring
        
        for right in range(len(s)):
            # While the current character is in the set, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add the current character to the set
            char_set.add(s[right])
            # Update max_length if the current window is larger
            max_length = max(max_length, right - left + 1)
        
        return max_length

# Test the solution
def main():
    solution = Solution()
    s = "abcabcbb"
    result = solution.lengthOfLongestSubstring(s)
    print(f"Test 1: Input = {s}, Output = {result}")  # Expected: 3
    
    s = "bbbbb"
    result = solution.lengthOfLongestSubstring(s)
    print(f"Test 2: Input = {s}, Output = {result}")  # Expected: 1
    
    s = "pwwkew"
    result = solution.lengthOfLongestSubstring(s)
    print(f"Test 3: Input = {s}, Output = {result}")  # Expected: 3
    
    s = ""
    result = solution.lengthOfLongestSubstring(s)
    print(f"Test 4: Input = {s}, Output = {result}")  # Expected: 0
    
    # Test case 5: s = "dvdf" -> 3
    s = "dvdf"
    result = solution.lengthOfLongestSubstring(s)
    print(f"Test 5: Input = {s}, Output = {result}")  # Expected: 3

if __name__ == "__main__":
    main()
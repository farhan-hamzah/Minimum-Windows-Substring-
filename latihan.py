from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        # Initialize frequency maps
        target_counts = defaultdict(int)
        window_counts = defaultdict(int)
        
        for char in t:
            target_counts[char] += 1
        
        required = len(target_counts)  # Number of unique characters in t
        formed = 0                    # Number of unique characters matched
        
        # Sliding window pointers
        left = 0
        min_len = float('inf')
        result = ""
        
        for right in range(len(s)):
            char = s[right]
            window_counts[char] += 1
            
            # Check if current character completes a requirement
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1
            
            # Try to contract the window from the left
            while formed == required and left <= right:
                # Update minimum window
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    result = s[left:right+1]
                
                # Move left pointer forward
                left_char = s[left]
                window_counts[left_char] -= 1
                
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    formed -= 1
                
                left += 1
        
        return result
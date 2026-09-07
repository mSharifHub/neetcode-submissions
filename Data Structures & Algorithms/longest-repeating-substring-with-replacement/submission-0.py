class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        result = 0

        left = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            size_window = (right - left) + 1

            most_frequent = max(count.values())

            if size_window - most_frequent > k:
                count[s[left]] -= 1

                left += 1


            result = max(result, (right - left) + 1)

        return result
        
        
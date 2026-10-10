
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []

        if len(p) > len(s):
            return result

        p_count = {}
        window_count = {}

        # Count characters in p
        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1

        k = len(p)

        # Build the first window
        for i in range(k):
            window_count[s[i]] = window_count.get(s[i], 0) + 1

        # Check the first window
        if window_count == p_count:
            result.append(0)

        # Slide the window
        for right in range(k, len(s)):
            new_char = s[right]
            old_char = s[right - k]

            # Add the new character
            window_count[new_char] = window_count.get(new_char, 0) + 1

            # Remove the outgoing character
            window_count[old_char] -= 1

            if window_count[old_char] == 0:
                del window_count[old_char]

            # Compare frequencies
            if window_count == p_count:
                result.append(right - k + 1)

        return result

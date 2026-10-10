class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'

        mx = cnt = 0
        n = len(s)

        for i in range(n):
            if i >= k and s[i-k] in vowels:
                cnt -= 1
            if s[i] in vowels:
                cnt += 1
            mx = max(mx,cnt)

        return mx
        

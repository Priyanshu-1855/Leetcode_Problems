class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0)+1

        result = sorted(freq,key = freq.get,reverse =True)

        return result[:k]
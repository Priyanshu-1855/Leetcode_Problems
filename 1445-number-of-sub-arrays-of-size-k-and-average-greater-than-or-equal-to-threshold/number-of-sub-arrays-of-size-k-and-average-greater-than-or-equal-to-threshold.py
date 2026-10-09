class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[:k])
        count = 0

        for i in range(k,len(arr)):
            window_avg = window_sum / k
            if (window_avg >= threshold):
                count += 1

            window_sum += arr[i] - arr[i-k]


        if (window_sum / k) >= threshold:               # for last value , window_sum
            count += 1

            
        return count

class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        result = 0
        cur_sum = sum(arr[:k-1])

        for l in range(len(arr) - k + 1):
            cur_sum += arr[l+k-1]
            if (cur_sum/k) >= threshold:
                result += 1
            cur_sum -= arr[l]

        return result
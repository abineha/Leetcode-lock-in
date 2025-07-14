class Solution:
    def maxProduct(self, s: str) -> int:
        N, map = len(s), {}     # subseq:count
        result = 0

        for mask in range(1 << N):  # 2**N
            subseq=""
            for i in range(N):
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:
                map[mask] = len(subseq)

        for m1 in map:
            for m2 in map:
                if m1 & m2 == 0:
                    result = max(result, map[m1]*map[m2])

        return        
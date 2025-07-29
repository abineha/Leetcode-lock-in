class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        cur_window, max_window = 0, 0
        l, satisfied = 0, 0

        for r in range(len(customers)):
            if grumpy[r]:
                cur_window += customers[r]
            else:
                satisfied += customers[r]
            if r-l+1 > minutes:
                if grumpy[l]:
                    cur_window -= customers[l]
                l += 1
            max_window = max(max_window, cur_window)
        
        return satisfied + max_window
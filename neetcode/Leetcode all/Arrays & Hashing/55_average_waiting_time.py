class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        start, finish = 0, 0
        wt = 0
        for i in range(len(customers)):
            if start > customers[i][0]:
                finish = start + customers[i][1]
                wt += (finish - customers[i][0])
            else:
                start = customers[i][0]
                finish = start + customers[i][1]  
                wt += (finish - start)      

            start = finish
        
        return wt/len(customers)
    
class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        current_time = 0
        total_wait_time = 0

        for arrival, time_needed in customers:
            # If chef is idle, wait for customer
            if current_time < arrival:
                current_time = arrival
            
            # Finish the current customer
            current_time += time_needed
            total_wait_time += current_time - arrival  # waiting time = finish - arrival

        return total_wait_time / len(customers)

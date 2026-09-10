### Problem 1011. Capacity To Ship Packages Within D Days (Medium): https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

### Tags: Binary Search, Greedy

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def can_ship_in_days(capacity):
            total = 0
            required_days = 1
            for weight in weights:
                if((total + weight) > capacity):
                    required_days += 1
                    total = 0
                total += weight
            return required_days <= days


        # range 10 -45
        # w: 27 : 3 days
        # if(true) high = mid
        # else: increase capacity of ship mid + 1
        # range 10 - 27
        # w: 18 : 4 days
        n = len(weights)
        # assume a safe range of capacity of the ship
        low = max(weights)
        high = sum(weights)
        # result = low + (high - low) // 2 
        while(low <= high):
            capacity = low + (high - low) // 2 
            if(can_ship_in_days(capacity)):
                # we can do better
                high = capacity - 1
                # result = min(capacity, result)
            else:
                low = capacity + 1
            
        # print("low=", low, " result=", result)
        return low


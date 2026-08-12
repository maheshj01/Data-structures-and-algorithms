### Problem 34. Find First and Last Position of Element in Sorted Array (Medium): https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        if(len(nums) == 0 or target < nums[0] or target > nums[-1]):
            return result
        i = 0
        while(nums[i] != target and i < len(nums)):
            if(nums[i] > target):
                return [-1, -1] 
            i+=1
        result[0] = i
        i = len(nums) - 1
        while(nums[i] != target and i > result[0]):
            i -= 1
        result[1] = i
        return result


# Solution 2: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Idea is we will run binary search twice once to find the first position and once to find the last.
# if finding first position, we will move the right pointer to the middle - 1 until we find the first position.
# if finding last position, we will move the left pointer to the middle + 1 until we find the last position.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # l            m            r
        # [5, 7, 7, 8, 8, 8, 8, 8, 10]
        #  0           4         8
        
        # l   m      r 
        # [5, 7, 7, 8, 8, 8, 8, 8, 10]
        #  0        3  
        
        #        l  r 
        # [5, 7, 7, 8, 8, 8, 8, 8, 10]
        #        2  3  
        
        #           lr 
        # [5, 7, 7, 8, 8, 8, 8, 8, 10]
        #        2  3  
        
        #              l     m      r 
        # [5, 7, 7, 8, 8, 8, 8, 8, 10]
        #        2  3  
        
        #                       l    r 
        # [5, 7, 7, 8, 8, 8, 8, 8, 10]
        #        2  3  
        
        #  l = 0
        #  r = 8
        # target = 8
        # mid = 4, nums[mid] = 8 
        # find left = true
        #  
        #  l   m   r   
        

        def binSearch(firstTarget):
            left = 0
            right = len(nums) - 1
            result = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    result = mid
                    if firstTarget:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif(nums[mid] < target):
                    left = mid + 1
                else:
                    right = mid - 1
            return result
        
        # mid = binSearch(0, len(nums) - 1)
        # left = binSearch(0, mid)
        # right = binSearch(mid + 1, len(nums) - 1)
        result1 = binSearch(True)
        if(result1 == -1):
            return [-1, -1] 
        result2 = binSearch(False)
        return [result1, result2]

            
       



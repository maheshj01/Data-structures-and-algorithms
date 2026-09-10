### Problem 74. Search a 2D Matrix (Medium): https://leetcode.com/problems/search-a-2d-matrix/
### Tags: Array, Binary Search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 
        # low = 0
        # high = 6
        # mid =  low + (high - low) // 2 
        # mid = 3
        # rows = 3
        # cols = 4
        # r = 3 // cols = 0
        # c = 3 % cols = 1
        # mid_el = 7
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        low = 0
        high = (rows * cols) - 1

        while(low <= high):
            mid = low + (high - low) // 2
            mid_elem = matrix[mid // cols][mid % cols]
            if(target == mid_elem):
                return True
            elif(target < mid_elem):
                high = mid - 1
            else:
                low = mid + 1
        
        return False

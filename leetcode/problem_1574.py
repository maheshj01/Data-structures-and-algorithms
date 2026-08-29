## Problem 1574. Shortest Subarray to be Removed to Make Array Sorted

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        #        l          r 
        # [1,2,3,10,4,2,3,5]
        # left = 3
        # right = 8
        
        # end pointer of left sorted array
        leftEnd = 0
        for i in range(len(arr)):
            if(arr[i] >= arr[leftEnd]):
                leftEnd = i
            else:
                break
        print("leftEnd=", leftEnd)

        # start point of right sorted array
        rightStart = len(arr) - 1
        while(rightStart > 0 and arr[rightStart] >= arr[rightStart - 1] and leftEnd < rightStart):
            rightStart -= 1
        
        print("rightStart=", rightStart)
        #        l    r     
        # [1,2,3,10,4,2,3,5]
        # left = 3
        # right = 8
        # [4,4,4,6]
        if(leftEnd == rightStart):
            return 0
        left = 0
        result = min(len(arr) - leftEnd - 1 ,rightStart)
        while(left <= leftEnd and rightStart < len(arr)):
            if(arr[left] <= arr[rightStart]):
                result = min(result, rightStart - left - 1)
                left += 1
            else:
                rightStart += 1
        
        return result
        
        

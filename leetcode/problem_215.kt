class Solution {
    fun findKthLargest(nums: IntArray, k: Int): Int {
       val maxHeap = PriorityQueue<Int>(compareByDescending { it })
        for(num in nums){
            maxHeap.add(num)
        }
        var i = k
        while(i != 1){
            maxHeap.poll()
            i -= 1
        }
        return maxHeap.poll()
    }
}
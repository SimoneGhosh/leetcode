class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:

            print (nums[l], nums[r])
            if nums[l] < nums[r]:
                return nums[l]
            
            m = (l+r) // 2
            print (m)
        
            if nums[m] > nums[r]:
                print ("moved left")
                l = m + 1
            else:
                print ("moev r")
                r = m 
        
        return nums[l]


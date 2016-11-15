'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

You may assume no duplicate exists in the array.

'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return min(self.findMin(nums[:mid+1]), self.findMin(nums[mid+1:]))
        return nums[left]
        

# testing
def main():
    inArray = [10, 10, 10, 10, 5, 10]
    expected = 5
    solution = Solution()   #instance of Solution class
    if solution.findMin(inArray) == expected:
        print("Success")
    else:
        print("Failure, your output is ", solution.findMin(inArray))
        
if __name__ == "__main__":
    main()
            

        
        
        
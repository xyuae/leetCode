'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)  # n is the length of the array
        if n == 1:
            # the element must be minimum in the subarray if it has only one size
            return nums[0]
        # if there is two element in the array, mid = 1, 
        mid = n // 2
        if mid > 0 and nums[0] > nums[mid -1]:
            return self.findMin(nums[0: mid])
        elif mid < n and nums[mid] > nums[n - 1]:
            return self.findMin(nums[mid: n])
        else:
            return min(nums[0], nums[mid])

# testing
def main():
    inArray = [5, 2, 2, 3, 5]
    expected = 2
    a = Solution()
    if a.findMin(inArray) == expected:
        print("Success")
    else:
        print("Failure, your output is ", a.findMin(inArray))
        
if __name__ == "__main__":
    main()
            

        
        
        
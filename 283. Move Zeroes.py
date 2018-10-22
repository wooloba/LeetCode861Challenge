class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        count = 0
        while index < len(nums)-1:
            if nums[index] == 0:
                nums.pop(index)
                count += 1
                index -= 1
            index += 1
        nums += [0]*count
        return nums

def main():
    nums = [0,1,0,3,12]
    so = Solution()
    res = so.moveZeroes(nums)

    print(res)

if __name__ == "__main__":
    main()
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1, 1, 2, 8
        # 48,24,6,1
        list1, list2 = [], []

        for i in range(len(nums)):
            if i == 0:
                list1.append(1)
            else:
                list1.append(list1[i-1]*nums[i-1])

        reversed_nums = nums.reverse()
            
        for j in range(len(nums)):
            if j == 0:
                list2.append(1)
            else:
                list2.append(list2[j-1]*nums[j-1])

        list2.reverse()
        res = []

        for k in range(len(list1)):
            res.append(list1[k]*list2[k])
        
        return res
        
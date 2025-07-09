def singleNumber(nums):
        num=None
        for i in nums:
            if nums.count(i)==1:
                num=i 
                break
        return num
print(singleNumber([4,1,2,1,2]))

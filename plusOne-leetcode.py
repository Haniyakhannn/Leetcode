def plusOne(digits):
        new=""
        for i in digits:
            new += str(i)  
        num=int(new)+1
        return [int(i) for i in str(num)] 


print(plusOne([2,3,2,1]))

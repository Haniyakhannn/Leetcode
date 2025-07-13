def isValid(self, s):
        stack=[]
        closetoopen={')':'(','}':'{',']':'['} #using a hashmap
        for i in s: 
            if i in closetoopen: #checking if it is a opening bracket
                if stack and stack[-1]==closetoopen[i]: #checking the top is same as the corresponding key value 
                    stack.pop()  #pop from a stack if it is a closing bracket
                else:
                    return False
            else:
                stack.append(i) #if it is a opening bracket we will push it on to the stack
        return True if not stack else False
                

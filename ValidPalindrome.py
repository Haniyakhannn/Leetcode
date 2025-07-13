def isPalindrome(self, s):
        snew=''   #initializing a new string
        s=s.strip() #removing whitespaces
        for i in s: #looping over the string 
            if i.isalnum(): 
                snew+=i.lower()

        return snew == snew[::-1] #returning True if s is a palindrome 
           
        

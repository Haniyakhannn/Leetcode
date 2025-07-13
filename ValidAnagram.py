def isAnagram(self, s, t):
        if len(s) != len(t): #checking the length of both strings
            return False

        for i in s:
            if s.count(i) != t.count(i): #Checking the frequency of each element and comparing if the frequency matches or not
                return False

        return True


        

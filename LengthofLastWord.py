def lengthOfLastWord(self, s):
        s=s.strip()
        new=s.split(' ')
        return len(new[-1])

def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
    
        
        slen = len(s)
        for i in range(slen):
            for j in range(i+1):
                str = s[j:slen-i+j]
                if self.ispalindrome(str) == 1:
                    return str
                    
def ispalindrome(self, s):
    slen = len(s)
    slist = list(s)
    ret = []
    if (slen%2 == 1):
        ran = int(slen/2+1)
    else:
        ran = int(slen/2)
    for i in range(int(slen/2)):
        ret.append(slist[i])
    for j in range(ran, slen):
        #print(ret[-1])
        if slist[j] != ret[-1]:
            return 0
        else:
            ret.pop(-1)
    return 1
                
if __name__ == "__main__":
    print(longestPalindrome("abb"))
    
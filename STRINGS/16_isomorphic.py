class Solution():
    def isomorphic(self,s,t):
        if len(s)!=len(t):
            return False
        map_s={}
        map_t={}
        for i in range(len(s)):
            ch1=s[i]
            ch2=t[i]
            if ch1 in map_s:
                if map_s[ch1]!=ch2:
                    return False
            else:
                map_s[ch1]=ch2
                    
            if ch2 in map_t:
                if map_t[ch2]!=ch1:
                    return False
            else:
                map_t[ch2]=ch1
                    
        return True
    
s=input("Enter any string1:")
t=input("Enter any string2:")
answer=Solution()
print(answer.isomorphic(s,t))
class Solution():
    def lps(self,s):
        max_len=0
        req=''
        for i in range(len(s)):
            l=r=i
            while l>=0 and r<len(s) and s[r]==s[l]:
                if r-l+1>max_len:
                    max_len=r-l+1
                    req=s[l:r+1]
                l-=1
                r+=1
                
            l,r=i,i+1
            while l>=0 and r<len(s) and s[r]==s[l]:
                if r-l+1>max_len:
                    max_len=r-l+1
                    req=s[l:r+1]
                l-=1
                r+=1
                
        return max_len,req  
        
    
s=input("Enter any string:")
answer=Solution()
print(answer.lps(s))

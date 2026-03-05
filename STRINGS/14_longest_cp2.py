class Solution():
    def lcp(self,strs):
        if not strs:
            return ''
        prefix=strs[0]
        for word in strs[1:]:
            i,j=0,0
            while i<len(prefix) and j<len(word) and prefix[i]==word[j]:
                i+=1
                j+=1
            prefix=prefix[:i]
            
            if prefix=="":
                return ""
            
        
        return prefix
    
answer=Solution()
string=list(input("enter any strings:").split(" "))
print(answer.lcp(string))
class Solution():
    def character_freq(self,s):
        
        seen={}
        for ch in s:
            if ch in seen:
                seen[ch]+=1
            else:
                seen[ch]=1
        seen=sorted(seen.items(),key=lambda g:g[1],reverse=True)
        result=''
        for ch,count in seen:
            result+=ch*count
        
        return result
    
    
s=input("Enter any string:")
answer=Solution()
print(answer.character_freq(s))
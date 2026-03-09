class Solution():
    def beauty(self,s):
        ans=0
        for i in range(len(s)):
            freq=[0]*26
            for j in range(i,len(s)):
                freq[ord(s[j])-ord('a')]+=1
                min_freq=float('inf')
                max_freq=0
                for f in freq:
                    if f>0:
                        min_freq=min(min_freq,f)
                        max_freq=max(f,max_freq)
    
                ans+=max_freq-min_freq
                
        return ans
    
answer=Solution()
s=input('Enter any string:')
print(answer.beauty(s))
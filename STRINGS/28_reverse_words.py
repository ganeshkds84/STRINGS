class Solution():
    def reverse_words(self,s):
        s=s.split()
        start=0
        end=len(s)-1
        while start<end:
            s[start],s[end]=s[end],s[start]
            start+=1
            end-=1
            
        
        return " ".join(s)
    
s='''Goutham needs Ashuu but    Ashu  don't need Goutham   '''
answer=Solution()
print(answer.reverse_words(s))


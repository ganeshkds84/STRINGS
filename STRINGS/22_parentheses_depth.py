class Solution():
    def parentheses_depth(self,s):
        high=0
        current=0
        for ch in s:
            if ch=='(':
                current+=1
                high=max(high,current)
            elif ch==')':
                current-=1
                
        return high
    
s=input("Enter the string:")
answer=Solution()
print(answer.parentheses_depth(s))
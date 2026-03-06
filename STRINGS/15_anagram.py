class Solution():
    def anagram(self,s,t):
        if len(s)!=len(t):
            return False
        seen={}
        for ch in s:
            if ch in seen:
                seen[ch]+=1
            else:
                seen[ch]=1
        for ch in t:
            if ch in seen:
                seen[ch]-=1
            else:
                return False
            if seen[ch]<0:
                return False
            
        return True 
answer=Solution()
s=input("Enter first string:")
t=input("enter second string:")
print(answer.anagram(s,t))

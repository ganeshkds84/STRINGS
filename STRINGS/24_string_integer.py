class Solution():
    def string_integer(self,s):
        s=s.strip()
        i=0
        result=0
        sign=1
        if s[0]=='+':
            i+=1
        elif s[0]=='-':
            sign=-1
            i+=1
            
        while i<len(s):
            if s[i].isdigit():
                result=result*10+int(s[i])
                i+=1
            else:
                break
            
        result=result*sign
        int_MIN=-2**31
        int_MAX=2**31-1
        
        if result>int_MAX:
            result=int_MAX
        if result<int_MIN:
            result=int_MIN
            
        return result
    
answer=Solution()
s=input("Enter your atoi:")
print(answer.string_integer(s))
class Solution():
    def remove_paranthesis(self,string):
        final=""
        count=0
        for ch in string:
            if ch=='(':
                if count>0:
                    final=final+ch
                count+=1
            else:
                count-=1
                if count>0:
                    final=final+ch
        
        return final
    
string1=input("please give parenthesis as inputs:")
answer=Solution()
print(answer.remove_paranthesis(string1))
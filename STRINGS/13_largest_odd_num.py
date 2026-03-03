class Solution():
    def Largest_Odd(self,string):
        stop=-1
        i=len(string)-1
        while i>=0:
            if int(string[i])%2!=0:
                stop=i
                break
            i-=1
        if stop==-1:
            return ""
        start=0
        i=0
        while i<len(string):
            if string[i]=='0':
                i+=1
            else:
                start=i
                break
        
        return string[start:stop+1]
    
answer=Solution()
string=input('Enter any number:')
print(answer.Largest_Odd(string))
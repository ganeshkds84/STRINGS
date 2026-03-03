class solution():
    def is_palindrome(self,string):
        string=string.lower()
        i,j=0,len(string)-1
        while i<j:
            if string[i]!=string[j]:
                return "Not palindrome"
            i+=1
            j-=1
        return "Palindrome"
    
string=input("Enter the string:")
answer=solution()
print(answer.is_palindrome(string))

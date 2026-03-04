class Solution():
    def rotate_string(self,s,goal):
        if len(s)!=len(goal):
            return False
        temp=s+s
        if goal in temp:
            return True
        return False
    
answer=Solution()
s=input("Enter any string:")
goal=input("Enter string to be compared:")
print(answer.rotate_string(s,goal))
class Solution:
    def isPalindrome(self, s: str) -> bool:
        flag = 0 
        left =  0
        right = len(s) - 1
        while left < right: 
            if s[left] == " ":
                left = left + 1
            if s[right] == " ":
                right = right - 1
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1 
            
            if s[left] != " " and s[right] != " ":
                if s[left].lower() != s[right].lower():
                    flag = 1
                    break 
                left = left + 1
                right = right - 1 
        
        if flag == 1:
            return False
        else :
            return True 


        
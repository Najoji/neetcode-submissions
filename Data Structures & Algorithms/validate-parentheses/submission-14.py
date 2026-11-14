class Solution:
    def isValid(self, s: str) -> bool:

        signs = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

       

        length = len(s)
        parenth = []
        flag = 0 

        for i in range(0 ,length):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                parenth.append(s[i])
            
            if s[i] == ")" or s[i] == "}" or s[i] == "]":
                if parenth and parenth[-1] == signs[s[i]]:
                    parenth.pop()
                else :
                    return False 

                 
        if not parenth :
            return True 
        else :
            return False 


        
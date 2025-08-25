class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        top=-1
        
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                top=top+1
                stack.append(s[i])
                

            elif s[i]==')':
                if len(stack)==0 or stack[top]=='[' or stack[top]=='{':
                   return False
                elif stack[top]=='(':
                   del stack[top]
                   top=top-1
                   

            elif s[i]==']':
                if len(stack)==0 or stack[top]=='(' or stack[top]=='{':
                   return False
                elif stack[top]=='[':
                   del stack[top]
                   top=top-1
                   
                   
            elif s[i]=='}':
                if len(stack)==0 or stack[top]=='[' or stack[top]=='(':
                   return False
                elif stack[top]=='{':
                   del stack[top]
                   top=top-1
                   
        if len(stack)==0:
            return True
        else:
            return False
        

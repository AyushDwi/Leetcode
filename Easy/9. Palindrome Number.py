class Solution(object):
    def isPalindrome(self, x):
        l=str(x)
        for i in range (len(l)//2):
              if (l[i]!=l[len(l)-1-i]):
                  return False 
        return True 

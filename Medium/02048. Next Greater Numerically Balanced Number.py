class Solution(object):
    def nextBeautifulNumber(self, n):
        def isBalanced(x):
            s = str(x)
            return all(s.count(d) == int(d) for d in set(s))
        
        x = n + 1
        while not isBalanced(x):
            x += 1
        return x

class Solution(object):
    def romanToInt(self, s):
        i = 0
        l = len(s)
        total = 0

        roman = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

        while i < l:
            if i + 1 < l and roman[s[i]] < roman[s[i + 1]]:
              total += roman[s[i + 1]] - roman[s[i]]
              i += 2
            else:
              total += roman[s[i]]
              i += 1
        return total 

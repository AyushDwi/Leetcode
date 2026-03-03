class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        while n > 1:
            n -= 1
            s += '1' + self.reverseS(s)
            if len(s) >= k:
                break
        return s[k-1]

    def reverseS(self, s: str):
        s = list(s[::-1])
        reverse = {'0' : '1', '1' : '0'}
        for i in range(len(s)):
            s[i] = reverse[s[i]]
        return ''.join(s)

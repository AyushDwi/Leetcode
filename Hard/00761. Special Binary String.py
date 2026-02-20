class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 2:
            return s
        subs = []
        cnt, left = 0, 0
        for i, c in enumerate(s):
            if c == "1":
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                subs.append("1" + self.makeLargestSpecial(s[left + 1 : i]) + "0")
                left = i + 1
        subs.sort(reverse=True)
        return "".join(subs)

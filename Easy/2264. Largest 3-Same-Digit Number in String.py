class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        max_good = ""
        for i in range(len(num) - 2):
            triplet = num[i:i+3]
            if triplet[0] == triplet[1] == triplet[2]:
                if triplet > max_good:
                    max_good = triplet
        return max_good

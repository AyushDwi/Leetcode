class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        xz = abs(x - z)
        yz = abs(y - z)
        if xz == yz:
            return 0
        return 1 if xz < yz else 2

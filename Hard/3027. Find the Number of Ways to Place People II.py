class Solution(object):
    def numberOfPairs(self, points):
        n = len(points)
        if n < 2:
            return 0
        points.sort(key=lambda point: (point[0], -point[1]))
        count = 0
        for i in range(n):
            alice_x, alice_y = points[i]
            max_y = float('-inf')
            for j in range(i + 1, n):
                bob_x, bob_y = points[j]
                if max_y < bob_y <= alice_y:
                    max_y = bob_y
                    count += 1
        return count

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [0] * len(mat)
        cols = [0] * len(mat[0])
        for i in range(len(mat)):
          for j in range(len(mat[i])):
            if mat[i][j] == 1:
              rows[i] += 1
              cols[j] += 1
        special = 0
        for i in range(len(mat)):
          for j in range(len(mat[i])):
            if mat[i][j] == 1:
              if rows[i] == 1 and cols[j] == 1:
                special += 1
        return special

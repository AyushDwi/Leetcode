class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        Pascal_Triangle=[[1]]
        for i in range(1,numRows):
            curr_row=[]
            for j in range(0,i+1):
                if j==0 or j==i:
                    curr_row.append(1)
                else:
                    curr_row.append(Pascal_Triangle[-1][j-1]+Pascal_Triangle[-1][j])
            Pascal_Triangle.append(curr_row)
        return Pascal_Triangle               
        

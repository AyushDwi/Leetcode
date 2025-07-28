class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        dec_num=0
        po=0
        for i in a:
           dec_num+=int(i)*2**(len(a)-1-po)
           po+=1

        po=0    
        for j in b:
           dec_num+=int(j)*2**(len(b)-1-po)
           po+=1
        if dec_num==0:
            return '0'
        s=''
        while dec_num>0:
            rem=dec_num%2
            dec_num//=2
            s+=str(rem)
        return s[::-1] 

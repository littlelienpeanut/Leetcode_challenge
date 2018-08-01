class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = list(num1)[::-1], list(num2)[::-1]
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        
        carr = 0
        output = ''
        for i in range(len(num1)):
            if carr == 1:
                num1[i] = str(int(num1[i]) + 1)
                carr = 0
            
            if i > len(num2)-1:
                for j in range(i, len(num1)):
                    tmp = int(num1[j]) + carr
                    if tmp > 9:
                        tmp -= 10
                        carr = 1
                    
                    else:
                        carr = 0
                        
                    output += str(tmp)
                
                if carr == 1:
                    output += str(1)
                
                return  (''.join(ch for ch in list(output)[::-1]))
                    
            tmp = int(num1[i]) + int(num2[i])
            if tmp > 9:
                tmp -= 10
                carr = 1
            
            else:
                carr = 0
            
            output += str(tmp)
            
        if carr == 1:
            output += str(1)
        return  (''.join(ch for ch in list(output)[::-1]))
        
        
            
            
        

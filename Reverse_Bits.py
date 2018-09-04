class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = bin(n)[2:][::-1]
        while len(n)<32:
            n += '0'
        return int(n, 2)
        

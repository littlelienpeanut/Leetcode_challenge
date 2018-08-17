class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        def cnt_n(ind, c):
            cnt = 0
            tmp = []
            for i in range(ind, len(chars)):
                if chars[i] == c:
                    cnt += 1
                else:
                    break
            
            for ch in str(cnt):
                tmp.insert(0, ch)
            
            return tmp, cnt
        
        ind = 0
        while (ind < len(chars)):
            tmp, cnt = cnt_n(ind, chars[ind])
            if cnt != 1:
                while (ind+1 < len(chars) and chars[ind] == chars[ind+1]):
                    chars.pop(ind+1)
                ind += 1
                for ch in tmp:
                    chars.insert(ind, ch)
                ind += len(tmp)
                
            else:
                ind += 1
        
        return len(chars)
                
                

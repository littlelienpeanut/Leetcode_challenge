class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        output = ['']

        if S.isdigit():
            output.remove('')
            output.append(S)


        else:
            for i in range(len(S)):
                if S[i].isdigit():
                    tmp_output = []
                    for ele in output:
                        tmp = ele
                        tmp_output.append(tmp + S[i])
                    output = tmp_output

                else:
                    tmp_output = []
                    for ele in output:
                        tmp = ele
                        tmp_output.append(tmp + S[i].upper())
                        tmp_output.append(tmp + S[i].lower())
                    output = tmp_output

        return output

class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dict = {}
        output = []

        for url in cpdomains:
            times, tmp_url = url.split( )
            times = int(times)
            if tmp_url in dict.keys():
                dict[tmp_url] += times
            else:
                dict.update({tmp_url: times})
            while (tmp_url.find('.') != -1):
                pop, tmp_url = tmp_url.split('.', 1)
                if tmp_url in dict.keys():
                    dict[tmp_url] += times

                else:
                    dict.update({tmp_url: times})


        for key in dict.keys():
            tmp_output = str(dict[key]) + ' ' + key
            output.append(tmp_output)

        return output

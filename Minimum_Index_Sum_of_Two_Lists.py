class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        output = []
        tmp_l1 = {}
        res = {}

        for ind, r in enumerate(list1):
            tmp_l1.update({r:ind})

        for ind, r in enumerate(list2):
            if r in tmp_l1:
                res.update({r:(ind+tmp_l1[r])})
        min_value = min(res.values())

        for r, value in res.items():
            if value == min_value:
                output.append(r)

        return output
        

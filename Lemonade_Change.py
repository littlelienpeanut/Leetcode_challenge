class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = []
        ten = []
        for i in bills:
            if i == 5:
                five.append(1)

            elif i == 10:
                if len(five) == 0:
                    return False

                else:
                    five.pop(0)
                    ten.append(1)


            else:
                if len(five) != 0 and len(ten) != 0:
                    five.pop(0)
                    ten.pop(0)

                elif len(five) > 2:
                    five.pop(0)
                    five.pop(0)
                    five.pop(0)

                else:
                    return False

        return True

        

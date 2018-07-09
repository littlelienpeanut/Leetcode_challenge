"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emp = {emp.id: [emp.importance, emp.subordinates] for emp in employees}
        value = 0

        if emp[id][1] == []:
            return emp[id][0]

        else:
            value = emp[id][0]
            d = emp[id][1]

            for e in d:
                print(e)
                if emp[e][1] == []:
                    value += emp[e][0]

                else:
                    value += emp[e][0]
                    for i in emp[e][1]:
                        d.append(i)

            return value

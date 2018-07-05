class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        for i in range(1, n+1, 1):
            if i % 3 == 0:
                output.append('Fizz')

            elif i % 5 == 0:
                output.append('Buzz')

            else:
                output.append(str(i))

            if i % 15 == 0:
                output.pop(len(output)-1)
                output.append('FizzBuzz')


        return output

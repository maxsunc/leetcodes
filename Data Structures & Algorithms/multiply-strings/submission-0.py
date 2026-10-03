class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # can there be leading 0s?
        # we can convert single digits here right?


        # 123 * 456
        # accumulate everything into a one digit array

        # each digits of num1 multiplied by each digit of num2 one by one

        # two arrays: one for carry one and another for the actual digits
        # 999 * 999
        # never reach n + m digits: n is the length of num1 and m isthe length of num2
        n,m = len(num1), len(num2)
        digits = [0 for i in range(0,n + m)]
        # lowest digits on the right side

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                position = i + j + 1
                val1, val2 = ord(num1[i]) - ord('0'),ord(num2[j]) - ord('0')
                total = val1 * val2 + digits[position]
                digits[position] = total % 10
                digits[position - 1] += total // 10

        print(digits)
        res = ""
        isLeadingZeros = True
        for i in range(0, len(digits)):
            if isLeadingZeros and digits[i] == 0:
                continue
            else:
                isLeadingZeros = False
            res += str(digits[i])
        return res if len(res) != 0 else "0"
            

            

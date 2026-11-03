class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # reverse polish notation
        # get apply operand onto the 2 most recent numbers 
        
        # use a stack for this
        stack = []

        # everytime we find a notation pop two from sstack and append res
        # are we guarunteed it a;ways going to be vlaid notation? Yes
        for val in tokens:
            if val in "+-*/":
                val1,val2 = stack.pop(), stack.pop()
                res = 0
                if val == "+":
                    res = val1 + val2
                elif val == "-":
                    res = val2 - val1
                elif val == "*":
                    res = val1 * val2
                else:
                    res = math.floor(val2 / val1) if val2 / val1 >= 0 else math.ceil(val2/val1)
                # print(f"{val1}  {val} {val2} = {res}")
                stack.append(res)
            else:
                stack.append(int(val))

        return stack[0]
                    
                    
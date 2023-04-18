# Task
# A game I played when I was young: Draw 4 cards from playing cards, use + - * / and () to make the final results equal to 24.

# You will coding in function equalTo24. Function accept 4 parameters a b c d(4 numbers), value range is 1-100.

# The result is a string such as "2*2*2*3" ,(4+2)*(5-1); If it is not possible to calculate the 24, please return "It's not possible!"

# All four cards are to be used, only use three or two cards are incorrect; Use a card twice or more is incorrect too.

# You just need to return one correct solution, don't need to find out all the possibilities.

# The different between "challenge version" and "simple version":

# 1) a,b,c,d range:  In "challenge version" it is 1-100, 
#                    In "simple version" it is 1-13.
# 2) "challenge version" has 1000 random testcases,
#    "simple version" only has 20 random testcases.

def equalTo24(a, b, c, d):
    def dfs(nums, path):
        if len(nums) == 1:
            if nums[0] == 24:
                return path
            else:
                return None
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                num1, num2 = nums[i], nums[j]
                for op in ops:
                    if (op == '/' and num2 == 0) or (op == '*' and num1 == 1) or (op == '-' and num1 == num2):
                        continue
                    if op == '+':
                        res = num1 + num2
                    elif op == '-':
                        res = num1 - num2
                    elif op == '*':
                        res = num1 * num2
                    else:
                        res = num1 / num2
                    new_nums = nums[:i] + [res] + nums[i+1:j] + nums[j+1:]
                    new_path = path + f" {op} {num2}" if op in '+-' else path + f" {op} ({num2})"
                    ans = dfs(new_nums, new_path)
                    if ans:
                        return ans
        return None

    ops = ['+', '-', '*', '/']
    nums = [a, b, c, d]
    return dfs(nums, str(nums[0]))

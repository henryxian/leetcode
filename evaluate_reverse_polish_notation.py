# 150. Evaluate Reverse Polish Notation

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        if len(tokens) == 0:
        	return 0
        else:
        	for token in tokens:
        		if token == "+":
        			if len(stack) != 0:
        				rhs = stack.pop()
        			if len(stack) != 0:
        				lhs = stack.pop()
        			res = lhs + rhs
        			stack.append(res)
        		elif token == "-":
        			if len(stack) != 0:
        				rhs = stack.pop()
        			if len(stack) != 0:
        				lhs = stack.pop()
        			res = lhs - rhs
        			stack.append(res)
        		elif token == "*":
        			if len(stack) != 0:
        				rhs = stack.pop()
        			if len(stack) != 0:
        				lhs = stack.pop()
        			res = lhs * rhs
        			stack.append(res)
        		elif token == "/":
        			if len(stack) != 0:
        				rhs = stack.pop()
        			if len(stack) != 0:
        				lhs = stack.pop()
        			res = abs(lhs) / abs(rhs)
        			res = (-1) * res if (lhs < 0 and rhs >0) or (lhs > 0 and rhs < 0) else res
        			stack.append(res)
        		else:
        			num = int(token)
        			stack.append(num)
        if len(stack):
        	return stack[-1]
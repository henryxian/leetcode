# 50. Pow(x, n)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def equal(num1, num2):
        	if num1 - num2 > -0.000001 and num1 - num2 < 0.000001:
        		return True
        	else:
        		return False

        def powerWithUnsignedExponent(base, exp):
        	if exp == 0:
        		return 1.00000
        	if exp == 1:
        		return base
        	result = powerWithUnsignedExponent(base, exp >> 1)
        	result = result * result
        	if exp & 0x1 == 1:
        		result = result * base
        	return result

        if equal(x, 0.00000):
        	return 0.00000
        elif equal(n, 0.0):
        	return 1.00000
        else:
        	if n < 0:
        		x = 1.0 / x
        		n = n * (-1)
        	result = powerWithUnsignedExponent(x, n)
        	return result
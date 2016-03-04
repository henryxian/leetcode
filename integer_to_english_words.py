# Integer to English Words
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_list = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", 
            "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen",]
        num_list2 = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety",] 
        level = ["Hundred", "Thousand", "Million", "Billion",]
        
        def threedigit(n):
            word = ""
            if n == 0:
                return word
            elif n < 20:
                word = num_list[n] + word
            elif n >= 20 and n < 100:
                remainder = n % 10
                n = n / 10
                if remainder != 0:
                    word = num_list[remainder] + word
                    word = num_list2[n - 2] + " " + word
                else:
                    word = num_list2[n - 2] + word
            else:
                remainder = n % 100
                n = n / 100
                if remainder == 0:
                    word = num_list[n] + " " + level[0]
                else:
                    word = num_list[n] + " " + level[0] + " " + threedigit(remainder)
            return word


        if num == 0:
            return "Zero"
        cnt = 0
        word = ""
        while num > 0:
            cnt = cnt + 1
            remainder = num % 1000
            num = num / 1000
            word = threedigit(remainder) + word
            if num != 0:
                word = " " + level[cnt] + " " + word
            # if num != 0:
            #     word = level[cnt] + word
        return word

if __name__ == '__main__':
    solution = Solution()
    print solution.numberToWords(0)
    print solution.numberToWords(5)
    print solution.numberToWords(11)
    print solution.numberToWords(20)
    print solution.numberToWords(23)
    print solution.numberToWords(223)
    print solution.numberToWords(2223)
    print solution.numberToWords(100)
    print solution.numberToWords(1000)
    print solution.numberToWords(10000)

    # bug
    print solution.numberToWords(1000001)

        
class Solution1:


    def __init__(self):
        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                           "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        res = ""
        i = 0
        while (num != 0):
            # 只取最后三位
            res = self.helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000  # num去掉后三位
            i += 1

        return res

    def helper(self, num):
        if num < 20:
            return self.lessThan20[num]
        elif num < 100:
            # 十位上的数                个位上的数
            return self.tens[num // 10] + " " + self.helper(num % 10)
        elif num < 999:
            # 百位上的数                            # 两位数
            return self.lessThan20[num // 100] + " " + "Hundred" + " " + self.helper(num % 100)
    """
    空格总是处理不好
    """



class Solution2:
    """
    第二版：递归里面加 “ ”

    """

    def __init__(self):
        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                           "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        res = ""
        i = 0
        while (num != 0):
            # 只取最后三位
            res = self.helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000  # num去掉后三位
            i += 1

        return res

    def helper(self, num):
        if num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            # 十位上的数                个位上的数
            return self.tens[num // 10] + " " + self.helper(num % 10)
        elif num < 999:
            # 百位上的数                            # 两位数
            return self.lessThan20[num // 100] + " " + "Hundred" + " " + self.helper(num % 100)

    """
    那么：
        怎么处理首尾的空格呢？
    """


class Solution3:
    """
     use strip() to remove begin and end space

    """

    def __init__(self):
        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                           "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        res = ""
        i = 0
        while (num != 0):
            # 只取最后三位
            res = self.helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000  # num去掉后三位
            i += 1

        return res.strip()

    def helper(self, num):
        if num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            # 十位上的数                个位上的数
            return self.tens[num // 10] + " " + self.helper(num % 10)
        elif num < 999:
            # 百位上的数                            # 两位数
            return self.lessThan20[num // 100] + " " + "Hundred" + " " + self.helper(num % 100)

    """
    but this case cannot through!! 
    
    680901192
    "Six Hundred Eighty  Million Nine Hundred One Thousand One Hundred Ninety Two"
                       | this place has two space
                       
                       
    This is because 680 in helper will return two space in the end:
    num = 0  return " "
    num = 80  return "Eighty" + " " + num=0(" ") 
    """



class Solution:
    """
     最终版： in recursion, add num == 0

    """

    def __init__(self):
        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                           "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        res = ""
        i = 0
        while (num != 0):
            # 只取最后三位
            res = self.helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000  # num去掉后三位
            i += 1

        return res.strip()

    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            # 十位上的数                个位上的数
            return self.tens[num // 10] + " " + self.helper(num % 10)
        elif num < 999:
            # 百位上的数                            # 两位数
            return self.lessThan20[num // 100] + " " + "Hundred" + " " + self.helper(num % 100)


if __name__ == '__main__':
    a = Solution3()
    res = a.numberToWords(680901192)

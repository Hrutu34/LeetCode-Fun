class Solution:
    def isPalindrome(self, x: int) -> bool:
        flag = False
        str_1 = str(x)
        str_2 = str_1[::-1]
        if str_1 == str_2:
            flag = True
        return flag
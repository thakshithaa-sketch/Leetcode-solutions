class Solution(object):
    def isPalindrome(self, num):
        """
        :type x: int
        :rtype: bool
        """
        original = num
        reverse = 0
        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10

        if original == reverse:
            return(True)
        else:
            return(False)
        
""" CODE SAMPLE 
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        return str(x) == str(x)[::-1]

"""
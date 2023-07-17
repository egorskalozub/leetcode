def isPalindrome(self, x: int) -> bool:
    string1 = str(x)
    string2 = (str(x))[::-1]
    if string1 == string2:
        return True
    else:
        return False

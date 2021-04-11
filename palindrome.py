

def palindrome(word):
    if len(word) <= 1:
        return True

    length = len(word)
    if word[0] == word[-1]:
        return palindrome(word[1: length - 1])
    else:
        return False

sample = str(input("enter the string to test: "))
print(f'The String entered is {sample}')
if (palindrome(sample) == True):
    print("The string is a Palindrome")
else:
    print("The string is not a palindrome!")


"""  sample outputs
    ➜  python_Projects git:(main) ✗ python3 palindrome.py 
    enter the string to test: m
    The String entered is m
    The string is a Palindrome
    ➜  python_Projects git:(main) ✗ python3 palindrome.py
    enter the string to test: ono
    The String entered is ono
    The string is a Palindrome
    ➜  python_Projects git:(main) ✗ python3 palindrome.py
    enter the string to test: hello there
    The String entered is hello there
    The string is not a palindrome!
    ➜  python_Projects git:(main) ✗ python3 palindrome.py                                                                  
    enter the string to test: madam
    The String entered is madam
    The string is a Palindrome

"""


n = int(input("Enter any number: "))

def palindrome(a):
    if(a == a[::-1]):
        return True
    


def rev(a):
    return int((str(a)[::-1]))


def make_pallindrome(a):
    reverse = rev(a)

    total = a + int(reverse)

    if (palindrome(str(total)) == True):
        print (total)
    else:
        make_pallindrome(total)


make_pallindrome(n)






    
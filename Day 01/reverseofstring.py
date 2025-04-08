def stringreverse(string):
    """
    This function takes a string as input and returns the reversed string.
    """
    return string[::-1]
string = input("Enter a string: ")
print("Reversed string is:", stringreverse(string))

#for reversing numbers
def numberreverse(number):
    """
    This function takes a number as input and returns the reversed number.
    """
    return int(str(number)[::-1])
number = int(input("Enter a number: ")) 
print("Reversed number is:", numberreverse(number))
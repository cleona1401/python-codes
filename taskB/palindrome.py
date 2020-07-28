#palindrome
str=input("Enter a String: ")#will take input from user and store in str
def reverse(str):#reverse function
    rev=""  #declaring the variable
    for i in str:#for loop to iterate each character in string
        rev=i+rev #reverse logic
    return rev #function will return the reversed string 
s=reverse(str) #reversed value will be stored in s variable
if str==s:  #if reversed value and original string is same then it is palindrome ekse not palindrome
    print("String is palindrome")
else:
    print("String is not a palindrome")
#op:Enter a String: abcba
#String is palindrome
#Enter a String: hello
#String is not a palindrome   
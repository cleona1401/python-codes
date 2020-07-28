n=4                     #user defined number
def fact(n):            #factorial function
    if n==0:            #if number becomes is 0 after recurcively calling function then the value should be 1
        return 1        
    return n * fact(n-1)#Factorial logic

print("Factorial is:" ,fact(n))          #prints the factorialof the number by calling the function
"""op:>python fac.py
Factorial is: 24"""
import random
a=random.randint(0,100)#will choose a random number from 1 to 100 and store it in a variable .
count=0 #declaring the count variable to print your attempts at last.
while True:
    guess=int(input("guess the number"))#will take input from user and store in guess variable
    if guess>a: #if guessed value is greater than the number generated by computer it will print the statement and increment count
        count=count+1
        print("your guess is bigger than the hidden number")
    elif guess<a:#if guessed value is smaller than the number generated by computer it will print the statement and increment count
        count=count+1
        print("your guess is smaller than hidden number")
    elif guess==a:#if your guess is correct then it will print the statements and no of attempts and break from the loop.
        print("you guess is correct")
        print("attempts",count)
        break
***OP:guess the number8
your guess is smaller than hidden number
guess the number54
your guess is smaller than hidden number
guess the number60
your guess is smaller than hidden number
guess the number70
your guess is smaller than hidden number
guess the number80
your guess is smaller than hidden number
guess the number90
your guess is smaller than hidden number
guess the number100
your guess is bigger than the hidden number
guess the number91
you guess is correct
attempts 7***
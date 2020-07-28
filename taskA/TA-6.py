les=[]      #delared an empty list
num=int(input("enter no of elements to be inserted"))#take the no of elements that user wants to enter from user
for i in range(num): will iterate through the range given by user
    elem=input()    #will take input from user that many times
    les.append(elem)#will append the input to the list
print("**********")
for eles in les:    #will iterate through the list
    print("*", eles ,"*") #print the string
print("**********")  
"""op:>python TA-6.py
enter no of elements to be inserted4
python
pycharm
jupyter
spyder
**********
* python *
* pycharm *
* jupyter *
* spyder *
**********
 
"""
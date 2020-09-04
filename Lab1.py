import math
'''
Lab 1 
'''

########## Part 1 ###########

'''
   1) Create a variable, x, and set its value to 16
      Create a variable, y, and set its value to square root of x
      Divide x by three fifths of y, and store the result in x (hint: /=)

'''
print("-----------------------------------\n            PART 1.1")
# YOUR CODE GOES HERE

x = 16
y = math.sqrt(x)
x /= ((3/5)*y)


'''
    2)  A cube has the edge defined below.

    Store its space diagonal, surface area and volume in new variables.
    Print out the results and check your answers.
    Change the value of the edge and ensure the results are still correct.
'''

edge = 10
print("-----------------------------------\n            PART 1.2")
# YOUR CODE GOES HERE

cube_diagonal = math.sqrt(3) * edge
cube_surfaceArea = 6*edge**2
cube_volume = edge**3

print(f"diagonal = {cube_diagonal}\nsurface area = {cube_surfaceArea} \nvolume = {cube_volume}")


######### Part 2 ###########

'''
    1)  For each of the following Python expressions, write down the output value. If it would give an error then write error.

                (a)False == 0
                
                (b) True != 1
                
                (c) 40 // 2
                
                (d) 41 // 2
                
                (e) 41 % 2
                
                (f) True + 1.33
                
                (g) False - `True'
                
                (h) False + \True"
                
                (i) 15/7+5*8**4
                
                (j) ('Hello' == 'Hi') or ( 12 > -6 )

'''
# YOUR CODE GOES HERE


'''

a) true
b) false
c) 20
d) 20
e) 1
f) error data types dont match
g) error data types dont match
h) error data types dont match
i) 20482.142
j) true

 
'''


######### Part 3 ###########


'''
    1) write a python code to calculate the age based on the user's birthdate (the year of birth, e.g.: age = 1989), if age is greater than 18 then outputs “adults' category” otherwise outputs “Children Category”.

'''

year = 1989
print("-----------------------------------\n            PART 3.1")
# YOUR CODE GOES HERE

currentYear = 2020
age = currentYear - year

if(age > 18):
    print("adults")
else:
    print("“Children Category”")

'''
	2) Repeat q1:
    If the year is not within 1910-2020 then prints an error message for the user
    Otherwise: calculates his/her age, if age is greater than 18 then outputs “adults' category” otherwise outputs “Children Category”.

'''

year1 = 1989
year2 = 1857

year = year2
print("-----------------------------------\n            PART 3.2")

# YOUR CODE GOES HERE
if(year >= 1910 and year <= 2020):
    if((2020 - year) > 18):
        print("adults")
    else:
        print("“Children Category”")
else:
    print("Error message: Year is out of bounds. 1910 - 2020")
   
######### Part 4 ###########


'''
    1) Write a python code to print all the perfect square numbers less than 300.
'''
print("-----------------------------------\n            PART 4.1")
# YOUR CODE GOES HERE

number = 1
perfect_square = number**2
while(perfect_square < 300):
    print(f"{number}^2 = {perfect_square}")
    number+=1
    perfect_square = number**2
    
    

'''
    2) Write a python code to print all the perfect square numbers less than 300 and greater than 20 except for 100 and 121.
'''
print("-----------------------------------\n            PART 4.2")
# YOUR CODE GOES HERE
def perfectSquareFunc(lessThan, greaterthan, *exclude):
    flag = True
    number1 = 1
    perfectSquare = number1**2
    while(flag):
        if(perfectSquare > greaterthan and perfectSquare < lessThan and not any(perfectSquare in i for i in exclude)):
            print(f"{number1}^2 = {perfectSquare}")
        number1 += 1
        perfectSquare = number1**2
        if(perfectSquare > 300):
            flag = False
            
perfectSquareFunc(300, 20, (100, 121))

'''
    3) Write a python code to calculate 100*101*102...*200
'''
print("-----------------------------------\n            PART 4.3")
# YOUR CODE GOES HERE

total = 1
for i in range(100, 201, 1):
    total *= i
    
print(total)

######### Part 5 ###########

'''
    1) Given a list of values: x = [1,'ok',3, 17.01, True]
    Write a code to print the last element of it
'''
print("-----------------------------------\n            PART 5.1")
# YOUR CODE GOES HERE

x = [1,'ok',3, 17.01, True]
 
print(x[len(x) - 1])

'''   2) Given a list of integers: e.g.: 
        (a) return the average
        (b) return the list resulted from adding up each number with its index. e.g.: output:[1,3,5,5,4]
        (c) given another list, return their common elements. e.g.: SecondList = [1; 1; 2; 2; 2; 2; 4; 6; 7; 88; 8], output :[1,2]
      
        
'''
print("-----------------------------------\n            PART 5.2a")
  # YOUR CODE GOES HERE

def listAverage(list):
    total = 0
    for i in list:
        total+=i
    return total

list = [1,2,3,2,0]
print(listAverage(list))
print("-----------------------------------\n            PART 5.2b")
def sumToIndex(list):
    resultList = list
    for i in range(0, len(list), 1):
        resultList[i] = list[i] + i
    return resultList

print(sumToIndex([1,2,3,4,5]))

print("-----------------------------------\n            PART 5.3")

def commonElements(list2):
    result = []
    for i in range(0, len(list2), 1):
        for j in range(0, len(list2), 1):
            if(list2[i] == list2[j] and i != j):
                result.append(list2[i])
                break
    return result
            
print(commonElements([1,1,2,2,2,2,2,3,4,5,6]))
print("need some working on lol")           
   
######### Part 6 ###########

'''
    1)  Write a function to find the even numbers in the list and return a list of those numbers:
        e.g.: list1 = [9,-6, 0, 7, 1, 5, 6, 8]-->[-6, 0, 6, 8]
'''
print("-----------------------------------\n            PART 6.1")
# YOUR CODE GOES HERE

def FindEvens(list1):
    ListOfEvens = []
    for x in list1:
        if(x % 2 == 0):
            ListOfEvens.append(x)
    return ListOfEvens


print(FindEvens([9,-6, 0, 7, 1, 5, 6, 8, 10, 12, 14]))

'''
    2)  Write a function to find the odd numbers in the list and return a list of their indices: e.g.: list1 = [9,-6, 0, 7, 1, 5, 6, 8] --> [0,3,4,5]
'''
print("-----------------------------------\n            PART 6.2")
# YOUR CODE GOES HERE
######### Part 7 ###########

def FindOddIndexs(list3):
    indexList = []
    for x in range(0, len(list3)):
        if(list3[x] % 2 != 0):
            indexList.append(x)
    return indexList

print(FindOddIndexs([9,-6, 0, 7, 1, 5, 6, 8]))

'''
    1) Write a function to get a message as an input and to replace all instances of ‘o’ with ’a’ and to return the updated message.
'''
print("-----------------------------------\n            PART 7")

# YOUR CODE GOES HERE

def replace():
    inputStr = input("Enter a string => ")
    inputStr = inputStr.replace('o', 'a')
    return inputStr

print(replace())
######### Part 8 ###########
'''
    1) Write a function to drop the duplications in a list of numbers.
    (Hint: use dictionary)  e.g.: 
    Input_list = [11,2,3,8,0,11,4,2,2,7,0]-->[11,2,3,8,0,4,7]

'''
print("-----------------------------------\n            PART 8")

# YOUR CODE GOES HERE

def dropDup(ListDup):
    newList = dict.fromkeys(ListDup)
    newList = dict.keys(newList)
    return newList


print(dropDup([11,2,3,8,0,11,4,2,2,7,0]))
######### Part 9 ###########
'''
    1) Write a function to get the radius of a circle and to return its area. (import pi and exponentiation from math module)
    
'''  
print("-----------------------------------\n            PART 9")  
# YOUR CODE GOES HERE

def AreaOfCirlce(radius):
    return math.pi * (radius ** 2)

print(f"Area: {AreaOfCirlce(12.2)}")

######### Part 10 ###########  
'''
   1) Write a python function to find the frequency of the characters in a sentence.
(Hint : Use a dictionary)

e.g.:  ‘Hhellloo’      {‘H’:1 , ‘h’: 1, ‘e’:1, ‘l’:3 , ‘o’:2}
    
'''  
print("-----------------------------------\n            PART 10")
# YOUR CODE GOES HERE

def frequencyFunc(str1):
    dicResult = {}
    for x in str1:
        if(x not in dicResult):
            dicResult[x] = 1
        else:
            dicResult[x] += 1

    print(dicResult)
frequencyFunc("Hhellloo")




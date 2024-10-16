import string

#1.Function getsum to get sum of two numbers?

# Exact syntax of python function
def getSum(num1:int ,num2:int)-> int:
    sum=num1+num2;
    return sum;
#function invocation
def invoke_getSum():
    result=getSum(2,3) 
    print("sum of two numbers is ",result)

# you can also written function like this
def getsum(number1,number2):
    return number1+number2

def invoke_getsum():
    print("enter two number to add")
    a=int(input("enter a"))
    b=int(input("enter b"))
    sum=getsum(a,b)
    print(f"sun of {a} and {b} is {sum}")

#2.Function swapnumbers to swap two variables values?

def swapnumber(num1,num2):
    temp=num1
    num1=num2
    num2=temp
    return num1,num2
def invok_swapnumber():
    number1=10
    number2=20
    print(f"before swap::number1={number1}and number2={number2}")
    number1,number2=swapnumber(number1,number2)
    print(f"After swap::number1={number1}and number2={number2}")

def swapSimple(num1,num2):
    return num2,num1

def invoke_swapsimple():
    number1=10
    number2=20
    print(f"before swap::number1={number1}and number2={number2}")
    number1,number2=swapSimple(number1,number2)
    print(f"After swap::number1={number1}and number2={number2}")

#3.Function isEven to return if number is even otherwice false?

def isEven(number):
    if(number%2==0):
        return True
    else:
        return False
    
def invoke_isEven():
    num=-2
    if(isEven(num)):
        print(f"{num} is even numbar")
    else:
        print(f"{num} is not even")


#4.Function is Digit to return true if it is true?

def isNumber(str):
    flag=True
    for char in str:
        if(char>='0' and char<='9'):
            continue
        else:
            flag=False
            break
    return flag
def invoke_isNumber():    
    str=input()        
    result=isNumber(str)
    if(result):
        print("enterd str is number");
    else:
        print("enterd str is not a number")

def isNumber_v2(str):
    for char in str:
        if(char < '0' or char > '9'):
            return False

    return True

def invoke_isNumber_v2():
    number="32"
    if(isNumber_v2(number)):
        print(f"{number} is  a number")
    else:
        print(f"{number} is is not a number")

#5.Function getgreeting by accepting name and print greeting with name?

def getGreeting(name):
    print("hello,",name)
    print(f"how are you {name}")

def invoke_getGreeting()->None:
    name=input("enter a name to get greeting to that name>>")
    getGreeting(name)

#6.Functionto print ASCII values of string input?

def print_ASCII(str):
    for ele in str:
        print(f"{ele}->",ord(ele)) #in python ord is a built in function to print ASCII value

def invoke_print_ASCII():
    print_ASCII("3497")


#7.Function getstrlength to get String to get string length?

def getStringLength(str):
    count=0
    if(str!=None):      
        for ele in str:
            count=count+1

    return count
def invoke_getStringLength():
    name="hello to all"
    length=getStringLength(name)
    print(length)


  #8.Function getCOUNTOfOvewel to count ovewels in given string?

def getCOUNTOfOvewel(str):
    count=0
    if(str==None):
        return count
    for ch in str:
        if(ch>='A' and ch<='Z'):
            ch=ord(ch)+32
            ch=chr(ch)
            
        if(ch=='a' or ch=='e' or 
           ch=='i' or ch=='o' or
            ch=='u'):
            count+=1
    return count

def invoke_getCOUNTOfOvewel():
    input1=None
    print(getCOUNTOfOvewel(input1))
    input2="None"
    print(getCOUNTOfOvewel(input2))
    input3=""
    print(getCOUNTOfOvewel(input3))

#9.Function to reverse a string using other memory and also in same memory?

#In python variables are immutable so we can not be overwrite the variables
#it always stores in the new variables (old variables are freed by the garbage collecter) 
def reversString(string):
    length=len(string)
    for ele in range(length-1,-1,-1):
        print(string[ele],end="")

def invoke_reversString():
    name="hello"
    reversString(name)

#10.Function to revers List elements?

def reversList(numbers):
    revers=[]
    end=len(numbers)-1
    for ele in range(end,-1,-1):
        revers.append(numbers[ele])
    
    return revers

def invoke_reversList():
    marks=[10,20,30]
    result=reversList(marks)
    print(result)

# Sum of element in a list

def getSum(numbers):
    sum=0
    for i in numbers:
        sum+=i

    return sum

list= [10,63,1.32]
SUM=getSum(list)
print(SUM)

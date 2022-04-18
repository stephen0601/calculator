# using functions for operations
def add(x,y):
    return (x+y)    
#addition
def sub(x,y):
    return (x-y)
def mult(x,y):
    return (x*y)
#multiplies
def division(x,y):
    return (x / y)
#divides
def power(x,y):
    return(x**y)
#exponents
continue_ = True
while continue_ == True:
    message = 'Please type in what operation you want, using the first letter of the operation. (a for add, s for subtract, m for multiply, d for division, p for power)'
    print(message)

    operation = input("Enter operation here: ")

    if operation in ('a', 's', 'm', 'd', 'p'):
        xchoice = float(input("Please type in your first value : "))
        ychoice = float(input("Please type in your second value : "))
    if operation == 'a':
        print(xchoice, "+", ychoice, '=' , add(xchoice, ychoice))
    
    elif operation == 's':
        print(xchoice, '-' , ychoice, '=' , sub(xchoice, ychoice))
    
    elif operation == 'm':
        print(xchoice, '*' , ychoice, '=' , mult(xchoice, ychoice))
        
    elif operation == 'd':
        print(xchoice , '/' , ychoice , '=' , division(xchoice , ychoice))
        
    elif operation == 'p':
        print(xchoice, '**', ychoice, '=', power(xchoice , ychoice))
                                                #calls functions
    readstring = input("Do you want to keep on going? (yes/no): ")
    if readstring == "no":
        quit()
    if readstring == "yes":
        continue_ == True

else: 
    print("Error, please try again.")

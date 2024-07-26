import random
def check(Computer,User):
    
  
    if(Computer == User ):
        print("Draw!")
    elif(Computer == 0 and User == 1):
        print("Computer win!")
    elif(Computer == 1 and User == 2):
        print("Computer Win!")
    elif(Computer == 2 and User == 0):
        print("Computer Win!")

    else:
        print("You Win!")

Computer = random.randint(0,2)
print("---------Welcome to Snake ,Water and Gun Game ---------")
print("0 for Snake , 1 for Water ,2 for Gun")
User = int(input("Enter your choice: "))
if(User>2):
    print("Invalid Input!")
    print("please press 0 to 2 ")
else:

   print("Computer's Choice- :",Computer)
   print("User's Choice -",User)
   check(Computer,User)
   
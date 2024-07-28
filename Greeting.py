



import time 
t = time.strftime('%H:%M:%S')
hour = int(time.strftime("%H"))
name = input("Enter Your Name :")

# print(hour)
if hour >= 0 and hour < 12:
    print("Good Morning!",name)
elif hour>=12 and hour <17:
    print("Good Afernoon!",name)
elif hour>= 17 and hour > 0:
    print("Good Night!",name)




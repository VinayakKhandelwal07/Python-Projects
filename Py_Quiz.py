3
questions = [
    ["1: What is the output of the following code: print(type([]))?", 
      "<class 'tuple'>", "<class 'dict'>", "<class 'set'>","<class 'list'>", 4],
    ["2: Which of the following is used to define a function in Python?", 
     "define", "function", "def","func", 3],
    ["3: How do you insert comments in Python code?", 
     "/* This is a comment*/", "// This is a comment", "# This is a comment", "<!-- This is a comment -->", 3],
    ["4: Which method can be used to return a string in upper case letters?", 
     "upper()", "uppercase()", "toUpperCase()", "upcase()", 1],
    ["5: What is the correct file extension for Python files?", 
     ".pyt", ".python", ".py", ".p", 3],
    ["6: Which keyword is used to create a class in Python?", 
     "tuple", "class", "object", "new", 2],
    ["7: What is the output of the following code: print(2**3)?", 
     "8", "6", "9", "5", 1],
    ["8: Which of the following data types is immutable?", 
     "set", "list", "dictionary", "tuple", 4],
    ["9: What is the output of the following code: print('Hello' + 'World')?", 
     "HelloWorld", "Hello World", "Hello+World", "Hello", 1],
    ["10: Which of the following is a valid variable name in Python?", 
     "_my_var", "$my_var", "my var", "2myvar", 1]
]

# Scores for each correct answer
score_values = [10, 10, 10, 10, 10, 10,10, 10, 10, 10]

points = 0
count = 0

print("\n||-----------------Welcome to Basic Python Quiz----------------||\n")

for question in questions:
    print(question[0])
    print(" ")
    print('1.', question[1])
    print('2.', question[2])
    print('3.', question[3])
    print('4.', question[4])
    print(" ")
    answer = int(input("Enter the option number or press 0 to quit: "))
    
    if answer == 0:
        confirm_quit = int(input("Are you sure you want to quit? Press 1 for Yes or 0 to continue the quiz: "))
        if confirm_quit == 1:
            print("Your score is:", points)
            break
        else:
            print("Welcome back to the quiz!")
            continue

    if answer == question[-1]:
        points += score_values[count]
        count += 1
        print("Correct Answer!\n")
    else:
        print("Wrong Answer!")
        print("\nThe correct answer is option:", question[-1], '\n')
        print("Your final score is:", points)
        break
    
    if count == len(questions):
        print("Congratulations!!")
        print("Your final score is:", points)
        break

if points <= 30 :
    print("Ouch! Better luck next time") 
    
# elif points <= 70:
#     print("Bravo! You are Good ")
# else :
#     print("Brilliant! You are Amazing!")
print(" ")
print("Thank You for playing the quiz!")

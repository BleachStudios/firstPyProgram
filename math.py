# python Math question generator
import random
# ask user for question type
questionType = input("What type of question would you like? +, -, * or /? ")

def q(qt):
    global ans
    global num1
    global num2
    global score
    global userAns
    score = 0
    if qt == "+":
        #addition
        print("You Selected addition!")
        num1 = random.randint(-99,99)
        num2 = random.randint(-99,99)
        ans = num1 + num2
        userAns = input("Whats is "+ str(num1) +" + "+ str(num2) +"? ")
        userAns = int(userAns)
        if userAns == ans:
            print("You are right!")
            score += 1
        else:
            print("You are wrong!")
            print("The correct answer was: ", ans)
    elif qt == "-":
        #subtraction
        print("You Selected subtraction!")
        num1 = random.randint(-99,99)
        num2 = random.randint(-99,99)
        ans = num1 - num2
        userAns = input("Whats is "+ str(num1) +" - "+ str(num2) +"? ")
        userAns = int(userAns)
        if userAns == ans:
            print("You are right!")
            score += 1
        else:
            print("You are wrong!")
            print("The correct answer was: ", ans)
    elif qt == "*":
        #multiplication
        print("You Selected multiplication!")
        num1 = random.randint(-99,99)
        num2 = random.randint(-99,99)
        ans = num1 * num2
        userAns = input("Whats is "+ str(num1) +" * "+ str(num2) +"? ")
        userAns = int(userAns)
        if userAns == ans:
            print("You are right!")
            score += 1
        else:
            print("You are wrong!")
            print("The correct answer was: ", ans)
    elif qt == "/":
        #division
        print("Your answer will be rounded to the nearest tenth")
        print("You Selected division!")
        num1 = random.randint(-99,99)
        num2 = random.randint(-99,99)
        ans = num1 / num2
        userAns = input("Whats is "+ str(num1) +" / "+ str(num2) +"? ")
        userAns = float(userAns)
        ans = round(ans,1)
        if userAns == ans:
            print("You are right!")
            score += 1
        else:
            print("You are wrong!")
            print("The correct answer was: ", ans)
    else:
        print("Please enter a valid operation, such as +, -, * and /")
        qt = input("What type of question would you like? +, -, * or /? ")
        q(qt)
def again():
    #ask user if they wanna play again
    question = input("Would you like to play again? Y/N ")
    question = question.upper()
    if question == "Y":
        questionType = input("What type of question would you like? +, -, * or /? ")
        #wrap functions around
        q(questionType)
        again()
        return
    else:
        print("Hope you enjoyed your stay!")
        return
q(questionType)    
again()


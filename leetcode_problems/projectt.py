print("*" * 50)
print('\t', '\t', "CHECK YOUR IQ ")
print("*" * 50)
print("Hey Hi Hello friends ", '\n', "We are charu and Rohini", '\n', "welcome to our IQ test")
print("Have you already visited our IQ test?")
n = input()
if n == "yes" or n == "YES" or n == "Yes":
    print("OK friends thanks for coming to check your IQ\n")
    name = input("please enter your name=")
else:
    name = input("Please input your name=")
    password = int(input("Enter the four digit number as password="))
print("Let's start")
print("There are various ways to check input IQ")
print("They are")
print('\t', "MATHEMATICAL")
print('\t', "FUNNY")
print('\t', "GENERAL KNOWLEDGE")
print('\t', "LOGICAL")
print('\t', "SCIENTIFIC")
print('\t', "PROGRAM and so on ")
while True:
    print("If you want to leave enter NONE")
    type_Quiz = input(
        "Enter the type of Quiz you want(Funny,logical,mathematical,program,general knowledge,scientific)=")
    print()
    if type_Quiz == "Mathematical":
        question = ["Which one of the numbers not belong in the following series [2,3,6,7,8,14,15,30]",
                    "1/4 of 1/2 of 1/5 of 200=", "What is the missing number in the sequence [1,8,27,X,125,216]=",
                    "Which one of the numbers do not belong in the following series[1,2,5,10,13,26,29,48]=",
                    "sin(90)+cos(90)", "solve x**2-4*x+4", "cos**(30)+sin**(30)"]
        answer = ["8", "5", "64", "48", "1", "2", "1"]
        point = 0
        for a in range(len(question)):
            print(question[a])
            ans = input("Enter the answer for above question=")
            if ans == answer[a]:
                print("Your answer is correct!\n")
                point = point + 1
            else:
                print("Sorry your answer is wrong\n")
        print("-" * 30)
    elif type_Quiz == "Funny":
        question = ["What has keys but can't open locks?", "I speak without a mouth and hear without ears. What am I?",
                    "What comes once in a minute, twice in a moment, but never in a thousand years?",
                    "What do you call a fish with no eyes?", "What's a vampire's favorite fruit?",
                    "What gets wetter as it dries?"]
        answer = ["piano", "telephone", "m", "fsh", "blood orange", "towel"]
        point = 0
        for a in range(len(question)):
            print(question[a])
            ans = input("Enter the answer for above question=")
            if ans == answer[a]:
                print("Your answer is correct!\n")
                point = point + 1
            else:
                print("Sorry your answer is wrong\n")
        print("-" * 30)
    elif type_Quiz == "general knowledge":
        question = ["What is the capital city of Australia?", "Which gas do plants absorb during photosynthesis?",
                    "In which year did Christopher Columbus reach the Americas?",
                    "Who wrote the play Romeo and Juliet?", "Who is known as the King of Pop?",
                    "What is the value of π (pi) to two decimal places?",
                    "What is the largest planet in our solar system?"]
        answer = ["canberra", "carbon dioxide", "1492", "william shakespeare", "michael jackson", "3.14", "jupiter"]
        point = 0
        for a in range(len(question)):
            print(question[a])
            ans = input("Enter the answer for above question=")
            if ans == answer[a]:
                print("Your answer is correct!\n")
                point = point + 1
            else:
                print("Sorry your answer is wrong\n")
        print("-" * 30)
    elif type_Quiz == "logical":
        point = 0
        question = [
            " I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            "The more you have of it, the less you see. What is it?",
            " If you drop me, I'm sure to crack, but give me a smile, and I'll always smile back. What am I?",
            "The more you take, the more you leave behind. What am I?",
            "What 5-letter word becomes shorter when you add two letters to it?",
            "If you rearrange the letters CIFAIP you would have a name of an_________"]
        answer = ["echo", "darkness", "mirror", "foot step", "short", "ocean"]
        for a in range(len(question)):
            print(question[a])
            ans = input("Enter the answer for above question=")
            if ans == answer[a]:
                print("Your answer is correct!\n")
                point = point + 1
            else:
                print("Sorry your answer is wrong\n")
        print("_" * 30)
    elif type_Quiz == "program":
        point = 0
        qa = {"range(10,2,-2)": "[10,8,6,4,2]", "How to create a dictionary?": "dict()", "Output for 14>=14": "True",
              "Output for 10/2": "5.0", "what is the list function to find the element": "index()",
              "What error will appear when unknown key is searched ?": "Key error"}

        for i in qa:
            ans = input(i + "")
            if ans == qa[i]:
                print("Your answer is correct!\n")
                point = point + 1
            else:
                print("Sorry your answer is wrong\n")
        print("_" * 30)
    elif type_Quiz == "scientific":
        question = ["what is the electric current?", "What is the atomic number of carbon?",
                    "What is the ph scale value of water?", "What is the SI unit of force?",
                    "What is the chemical formual for gold?", "How many types of quantum numbers are there?",
                    "What is the SI unit of energy?", ]
        answer = ["ampere", "12", "7", "newton", "au", "4", "joule"]
        point = 0
        for a in range(len(question)):
            print(question[a])
            ans = input("Enter the answer for above question=")
            if ans == answer[a]:
                print("Your answer is correct!\n")
                point = point + 1
            else:
                print("Sorry your answer is wrong\n")
        print("-" * 30)
    else:
        print("Other type quiz are not present")
        break

print("The user had sourced=", point, "points")
if point >= 6:
    print("Your IQ is very high")
elif 4 <= point <= 5:
    print("Your IQ is good")
else:
    print("You can try again")
user = dict()
print("number of question you want to enter=")
n = eval(input())
for i in range(0, n):
    q = input("Enter the question=")
    ans = input("Enter the correct answer=")
    user[q] = ans
print(user)
print('\t', '\t', '\t', "HISTORY OF OUR WEBSITE ")
marks = {name: point}
print(marks)
print("Provide rating your our website")
rate = int(input())

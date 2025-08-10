print("welcome to the game!!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Great! Let's start the game.")
print("Here are the rules:")
print("1. You will be asked a series of questions.")
print("2. Type your answer and press Enter.")
print("3. You will get feedback on your answer.")
print("4. Try to answer as many questions correctly as you can.")
print("5. answer all question in lowercase")
print("Let's begin!")

score = 0

answer = input("What is the capital of France? ")
if answer == "paris":
    print("Correct! Paris is the capital of France.")
    score += 1
else:
    print("Incorrect. The correct answer is Paris.")

answer = input("What is 2 + 2? ")
if answer == "4":
    print("Correct! 2 + 2 equals 4.") 
    score += 1  
else:
    print("Incorrect. The correct answer is 4.")
answer = input("What is the largest planet in our solar system? ")
if answer == "jupiter":         
    print("Correct! Jupiter is the largest planet in our solar system.")
    score += 1
else:
    print("Incorrect. The correct answer is Jupiter.")
answer = input("What is the chemical symbol for water? ")
if answer == "h2o":
    print("Correct! The chemical symbol for water is H2O.")
    score += 1
else:
    print("Incorrect. The correct answer is H2O.")
answer = input("What is the smallest prime number? ")
if answer == "2":
    print("Correct! The smallest prime number is 2.")
    score += 1
else:   
    print("Incorrect. The correct answer is 2.")
answer = input("What is the capital of Japan? ")
if answer == "tokyo":
        print("Correct! Tokyo is the capital of Japan.")
        score += 1
else:
        print("Incorrect. The correct answer is Tokyo.")

print("Game over! Your final score is: " + str(score / 6 * 100) + " %")
print("Thank you for playing! Hope you had fun.")
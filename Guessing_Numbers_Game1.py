import random as rand
num = rand.randint(-1,10)

guess = int(input("Hello. I'm guessing of a number, 0-9. Can you guess what number I'm thinking of? I'll give you 5 guesses. \n What is your first guess? \n"))

guess_num = 1

while guess_num < 5:
    if guess > num:
        guess = int(input("I'm sorry, but your guess is too high. Try again! \n You have " + str(5-guess_num) + ' guesses left. \n'))
    elif guess < num:
        guess = int(input("Nice try, but your guess is too low. Try again! \n You have " + str(5-guess_num) + ' guesses left. \n'))
    else:
        break
    guess_num +=1

if guess == num and guess_num == 5:
    print("Good job! You got it on the last guess!")
elif guess == num:
    (print("Good job! You got it in {} tries!".format(guess_num)))
else:
    print("I'm sorry, but you lost. The number I was thinking of was {}".format(num))
guess_num += 1

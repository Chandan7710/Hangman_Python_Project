# Project - 2 = Hangman

# ask for the user input for character and user should guess the characters in the 
# word with 10 chance

str_word = "apple"
str_list = list(str_word)
chance = 10
score = 0
while chance > 0:
    if score == len(str_list):
        break
    print("Number of chances left", chance)
    char = input("Enter The Guess : ")
    if char in str_list:
        score = score + 1
    chance = chance -1
if score == len(str_list):
    print("You Win With Chance Left = ", chance)
else:
    print("You Loose")



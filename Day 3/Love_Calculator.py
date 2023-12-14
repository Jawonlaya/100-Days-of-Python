'''
Instructions
💪 This is a difficult challenge! 💪
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

These functions will help you:
lower() count()

Example Input 1

'''

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

comb_names = (name1 + name2).lower()

comb_names.count("t")
comb_names.count("r")
comb_names.count("u")
comb_names.count("e")
true = int(comb_names.count("t") + comb_names.count("r") + comb_names.count("u") + comb_names.count("e"))

comb_names.count("l")
comb_names.count("o")
comb_names.count("v")
comb_names.count("e")
love = int(comb_names.count("l") + comb_names.count("o") + comb_names.count("v") + comb_names.count("e"))

score = int(f"{true}{love} ")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos. ")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together. ")
else:
    print(f"Your score is {score}.")

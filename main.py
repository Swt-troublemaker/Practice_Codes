print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1 + name2
name3 = name.lower()
t = int(name3.count('t'))
r = int(name3.count('r'))
u = int(name3.count('u'))
e = int(name3.count('e'))
l = int(name3.count('l'))
o = int(name3.count('o'))
v = int(name3.count('v'))
e = int(name3.count('e'))
true = t + r + u + e
love = l + o + v + e
love_score = int(str(true) + str(love))
if (love_score < 10) or (90 < love_score):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

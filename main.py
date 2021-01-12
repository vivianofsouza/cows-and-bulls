from myfile import count
import random
value = ""
digits = ""
guess = ""
counter = 0

digits = random.sample(range(1,10),4)
for i in range(len(digits)):
    value+=str(digits[i])

while(guess != value):
    if(guess == value):
        break
    guess = input("Enter a guess. ")
    counter += 1
    count(str(value), str(guess))
    
print("You've won! It took you " + str(counter) + " tries.")
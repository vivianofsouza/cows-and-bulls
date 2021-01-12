def count(value, guess):
    cows = 0
    bulls = 0
    for i in range(len(guess)):
        if guess[i] == value[i]:
            bulls += 1
        elif value.find(guess[i]) != -1:
            cows += 1
    print("You have " + str(cows) + " cows and " + str(bulls) + " bulls.")
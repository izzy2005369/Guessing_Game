import random

numbers = range(51)
guess = random.choice(numbers)

over = 0
limit = 10
user = ''
out_of_guesses = False
points = 10

def hint():
    range1 = [0,1,2,3,4,5,6,7,8,9,10]
    range2 = [11,12,13,14,15,16,17,18,19,20]
    range3 = [21,22,23,24,25,26,27,28,29,30]
    range4 = [31,32,33,34,35,36,37,38,39,40]
    range5 = [41,42,43,44,45,46,47,48,49,50]

    for number in range1:
        if number == guess:
            print('Hint: 7')
        
    for number in range2:
        if number == guess:
            print('Hint: 15')
        
    for number in range3:
        if number == guess:
            print('Hint: 27')
        
    for number in range4:
        if number == guess:
            print('Hint: 31')
        
    for number in range5:
        if number == guess:
            print('Hint: 47')
        

while user != guess and not(out_of_guesses):
    if over < limit:
        print(f'You have {points} scores') 
        user = int(input('Guess a number from the range of 0 - 50 : '))
        hint()
        points -= 1
        over += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print('You have 0 score, You lose!.')    
else:
    print('You get the number correctly, You win!.')    








    


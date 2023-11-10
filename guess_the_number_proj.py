"""
1. change the number range from 1 to 100000
2. game should ask us to guess the number
3. give a clue if th number is higher or lower than the guess
4. inform the player if he wone
"""
def game():
    
    from random import randint
    start=1
    end=1000

    value=randint(start, end)

    print("The computer choose a number between",start, "and",end)



    guess=None
    while guess!=value:
        
       text=input("guess the number :")
       guess=int(text)

       if(guess<value):
           
           print("Your guess is lower than the number")

       elif guess > value:
           
        
          print("Your guess is higher than the number")
       else:
           

          print("Congratulations  !! you guessed the number you wone")
#print("hello")
            
            

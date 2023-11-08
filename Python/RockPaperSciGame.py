import random
l=["Rock","Scissor","Paper"]

'''
rock vs paper:- paper wins
rock vs scissor:-rock wins
paper vs scissor:-scissor wins.
'''

while True:
    Ccount=0
    Ucount=0
    uc=int(input('''
Game Start...
1 Yes
2 No | Exit
               '''))
    if(uc==1):
       for i in range(1,6):
            uinput=int(input('''
1. Rock
2. ScPissor
3. Paper
                            '''))    
            if(uinput==1):
               uchoice="rock"
            elif(uinput==2):
               uchoice="Scissor"
            elif(uinput==3):
               uchoice="Paper"
            Cchoice=random.choice(l)
            if(Cchoice==uchoice):
               print("computer choice",Cchoice)
               print("user choice",uchoice)
               print("Game Draw")
               Ucount=Ucount+1
               Ccount=Ccount+1
            elif(uchoice=="rock" and Cchoice=="Scissor") or (uchoice=="Paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="Paper"):
                print("computer choice",Cchoice)
                print("user choice",uchoice)
                print("You win")
                Ucount=Ucount+1
            else:
                print("computer choice",Cchoice)
                print("user choice",uchoice)
                print("computer win")
                Ccount=Ccount+1
       if(Ucount==Ccount):
         print("Final Game Draw")
         print("User Score",Ucount)
         print("Computer Score",Ccount)
       elif(Ucount>Ccount):
         print("Final you win the Game")
         print("User Score",Ucount)
         print("Computer Score",Ccount)
       else:
         print("Final computer win the Game")
         print("User Score",Ucount)
         print("Computer Score",Ccount)    
    else:
      break
                
                
                
            
         

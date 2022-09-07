'''The game() function in a program kets a user play a game and returns 
the score as an integer. You need to read a file 'Hiscore.txt' which is 
either blank or contains the previous Hi_score you need to write a program to update 
the Hi_score whenever game() breaks the Hi_score .'''



def game():
    return 4567


score = game()
with open("hiscore.txt") as f:
    hiscorestr = f.read()

if  hiscorestr =='':
    with open("hiscore.txt" , "w") as f:
        f.write(str(score))


elif int(hiscorestr)<score:
    with open("hiscore.txt" , "w") as f:
        f.write(str(score))     
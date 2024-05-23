import random
def cardverify(cno,p):
    cno=int(input())
    if 'H7' in p[cno-1]:
        p[cno-1].remove('H7')
        return cno
    else:
        print("Invalid Card!!!.Try Again")
        return cardverify(cno,p)
def verify(ecard,play,p,p1):
    play=play%4
    print("==============================================================================")
    print("Current Cards are:-\n")
    print(*p1)
    if play==0 and len(p[3])==0:
        print("Player 4 is the Winner")
    elif play!=0 and len(p[play-1])==0:
        print("Player ",play, " is the winner")
    else: 
        print("Now Player ",play+1,"Turn:-\n")
        print(p[play])
        ecard=input("Choose a Suitable Card from your Cards or Pass P:-\n").upper()
        if(ecard in p[play]) and (ecard not in p1[a.index(ecard[0])]) and (len(p1[a.index(ecard[0])])<15) and (ecard[0] in a):      
            ind=a.index(ecard[0])
            if ecard[-1]=='7':
                p1[ind].append(ecard)
                p[play].remove(ecard)
                play+=1
                return verify(ecard,play,p,p1)
            elif (ecard[:1]+'7' in p1[ind]) and (ecard[1:3]=='10'):
                if(ecard[:1]+str(int(ecard[1:3])-1) in p1[ind]):
                    p1[ind].append(ecard)
                    p[play].remove(ecard)
                    play+=1
                    return verify(ecard,play,p,p1)
                else:
                    print("Invalid Card!!! Try Again\n")
                    return verify(ecard,play,p,p1)
            elif (ecard[:1]+'7' in p1[ind]) and (ecard[1:3]=='J' or ecard[1:3]=='Q' or ecard[1:3]=='K'):
                if (ecard[1:3]=="J" and (ecard[:-1]+"10" in p1[ind])):
                    p1[ind].append(ecard)
                    p[play].remove(ecard)
                    play+=1
                    return verify(ecard,play,p,p1)
                elif(ecard[1:3]=="Q" and (ecard[:-1]+"J" in p1[ind])):
                    p1[ind].append(ecard)
                    p[play].remove(ecard)
                    play+=1
                    return verify(ecard,play,p,p1)
                elif(ecard[1:3]=="K" and (ecard[:-1]+"Q" in p1[ind])):
                    p1[ind].append(ecard)
                    p[play].remove(ecard)
                    play+=1
                    return verify(ecard,play,p,p1)
                elif(ecard[1:3]=="A" and (ecard[:-1]+"2" in p1[ind])):
                    p1[ind].append(ecard)
                    p[play].remove(ecard)
                    play+=1
                    return verify(ecard,play,p,p1)
                else:
                    print("Invalid Card!!! Try Again\n")
                    return verify(ecard,play,p,p1)
            elif (ecard[:1]+'7' in p1[ind]) and ((ecard[:-1]+str(int(ecard[-1])-1) in p1[ind]) or (ecard[:-1]+str(int(ecard[-1])+1) in p1[ind])):
                p1[ind].append(ecard)
                p[play].remove(ecard)
                play+=1
                return verify(ecard,play,p,p1)
            else:
                print("Invalid Card!!!Try Again \n")
                return verify(ecard,play,p,p1)
        elif ecard=='P':
            play+=1
            return verify(ecard,play,p,p1)
        else:
            print("Invalid Card !! Try Again!!! \n")
            return verify(ecard,play,p,p1)
# Step 1: Initialize the deck
print("\tWelcome to Cards Game:")
print("========================================\n")
print("\tRules:-")
print("--------------------------")
print("Rule 1:- Game Starts with the Card - 'H7'.Player who holds the Card - 'H7' should Enter the Player Number\n")
print("Rule 2:- From there, Every Next Player is eligible to place card if he holds:-\n\t i) Either Preceeding or Succeeding Card of before Card\n\t ii) Or Another symbol with 7 number card\n")
print("Rule 3:- If a Player doesn't have a card from 2 cases,then the Player should Enter Pass as 'p'\n")
print("Rule 4:- Atlast who places the last card and don't have any other cards with the player, then that player is the Winner\n")
a=['C','D','H','S']
cno=0
ecard=''
p1=[["Clubs     ",],["Diamonds  ",],["Hearts    ",],["Spades    ",]]
ranks=['1','2','3','4','5','6','7','8','9','10','J','Q','K']
deck=[(suit,rank) for suit in a for rank in ranks]
random.shuffle(deck)
p=[[] for _ in range(4)]
for i in range(4):
    p[i] = deck[i::4]
    p[i] = [f'{j[0]}{j[1]}' for j in p[i]]
for i in range(4):
    print("Player",(i+1),":-",p[i],"\n")
print("Enter the Player Number who had Card -  H7:-")
fn=cardverify(cno,p)
p1[a.index('H')].append('H7')
play=fn%4
ver=verify(ecard,play,p,p1)
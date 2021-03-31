import sys

#Tic Tac Toe Game


def show(a,b,c):
    print(a[0]," | ",a[1]," | ",a[2],sep='')
    print(b[0]," | ",b[1]," | ",b[2],sep='')
    print(c[0]," | ",c[1]," | ",c[2],sep='')


def inp(u,a,b,c1):
    eh='y'
    while eh=='y':
        print("Player ",u," Please Enter")
        r=int(input("Row => "))
        c=int(input("Column => "))
        if (r==1 and a[c-1]=='  ') or (r==2 and b[c-1]=='  ') or (r==3 and c1[c-1]=='  '):
            if r==1:
                a[c-1]=u
                eh='n'
            elif r==2:
                b[c-1]=u
                eh='n'
            elif r==3:
                c1[c-1]=u
                eh='n'
        else:
            continue
        
        show(lst1,lst2,lst3)


def score():
    pass

def obs(a,b,c,u,scr1,scr2):
    n=0
    w='y'
    for i in range(0,3):
        if a[i]==b[i] and b[i]==c[i] and a[i]!='  ':
            n=1
    if a[0]==a[1] and a[2]==a[1] and a[0]!='  ':
        n=1
    elif b[0]==b[1] and b[2]==b[1] and b[0]!='  ':
        n=1
    elif c[0]==c[1] and c[2]==c[1] and c[0]!='  ':
        n=1
    elif a[0]==b[1] and b[1]==c[2] and a[0]!='  ':
        n=1
    elif a[2]==b[1] and b[1]==c[0] and c[0]!='  ':
        n=1
    if n==1:
        print("User ",u," Wins!!!")
        w='n'
        if u=='O':
            scr2+=1
        elif u=='X':
            scr1+=1
    elif a[0]!='  ' and a[1]!='  ' and a[2]!='  ':
        if b[0]!='  ' and b[1]!='  ' and b[2]!='  ':
            if c[0]!='  ' and c[1]!='  ' and c[2]!='  ':
                print("Draw!!!")
                if u=='O':
                    scr2+=1
                elif u=='X':
                    scr1+=1
                w='n'
    return w
    


def disscr(scr1,scr2):
    print("Player X Points : ",scr1)
    print("Player O Points : ",scr2)
    



 



print('''Welcome to the game of Tic Tac Toe
Two Players in a game
Decide
                Player 1
                &
                Player 2

Player 1 = X
Player 2 = O
''')

choice=input('If You Want to continue Press Y!').lower()


t='y'
scr1=0
scr2=0
while choice=='y':
    lst1=['  ','  ','  ']
    lst2=['  ','  ','  ']
    lst3=['  ','  ','  ']
    t='y'
    while t=='y':
        u='X'
        inp(u,lst1,lst2,lst3)
        t=obs(lst1,lst2,lst3,u,scr1,scr2)
        if t=='n':
            #disscr(scr1,scr2)
            continue
        
        
        u='O'
        inp(u,lst1,lst2,lst3)
        t=obs(lst1,lst2,lst3,u,scr1,scr2)
        if t=='n':
            #disscr(scr1,scr2)
            continue
    choice=input("\n\nPress y if you want to continue => ")






    

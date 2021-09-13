# THE GAME
#By Tobias Kooijman


# INTRO

print("_______________________________________________________________________________________________________________________")
print("Welcome to THE GAME")
print("")
Begin = input('Type START to begin or QUIT to quit ')
start = 0
if (Begin.lower() =="start"or"y"):
    Start = 1
elif (Begin.lower() =="quit"or"n"):
    exit()


# GAME BEGINNING

print("Starting game...")
import time
time.sleep(3)

print("loading assets...")
time.sleep(2)
print("done!")
print("")
print("")
print("----------------------------------------------------------------------------------------------------------------------")
print("")
print("")
time.sleep(2)
name = input('Type your name here: ')
time.sleep(1)
hello_01 = 'hello ' +str(name)
print(hello_01)
time.sleep(1)

# Name Easter Eggs

if (name.lower()=="tobias kooijman"):
    print("Wow what a cool name! you sound very smart and handsome!!")
elif (name.lower()=="king kong"):
    print("you sound just like you're mother. ha!")
elif (name.lower()=="hans smit"):
    print("you sound kinda gay ngl")
elif (name.lower()=="jelle bol"):
    print("BRO WHY DID YOU STEAL MY LIGHT BULLETS BRO, ok i'm leaving")
elif (name.lower()=="max hofman"):
    print("you sound like someone who would buy an gaming laptop just to not play any games on it")
elif (name.lower()=="joe"):
    print("Joe Mama! HA!")




#Start Game
die = 'Rest In Peace '+str(name) + ' you will not be remembered...'
bgn = 0
start_adventure = input('are you ready to start your adventure? (Yes/No) ')
if (start_adventure.lower()=="yes"):
    print("The game will now begin.")
    bgn = 1
elif (start_adventure.lower()=="no"):
    print("then why did you start this game?")
    time.sleep(1)
    print("what is wrong with you?")
    time.sleep(1)
    exit()
time.sleep(2)
if bgn == 1:
    print("_______________________________________________________________________________________________________________>")
    print("")
    print("")
    print("A long time ago there was a weird monkey called: ")
    time.sleep(1)
    print("your mother")
    time.sleep(1)
    print("now this was a very weird creature")
    time.sleep(1)
    print("this was because she was super strong")
    time.sleep(1)
    print("so strong in fact that some people gave her the nickname: King Kong")
    time.sleep(1)
    bullied = name + ' got bullied a lot in school because of this'
    print(bullied)
    time.sleep(1)
    print("good thing he killed all his bullies...")
    time.sleep(1)
    print("now he got arrested")
    time.sleep(1)
    print("you are now in a small cell, what will you do?")
    time.sleep(2)
    escape = 0
    wwyd_01 = input('Escape/Wait it out/just give up ')
    if (wwyd_01.lower() =="just give up"):
        print("you give up...")
        time.sleep(5)
        print("why are you still here?")
        time.sleep(1)
        print("you gave up")
        exit()
    elif (wwyd_01.lower()=="wait it out"):
        time.sleep(2)
        print("you wait it out...")
        time.sleep(4)
        print("still waiting")
        time.sleep(3)
        print("still here")
        time.sleep(3)
        print("you suddenly remember that you're in jail for life... you still continue to wait and die of old age")
        time.sleep(2)
        die_01_injail = 'Rest In Peace '+str(name) + ' you will not be remembered...'
        print(die_01_injail)
        time.sleep(1)
        exit()
    elif (wwyd_01.lower()=="escape"):
        time.sleep(1)
        print("you try to escape")
        time.sleep(2)
        print("IT WORKED!")
        time.sleep(1)
        print("it was kind of easy, none of the doors where locked...")
        time.sleep(1)
        print("but you're proud of yourself anyway!")
        escape = 1
    else:
        print("                                                  ERROR")
        time.sleep(1.5)
        print("you've entered a unvalid awnser, restart the program and enter a valid awnser!!")

if (escape==int("1")):
    time.sleep(1)
    print("you've now escaped the prison")
    time.sleep(1)
    print("you are now in a large field")
    time.sleep(1)
    print("there are 3 roads, one to the north, one to the east ans one to the south")
    time.sleep(0.5)
    print("what will you do?")
    wwyd_02 = input('go north/ go east/ go south ')
    time.sleep(1)
    if (wwyd_02.lower()=="go north"):
        print("you go north")
        time.sleep(1)
        print("you've been walking for 10 minutes now and you've seen only a field and a couple of trees")
        time.sleep(3)
        print("you've been walking for 3 days now...")
        time.sleep(0.5)
        print("still nothing...")
        time.sleep(5)
        print("it's been 24 years since you've started walking")
        time.sleep(0.5)
        print("somehow you are still in a field")
        print("you're tired..")
        time.sleep(1)
        print("you see a tree")
        print("what will you do?")
        wwyd_03_tree = input('rest under the tree/ keep walking ')
        if (wwyd_03_tree.lower()=="rest under the tree"):
            time.sleep(1)
            print("you rest under the tree,")
            time.sleep(0.5)
            print("an apple falls on your head")
            time.sleep(1)
            print("you die...")
            print(die)
    elif (wwyd_02.lower()=="go east"):
        print("you go east")
        time.sleep(1)
        print("you walk into a village")
        time.sleep(1)
        print("you see a lot of police walking around")
        time.sleep(1)
        print("what will ou do?")
        police_WWYD = input('kill the police [kill]/ run away [run] /do a cool dance [dance]')
        if (police_WWYD.lower()=="kill"):
            time.sleep(1)
            print("you kill the police")
            time.sleep(0.5)
            print("they call for backup")
            time.sleep(1)
            print("you kill them too")
            time.sleep(2)
            print("the whole army is on you now")
            time.sleep(0.5)
            print("but you fight them off, but while fighting you trip over a rock")
            time.sleep(2)
            print("you died...")
            time.sleep(1)
            print(die)
            time.sleep(1.5)
            exit()





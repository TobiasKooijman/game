# THE GAME
#By Tobias Kooijman


# INTRO

print("_______________________________________________________________________________________________________________________")
print("Welcome to THE GAME")
print("")
Begin = input('Type START to begin or QUIT to quit ')
start = 0
if (Begin.lower() =="start"):
    Start = 1
elif (Begin.lower() =="quit"):
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
die = 'Rest In Peace '+str(name) + ' you will not be remembered...'
# Name Easter Eggs
swrd = 0
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
elif (name.lower()=="god"):
    print("praise the lord!!")
elif (name.lower()=="free sword"):
    print("wow you got a free sword, you cheater!")
    swrd = 1
elif (name.lower()=="priest"):
    print("Uh oh, why are you looking at that elementary school like that?")
elif (name.lower()=="god mode"):
    print("yeah, you wish")
elif (name.lower()=="jeff besos"):
    print("I LOVE AMAZON PLS GIVE ME YOUR MONEY")
elif (name.lower()=="mr crabs"):
    print("hello, I like money")
elif (name.lower()=="die"):
    print("you died!")
    time.sleep(1)
    print(die)
    time.sleep(1)
    exit()

#age

print("what is your age?")
age = input('[Enter Number] Type your age here: ')
if int(age) < int(12):
    print("wow you are VERY joung, hmmmm, The priest will like you ;) ")
elif int(age) < int(18):
    print("a bit joung but its ok, the priest likes em joung")
elif int(age) > int(18):
    print("Your an adult, why are you playing this??")
elif int(age) == int(18):
    ("You just turned into an adult, then wtf are you doing playing this game?")
else:
    print("                             ERROR")
    time.sleep(1)
    print("That is an unvalid awnser, the game will now close")
time.sleep(1)


#Start Game
die = 'Rest In Peace '+str(name) + ' you will not be remembered...'
bgn = 0
escape = 0
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
if bgn >= 1:
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


# field

walk_around = 0
swrd = 0

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
    # north
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
        elif (wwyd_03_tree.lower()=="keep walking"):
            time.sleep(1)
            print("you keep walking,")
            time.sleep(2)
            print("forever...")
            time.sleep(1.5)
            print("the walk wil never end...")
            print(die)
    # east
    elif (wwyd_02.lower()=="go east"):
        print("you go east")
        time.sleep(1)
        print("you walk into a village")
        time.sleep(1)
        print("you see a lot of police walking around")
        time.sleep(1)
        print("what will ou do?")
        police_WWYD = input('kill the police [kill]/ run away [run] /do a cool dance [dance] ')
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
        elif (police_WWYD.lower()=="run"):
            time.sleep(1)
            print("you try to run away from the police")
            time.sleep(1)
            print("you also forgot that the police have guns")
            time.sleep(1)
            print("you get shot 28 times")
            time.sleep(1)
            print("you died...")
            time.sleep(1)
            print(die)
        elif (police_WWYD.lower()=="dance"):
            time.sleep(1)
            print("you do a cool dance, for some reason")
            time.sleep(1)
            print("the police think the dance is so cool that they let you go")
            time.sleep(1)
            print("you buy a nice house and raise a happy family")
            time.sleep(1)
            print("it has now been 26 years since your prison escape")
            time.sleep(1)
            print("you now have 4 kids and 3 wives")
            time.sleep(1)
            print("life is good, too good")
            time.sleep(1)
            print("the end!")
            time.sleep(1)
            exit()
    #south
    elif (wwyd_02.lower()=="go south"): 
        time.sleep(1)
        print("you go south")
        time.sleep(1.5)
        print("you see a church")
        time.sleep(0.7)
        print("what will you do?")
        church_01 = input('enter the church [enter]/ walk around the church [walk around] ')
        if (church_01.lower()=="enter"):
            time.sleep(1)
            print("You walk towards the church")
            time.sleep(0.7)
            print("you hear singing inside the church")
            time.sleep(1)
            print("are you sure you still want to enter?")
            enter_church = input('yes/no ')
            if (enter_church.lower()=="yes"):
                time.sleep(1)
                print("you enter the church") 
                time.sleep(0.5)
                print("suddenly, the singing stops")
                time.sleep(0.5)
                print("as you open the chrurch doors you see that nobody is inside")
                time.sleep(0.5)
                print("then where did that singing come from?")
                time.sleep(0.5)
                print("as you examine the church further, you see a beautiful sword on a pedestal")
                time.sleep(0.5)
                print("will you take it?")
                take_sword = input('yes/no ')
                if (take_sword.lower()=="yes"):
                    time.sleep(0.8)
                    print("you've obtained a sword! Congratulations!")
                    time.sleep(1)
                    print("you hear weird noises outside")
                    time.sleep(1)
                    print("you decide to check it out")
                    time.sleep(1)
                    print("the moment you walk outside you instantly see it")
                    time.sleep(1)
                    print("it's YOUR MOTHER!! (aka king kong)")
                    time.sleep(1)
                    print("she throws a punch at you but misses")
                    time.sleep(1)
                    print("what will you do?")
                    swrd_mother = input('Throw rocks [rocks] / use sword [sword] / summon god [god] ')
                    if (swrd_mother.lower()=="rocks"):
                        time.sleep(1)
                        print("you throw rocks at your mother")
                        time.sleep(1)
                        print("suprisingly, this doesn't do much")
                        time.sleep(1)
                        print("then she crushes you in one blow")
                        time.sleep(1)
                        print("you died!")
                        time.sleep(1)
                        print(die)
                        time.sleep(1)
                        exit()
                    elif (swrd_mother.lower()=="sword"):
                        time.sleep(1)
                        print("you use the sword to attack your mother")
                        time.sleep(1)
                        print("you can see that she's getting scared")
                        time.sleep(1)
                        print("you stab her in the neck and she instantly dies")
                        time.sleep(1)
                        print("you won!")
                        time.sleep(1)
                        print("you're also an orphan now...")
                        time.sleep(1)
                        print("unless your dad comes back with the milk")
                        time.sleep(1)
                        print("the end!") 
                        time.sleep(1)
                        exit()
                    elif (swrd_mother.lower()=="god"):
                        time.sleep(1)
                        print("you summon god")
                        time.sleep(1)
                        print("but then you remember that you're not christian")
                        time.sleep(1)
                        print("while your busy trying to summon god, your mother smashes you to pieces")
                        time.sleep(1)
                        print("you died!")
                        time.sleep(1)
                        print(die)
                        time.sleep(1)
                        exit()
                    Swrd = 1
                elif (take_sword.lower()=="no"):
                    time.sleep(0.8)
                    print("you for some reason don't grab the sword...")
                time.sleep(1)
                print("you hear weird noises outside")
                time.sleep(1)
                print("you decide to check it out")
                time.sleep(1)
                print("the moment you walk outside you instantly see it")
                time.sleep(1)
                print("it's YOUR MOTHER!! (aka king kong)")
                time.sleep(1)
                print("she throws a punch at you but misses")
                time.sleep(1)
                print("what will you do?")
                swrd_mother_01 = input('Throw rocks [rocks] / become christian [Christ] / summon god [god] ')
                if (swrd_mother_01.lower()=="rocks"):
                        time.sleep(1)
                        print("you throw rocks at your mother")
                        time.sleep(1)
                        print("suprisingly, this doesn't do much")
                        time.sleep(1)
                        print("then she crushes you in one blow")
                        time.sleep(1)
                        print("you died!")
                        time.sleep(1)
                        print(die)
                        time.sleep(1)
                        exit()
                elif (swrd_mother_01.lower()=="god"):
                        time.sleep(1)
                        print("you summon god")
                        time.sleep(1)
                        print("but then you remember that you're not christian")
                        time.sleep(1)
                        print("while your busy trying to summon god, your mother smashes you to pieces")
                        time.sleep(1)
                        print("you died!")
                        time.sleep(1)
                        print(die)
                        time.sleep(1)
                        exit()
                elif (swrd_mother_01.lower()=="christ"):
                            time.sleep(1)
                            print("you become christian")
                            time.sleep(1)
                            print("this suprisingly doesn't do much")
                            time.sleep(1)
                            print("while your busy thinking about god, your mother smashes you to pieces")
                            time.sleep(1)
                            print("but the lord protected you!")
                            time.sleep(1)
                            print("what will you do now?")
                            time.sleep(1)
                            swrd_mother_02 = input('Throw rocks [rocks] / summon god [god] ')
                            if (swrd_mother_02.lower()=="rocks"):
                                time.sleep(1)
                                print("you throw rocks at your mother")
                                time.sleep(1)
                                print("suprisingly, this doesn't do much")
                                time.sleep(1)
                                print("then she crushes you in one blow")
                                time.sleep(1)
                                print("you died!")
                                time.sleep(1)
                                print(die)
                                time.sleep(1)
                                exit()
                            elif (swrd_mother_02.lower()=="god"):
                                time.sleep(1)
                                print("you summon god")
                                time.sleep(1)
                                print("IT SOMEHOW WORKS!")
                                time.sleep(1)
                                print("your mother gets sucked into hell")
                                time.sleep(1)
                                print("she's gone...")
                                time.sleep(1)
                                print("you won")
                                time.sleep(1)
                                print("you will now become a priest and spread the word of god")
                                time.sleep(1)
                                print("amen")
                                time.sleep(1)
                                print("the end!")
                                time.sleep(1)
                                exit()
                             
                             
                            
            if (enter_church.lower()=="no"):
                time.sleep(1)
                print("you decide to walk around the church, as you're too much of a pussy to go inside")
                walk_around = 1

        elif (church_01.lower()=="walk around"):
            time.sleep(1)
            print("you walk around the church")
            walk_around = 1

if walk_around > 0:
    time.sleep(0.5)
    print("while you are walking around the church you get attacked by:")
    time.sleep(1.5)
    print("YOUR MOTHER (aka king kong)")
    time.sleep(1)
    print("she attacks you and you can't fight back, you have no weapon")
    time.sleep(1)
    print("what will you do?")
    time.sleep(1)
    wwyd_monkay = input('run/ try to fight [fight] ')
    time.sleep(0.3)
    print("Your mother throws a punch at you and it barely misses")
    time.sleep(0.7)
    print("you decide to run")
    time.sleep(1)
    print("then you remember that your mother is king kong")
    time.sleep(1)
    print("and king kong can just jump on you and kill you...")
    time.sleep(1)
    print("and guess what, that's exactly what happens!")
    time.sleep(1)
    print("you died!")
    time.sleep(1)
    print(die)
    time.sleep(1)
    exit()
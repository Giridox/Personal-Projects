import pygame
pygame.init()

sword_clash = pygame.mixer.Sound(r"C:\Users\girid\sword_clash.wav")
victory_music = pygame.mixer.Sound(r"C:\Users\girid\435062__fritzsounds__cartoon-voice-bean-game-set-3-victory-nice-one-oh-no-maybe-next-time.wav")
victory_music.set_volume(1)  # 100% volume
import random

def get_input(prompt, valid_range):
    """Helper function to get valid input from the player."""
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_range:
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_health(php, ohp, whp, uhp):
    print(f"Your health: {php}")
    print(f"Mr. Ogre's health: {ohp}")
    print(f"The Wizard's health: {whp}")
    print(f"Mrs. Unicorn's health: {uhp}")

# Game start
print("Welcome to play my first ever game!")
print("It's an adventure game where you make choices and try to survive until the end.")
print()

print("First, start by writing '1' below (no other numbers, please).")
ok = get_input("", [1])
print()
print("Okay, let's start!")
print()
print()

php = 100  # Player health
ohp = 200  # Mr. Ogre
whp = 80   # The Wizard
uhp = 20   # Mrs. Unicorn

print("Your starting health is 100")
print()
print("Let's introduce your crew:")
print("Mr. Ogre (hp 200): He has a lot of strength but is dumb as hell.")
print("The Wizard (hp 80): A cool chill dude.")
print("Mrs. Unicorn (hp 20): Pretty useless, but at least she looks cool.")
print()

print("You all spawn in a forest and see a castle on the edge of the forest.")
print("The castle is your target.")
print()

# First choice
print("You start moving towards the castle until you encounter a bunch of little ogres.")
print("Do you attack them (1) or try to walk past them (2)?")
q1 = get_input("", [1, 2])

if q1 == 1:
    print("You and your crew absolutely demolish them. Only you and The Wizard take 10 damage.")
    php -= 10
    whp -= 10
else:
    print("All of you got past the ogres. Except Mrs. Unicorn. She dies a horrible death.")
    uhp = 0

display_health(php, ohp, whp, uhp)

# Second choice
print("Next, you walk to a river with no bridge in sight.")
print("Do you walk through the river (1) or make Mr. Ogre be a bridge for everyone else (2)?")
q2 = get_input("", [1, 2])

if q1 == 1 and q2 == 1:
    print("You all make it through, but you and The Wizard lose a significant amount of health (-50 hp).")
    php -= 50
    whp -= 50
elif q2 == 1:
    print("All of you make it safely through the river.")
elif q1 == 1 and q2 == 2:
    print("You and The Wizard make it over safely, but Mrs. Unicorn falls and dies. Mr. Ogre takes 10 damage.")
    uhp = 0
    ohp -= 10
elif q1 == 2 and q2 == 2:
    print("You and The Wizard make it over the river, but Mr. Ogre takes 10 damage.")
    ohp -= 10

display_health(php, ohp, whp, uhp)

# Dice game
print("You have almost made it to the castle but want to take a little break.")
print("You and The Wizard decide to roll a dice and see if it lands on the number you choose.")
num = random.randint(1, 6)  # Dice roll
wnum = random.randint(1, 6)  # The Wizard's guess
print(f"The Wizard chose {wnum}. Now choose a number from 1 to 6 (not the same as The Wizard's).")
pnum = get_input("", [x for x in range(1, 7) if x != wnum])

while pnum != num and wnum != num:
    print(f"The dice landed on {num}. None of you guessed right, so you roll again.")
    wnum = random.randint(1, 6)
    print(f"The Wizard chose {wnum}.")
    pnum = get_input("Choose your number: ", [x for x in range(1, 7) if x != wnum])
    num = random.randint(1, 6)

if pnum == num:
    print(f"The dice landed on {num}. You got it right!")
    print("The Wizard got mad and tried to push you, but you dodged it. You pushed him back and he died.")
    whp = 0
elif wnum == num:
    print(f"The dice landed on {num}. The Wizard guessed it right. You got a little mad but did nothing.")

display_health(php, ohp, whp, uhp)

# Final choice
print("You finally make it to the castle. But there is a giant dragon guarding it.")
print("Do you fight it (1) or try to sneak past it (2)?")
q4 = get_input("", [1, 2])

if q4 == 1:
    if q2 == 1 and q1 == 1:
        print("Mrs. Unicorn surprisingly attacks the dragon. The dragon dies!")
    elif q2 == 1 and q1 == 2:
        print("Mr. Ogre defeats the dragon all by himself!")
    elif q2 == 2 and q1 == 2 and whp > 0:
        print("Mr. Ogre and The Wizard team up to defeat the dragon!")
    else:
        print("Your crew was too weak for the dragon. You all died. YOU LOSE.")
        exit()
else:
    if q2 == 1 and q1 == 1 and whp > 0:
        print("You try to sneak, but you and The Wizard have taken too much damage. The dragon kills everyone. YOU LOSE.")
        exit()
    elif q2 == 1 and q1 == 1:
        print("You try to sneak, but the dragon notices and kills everyone. YOU LOSE.")
        exit()
    elif q2 == 2 and q1 == 1:
        print("Your crew sneaks past the dragon successfully!")
    else:
        print("Your crew fails to sneak past the dragon. It kills everyone. YOU LOSE.")
        # Play victory sound effect
        victory_music.play()
        exit()

# Game End
print()
print("You have defeated the dragon and made it into the castle!")
if ohp > 0 and whp > 0 and uhp > 0:
    print("Everyone survives!")
elif ohp > 0 and whp > 0 and uhp == 0:
    print("Everyone survives except Mrs. Unicorn!")
elif ohp > 0 and whp == 0 and uhp > 0:
    print("Everyone survives except The Wizard!")
elif ohp == 0 and whp > 0 and uhp > 0:
    print("Everyone survives except Mr. Ogre!")
elif ohp > 0 and whp == 0 and uhp == 0:
    print("Only you and Mr. Ogre survived!")
elif ohp == 0 and whp > 0 and uhp == 0:
    print("Only you and The Wizard survived!")
elif ohp == 0 and whp == 0 and uhp > 0:
    print("Only you and Mrs. Unicorn survived!")
else:
    print("Only you survived!")
# Play victory sound effect
victory_music.play()
pygame.time.delay(20000)

print("THE END")
exit()

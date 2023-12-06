# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Susan")
define w = Character("Xilun")

define relationship_value = 50
define skip_points = 3
define config.menu_include_disabled = True

image Susan_D = "images/Susan_default.png"
image Susan_U = "images/Susan_unhappy.png"
image Susan_H = "images/Susan_happy.png"
image Susan_S = "images/Susan_sad.png"
image Susan_A = "images/Susan_angry.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ renpy.music.set_volume(0.2, delay=0, channel='music')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')

    play music "LudumDare38Track1.wav"

    "You are a resident that has just recently moved into Block 18, and your goal is to reduce the noise level around the neighborhood without causing too much conflict."
    "Your relationship with your neighbors is represented by your Relationship Value(RV), which can vary from 0 to 100."
    "Your RV will change based on how you approach several conflicts."
    "Since you have just moved in, your neighbors are neutral to you, starting you at 50 RV"
    "You also start with 3 HP, which represents your tolerance for noise. If you fail to resolve the noise issues in any given scenario, you will lose 1 HP. At 0 HP, you will end up with a Game Over."
    "We hope you enjoy the game!"

    "1.."
    ".2."
    "..3"

    scene bg room
    play music "LudumDare38Track4.wav"
    # play music at lower volume
    "On the first night after you move in, you hear loud music coming from one of your neighbours houses."
    menu:
        "Try to ignore the music":
            "Sleep does not come easy due to the noise, but you manage to get some rest."
            "HP -1"
            $ skip_points -= 1
            jump scenario2
        "It's time to face the music":
            jump scenario1

    #第一幕 / 1st Scenario
    label scenario1:
        $ renpy.music.set_volume(0.7, delay=0, channel='music')
        "After a brief investigation, you determine that the music is coming from the neighbor across your unit."
        "How do you deal with this issue?"
        menu:
            "Report the noise to building management":
                "Your neighbor recieves a formal warning. They are very unhappy with you, but they do grudgingly quiten down."
                $ renpy.music.set_volume(0, delay=0, channel='music')
                "You have ruined your relationship with your neighbors"
                "RV has been set to 0!"
                $ relationship_value = 0
                jump scenario2

            "Leave a friendly note to ask them to lower their volume":
                play sound "knocking-on-door-6022.mp3"
                "You leave a post-it note on their door and knock on their door before leaving."
                $ random_num = renpy.random.random()
                if random_num<0.5:
                    jump scenario1_win
                else:
                    jump scenario1_lose

            "Gently knock on the door":
                play sound "knocking-on-door-6022.mp3"
                "You gently knock on their door."
                $ relationship_value == relationship_value

        "Several minutes have passed, but no one seems to be coming. You..."
        menu:
            "Bang loudly on the door":
                play sound "door-bang-1wav-14449.mp3"
                "You pound on the door, keeping it up until your neighbor acknowledges your presence."
                "RV -10"
                $ relationship_value -= 10
                jump scenario1_opendoor

            "Try knocking again, a little louder this time":
                "Your neighbor must not have heard you knocking. You try again, this time with a little more force."
                $ renpy.music.set_volume(1.0, delay=0, channel='sound')
                play sound "knocking-on-door-6022.mp3"
                $ relationship_value == relationship_value
                jump scenario1_opendoor

        label scenario1_opendoor:
            "This time your neighbor actually responds, opening the door after a while."
            show Susan_D
            "Susan" "Oh, you're the one that just moved in! What can I do for you?"
            "You can barely hear your neighbor over the music."
            "You explain that their music has been too loud and is preventing you from sleeping, practically having to shout your explanation. You..."
        menu:
            "Demand that your neighbor turn off their music":
                show Susan_A
                s "Alright, but you don't have to be so darned rude about it!"
                "Your neighbor frowns, visibly annoyed."
                "RV -10"
                $ relationship_value -= 10
                jump scenario1_end
            "Politely ask if your neighbor could lower the volume of their music.":
                show Susan_U
                s "Oh! I'm really sorry about that, I can do that no problem!"
                show Susan_H
                s "Thanks for letting me know!"
                "When your neighbour realises that her music has been disturbing her neighbors, she immediately apologizes and promises to lower the volume of her music."
                "RV +10"
                $ relationship_value += 10
                jump scenario1_end

    label scenario1_end:
        $ renpy.music.set_volume(0.1, delay=0, channel='music')
        "Having resolved the noise issue, you settle down for a good night's rest"
        jump scenario2

    label scenario1_win:
        $ renpy.music.set_volume(0.1, delay=0, channel='music')
        "A few minutes later, you hear the volume of the music being lowered. You settle down for a good night's rest."
        "RV +10"
        $ relationship_value += 10
        jump scenario2

    label scenario1_lose:
        "Hours later, the music is still as loud as ever. It seems your note was either not noticed or ignored."
        "HP -1"
        $ skip_points -= 1
        jump scenario2

    #第二幕 / 2nd Scenario
    label scenario2:
        "loud noise again"
        "community gathering"
        menu:
            "do not go":
                $ skip_points -=1
                jump scenario3
            "go":
                jump community
            "forcefully end":
                "neighbour annoyed"
                $ relationship_value -=20
                jump scenario3
        label community:
            menu:
                "help":
                    "appreciate"
                    $ relationship_value += 20
                    jump scenario3
                "talk" if relationship_value >= 60:
                    "convince"
                    jump scenario3
    #第三幕 / 3rd Scenario
    label scenario3:
        "new furniture came in"
        "moving furniture around"
        "you hear knock on the door"
        menu:
            "you ignore":
                $ relationship_value -= 20
                jump scenario4
            "answer the door"
            "neighbour ask about your noise":
                menu:
                    "you apologize and explain why":
                        $ relationship_value += 10
                        if relationship_value >= 80:
                            jump offer_help
                        elif 30 < relationship_value < 80:
                            "neighbour says they understand"
                            menu:
                                "continue moving":
                                    jump scenario4
                                "implement method to lower noise":
                                    jump  scenario4
                        else:
                            "neighbour ask you to lower your noise"
                            menu:
                                "implement method":
                                    $ relationship_value +=10
                                    jump scenario4
                                "ignore demand":
                                    $ relationship_value -= 10
                                    jump scenario4
                    "tell them step out":
                        $ relationship_value -= 10
    label offer_help:
        "neighbour offer help you moving furnitures"
        jump scenario4
    #第四幕 / 4th Scenario
    label scenario4:
        "studying"
        "hearing lot of noise, difficult to focus"
        menu:
            "do not investigate":
                $ skip_points -= 1
                if skip_points <= 0:
                    return
                else:
                    jump scenario5
            "investigate noises":
                "found children gathering at lobby"

    #第五幕 / 5th Scenario
    label scenario5:
        "this is the 5th scenario"


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # This ends the game.

    return

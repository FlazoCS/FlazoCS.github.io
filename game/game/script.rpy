# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define w = Character("Xilun")

define relationship_value = 50
define skip_points = 3
define config.menu_include_disabled = True
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    "you move in"
    "Loud Noises"
    menu:
        "you ignore":
            $ skip_points -= 1
            jump scenario2
        "you confront":
            jump scenario1
    #第一幕
    label scenario1:
        menu:
            "you report the noise to building management":
                $ relationship_value = 0
                jump scenario2
            "leave a friendly note":
                $ random_num = renpy.random.random()
                if random_num<0.5:
                    jump scenario1_win
                else:
                    jump scenario1_lose
            "you knock on the door":
                $ relationship_value == relationship_value
        "knock is ignored"
        menu:
            "bang on the door":
                $ relationship_value -= 10
            "try knocking again":
                $ relationship_value == relationship_value
        "neighbour opens door"
        menu:
            "demand":
                "neighbour annoyed"
                $ relationship_value -= 10
                jump scenario2
            "politely":
                "neighbour apologize"
                $ relationship_value += 10
                jump scenario2
    label scenario1_win:
        "neighbour apologize[random_num]"
        $ relationship_value += 10
        jump scenario2
    label scenario1_lose:
        "neighbour didnt see[random_num]"
        jump scenario2
    #第二幕
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
    #第三幕
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
    #第四幕
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
                


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
   
        
    # This ends the game.

    return

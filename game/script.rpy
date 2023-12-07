# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Susan")
define w = Character("Xilun")
define n = Character("Neighbor")

default relationship_value = 50
default skip_points = 3
default db = 60
define config.menu_include_disabled = True

#Scenario1
image Susan_D = "images/Susan_default.png"
image Susan_U = "images/Susan_unhappy.png"
image Susan_H = "images/Susan_happy.png"
image Susan_S = "images/Susan_sad.png"
image Susan_A = "images/Susan_angry.png"
# music Normal = "LudumDare38Track1.wav"
# music Noisy = "LudumDare38Track4.wav"
# sound Knock = "knocking-on-door-6022.mp3"
# sound Slam = "door-bang-1wav-14449.mp3"

#Scenario2
image FrontDoor = "images/HBD_closed_door.jpg"
image Gathering = "images/HBD_gathering.jpg"
image Conversation = "images/HBD_conversation.jpg"
image BuffetPrep = "images/HBD_buffet_preparing.jpg"
image BuffetReady = "images/HBD_buffet_ready.jpg"
image OW = "images/office_worker.png"
# music Crowd = "crowd_talking-6762.mp3"
# sound DoorSlam = "door-slam-sound-effect-21878"

# The game starts here.

screen stats:
    frame:
        xalign 1.0
        yalign 0.5
        vbox:
            text "{color=#FF0000}HP: [skip_points] {/color}"
            text "RV: " + str(relationship_value)
            text "Volume: " + str(db)

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ renpy.music.set_volume(0.2, delay=0, channel='music')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')

    play music "LudumDare38Track1.wav"

    "You are a resident that has just recently moved into Block 18, and your goal is to reduce the noise level around the neighborhood without causing too much conflict."
    show screen stats
    "In this game, your relationship with your neighbors is represented by your Relationship Value(RV), which can vary from 0 to 100."
    "Your RV will change based on how you approach several conflicts."
    "Since you have just moved in, your neighbors are neutral to you, starting you at 50 RV"
    "You also start with 3 HP, which represents your tolerance for noise. If you fail to resolve the noise issues in any given scenario, you will lose 1 HP."
    "At 0 HP, you will end up with a Game Over."
    "We hope you enjoy the game!"

    "..."

    scene bg room
    play music "LudumDare38Track4.wav"
    $ db = 70
    "On the first night after you move in, you hear loud music coming from one of your neighbours houses."
    menu:
        "Try to ignore the music":
            jump scenario1_bad_end
        "It's time to face the music":
            jump scenario1

    #第一幕 / 1st Scenario
    label scenario1:
        $ renpy.music.set_volume(0.7, delay=0, channel='music')
        "After a brief investigation, you determine that the music is coming from the neighbor across your unit."
        $ db = 85
        "How do you deal with this issue?"
        menu:
            "Report the noise to building management":
                "Your neighbor recieves a formal warning. They are very unhappy with you, but they do grudgingly quiten down."
                $ renpy.music.set_volume(0, delay=0, channel='music')
                "You have ruined your relationship with your neighbors"
                $ relationship_value = 0
                "{color=#FF0000}RV has been set to 0!{/color}"
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
                $ relationship_value -= 10
                "{color=#FF0000}RV -10{/color}"
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
                "Susan frowns, visibly annoyed."
                $ relationship_value -= 10
                "{color=#FF0000}RV -10{/color}"
                jump scenario1_good_end

            "Politely ask if your neighbor could lower the volume of their music.":
                show Susan_U
                s "Oh! I'm really sorry about that, I can do that no problem!"
                show Susan_H
                s "Thanks for letting me know!"
                "When your neighbour realises that her music has been disturbing her neighbors, she immediately apologizes and promises to lower the volume of her music."
                $ relationship_value += 10
                "{color=#00FF00}RV +10{/color}"
                jump scenario1_good_end


    label scenario1_win:
        $ renpy.music.set_volume(0.1, delay=0, channel='music')
        "A few minutes later, you hear the volume of the music being lowered. You settle down for a good night's rest."
        $ relationship_value += 10
        "{color=#00FF00}RV +10{/color}"
        jump scenario1_good_end

    label scenario1_lose:
        "Hours later, the music is still as loud as ever. It seems your note was either not noticed or ignored."
        $ skip_points -= 1
        "{color=#FF0000}HP -1{/color}"
        jump scenario1_bad_end

    label scenario1_good_end:
        scene bg room
        $ renpy.music.set_volume(0.1, delay=0, channel='music')
        "Having resolved the noise issue, you settle down for a good night's rest"
        jump scenario1_fin

    label scenario1_bad_end:
        scene bg room
        "Sleep does not come easy due to the noise, but you manage to get some rest."
        $ skip_points -= 1
        "{color=#FF0000}HP -1{/color}"
        jump scenario1_fin

    label scenario1_fin:
        scene black
        "You have reached the end of Scenario 1, take a moment to reflect on how your actions, or lack of, have affected your relationship with your neighbors"
        menu:
            "Continue to Scenario 2":
                jump scenario2

    #第二幕 / 2nd Scenario
    label scenario2:
        "It's a sunny Saturday afternoon, and the warm weather makes you sleepy."
        scene black
        show FrontDoor
        $ renpy.music.set_volume(0.5, delay=0, channel='music')
        play music "crowd_talking-6762.mp3"
        "Just as you are about to lie down for a nap however, you pick up on the din of lively conversation and laughter from outside your front door"
        scene Gathering
        "Looking through your peephole, you discover a sizable gathering of your neighbors at the common space right outside your door. They seem to be celebrating something. You..."
        menu:
            "Stay inside and do not participate":
                jump scenario2_bad_end
            "Check it out":
                "You step outside to join in the festivities."
                jump scenario2_join_community
            "Attempt to break up the gathering":
                "You yell at the group of people and attempt to chase them away."
                "You hear murmurs of discontentment and get some glares, but eventually the gathering relocates further away."
                "{color=#F0000}RV -20{/color}"
                $ relationship_value -=20
                jump scenario2_neutral_end

        label scenario2_join_community:
            $ renpy.music.set_volume(1.0, delay=0, channel='music')
            play music "crowd_talking-6762.mp3"
            scene BuffetPrep
            "As you approach the gathering of people, you notice a small group of people setting up a buffet."
            menu:
                "Offer to help":
                    "You offer to help with the preparations."
                    "..."
                    "With your help, preparations are completed very quickly."
                    show OW
                    "Neighbor" "Thanks man, we appreciate the help!"
                    n "Wait, you're the one that just moved in last week right? Glad to see you're fitting in well!"
                    "{color=#00FF00}RV +20{/color}"
                    $ relationship_value += 20
                    jump scenario2_good_end
                "Join the people waiting around.":
                    scene Conversation
                    "You join the others waiting around for preparations to be completed, but otherwise do not interact with anyone."
                    jump scenario2_good_end
                "Strike up a conversation with some of the people waiting around." if relationship_value >= 60:
                    scene Conversation
                    #show crowd
                    "You greet some of the people waiting around and introduce yourself."
                    "After a couple rounds of lively conversation, you feel like you have gotten to know your neighbors better"
                    "{color=#00FF00}RV +10{/color}"
                    $ relationship_value += 10
                    jump scenario2_good_end
                "Abort":
                    scene FrontDoor
                    "On second thought, never mind."
                    jump scenario2_bad_end

        label scenario2_good_end:
            scene BuffetReady
            "Once the preparations are finished, you join the others in lining up to get some food and drinks."
            "Taking the opportunity, you ask about the noise situation around the block in the past few months."
            show OW
            n "Have there been consistent loud noises in the last few months?"
            n "Well, there's Sarah who likes her music loud, but she's pretty reasonable about it."
            n "The children around the block can be pretty noisy when they play, but that's to be expected."
            n "Oh yeah, there's Dave too. Haven't talked to him myself, but I hear he works the night shift, so we don't see him around often."
            n "I know he doesn't mean to, but he can be rather loud when he comes home in the early morning."
            "Having gotten the information you needed, you decide to settle in for an afternoon of community engagement."
            "The food is nothing to write home about, but you are satisfied all the same."
            "{color=#00FF00}RV +10{/color}"
            $ relationship_value += 10
            jump scenario2_fin

        label scenario2_bad_end:
            $ renpy.music.set_volume(0.5, delay=0, channel='sound')
            play sound "door-slam-sound-effect-21878"
            "Having just moved in, you do not feel comfortable joining in activities with what are basically strangers."
            "However, not being able to have a nap leaves you lethargic for the rest of the day"
            "{color=#FF0000}HP -1{/color}"
            $ skip_points -=1
            jump scenario2_fin

        label scenario2_fin:
            scene black
            "You have reached the end of Scenario 3, take a moment to reflect on how your actions, or lack of, have affected your relationship with your neighbors"
            menu:
                "Continue to Scenario 3":
                    jump scenario3_EoC
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

    label scenario3_EoC:
        "Congratulations! You have reached the end of the currently implemented content."
        "If you wish to keep going, be warned that there is only the bare minimum ahead"
        menu:
            "Keep going.":
                jump scenario3
            "I've seen enough, I'm satisfied.":
                jump end

    label end:
        "Thanks for playing! Shutting down..."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # This ends the game.

    return

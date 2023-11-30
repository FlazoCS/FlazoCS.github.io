# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# define mc = Character("Resident")
define mc = Character("You")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg void

    scene bg corridor

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show ow
    show office worker
    # These display lines of dialogue.

    "You are a resident of Block 000, and you have been hearing a lot of noise recently."

    "Resident" "Wow it's so noisy."

    mc "Wonder what's going on?"

    # "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent iaculis, dolor ac pulvinar facilisis, ex diam vehicula ex, ac pharetra neque dolor a nunc. Quisque ultrices mi sit amet dignissim euismod. Aenean bibendum ante sapien, et consectetur nibh venenatis ac."
#     "Nam volutpat quis risus ut fringilla. Pellentesque tempus diam nibh, non mattis lacus pharetra a. Praesent dignissim pharetra ex. Aliquam vehicula risus eget risus elementum, sed accumsan quam mollis."
#     "Quisque sollicitudin, nulla nec ultrices hendrerit, libero neque facilisis lorem, id commodo mi mi in risus. Phasellus id arcu ac magna mattis dictum in in mauris. Duis consectetur a tortor quis consectetur. Nunc venenatis scelerisque semper."
#     "Donec fringilla sem in risus luctus, vel luctus nulla ultricies. Ut risus risus, volutpat sed tortor ac, volutpat semper erat. Proin sollicitudin quam nulla, ac finibus purus gravida non. Sed non posuere tortor."
#     "Sed porttitor dui ac mollis scelerisque. Vivamus rhoncus pretium quam, vel tincidunt mi ultrices a. Donec at mattis nulla. Mauris sed suscipit leo. Proin lobortis nunc euismod scelerisque faucibus. Aliquam porta mollis nisi, sed suscipit ante tincidunt vitae."
#
# menu:
#
#     "Option 1":
#         jump choice_1_1
#
#     "Option 2":
#         jump choice_1_2
#
# label choice_1_1:
#
#     $ menu_flag = True
#
#     mc "You chose option 1."
#
#     jump choice_1_finish
#
# label choice_1_2:
#
#     $ menu_flag = False
#
#     mc "You chose option 2."
#
#     jump choice_1_finish
#
#     #options merge here
# label choice_1_finish:
#
#     "You chose something in choice 1"

    # This ends the game.
label end:

    scene bg endscreen
    with Dissolve(.5)
    "End of current code. Exiting..."



    return

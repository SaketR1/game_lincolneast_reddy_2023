from tkinter import * 
from tkinter import ttk
from tkinter.ttk import *
import random


global INSTRUCTIONS
INSTRUCTIONS = '''
NOTE: Please do not close a window until after a game (6 levels) is over and you have clicked the 'Enter' button.
Closing a window too early can cause data to be registered incorrectly.

USER INTERFACE INSTRUCTIONS
- Once you type your answer into the text box, click 'Guess!' (or click the return key) to move on to the next set of words.
- Once you have completed a game (6 levels) and click the 'Enter' button, you will be returned to the Title Screen.

RULES
- You will be presented with a set of 4 words. You need to guess the word that does NOT match.
- For example, in the set 'gas, coal, wind, oil', you would guess 'wind' because it doesn't fit.
- (This is because wind is a renewable energy source while the other energy sources are non-renewable)
- You need to type the word that you think doesn't match into the text box and click 'Guess!' (or click the return key).
- You need to type the word EXACTLY as displayed, including the displayed capitalization and any hyphens.

DIFFICULTY
- Each set of words has a difficulty level of either 1, 2, or 3. 1 is the most simple difficulty, and 3 is the hardest difficulty.
- If you guess the 'imposter' word correctly, you will receive the same number of points as the difficulty level.
- For example, if you guess the imposter word correctly for a word set of difficulty level 2, you receive 2 points.
- You do NOT lose points for incorrect guesses.

LEVELS
- Each game lasts for 6 levels. The further you progress, the harder the levels will be.
- Levels 1 and 2 use word sets with a difficulty level of 1. 
- Levels 3 and 4 use word sets with a difficulty level of 2. 
- Levels 5 and 6 use word sets with a difficulty level of 3.
- Currently, there are enough word sets to experience 5 games where every word set is new.
- After 5 games, the word sets are reused.

AT THE END OF A GAME
- You will see the celebratory message 'Great Job!', 'Good Job!', or 'Better Luck Next Time!' depending on your performance.
- You can type in your name and date (e.g. 'Satoru 1/1/23') to be shown on the leaderboard.
- If you close the window instead of clicking 'Enter', your name and score will not be shown on the leaderboard.
- If no games have been played, this will be noted on the leaderboard.
'''


global LEVEL_CREATOR_INSTRUCTIONS
LEVEL_CREATOR_INSTRUCTIONS = '''
LEVEL CREATOR OVERVIEW
- MULTIPLAYER FEATURE/ADVANCED RULE FEATURE: You can create your own levels! 
- You are encouraged to find a friend to play your custom levels!
- You must create 6 levels at a time, then click 'Add Words'. The 'Exit' button will NOT save the words you type in. 

CREATING CUSTOM LEVELS
- Type in the words you want shown in 'Word Set' and the answer in 'Answer Word'. 
- For example, 'gas, coal, wind, oil' would go in a 'Word Set' box and 'wind' would go in an 'Answer Word' box.
- Pay attention to the difficulty on the left - word sets with higher difficulties should be harder to guess.
- Feel free to type in the pre-made levels found in the code to get a feel for how the level creator works.
- A few of these pre-made levels are listed below:

PRE-MADE LEVELS
gas, coal, wind, oil --- wind
notebook, video, paper, textbook --- video
Earth, Sun, Mercury, Venus --- Sun
rose, daisy, sunflower, tree --- tree
key, vault, password, safe --- password
flute, trumpet, trombone, xylophone --- xylophone

PLAYING CUSTOM LEVELS
- Click 'Play Custom Levels' to play the levels you created!
- The custom levels will be generated randomly according to difficulty, not the exact order you entered them in.
- If no custom levels have been made, this will be noted if the user tries to play custom levels.
'''


# There are 30 pre-made word sets - 10 for each difficulty
# Each element contains the word set, answer, difficulty level, and a fourth variable
# The fourth variable indicates whether the word set has been displayed before
# 0 means the word set has not been displayed, 1 means it has been displayed
global premade_word_combinations
premade_word_combinations = [
                    ["notebook, video, paper, textbook", "video", "1", "0"],
                    ["Earth, Sun, Mercury, Venus", "Sun", "1", "0"],
                    ["web browser, computer, mouse, keyboard", "web browser", "1", "0"],
                    ["gas, coal, wind, oil", "wind", "1", "0"],
                    ["math, physics, english, chemistry", "english", "1", "0"],
                    ["car, airplane, bus, truck", "airplane", "1", "0"],
                    ["helicopter, airplane, SUV, hot air balloon", "SUV", "1", "0"],
                    ["nurse, scientist, doctor, dentist", "scientist", "1", "0"],
                    ["chess, checkers, Pac-Man, Connect Four", "Pac-Man", "1", "0"],
                    ["rose, daisy, sunflower, tree", "tree", "1", "0"],

                    ["key, vault, password, safe", "password", "2", "0"],
                    ["documentary, movie, GIF, podcast", "GIF", "2", "0"],
                    ["flute, trumpet, trombone, xylophone", "xylophone", "2", "0"],
                    ["MLK Day, Presidents' Day, Kwanzaa, Black History Month", "Presidents' Day", "2", "0"],
                    ["apple, artichoke, strawberry, pomegranate", "artichoke", "2", "0"],
                    ["laptop, phone, earbuds, smartwatch", "laptop", "2", "0"],
                    ["cake, coffee, donuts, brownies", "coffee", "2", "0"],
                    ["oxygen, iron, carbon, helium", "iron", "2", "0"],
                    ["living room, bedroom, basement, patio", "patio", "2", "0"],
                    ["Sun, light bulb, firefly, spider", "spider", "2", "0"],

                    ["grass, flower, stalagmite, stalactite", "stalactite", "3", "0"],
                    ["Mario, Sonic, Zelda, Donkey Kong", "Sonic", "3", "0"],
                    ["Spider-Man, Superman, Iron Man, Ant Man", "Superman", "3", "0"],
                    ["United States, United Kingdom, Russia, Turkey", "United States", "3", "0"],
                    ["circus, merry-go-round, Ferris wheel, roller coaster", "circus", "3", "0"],
                    ["Aztecs, Maya, Olmecs, Mesopotamians", "Mesopotamians", "3", "0"],
                    ["bowling, golf, hockey, basketball", "hockey", "3", "0"],
                    ["school, post office, university, grocery store", "university", "3", "0"],
                    ["one, seven, eight, three", "seven", "3", "0"],
                    ["car, bike, golf cart, go-kart", "bike", "3", "0"],
                    ]


global custom_word_combinations
custom_word_combinations = []


global word_combinations
word_combinations = premade_word_combinations


global leaderboard_text #Stores all leaderboard information
leaderboard_text = ""


# This function controls game play, and includes many different functions
def play_game():
    

    global word_combinations
    global premade_word_combinations
    global custom_word_combinations
    global current #Indicates what level the game is on. The current level is 'current' + 1
    global score #Indicates the player's score
    global current_index #Indicates the index of the currently displayed word set in 'word_combinations'
    current = 0
    score = 0
    current_index = 0


    # This function increases the player's score and displays the new score
    def increase_score():
        global current_index
        global score

        score_text_field['state'] = 'enabled' #Allow the score text field to be changed
        score_text_field.delete(0, END) #Delete everything in the text field

        score += int(word_combinations[current_index][2]) #Increase the score according to the word set's difficulty level
        new_score_text = "Score: " + str(score) #Create the text with the new score

        score_text_field.insert(0, new_score_text) #Insert the new text into the text field
        score_text_field['state'] = 'disabled' #Disable the score text field from being changed


    # This function displays the new level
    def change_level_label():
        global current_index

        level_text_field['state'] = 'enabled'
        level_text_field.delete(0, END)

        new_level_text = "Level: " + str(current + 1)

        level_text_field.insert(0, new_level_text)
        level_text_field['state'] = 'disabled'
    

    # This function displays the new word set's difficulty
    def change_difficulty_label():
        global current_index

        difficulty_text_field['state'] = 'enabled'
        difficulty_text_field.delete(0, END)

        difficulty_level = ""
        if(current >= 0 and current <= 1):
            difficulty_level = "1"
        elif(current >= 2 and current <= 3):
            difficulty_level = "2"
        elif(current >= 4 and current <= 5):
            difficulty_level = "3"

        new_difficulty_text = "Difficulty: " + difficulty_level + "/3"
        difficulty_text_field.insert(0, new_difficulty_text)
        difficulty_text_field['state'] = 'disabled'


    """
    This function chooses and displays the next word set
    The function determines what level it is, determines if all the words have been shown, 
    then randomly chooses and displays a word set.
    """
    def next_level():
        global current
        global current_index


        words_text_field['state'] = 'enabled'
        words_text_field.delete(0, END)


        if(current >= 0 and current <= 1): #If it's level 1 or 2

            all_words_used = True
            level_1_combinations = []

            # Put all of the word sets of difficulty level 1/3 into the list 'level_1_combinations'
            for i in range(len(word_combinations)):
                if(word_combinations[i][2] == "1"):
                    level_1_combinations.append(word_combinations[i])
            
            # Iterate through 'level_1_combinations' and if any word set has not been used,
            # set 'all_words_used' to False
            for i in range(len(level_1_combinations)):
                if(level_1_combinations[i][3] == "0"):
                    all_words_used = False
                    break

            # This block of code reverts all the difficulty level 1 word sets to being unused.
            # If all of the words have been used after iterating through 'level_1_combinations',
            # iterate through 'word_combinations' and change the fourth variable in the
            # difficulty level 1 word sets to '0'. 0 indicates that the word set has not been shown.
            if(all_words_used):
                for i in range(len(word_combinations)):
                    if(word_combinations[i][2] == "1"):
                        word_combinations[i][3] = "0"

            # Now, because of the previous code, the program can randomly choose a word set
            # regardless of whether or not all words have been used. This helps prevent errors from
            # occurring if the user closes the window in the middle of a game.
            
            # This block of code randomly chooses a word set in 'word_combinations'
            # If the chosen word set is of difficulty level 1 and has not been displayed,
            # Set 'current_index' to this word set and display this word set.
            # Otherwise, randomly choose another word set.
            # This process may be iterated up to 1000 times to ensure that an unused, difficulty level 1
            # word is chosen instead of a used and/or difficulty level 2 or 3 word.
            for i in range(1000):
                selected_index = random.randint(0, len(word_combinations)-1)
                if(word_combinations[selected_index][2] == "1" and word_combinations[selected_index][3] == "0"):
                    current_index = selected_index
                    words_text_field.insert(0, word_combinations[current_index][0])
                    break
                else:
                    pass


        elif(current >= 2 and current <= 3): #If it's level 3 or 4

            all_words_used = True
            level_2_combinations = []

            for i in range(len(word_combinations)):
                if(word_combinations[i][2] == "2"):
                    level_2_combinations.append(word_combinations[i])

            for i in range(len(level_2_combinations)):
                if(level_2_combinations[i][3] == "0"):
                    all_words_used = False
                    break

            if(all_words_used):
                for i in range(len(word_combinations)):
                    if(word_combinations[i][2] == "2"):
                        word_combinations[i][3] = "0"

            for i in range(1000):
                selected_index = random.randint(0, len(word_combinations)-1)
                if(word_combinations[selected_index][2] == "2" and word_combinations[selected_index][3] == "0"):
                    current_index = selected_index
                    words_text_field.insert(0, word_combinations[current_index][0])
                    break
                else:
                    pass
                    

        elif(current >= 4 and current <= 5): #If it's level 5 or 6

            all_words_used = True
            level_3_combinations = []

            for i in range(len(word_combinations)):
                if(word_combinations[i][2] == "3"):
                    level_3_combinations.append(word_combinations[i])
            for i in range(len(level_3_combinations)):
                if(level_3_combinations[i][3] == "0"):
                    all_words_used = False
                    break

            if(all_words_used):
                for i in range(len(word_combinations)):
                    if(word_combinations[i][2] == "3"):
                        word_combinations[i][3] = "0"
                
            for i in range(1000):
                selected_index = random.randint(0, len(word_combinations)-1)
                if(word_combinations[selected_index][2] == "3" and word_combinations[selected_index][3] == "0"):
                    current_index = selected_index
                    words_text_field.insert(0, word_combinations[current_index][0])
                    break
                else:
                    pass


        words_text_field['state'] = 'disabled'


    """
    This function displays text when a game has been completed
    The function displays the appropriate celebratory message depending on your score,
    as well as instructions on how to be added to the leaderboard.
    """
    def display_ending():
        global score

        if(current == 6): #This if-statement ensures that multiple labels and buttons appear
            ending_label = Label(gameWindow, text="", font=('Helvetica 13')) #Celebratory message label
            ending_label.pack(pady=35)
            ttk.Button(gameWindow, text= "Enter", command= update_leaderboard_text).pack(pady=5) #Updates leaderboard if clicked   
        
        words_text_field['state'] = 'enabled'
        words_text_field.delete(0, END)
        words_text_field['state'] = 'disabled'

        # Determine the appropriate celebratory message,
        # then add instructions on how to be added to the leaderboard to the message
        # and display this text in 'ending_label'
        name_question = " Please type your name and today's date into the text box, then click 'Enter'."
        if(score >= 9 and score <= 12):
            ending_label.config(text="Great Job!" + name_question, font=('Helvetica 13'))
        elif(score >= 6 and score < 9):
            ending_label.config(text="Good Job!" + name_question, font=('Helvetica 13'))
        elif(score >= 0 and score < 6):
            ending_label.config(text="Better Luck Next Time!" + name_question, font=('Helvetica 13'))


    """
    This function updates the leaderboard
    The function formats global variable 'leaderboard_text' so that it displays all of the 
    necessary information
    """
    def update_leaderboard_text():
        global leaderboard_text
        global score

        # If the user clicks on the leaderboard button before playing a game, the leaderboard will say
        # 'No one has played the game.' This code updates 'leaderboard_text' so that it no longer says
        # this once a game is played.
        if(leaderboard_text == "No one has played the game."):
            leaderboard_text = ""

        # This code formats 'leaderboard_text' if the player didn't type any information in when
        # prompted by the celebratory message at the end of the game
        name_date = answer_text_box.get()
        if(name_date == "" or name_date == " "):
            name_date = "Anonymous (Date Unknown)"

        # Determines if the user played pre-made levels or custom levels
        game_type = ""
        if(word_combinations == premade_word_combinations):
            game_type = "[Pre-Made Levels] "
        elif(word_combinations == custom_word_combinations):
            game_type = "[Custom Levels] "
        else:
            game_type = " "

        # Append the game's information to 'leaderboard_text'
        leaderboard_text += "\n" + game_type + name_date + " --- " + str(score)
        gameWindow.destroy()


    """
    This function handles changing levels
    The function determines what level it is and if the answer is correct, 
    then calls certain functions and updates variables accordingly
    """
    def get_answer():
        global current
        global current_index
        
        if(current <= 5): #If the game is still in progress
            if(answer_text_box.get() == word_combinations[current_index][1]):
                verification_label.config(text="Correct!", font=('Helvetica 13'))
                increase_score()
            else:
                verification_label.config(text="Wrong", font=('Helvetica 13'))

            word_combinations[current_index][3] = "1" #Indicate that the word has been shown before
            current += 1
            answer_text_box.delete(0, END)

            if(current == 6): #If it's the last level
                display_ending()
            elif(current <= 5): #If the game is still in progress
                change_level_label()
                change_difficulty_label()
                next_level()


    # This code is ran once you click 'Play Pre-Made Levels' or 'Play Custom Levels'
    # The window and all of its widgets are created and placed
    gameWindow = Toplevel(root) #Create the window
    gameWindow.state('zoomed') #Make the window full-screen
    gameWindow.title("Game Window")

    title_label = Label(gameWindow, text ="IMPOSTER", font=('Sans Serif', 48)).pack(pady=15)

    words_text_field = Entry(gameWindow, width=50, justify=CENTER, font=('Sans Serif', 20,'bold'))
    next_level() #Start the game by calling 'next_level'
    words_text_field.pack(pady=15)

    answer_text_box = Entry(gameWindow, width=30, justify=CENTER, font=('Sans Serif', 20,'bold'))
    answer_text_box.pack(pady=15)

    ttk.Button(gameWindow, text= "Guess!", command= get_answer).pack(pady=15)
    gameWindow.bind('<Return>', lambda e: get_answer()) #Allow user to press the return key to submit their guess

    verification_label = Label(gameWindow, text="", font=('Helvetica 13'))
    verification_label.pack()

    score_text_field = Entry(gameWindow, width=15, justify=CENTER, font=('Sans Serif', 10,'bold'))
    score_text_field.insert(0, "Score: 0")
    score_text_field['state'] = 'disabled'
    score_text_field.pack(pady=5)

    level_text_field = Entry(gameWindow, width=15, justify=CENTER, font=('Sans Serif', 10,'bold'))
    level_text_field.insert(0, "Level: 1")
    level_text_field['state'] = 'disabled'
    level_text_field.pack(pady=5)

    difficulty_text_field = Entry(gameWindow, width=15, justify=CENTER, font=('Sans Serif', 10,'bold'))
    difficulty_text_field.insert(0, "Difficulty: 1/3")
    difficulty_text_field['state'] = 'disabled'
    difficulty_text_field.pack(pady=5)



"""
This function controls the level creator
The function creates the window and all of its widgets, and includes the functionality to create custom levels
"""
def open_level_creator():

    creatorWindow = Toplevel(root) #Create the window
    creatorWindow.state('zoomed') #Make the window full-screen
    creatorWindow.title("Level Creator")

    # This function allows you to create custom levels
    def add_levels():
        global custom_word_combinations

        # Determine if any of the text boxes have not been filled in
        all_fields_filled_in = True
        if(len(word1_text_box.get()) == 0 or len(answer1_text_box.get()) == 0):
            all_fields_filled_in = False
        elif(len(word2_text_box.get()) == 0 or len(answer2_text_box.get()) == 0):
            all_fields_filled_in = False
        elif(len(word3_text_box.get()) == 0 or len(answer3_text_box.get()) == 0):
            all_fields_filled_in = False
        elif(len(word4_text_box.get()) == 0 or len(answer4_text_box.get()) == 0):
            all_fields_filled_in = False
        elif(len(word5_text_box.get()) == 0 or len(answer5_text_box.get()) == 0):
            all_fields_filled_in = False
        elif(len(word6_text_box.get()) == 0 or len(answer6_text_box.get()) == 0):
            all_fields_filled_in = False
        
        # If all of the text boxes have been filled in (a requirement),
        # add all of the word sets to 'custom_word_combinations' in the proper formatting.
        # Otherwise, tell the user to fill in all of the text boxes.
        if(all_fields_filled_in):
            custom_word_combinations.append([word1_text_box.get(), answer1_text_box.get(), "1", "0"])
            custom_word_combinations.append([word2_text_box.get(), answer2_text_box.get(), "1", "0"])
            custom_word_combinations.append([word3_text_box.get(), answer3_text_box.get(), "2", "0"])
            custom_word_combinations.append([word4_text_box.get(), answer4_text_box.get(), "2", "0"])
            custom_word_combinations.append([word5_text_box.get(), answer5_text_box.get(), "3", "0"])
            custom_word_combinations.append([word6_text_box.get(), answer6_text_box.get(), "3", "0"])
            creatorWindow.destroy()
        else:
            fields_window = Toplevel(creatorWindow)
            fields_window.title("Missing Fields")
            fields_window = Label(fields_window, text="Please fill in ALL text boxes.", font=('Sans Serif', 10)).pack(pady=15)


    # This code creates all of the widgets
    difficulty_instruction_label = Label(creatorWindow, text="Difficulty", font=('Sans Serif', 20))
    words_instruction_label = Label(creatorWindow, text="Word Set", font=('Sans Serif', 20))
    answer_instruction_label = Label(creatorWindow, text="Answer Word", font=('Sans Serif', 20))
    add_levels_button = Button(creatorWindow, text="Add Levels!", command=add_levels)
    exit_button = Button(creatorWindow, text="Exit (Progress will NOT be saved)", command=creatorWindow.destroy)

    word1_difficulty_label = Label(creatorWindow, text="1/3", font=('Sans Serif', 20))
    word1_text_box = Entry(creatorWindow, width=50, justify=LEFT, font=('Sans Serif', 20,'bold'))
    word1_text_box.delete(0, END)
    answer1_text_box = Entry(creatorWindow, width=20, justify=LEFT, font=('Sans Serif', 20,'bold'))
    answer1_text_box.delete(0, END)

    word2_difficulty_label = Label(creatorWindow, text="1/3", font=('Sans Serif', 20))
    word2_text_box = Entry(creatorWindow, width=50, justify=LEFT, font=('Sans Serif', 20,'bold'))
    word2_text_box.delete(0, END)
    answer2_text_box = Entry(creatorWindow, width=20, justify=LEFT, font=('Sans Serif', 20,'bold'))
    answer2_text_box.delete(0, END)

    word3_difficulty_label = Label(creatorWindow, text="2/3", font=('Sans Serif', 20))
    word3_text_box = Entry(creatorWindow, width=50, justify=LEFT, font=('Sans Serif', 20,'bold'))
    word3_text_box.delete(0, END)
    answer3_text_box = Entry(creatorWindow, width=20, justify=LEFT, font=('Sans Serif', 20,'bold'))
    answer3_text_box.delete(0, END)

    word4_difficulty_label = Label(creatorWindow, text="2/3", font=('Sans Serif', 20))
    word4_text_box = Entry(creatorWindow, width=50, justify=LEFT, font=('Sans Serif', 20,'bold'))
    word4_text_box.delete(0, END)
    answer4_text_box = Entry(creatorWindow, width=20, justify=LEFT, font=('Sans Serif', 20,'bold'))
    answer4_text_box.delete(0, END)

    word5_difficulty_label = Label(creatorWindow, text="3/3", font=('Sans Serif', 20))
    word5_text_box = Entry(creatorWindow, width=50, justify=LEFT, font=('Sans Serif', 20,'bold'))
    word5_text_box.delete(0, END)
    answer5_text_box = Entry(creatorWindow, width=20, justify=LEFT, font=('Sans Serif', 20,'bold'))
    answer5_text_box.delete(0, END)

    word6_difficulty_label = Label(creatorWindow, text="3/3", font=('Sans Serif', 20))
    word6_text_box = Entry(creatorWindow, width=50, justify=LEFT, font=('Sans Serif', 20,'bold'))
    word6_text_box.delete(0, END)
    answer6_text_box = Entry(creatorWindow, width=20, justify=LEFT, font=('Sans Serif', 20,'bold'))
    answer6_text_box.delete(0, END)
    

    # This code places all of the widgets in their positions
    difficulty_instruction_label.grid(row=0, column=0, pady=10, padx=10)
    words_instruction_label.grid(row=0, column=1, pady=10, padx=10)
    answer_instruction_label.grid(row=0, column=2, pady=10, padx=10)
    add_levels_button.grid(row=7, column=2, pady=25, padx=10)
    exit_button.grid(row=8, column=2, pady=10, padx=10)

    word1_difficulty_label.grid(row=1, column=0, pady=10, padx=10)
    word1_text_box.grid(row=1, column=1, pady=10, padx=10)
    answer1_text_box.grid(row=1, column=2, pady=10, padx=10)

    word2_difficulty_label.grid(row=2, column=0, pady=10, padx=10)
    word2_text_box.grid(row=2, column=1, pady=10, padx=10)
    answer2_text_box.grid(row=2, column=2, pady=10, padx=10)

    word3_difficulty_label.grid(row=3, column=0, pady=10, padx=10)
    word3_text_box.grid(row=3, column=1, pady=10, padx=10)
    answer3_text_box.grid(row=3, column=2, pady=10, padx=10)

    word4_difficulty_label.grid(row=4, column=0, pady=10, padx=10)
    word4_text_box.grid(row=4, column=1, pady=10, padx=10)
    answer4_text_box.grid(row=4, column=2, pady=10, padx=10)

    word5_difficulty_label.grid(row=5, column=0, pady=10, padx=10)
    word5_text_box.grid(row=5, column=1, pady=10, padx=10)
    answer5_text_box.grid(row=5, column=2, pady=10, padx=10)

    word6_difficulty_label.grid(row=6, column=0, pady=10, padx=10)
    word6_text_box.grid(row=6, column=1, pady=10, padx=10)
    answer6_text_box.grid(row=6, column=2, pady=10, padx=10)


"""
This function ensures the game is played with pre-made levels.
If you click 'Play Pre-Made Levels',
'word_combinations', which is used in the main 'play_game' function,
will be set to 'premade_word_combinations', shown at the top of the code.
The function 'play_game' will then be called.
"""
def set_premade_games():
    global word_combinations

    word_combinations = premade_word_combinations
    play_game()


"""
This function ensures the game is played with custom levels.
If you click 'Play Custom Levels' and custom levels have been created,
'word_combinations', which is used in the main 'play_game' function,
will be set to 'custom_word_combinations', shown at the top of the code.
The function 'play_game' will then be called.
If custom levels haven't been created, the user will be told.
"""
def set_custom_games():
    global word_combinations

    if(len(custom_word_combinations) == 0): #If custom levels haven't been created
        no_custom_levels_window = Toplevel(root)
        no_custom_levels_window.title("No Custom Levels")
        no_custom_levels_text = '''
        No custom levels have been created.
        Click on the Level Creator button to make some!
        Then, invite your friends to play your custom levels!
        '''
        no_custom_levels_label = Label(no_custom_levels_window, text=no_custom_levels_text, font=('Helvetica 13', 10)).pack(pady=15)
    else:
        word_combinations = custom_word_combinations
        play_game()


"""
This function displays the leaderboard
The function creates a new window and displays 'leaderboard_text' (which stores all leaderboard information)
"""
def show_leaderboard():
    global leaderboard_text

    if(leaderboard_text == ""):
        leaderboard_text = "No one has played the game."

    leaderboard_window = Toplevel(root)
    leaderboard_window.title("Leaderboard")
    leaderboard_label = Label(leaderboard_window, text=leaderboard_text, font=('Helvetica 13', 10)).pack(pady=15)


# This function creates a new window and displays the general instructions and rules
def show_instructions():
    global INSTRUCTIONS

    instructions_window = Toplevel(root)
    instructions_window.title("Instructions and Rules")
    instructions_label = Label(instructions_window, text=INSTRUCTIONS, font=('Helvetica 13', 10)).pack(pady=15)


# This function creates a new window and displays the level creator instructions
def show_level_creator_instructions():
    global LEVEL_CREATOR_INSTRUCTIONS

    level_creator_instructions_window = Toplevel(root)
    level_creator_instructions_window.title("Level Creator Instructions")
    level_instruct_label = Label(level_creator_instructions_window, text=LEVEL_CREATOR_INSTRUCTIONS, font=('Helvetica 13', 10)).pack(pady=15)


# This function closes the main window (title screen)
def close_window(e):
   root.destroy()


root = Tk() #Create the main window (title screen)
root.state('zoomed') #Make the window full-screen
root.title("Imposter")
root.bind('<Escape>', lambda e: close_window(e)) #Allow user to press the escape key to close the main window


# Create and place all of the widgets on the main window
title_text = Label(root, text ="Welcome to Imposter!", font=('Sans Serif', 24)).pack(pady= 30)
play_premade_button = Button(root, text="Play Pre-Made Levels", command=set_premade_games).pack(pady= 5)
instructions_button = Button(root, text="General Instructions", command=show_instructions).pack(pady= 5)
placeholder_label_1 = Label(root, text="", font=('Helvetica 13', 10)).pack(pady= 5)
level_creator_button = Button(root, text="Level Creator", command=open_level_creator).pack(pady= 5)
play_custom_button = Button(root, text="Play Custom Levels", command=set_custom_games).pack(pady= 5)
level_instructions_button = Button(root, text="Level Creator Instructions", command=show_level_creator_instructions).pack(pady= 5)
placeholder_label_2 = Label(root, text="", font=('Helvetica 13', 10)).pack(pady= 5)
leaderboard_button = Button(root, text="Leaderboard", command=show_leaderboard).pack(pady= 5)
quit_button = Button(root, text="Quit", command=root.destroy).pack(pady= 5)


root.mainloop()
#imports for GUI and the matchmaking custom class
import tkinter as tk
from Matchmaker import Matchmaker

#create the menu window
menu = tk.Tk()
menu.geometry('2000x2000')
menu.configure(bg = 'light pink')

def close_menu():
    '''
    close menu screen
    '''
    
    menu.destroy()

#creaet a play game button
play_B = tk.Button(menu, text = 'Play Game', command = close_menu, font = (15))
play_B.place(x = 450, y = 200)
play_B.configure(width = 30)

#make a title for the menu screen
title = tk.Label(menu, text = 'Are You The One?', bg = 'light pink', fg = 'blue', font = ('MS Sans Serif', 50))
title.place(x = 355, y = 50)


#show the instructions for the game
show_instructions = tk.Label(menu, text = 'Synopsis: Welcome to the hit show \'Are You The One?\'.\n\n16 LUCKY contestants have been chosen to find out who their true love is.\n\nThey will all be assigned an alias of your choosing once the game starts.\n\n(To help confused viewers and raise our ratings we only allow unique aliases per person)\n\nOur trusty matchmaker who shall remain anonymous will select pairs of people they think best match.\n\nIt\'s up to you to compare each contestants traits and each week match the pairs you think are the best match together.\n\nIf you can guess all 8 pairs before week 30, then you win the cash prize of $1.\n\n Good Luck and Have Fun!', bg = 'light pink', font = ('Times', 14, 'bold'))
show_instructions.place(x = 150, y = 275)

#run the menu screen
menu.mainloop()



#create the ayto (are you the one) screen
ayto = tk.Tk()
ayto.configure(bg = 'light blue')
ayto.geometry('2000x2000')

#vairbles that need to be established for use later in the program, of note the fact that the player starts on week 1 is established here
week = 1
Error = tk.Label()
wrong = []
right = []

#create a label telling the user to enter names
enter_names = tk.Label(ayto, text = 'Enter The Names of 16 Contestants In the Boxes Below', bg = 'light blue', fg = 'red', font = ('Arial', 25))
enter_names.place(x = 235, y = 150)

#Creates text boxes to type names in
name1 = tk.Entry(ayto)
name2 = tk.Entry(ayto)
name3 = tk.Entry(ayto)
name4 = tk.Entry(ayto)
name5 = tk.Entry(ayto)
name6 = tk.Entry(ayto)
name7 = tk.Entry(ayto)
name8 = tk.Entry(ayto)
name9 = tk.Entry(ayto)
name10 = tk.Entry(ayto)
name11 = tk.Entry(ayto)
name12 = tk.Entry(ayto)
name13 = tk.Entry(ayto)
name14 = tk.Entry(ayto)
name15 = tk.Entry(ayto)
name16 = tk.Entry(ayto)

#places each entry box at a specific coordinate
name1.place(x = 275, y = 250)
name2.place(x = 475, y = 250)
name3.place(x = 675, y = 250)
name4.place(x = 875, y = 250)
name5.place(x = 275, y = 300)
name6.place(x = 475, y = 300)
name7.place(x = 675, y = 300)
name8.place(x = 875, y = 300)
name9.place(x = 275, y = 350)
name10.place(x = 475, y = 350)
name11.place(x = 675, y = 350)
name12.place(x = 875, y = 350)
name13.place(x = 275, y = 400)
name14.place(x = 475, y = 400)
name15.place(x = 675, y = 400)
name16.place(x = 875, y = 400)

def getGuess():
    '''
    -collects guesses and checks if they're wrong or right
    -updates the current week
    -allows for a gameover or win
    '''

    #make some varibales global for potential use elsewhere
    global right_str, wrong_str, week
    
    #increase the week every time a guess is made
    week += 1

    #if the week hits 30 and it's gameover, don't run the code for guesses
    if week < 31:
    
        #destroy the initial week label
        week1_wid.destroy()
        
        #create the new week label to be updated
        week_wid = tk.Label(ayto, text= f' Week {week}', bg = 'light blue', fg = 'red', font = ('MS Sans Serif', 40))
        week_wid.place(x = 515, y = 125)

        #guess one and two are collected
        one = guess1.get()
        two = guess2.get()

        #make empty strings to be added to in order to display past guesses
        right_str = ''
        wrong_str = ''

        #checks to see if the list containing the tuples of pairs has the guesses the user entered
        if (one, two) in list_pair:
        
            #correct guess
            guess = (one, two)
        
            #only add guess to the correct guesses if it's not already in there preventing duplicates or reversed duplicates
            if (one, two) not in right and (two, one) not in right:
        
                right.append(guess)

            #iterate over the guesses in the right guesses list 
            for guess in right:
        
                if guess == right[-1]:
            
                    #end of guesses
                    right_str += f'{guess}'

                else:
            
                    #guesses will continue
                    right_str += f'{guess}, '

            #remove the pair from the list so it can count towards winning
            list_pair.remove((one, two))
            
            #create a feedback label telling the user they were correct
            feedback = tk.Label(ayto, text = 'Correct! Guess Again', bg = 'light blue', font = (40))
            feedback.place(x = 530, y = 400)

            #create the correct guess label to show the user what they've already gotten right
            guess_list_correct = tk.Label(ayto, text = f'Correct Pairs You\'ve Guessed: {right_str}', bg = 'light blue')
            guess_list_correct.place(x = 10, y = 600)

        #checks to see if the list containing the tuples of pairs has the guesses the user entered (opposite box entries this time)
        elif (two, one) in list_pair:
        
            #correct guess
            guess = (two, one)
        
            #only add guess to the correct guesses if it's not already in there preventing duplicates or reversed duplicates
            if (one, two) not in right and (two, one) not in right:
        
                right.append(guess)

            #iterate over every guess in the right guesses list
            for guess in right:
        
                if guess == right[-1]:
            
                    #end of guesses
                    right_str += f'{guess}'

                else:
            
                    #guesses will continue
                    right_str += f'{guess}, '

            #remove the pair from the list so it can count towards winning
            list_pair.remove((two, one))
            
            #create a feedback label telling the user they were correct
            feedback = tk.Label(ayto, text = 'Correct! Guess Again', bg = 'light blue', font = (40))
            feedback.place(x = 530, y = 400)
            
            #create the correct guess label to show the user what they've already gotten right
            guess_list_correct = tk.Label(ayto, text = f'Correct Pairs You\'ve Guessed: {right_str}', bg = 'light blue')
            guess_list_correct.place(x = 10, y = 600)

        #checks if the guess was wrong
        elif (one, two) not in list_pair or (two, one) not in list_pair:
        
            #wrong guess
            guess = (one, two)

            #only add to wrong guesses list if it isn't already in there
            if ((one, two) not in wrong and (two, one) not in wrong) and ((one, two) not in right and (two, one) not in right):
        
                wrong.append(guess)

            #iterate over every guess in the wrong guesses list
            for guess in wrong:
        
                if guess == wrong[-1]:
            
                    #last guess
                    wrong_str += f'{guess}'

                else:
            
                    #guesses continue
                    wrong_str += f'{guess}, '

            #create a feeback label telling the user they were wrong
            feedback = tk.Label(ayto, text = 'Wrong! Guess Again  ', bg = 'light blue', font = (40))
            feedback.place(x = 530, y = 400)

            #create a incorrect guess list to show the user their past incorrect guesses
            guess_list_incorrect = tk.Label(ayto, text = f'Incorrect Pairs You\'ve Guessed: {wrong_str}', bg = 'light blue')
            guess_list_incorrect.place(x = 10, y = 575)

        #if there are no more guesses in the pair list, that means the user wins
        if len(list_pair) == 0:
        
            #create a feedback label telling the user they win
            feedback = tk.Label(ayto, text = 'Congratulations You Found All Pairs!', bg = 'light blue', font = (40))
            feedback.place(x = 475, y = 400)
    
    #if the user goes over week 30 they lose
    else:

        #create a game over text to appear
        game_over = tk.Label(text = 'Game Over! You Didn\'t Win $1', bg = 'light blue', font = (25))
        game_over.place(x = 500, y = 400)        


def getNames():
    '''
    -collects names and puts them into a list to be randomized
    -transitions to guess screen
    -assigns traits using Matchmaker class
    '''
    
    #globalizes variables for use outside of the function
    global names, list_pair, guess1, guess2, week1_wid, Match, Error, guess_button

    #collects all names
    a = name1.get()
    b = name2.get()
    c = name3.get()
    d = name4.get()
    e = name5.get()
    f = name6.get()
    g = name7.get()
    h = name8.get()
    i = name9.get()
    j = name10.get()
    k = name11.get()
    l = name12.get()
    m = name13.get()
    n = name14.get()
    o = name15.get()
    p = name16.get()

    #puts names into a list               
    names = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]
    
    #checks if the user has all unique names entered (covers empty names too)
    unique_names = True

    #iterate over the length of names
    for i in range(len(names) - 1):

        #if a nae in the list is equal to one index up then there are not all unique names or any name is empty
        if names[i] == names[i + 1] or names[i] == '' or names[i + 1] == '':

            #set unique names to false so the program won't continue
            unique_names = False

            #destroy the empty error and create a new error to remind the user they need unique names and all boxes must be filled
            Error.destroy()
            Error = tk.Label(ayto, bg = 'light blue', font = ('Times', 15), text = 'Invalid Choice Detected: All Slots Must Be Filled And Your Names Must Be Unique Due To The Studio Not Wanting To Confuse Viewers :(')
            Error.place(x = 80 , y = 550)

    #run the next code switching screens to the guessing game part
    if unique_names == True:
        
        #detsroy an error if there was one
        Error.destroy()
        
        #destroy everything from the previous screen to transition
        name1.destroy()
        name2.destroy()
        name3.destroy()
        name4.destroy()
        name4.destroy()
        name5.destroy()
        name6.destroy()
        name7.destroy()
        name8.destroy()
        name9.destroy()
        name10.destroy()
        name11.destroy()
        name12.destroy()
        name13.destroy()
        name14.destroy()
        name15.destroy()
        name16.destroy()
        name_button.destroy()
        enter_names.destroy()

        #establish a week 1 label that will be added to every time someone guesses
        week1_wid = tk.Label(ayto, text= f' Week 1', bg = 'light blue', fg = 'red', font = ('MS Sans Serif', 40))
        week1_wid.place(x = 515, y = 125)

        #create an instance of a matchmaker class given the list of names, creating random pairs and assigning them traits
        Match = Matchmaker(names)

        #create a variable for the pairs the matchmaker randomized
        list_pair = Match.pairs

        #creates label telling the user to guess
        guess_wid = tk.Label(ayto, text = 'Guess A Pair', bg = 'light blue', font = ('Arial', 20))
        guess_wid.place(x = 540, y = 275)
    
        #creates boxes to enter guesses
        guess1 = tk.Entry(ayto)
        guess2 = tk.Entry(ayto)

        #places the boxes to enter guesses at specific coordinates
        guess1.place(x = 450, y = 350)
        guess2.place(x = 675, y = 350)

        #retrive person 1's traits
        person1_traits = Match.pair_traits[names[0]]

        #display person 1's name and their traits
        person1 = tk.Label(ayto, text = f'{person1_traits}', bg = 'light blue')
        person1.place(x = 10, y = 40)
        person1_name = tk.Label(ayto, text = f'{names[0]}', bg = 'light blue', fg = 'dark red', font = ('BOLD'))
        person1_name.place(x = 75, y = 10)
        
        #retrieve person 2's traits
        person2_traits = Match.pair_traits[names[1]]

        #display person 2's traits and their name
        person2 = tk.Label(ayto, text = f'{person2_traits}', bg = 'light blue')
        person2.place(x = 240, y = 40)
        person2_name = tk.Label(ayto, text = f'{names[1]}', bg = 'light blue', fg = 'dark red', font = ('BOLD'))
        person2_name.place(x = 325, y = 10)

        #retrieve person 3's traits
        person3_traits = Match.pair_traits[names[2]]

        #display person3's traits and their name
        person3 = tk.Label(ayto, text = f'{person3_traits}', bg = 'light blue')
        person3.place(x = 10, y = 175)
        person3_name = tk.Label(ayto, text = f'{names[2]}', bg = 'light blue', fg = 'dark red', font = ('BOLD'))
        person3_name.place(x = 75, y = 145)
        
        #retrieve person 4's traits
        person4_traits = Match.pair_traits[names[3]]

        #display person 4's traits and their name
        person4 = tk.Label(ayto, text = f'{person4_traits}', bg = 'light blue')
        person4.place(x = 240, y = 175)
        person4_name = tk.Label(ayto, text = f'{names[3]}', bg = 'light blue', fg = 'dark red', font = ('BOLD'))
        person4_name.place(x = 325, y = 145)

        #retrieve person 5's traits
        person5_traits = Match.pair_traits[names[4]]

        #display person 5's traits and their name
        person5 = tk.Label(ayto, text = f'{person5_traits}', bg = 'light blue')
        person5.place(x = 10, y = 315)
        person5_name = tk.Label(ayto, text = f'{names[4]}', bg = 'light blue', fg = 'dark red', font = ('BOLD'))
        person5_name.place(x = 75, y = 285)
        
        #retrieve person 6's traits
        person6_traits = Match.pair_traits[names[5]]

        #display person 6's traits and their name
        person6 = tk.Label(ayto, text = f'{person6_traits}', bg = 'light blue')
        person6.place(x = 240, y = 315)
        person6_name = tk.Label(ayto, text = f'{names[5]}', bg = 'light blue', fg = 'dark red', font = ('BOLD'))
        person6_name.place(x = 325, y = 285)
        
        #retrieve person 7's traits
        person7_traits = Match.pair_traits[names[6]]

        #display person 7's traits and their name
        person7 = tk.Label(ayto, text = f'{person7_traits}', bg = 'light blue')
        person7.place(x = 10, y = 450)
        person7_name = tk.Label(ayto, text = f'{names[6]}', bg = 'light blue', fg = 'dark red', font = ('BOLD'))
        person7_name.place(x = 75, y = 420)
        
        #retrieve person 8's traits
        person8_traits = Match.pair_traits[names[7]]

        #display person 8's traits and their name
        person8 = tk.Label(ayto, text = f'{person8_traits}', bg = 'light blue')
        person8.place(x = 240, y = 450)
        person8_name = tk.Label(ayto, text = f'{names[7]}', bg = 'light blue', fg = 'dark red', font = ('BOLD'))
        person8_name.place(x = 325, y = 420)
        
        #retrieve person 9's traits
        person9_traits = Match.pair_traits[names[8]]

        #display person 9's traits and their name
        person9 = tk.Label(ayto, text = f'{person9_traits}', bg = 'light blue')
        person9.place(x = 830, y = 40)
        person9_name = tk.Label(ayto, text = f'{names[8]}', bg = 'light blue', fg = 'dark red', font = ('BOLD'))
        person9_name.place(x = 900, y = 10)
        
        #retrieve person 10's traits
        person10_traits = Match.pair_traits[names[9]]

        #display perosn 10's traits and their name
        person10 = tk.Label(ayto, text = f'{person10_traits}', bg = 'light blue')
        person10.place(x = 1060, y = 40)
        person10_name = tk.Label(ayto, text = f'{names[9]}', bg = 'light blue', fg = 'dark red', font = ('BOLD'))
        person10_name.place(x = 1130, y = 10)
        
        #retrieve person 11's traits
        person11_traits = Match.pair_traits[names[10]]

        #display person 11's traits and their name
        person11 = tk.Label(ayto, text = f'{person11_traits}', bg = 'light blue')
        person11.place(x = 830, y = 175)
        person11_name = tk.Label(ayto, text = f'{names[10]}', bg = 'light blue', fg = 'dark red', font = ('BOLD'))
        person11_name.place(x = 900, y = 145)
        
        #retrieve perosn 12's traits
        person12_traits = Match.pair_traits[names[11]]

        #display person 12's traits and their name
        person12 = tk.Label(ayto, text = f'{person12_traits}', bg = 'light blue')
        person12.place(x = 1060, y = 175)
        person12_name = tk.Label(ayto, text = f'{names[11]}', bg = 'light blue', fg = 'dark red', font = ('BOLD'))
        person12_name.place(x = 1130, y = 145)

        #retrieve person 13's traits
        person13_traits = Match.pair_traits[names[12]]

        #display person 13's traits and their name
        person13 = tk.Label(ayto, text = f'{person13_traits}', bg = 'light blue')
        person13.place(x = 830, y = 315)
        person13_name = tk.Label(ayto, text = f'{names[12]}', bg = 'light blue', fg = 'dark red', font = ('BOLD'))
        person13_name.place(x = 900, y = 285)

        #retrieve person 14's traits
        person14_traits = Match.pair_traits[names[13]]

        #display person 14's traits and their name
        person14 = tk.Label(ayto, text = f'{person14_traits}', bg = 'light blue')
        person14.place(x = 1060, y = 315)
        person14_name = tk.Label(ayto, text = f'{names[13]}', bg = 'light blue', fg = 'dark red', font = ('BOLD'))
        person14_name.place(x = 1130, y = 285)
        
        #retrieve person 15's traits
        person15_traits = Match.pair_traits[names[14]]

        #display person 15's traits and their name
        person15 = tk.Label(ayto, text = f'{person15_traits}', bg = 'light blue')
        person15.place(x = 830, y = 450)
        person15_name = tk.Label(ayto, text = f'{names[14]}', bg = 'light blue', fg = 'dark red', font = ('BOLD'))
        person15_name.place(x = 900, y = 420)
  
        #retrieve person 16's traits
        person16_traits = Match.pair_traits[names[15]]

        #display person 16's traits and their name
        person16 = tk.Label(ayto, text = f'{person16_traits}', bg = 'light blue')
        person16.place(x = 1060, y = 450)
        person16_name = tk.Label(ayto, text = f'{names[15]}', bg = 'light blue', fg = 'dark red', font = ('BOLD'))
        person16_name.place(x = 1130, y = 420)

        #gives a button to submit guesses and places it
        guess_button = tk.Button(ayto, text = 'Submit Guess', command = getGuess, font = (15))
        guess_button.place(x = 555, y = 450)
    
#gives a button to submit names and places it
name_button = tk.Button(ayto, text = 'Enter Names', command = getNames, font = (14))
name_button.place(x = 570, y = 475)

#runs the app after the menu screen is closed
menu.after(100, close_menu)
ayto.mainloop()


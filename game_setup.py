#Bryan Diep 27192773. ICS 32 Lab sec. 4. Lab asst 5

#This module starts the game

import tkinter
import logic
import gui
from functools import partial

class BoardInformation:
    def __init__(self):
        self._root_window = tkinter.Tk()

        self._root_window.configure(padx = 10, pady = 10, background = 'yellow')

        self._player_color = ['Black','White']

        self._win_mode = ['Most Pieces', 'Least Pieces']

        self._button_number = [4,6,8,10,12,14,16]

        #WELCOME LABEL################################################
        self._welcome_text = tkinter.StringVar()
        self._welcome_text.set('Welcome to Othello')

        welcome_label = tkinter.Label(
            master = self._root_window, textvariable = self._welcome_text,
            font = ('Helvetica', 15), background = 'yellow')

        welcome_label.grid(
            row = 0, column = 0, columnspan = 3, padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S)

        #COLUMN LABEL####################################################
        self._column_text = tkinter.StringVar()
        self._column_text.set('Pick the number of columns: ')

        column_label = tkinter.Label(
            master = self._root_window, textvariable = self._column_text,
            font = ('Helvetica', 12), background = 'yellow')

        column_label.grid(
            row = 1, column = 0, padx = 0, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W)
        
        #COLUMN BUTTONS####################################################
        button_frame = tkinter.Frame(
            master = self._root_window, background = 'yellow')

        button_frame.grid(
            row = 2, column = 0, padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W)

        for button_number in self._button_number:
            column_button = tkinter.Button(
                master = button_frame, text = '{}'.format(button_number),
                font = ('Helvetica', 15), command = partial(self._on_column_button, button_number))

            column_button.grid(
                row = 1, column = button_number - 2, padx = 0, pady = 0)

        #ROW LABEL####################################################
        self._row_text = tkinter.StringVar()
        self._row_text.set('Pick the number of rows: ')

        row_label = tkinter.Label(
            master = self._root_window, textvariable = self._row_text,
            font = ('Helvetica', 12), background = 'yellow')

        row_label.grid(
            row = 3, column = 0, padx = 0, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W)

        #ROW BUTTONS####################################################
        button_frame2 = tkinter.Frame(
            master = self._root_window, background = 'yellow')

        button_frame2.grid(
            row = 4, column = 0, padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W)

        for button_number in self._button_number:
            row_button = tkinter.Button(
                master = button_frame2, text = '{}'.format(button_number),
                font = ('Helvetica', 15), command = partial(self._on_row_button, button_number))

            row_button.grid(
                row = 0, column = button_number - 2, padx = 0, pady = 0)

        #PLAYER LABEL####################################################
        self._player_text = tkinter.StringVar()
        self._player_text.set('Which player will move first?: ')

        player_label = tkinter.Label(
            master = self._root_window, textvariable = self._player_text,
            font = ('Helvetica', 12), background = 'yellow')

        player_label.grid(
            row = 5, column = 0, padx = 0, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W)

        #PLAYER BUTTONS####################################################
        button_frame3 = tkinter.Frame(
            master = self._root_window, background = 'yellow')

        button_frame3.grid(
            row = 6, column = 0, padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W)

        for player_color in self._player_color:
            first_player_button = tkinter.Button(
                master = button_frame3, text = '{}'.format(player_color),
                font = ('Helvetica', 15), command = partial(self._on_first_player_button, player_color))

            first_player_button.grid(
                row = 0, column = self._player_color.index(player_color), padx = 0, pady = 0)

        #LEFT LABEL####################################################
        self._upper_left_text = tkinter.StringVar()
        self._upper_left_text.set('Which side should be in the upper-left of the four cells?: ')

        upper_left_label = tkinter.Label(
            master = self._root_window, textvariable = self._upper_left_text,
            font = ('Helvetica', 12), background = 'yellow')

        upper_left_label.grid(
            row = 7, column = 0, padx = 0, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W)

        #LEFT BUTTONS####################################################
        button_frame4 = tkinter.Frame(
            master = self._root_window, background = 'yellow')

        button_frame4.grid(
            row = 8, column = 0, padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W)

        for player_color in self._player_color:
            upper_left_button = tkinter.Button(
                master = button_frame4, text = '{}'.format(player_color),
                font = ('Helvetica', 15), command = partial(self._on_upper_left_button, player_color))

            upper_left_button.grid(
                row = 0, column = self._player_color.index(player_color), padx = 0, pady = 0)

        #WIN MODE LABEL####################################################
        self._win_mode_text = tkinter.StringVar()
        self._win_mode_text.set('How would you like to win by?: ')

        win_mode_label = tkinter.Label(
            master = self._root_window, textvariable = self._win_mode_text,
            font = ('Helvetica', 12), background = 'yellow')

        win_mode_label.grid(
            row = 9, column = 0, padx = 0, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W)

        #WIN MODE BUTTONS####################################################
        button_frame5 = tkinter.Frame(
            master = self._root_window, background = 'yellow')

        button_frame5.grid(
            row = 10, column = 0, padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W)

        for win_mode in self._win_mode:
            win_mode_button = tkinter.Button(
                master = button_frame5, text = '{}'.format(win_mode),
                font = ('Helvetica', 15), command = partial(self._on_win_mode_button, win_mode))

            win_mode_button.grid(
                row = 0, column = self._win_mode.index(win_mode), padx = 0, pady = 0)

        #LETS PLAY BUTTON####################################################
        lets_play_button = tkinter.Button(
            master = self._root_window, text = "Let's Play!",
            font = ('Helvetica', 15), command = self._on_lets_play_button)

        lets_play_button.grid(
            row = 11, column = 1, padx = 0, pady = 20,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        #CANCEL BUTTON#######################################################
        cancel_button = tkinter.Button(
            master = self._root_window, text = 'Cancel',
            font = ('Helvetica', 15), command = self._root_window.destroy)

        cancel_button.grid(
            row = 11, column = 2, padx = 5, pady = 20,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        #RESIZING############################################################
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.rowconfigure(3, weight = 1)
        self._root_window.rowconfigure(4, weight = 1)
        self._root_window.rowconfigure(5, weight = 1)
        self._root_window.rowconfigure(6, weight = 1)
        self._root_window.rowconfigure(7, weight = 1)
        self._root_window.rowconfigure(8, weight = 1)
        self._root_window.rowconfigure(9, weight = 1)
        self._root_window.rowconfigure(10, weight = 1)
        self._root_window.rowconfigure(11, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)
        self._root_window.columnconfigure(2, weight = 1)

        #PRIVATE VARIABLES###################################################
        self._column = 0
        self._row = 0
        self._first_player = ''
        self._upper_left = ''
        self._win_by = ''

    #ON BUTTON FUNCTIONS#######################################################
    #These 'on button' functions grabs the input the user made on the board and
    #stores them into a private variable
    ###########################################################################
    def _on_column_button(self, column_number):
        self._column = column_number
        self._column_text.set('Pick the number of columns: ' + str(self._column))

    def _on_row_button(self, row_number):
        self._row = row_number
        self._row_text.set('Pick the number of rows: ' + str(self._row))

    def _on_first_player_button(self, first_player):
        self._first_player = first_player
        self._player_text.set('Which player will move first?: ' + self._first_player)

    def _on_upper_left_button(self, upper_left):
        self._upper_left = upper_left
        self._upper_left_text.set('Which side should be in the upper-left of the four cells?: ' + self._upper_left)

    def _on_win_mode_button(self, win_mode):
        self._win_by = win_mode
        self._win_mode_text.set('How would you like to win by?: ' + self._win_by)
    
    def _on_lets_play_button(self):
        '''This button function checks if the user has given all of the inputs
before starting the game. An error window will pop up if the input has not been compeleted.'''
        if self._column == 0 or self._row == 0 or self._first_player == '' or self._upper_left == '' or self._win_by == '':
            self._error_window = tkinter.Toplevel()
            self._error_window.configure(background = 'white')
                      
            self._error_text = tkinter.StringVar()
            self._error_text.set('You did not finish setting up the board!')
            
            error_label = tkinter.Label(
                master = self._error_window, textvariable = self._error_text,
                font = ('Helvetica', 15), background = 'white')
            error_label.grid(
                row = 0, column = 0, padx = 30, pady= 50,
                sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

            ok_button = tkinter.Button(
                master = self._error_window, text = 'Okay',width = 10,height = 1, 
                font = ('Helvetica', 10), command = self._error_window.destroy)
            ok_button.grid(
                row = 1, column = 0, padx = 0, pady= 0,
                sticky = tkinter.N + tkinter.S + tkinter.E)
            
            self._error_window.rowconfigure(0, weight = 1)
            self._error_window.columnconfigure(0, weight = 1)
        else:
            self._root_window.destroy()
            game = gui.GameBoard(self._row, self._column, self._first_player,
                                  self._upper_left, self._win_by)
            game.start()
        
        
        

    def start(self):
        self._root_window.mainloop()

if __name__ == '__main__':
    BoardInformation().start()

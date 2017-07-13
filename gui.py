#Bryan Diep 27192773. ICS 32 Lab sec. 4. Lab asst 5

#The game_setup module starts the game

import tkinter
import game_setup
import logic

class GameBoard:
    def __init__(self, row, column, first_player, upper_left, win_by):
        self._root_window = tkinter.Tk()
        
        #Variables from GameSetup
        self._column = column
        self._row = row
        self._first_player = first_player
        self._upper_left = upper_left
        self._win_by = win_by

        #Private Variables in this class
        self._black_score = 2
        self._white_score = 2
        self._player = first_player

        #Calling my logic module
        self._othello = logic.GameState(self._row, self._column, self._first_player,
                                  self._upper_left, self._win_by)
        self._board = self._othello.create_game_state()
        
        ############################################################################
        #CREATING LABELS AND CANVAS
        ############################################################################
        #Title label
        self._title_text = tkinter.StringVar()
        self._title_text.set("Othello")
    
        self._title_label = tkinter.Label(
            master = self._root_window, background = '#FF6600',
            textvariable = self._title_text, font = ('Cooper Black', 20))
        self._title_label.grid(
            row = 0, column = 0, padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        
        #Indicate Turn
        self._turn_text = tkinter.StringVar()
        self._turn_text.set(self._player + "'s turn")
    
        self._turn_label = tkinter.Label(
            master = self._root_window, background = '#FFFF00',
            textvariable = self._turn_text, font = ('Helvetica', 20))
        self._turn_label.grid(
            row = 0, column = 1, padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        #Create canvas for the board
        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 500, height = 500,
            background = '#0066FF')
        self._canvas.grid(
            row = 1, column = 1, padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        #Create side bar left of board for scores
        self._title_text = tkinter.StringVar()
        self._title_text.set('Score    \nBlack: ' + str(self._black_score) + '\nWhite: ' + str(self._white_score))
    
        self._title_label = tkinter.Label(
            master = self._root_window, background = '#FFFF00',
            textvariable = self._title_text, font = ('Helvetica', 20))
        self._title_label.grid(
            row = 1, column = 0, padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas.bind('<Configure>', self.resize_canvas)
        self._canvas.bind('<Button-1>', self.click_on_canvas)

        self._root_window.rowconfigure(1, weight = 1)        
        self._root_window.columnconfigure(1, weight = 1)


    def start(self):
        '''Waits for the game_setup module to call the GameBoard class'''
        self._root_window.grab_set()
        self._root_window.wait_window()

    def resize_canvas(self, event: tkinter.Event):
        '''Resizes the board'''
        self._draw_board()
        
    def _draw_board(self):
        '''Draws board and draws the pieces in the board'''
        self._canvas.delete(tkinter.ALL)
        
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        
        width = canvas_width/self._row
        height = canvas_height/self._column
        
        for row in range(len(self._board)):
            self._canvas.create_line(row*width,0,row*width,canvas_height)
        for column in range(len(self._board[0])):
            self._canvas.create_line(0, column*height, canvas_width, column*height)

        for row in range(len(self._board)):
            for column in range(len(self._board[0])):
                if self._board[row][column] == 'B':
                    self._canvas.create_oval(row*width, column*height, (row+1)*width, (column+1)*height, fill = 'black', outline = 'black')
                elif self._board[row][column] == 'W':
                    self._canvas.create_oval(row*width, column*height, (row+1)*width, (column+1)*height, fill = 'white', outline = 'black')

    def change_player(self):
        '''Changes the color of the player from its private variable'''
        if self._player == 'Black':
            self._player = 'White'
        elif self._player == 'White':
            self._player = 'Black'

    def opposite_player(self):
        '''Gets the opposite color'''
        if self._player == 'Black':
            return 'White'
        elif self._player == 'White':
            return 'Black'
        
    def _update_score_board(self):
        '''This function updates the score of each player.
It is called after each move and updates the tkinter.Labels'''
        scores = self._othello.display_score(self._board)
        self._title_text.set('Score\nBlack: ' + str(scores[1]) + '\nWhite: ' + str(scores[0]))
        self._white_score = scores[0]
        self._black_score = scores[1]
        
    def click_on_canvas(self, event):
        '''Checks which row and column nearest to the coordinate of the mouse and passes into the logic module.
The logic module takes the move and checks if it is a valid move. Then it places and changes the piece on the board.
The GameBoard takes the board from the logic module and draws the spots onto the graphic board. This process repeats
until the game has ended with a victor or in a stalemate.'''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        width = canvas_width/self._row
        height = canvas_height/self._column  

        spot_x = 0
        spot_y = 0

        for row in range(len(self._board)):
            if row*width < event.x and (row+1)*width > event.x:
                spot_x = row
        for column in range(len(self._board[0])):
            if column*height < event.y and (column+1)*height > event.y:
                spot_y = column
                
        #I used the try method to prevent shell from calling the errors each
        #an invalid move is made.
        try:        
            list_of_pieces = self._othello.move_is_valid(spot_x, spot_y, self._board)
            
            if list_of_pieces != 0:
                self._board = self._othello.place_piece(spot_x, spot_y, self._board)
                self._board = self._othello.change_pieces(list_of_pieces, self._board)
                
                for row in range(len(self._board)):
                    for column in range(len(self._board[0])):
                        if self._board[row][column] == 'B':
                            self._canvas.create_oval(row*width, column*height, (row+1)*width, (column+1)*height, fill = 'black', outline = 'black')
                        elif self._board[row][column] == 'W':
                            self._canvas.create_oval(row*width, column*height, (row+1)*width, (column+1)*height, fill = 'white', outline = 'black')

                self._update_score_board()
                
                if self._othello.next_turn_is_valid(self._board) == True:
                    self.change_player()
                    self._turn_text.set(self._player + "'s turn")
                else:
                    if self._othello.next_turn_is_valid(self._board) == True:
                        other_player = self.opposite_player()
                        self._turn_text.set(other_player + " cannot move!       " + self._player + "'s turn")
                    else:
                        self._winner()
        except:
            pass
        
    def on_yes_button(self):
        '''Destroys the current game board and starts a new game'''
        self._root_window.destroy()
        game_setup.BoardInformation().start()
        
        
    def _winner(self):
        '''This function is called when the game is over. It announces
the winner then it asks whether the user wants to play again.'''
        winner = self._othello.winning_player()
        
        winner_window = tkinter.Toplevel()
        winner_window.configure(background = 'white')

        winner_text = tkinter.StringVar()
        if winner[0] == 'Tie':
            winner_text.set('The Black and White player have reached a tie!\n\nWould you like to start a new game?')
        else:
            winner_text.set('Congradulations, ' + winner[0] + ' is the winner!\n\nWould you like to start a new game?')
            
        winner_label = tkinter.Label(
            master = winner_window, textvariable = winner_text, font = ('Helvetica', 15), background = 'white')
        winner_label.grid(
            row = 0, column = 0, columnspan = 3, padx = 30, pady = 50,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        yes_button = tkinter.Button(
            master = winner_window, text = 'Yes', width = 10, height = 1,
            font = ('Helvetica', 10), command = self.on_yes_button)
        yes_button.grid(
            row = 1, column = 1, padx = 0, pady= 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        
        no_button = tkinter.Button(
            master = winner_window, text = 'No', width = 10, height = 1,
            font = ('Helvetica', 10), command = self._root_window.destroy)
        no_button.grid(
            row = 1, column = 2, padx = 0, pady= 0,
            sticky = tkinter.S + tkinter.N + tkinter.W + tkinter.E)
        
        winner_window.rowconfigure(0, weight = 1)
        winner_window.columnconfigure(0, weight = 1)
    
                

    

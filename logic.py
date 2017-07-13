#Bryan Diep 27192773. ICS 32 Lab sec. 4. Lab asst 5

#The game_setup module starts the game

#Exceptions
class MoveOutOfBoardError(Exception):
    pass
class InvalidMoveError(Exception):
    pass

class PlacePieceError(Exception):
    pass

class GameIsOverError(Exception):
    pass

#######################################

class GameState:
    def __init__(self, numRows, numCols, player, topLeft, winMode):
        self._numRows = numRows
        self._numCols = numCols
        self._player = player[0].upper()
        self._topLeft = topLeft
        self._win_mode = winMode
        self._black_score = 0
        self._white_score = 0

    def get_player(self):
        if self._player == 'B':
            return 'Black'
        elif self._player == 'W':
            return 'White'

    def create_game_state(self) -> list:
        '''Creates the board with four pieces in the center'''
        
        board = []
        
        for row in range(self._numRows):
            new_row = []
            for column in range(self._numCols):
                new_row.append(' ')
            board.append(new_row)
            
        if self._topLeft == 'Black':
            board[int(self._numRows/2) - 1][int(self._numCols/2) - 1] = 'B'
            board[int(self._numRows/2)][int(self._numCols/2)] = 'B'
            board[int(self._numRows/2)][int(self._numCols/2) - 1] = 'W'
            board[int(self._numRows/2) - 1][int(self._numCols/2)] = 'W'
        else:
            board[int(self._numRows/2) - 1][int(self._numCols/2) - 1] = 'W'
            board[int(self._numRows/2)][int(self._numCols/2)] = 'W'
            board[int(self._numRows/2)][int(self._numCols/2) - 1] = 'B'
            board[int(self._numRows/2) - 1][int(self._numCols/2)] = 'B'

        return board


    def move_is_valid(self, row_num, col_num, board) -> list:
        '''Checks if the user's move is valid'''
        
        if self._is_on_board(row_num, col_num) == False:
            raise MoveOutOfBoardError('Move is outside of the board\'s range')
        
        if self._player == 'B':
            opposite_piece = 'W'
        else:
            opposite_piece = 'B'
                    
        directions = [[0,1],[0,-1],[1,0],[-1,0],[-1,1],[1,-1],[-1,-1],[1,1]]
        pieces_to_flip = []
        
        if board[row_num][col_num] == ' ':
            for xandy in directions:
                pieces = []
                
                row_number = row_num
                column_number = col_num
                
                row_number += xandy[0]
                column_number += xandy[1]
                
                while self._is_on_board(row_number, column_number):
                    if board[row_number][column_number] == opposite_piece:
                        pieces.append([row_number,column_number])
                    elif board[row_number][column_number] == self._player and len(pieces) >= 1:
                        pieces_to_flip.extend(pieces)
                    else:
                        break

                    row_number += xandy[0]
                    column_number += xandy[1]
                    
        return pieces_to_flip        
                
    def place_piece(self, row_num, col_num, board) -> list:
        '''Places user's piece onto the board'''
        
        if len(self.move_is_valid(row_num, col_num, board)) == 0:
            raise InvalidMoveError('You cannot place your piece here')
        
        if board[row_num][col_num] != ' ':
            raise PlacePieceError('Place is already taken')
        
        board[row_num][col_num] = self._player
        return board

    def change_pieces(self, list_of_pieces, board) -> list:
        '''Changes the pieces that are affected by the piece placed by the user'''
        
        for pieces in list_of_pieces:
            board[pieces[0]][pieces[1]] = self._player
        return board

    def display_score(self, board) -> list:
        '''Displays the score after the user finishes his/her move'''
        
        number_of_white_pieces = 0
        number_of_black_pieces = 0
        
        for row in board:
            for piece in row:
                if piece == 'W':
                    number_of_white_pieces += 1
                elif piece == 'B':
                    number_of_black_pieces += 1
                    
        self._white_score = number_of_white_pieces
        self._black_score = number_of_black_pieces
                    
        return [number_of_white_pieces, number_of_black_pieces]

    def winning_player(self):
        if self._win_mode == 'Least Pieces':
            if self._white_score == self._black_score:
                return ['Tie', None]
            elif min(self._white_score, self._black_score) == self._white_score:
                return ['White', self._white_score]
            else:
                return ['Black', self._black_score] 
        if self._win_mode == 'Most Pieces':
            if self._white_score == self._black_score:
                return ['Tie', None]
            elif max(self._white_score, self._black_score) == self._black_score:
                return ['Black', self._black_score]
            else:
                return ['White', self._white_score]
            

    def next_turn_is_valid(self, board) -> bool:
        '''Checks if the next player can make a move on the board'''
        
        if self._player == 'B':
            self._player = 'W'
        else:
            self._player = 'B'
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                if len(self.move_is_valid(row, col, board)) != 0:
                    return True
                
        return False

    def _is_on_board(self, row_num, col_num)-> bool:
        '''Checks if the move is in the board'''
        
        if row_num >= 0 and row_num < self._numRows and col_num >= 0 and col_num < self._numCols:
            return True
        else:
            return False

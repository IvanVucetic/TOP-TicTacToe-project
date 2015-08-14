# Ivan Vucetic
# vuceta87@yahoo.com

# Tic Tac Toe game

# 14/08/2015


class Board(object):
    '''Represents a board, prints it out and checks for a winner of a game.'''
    
    fields = {"A1": " ", "A2": " ", "A3": " ", 
              "B1": " ", "B2": " ", "B3": " ",
              "C1": " ", "C2": " ", "C3": " "}

    def __init__(self):
        '''Creates a new table for playing.'''
        pass
        
    
    def printTable(self):
        '''Prints out a table with current positions.'''
        
        print """
        | A | B | C |
         --- --- ---
      1 | %s | %s | %s |
         --- --- ---
      2 | %s | %s | %s |
         --- --- ---
      3 | %s | %s | %s |
     """ % (self.fields['A1'], self.fields['B1'], self.fields['C1'],
            self.fields['A2'], self.fields['B2'], self.fields['C2'],
            self.fields['A3'], self.fields['B3'], self.fields['C3'],) 
             
   
    def isMoveValid(self, cell):
        ''' True if the user input is valid ("A1" or similar), False otherwise '''

        if cell in self.fields:
            return True
        else:
            return False

    
    def isFieldFree(self, cell):
        '''True if the field is empty, False if already occupied'''

        if self.fields[cell] == " ":
            return True
        else:
            return False



class Player(object):
    '''Player of the game.'''
    
    def __init__(self, marker):
        '''Creates a player with marker X or O.'''
        self.marker = marker;


    def submitMove(self, board, cell):
        '''Changes the value of the field to a players marker ('X'/'O').'''
        board.fields[cell] = self.marker



class Engine(object):
    '''Engine running the game.'''

    def __init__(self):
        '''Creates a new game-running engine.'''
        self.counter = 0


    def run(self, board, p1, p2):
        '''Runs the game untill there is a winner or untill there are no more free cells.'''
        
        while self.counter <10:

            # based on a turn, decides which player makes a move
            if (self.counter % 2) == 0:
                current_player = p1
            else:
                current_player = p2
    
            # keeps asking the player for input untill the input is valid
            while True:
                
                print "Player move (%s)" % current_player.marker
                targetCell = raw_input("> ")
                  
                if board.isMoveValid(targetCell) is True:
                    if board.isFieldFree(targetCell) is True:
                        break
                    else:
                        print "That field is already taken. Try another."
                else:
                    print "Invalid Input: Please enter the column and row of your move (Example: A1)."
            
            
            current_player.submitMove(board, targetCell)

            board.printTable()

            self.counter += 1

            # couldn't find a way to implement OR, to put all options in 1 if 
            if all(x == current_player.marker for x in (board.fields['A1'], 
                                                        board.fields['A2'], 
                                                        board.fields['A3'])):
                print "You win!"
                break
            elif all(x == current_player.marker for x in (board.fields['B1'], 
                                                          board.fields['B2'], 
                                                          board.fields['B3'])):
                print "You win!"
                break
            elif all(x == current_player.marker for x in (board.fields['C1'], 
                                                          board.fields['C2'], 
                                                          board.fields['C3'])):
                print "You win!"
                break
            elif all(x == current_player.marker for x in (board.fields['A1'], 
                                                          board.fields['B1'], 
                                                          board.fields['C1'])):
                print "You win!"
                break
            elif all(x == current_player.marker for x in (board.fields['A2'], 
                                                          board.fields['B2'], 
                                                          board.fields['C2'])):
                print "You win!"
                break
            elif all(x == current_player.marker for x in (board.fields['A3'], 
                                                          board.fields['B3'], 
                                                          board.fields['C3'])):
                print "You win!"
                break
            elif all(x == current_player.marker for x in (board.fields['A1'], 
                                                          board.fields['B2'], 
                                                          board.fields['C3']) ):
                print "You win!"
                break
            elif all(x == current_player.marker for x in (board.fields['A3'], 
                                                          board.fields['B2'], 
                                                          board.fields['C1'])):
                print "You win!"
                print "BYE"
                break
            elif self.counter == 9:
                print "It's a draw!"
                print "BYE"
                break



# Perhaps the game could work without the Engine class, with the run
# function in the Table class

# perhaps the checking of the Winner/Draw could be done in a separate function
# and just be called during the run, to avoid excessive indentation

    
# Gave up on the class Cell approach because I couldn't find a way to 
# manipulate cells based on user input. For example, I wanted for user to type 
# in the cell "a2" and have the a2.cellValue change to "X" or "O", but 
# couldn't do it, as user input "a2" is a string, which is different from the 
# object a2.

# class Cell(object):
#     '''Stores a value of a single field on the board.'''
#     
#     cellValue = " "
# 
#     def __init__(self):
#         '''Creates an empty cell'''
#         pass

tabla = Board()

player1 = Player("X")
player2 = Player("O")

tabla.printTable()

newGame = Engine()

newGame.run(tabla, player1, player2)

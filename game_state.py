# Code to model the game state

class GameState:
# __init__(self) is special method that is automatically called when a new object from the classs is created
    def __init__(self): # self refers to the object itself
        
        # Creates an attribute player1 within the GameState object
        self.player1 = {
            "health": 500,
            "gold": 1,
            "hand": [],
            "deck": [],
            "discard_pile": [],
        }

        self.player2 = {
            "health": 500,
            "gold": 2,
            "hand": [],
            "deck": [],
            "discard_pile": [],
        }
        self.monkey_board = {"player1": [], "player2": []} # Tracks monkeys on the board
        self.bloons_board = {"player1": [], "player2": []} # Tracks bloons on the board
        self.current_turn = "player1" # Tracks whose turn it is
        self.turn_num = 1
        self.winner = None # Tracks the winner of the game
    


    # Checks if the game has a winner
    def check_winner(self):
        if self.player1["health"] <= 0:
            self.winner  = "player2"
        elif self.player2["health"] <= 0:
            self.winner = "player2"
        

    # Rests game state
    def reset(self):
        self.__init__() # Call the constructor to reinitialize
    


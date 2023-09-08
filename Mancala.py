# Author: Kenny Tran
# Github username: trankenny4
# Date: 11/21/2022
# Description: A program that allows the Mancala game to be played between two players.

class Player:
    ''' Represents a player for the Mancala game '''

    def __init__(self, name):
        ''' Initalizing the Player class with the player's name '''
        self._name = name
        
    def get_name(self):
        ''' Method to get the Player's name '''
        return self._name
        
class Mancala:
    ''' Represents the Mancala game '''
    
    def __init__(self):
        ''' Initializing the Mancala class'''
        self._players = []                                              # List of current Player OBJECTS in the class
        self._board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]        # This is the starting board for the Mancala game
      
    def create_player(self, player_name):
        ''' Takes one parameter (player's name as a string) as returns the player object '''
        if len(self._players) < 2:                                      # Checking if there are more than 2 players. If there are more than 2, return an error.
            player = Player(player_name)
            return self._players.append(player)
        else:
            return "This game of Mancala already contains two players. No more players can be added."
            
    def get_player(self, index):
        ''' Method that returns the Player OBJECT in self._players depending on the index. Index 1 = Player 2, Index 2 = Player 2'''
        if index == 1:
            return self._players[0]
        elif index == 2:
            return self._players[1]
        else:
            return "Invalid index. Enter 1 for the index for Player 1 and enter 2 for index for Player 2."
               
    def final_board(self):
        ''' Method that returns the final board of the Mandala game. '''
        
        # Sum up player 1's pits and put the total in the store
        for pit_seeds in range(6):
            self._board[6] += self._board[pit_seeds]

        # Sum up player 2's pits and put the total in the store      
        for pit_seeds in range(7,13):
            self._board[13] += self._board[pit_seeds]

        # Set all of player 1's pit seeds to 0
        for pit in range(6):
            self._board[pit] = 0
            
        # Set all of player 2's pit seeds to 0
        for pit in range(7,13):
            self._board[pit] = 0
        
        return self._board
               
    def print_board(self):
        ''' Method that prints the board information in a specified format '''
        
        # First check if the game is already complete. If it is, show the final board
        if self.game_complete() is True:
            self.final_board()
        
        # Reversing player 2's list so that it can be printed in order from pits 1 to 6, as directed in the ReadMe.
        p2_reversed = self._board[7:]
        p2_reversed.reverse()
   
        # Chosen layout for the game board
        print(f"================ GAME BOARD ================")
        print(f"Player 2:  {p2_reversed[0]}   {p2_reversed[1:]}")
        print(f"Player 1:      {self._board[0:6]}   {self._board[6]}\n")
        
        print(f"Player 1:")
        print(f"       store: {self._board[6]}")
        print(f"    pits 1-6: {self._board[0:6]}\n")

        print(f"Player 2:")
        print(f"        store: {self._board[13]}")
        print(f"     pits 1-6: {self._board[7:13]}")
        print(f"============================================")
    
    def game_complete(self):
        ''' Method to check if the game is currently complete '''
        player1_pits = self._board[:6]             # Retrieving Player one's board from pits 1 to 6
        player2_pits = self._board[7:13]           # Retrieving Player two's board from pits 1 to 6
        
        # Game ends if one player's pits are all empty, so checking if each player's board has 6 zero pits
        if player1_pits.count(0) == 6 or player2_pits.count(0) == 6:   
            return True
        else:
            return False
                   
    def return_winner(self):   
        ''' 
        Method to return the winner of the game. 
            
        Takes no parameters. 
        Returns the winner in the format: "Winner is player1(or 2): player's name"."
        If the game is a tie, return "It's a tie"
        If the game is not complete, return "Game has not ended"
        '''   
        
        if self.game_complete() is False:                                           # Check if the game is complete first. If it is not, return an error messsage to the user
            return "Game has not ended"
        else:
            self.final_board()                                                      # If the game is complete, first set the final board of the game

            if self._board[6] == self._board[13]:                                   # Tie condition
                return "It's a tie"          
            elif self._board[6] > self._board[13]:                                  # Player 1 store > Player 2 store
                return f"Winner is player 1: {self.get_player(1).get_name()}"   
            else:                                                                   # Player 2 store > Player 1 store
                return f"Winner is player 2: {self.get_player(2).get_name()}"
            
    def play_game(self, player_index, pit_index):
        ''' 
        Method that allows the Mancala game to be played.
        
        Takes a parameter for the player index (1 or 2) and the pit index (1-6). Both values are integers.
               
        This method performs the following:
            - follows the rules of a typical Mancala game including two special rules 
            - updates seed numbers and in each pit and store accordingly per user action's in a turn
            - if the user inputs an invalid pit index (>6 or <= 0), return: "Invalid number for pit index"
            - if game is ended at this point, return "Game is ended"
            - if a player wins extra rounds following special rule 1, print out "Player 1 takes another turn" (same for player 2)
        
        The method returns a list of the current seeds and pits in the format:
                [player1 pit1, player1 pit2, player1 pit3, player1 pit4, player1 pit5, player1 pit6, player1 store,
                    Player2 pit1, player2 pit2, player2 pit3, player2 pit4, player2 pit5, player2 pit6, player2 store,]
           
        Does not enforce that player turns are in order.       

        '''
        
        if pit_index > 6 or pit_index < 1:
            return "Invalid number for pit index"
        elif self.game_complete() is True:
            return "Game is ended"
        elif player_index not in [1,2]:
            return "Invalid player. Enter 1 for player 1 and 2 for player 2."

        if player_index == 1:
            seeds_to_move = self._board[pit_index-1]
            seeds_to_move_copy = seeds_to_move
            self._board[pit_index-1] = 0                                    # Setting current pit to 0, essentially all seeds now picked up.
            counter_index = pit_index
            
            # The loop to add one seed into each pit            
            while seeds_to_move > 0:                                        
                if counter_index > 13:                                      # If the index is greater than the index length of the board, restart at 0.
                    counter_index = 0
                elif counter_index == 13:                                   # For player 1, if a seed reaches player 2's store, ignore the store and increment next pit.
                    counter_index += 1
                    continue 
                                        
                self._board[counter_index] = self._board[counter_index] + 1
                counter_index += 1
                seeds_to_move -= 1
            
            self.captured(player_index, pit_index, seeds_to_move_copy)      # Check if the player has captured anything under Special Rule #2
            self.go_again(player_index, pit_index, seeds_to_move_copy)      # Check if the player is allowed to go again under Special Rule #1
        
        if player_index == 2:
            seeds_to_move = self._board[pit_index + 6]                      # Since the pit_index is given in the range 1-6, must add 6 to get the proper index of the list.
            seeds_to_move_copy = seeds_to_move
            self._board[pit_index + 6] = 0
            counter_index = pit_index + 7
                        
            while seeds_to_move > 0:
                if counter_index > 13:
                    counter_index = 0
                elif counter_index == 6:                                   # For player 2, if a seed reaches player 1's store, ignore the store and increment next pit.
                    counter_index += 1
                    continue
                                        
                self._board[counter_index] = self._board[counter_index] + 1
                counter_index += 1
                seeds_to_move -= 1     

            self.captured(player_index, pit_index, seeds_to_move_copy)
            self.go_again(player_index, pit_index, seeds_to_move_copy)
         
        # Returning the board, depending on the current game status. If complete, return the final board. Otherwise, return the current board.    
        if self.game_complete() is True:
            return self.final_board()
        else:
            return self._board
                
    def captured(self, player_index, pit_index, seeds_to_move_copy):
        ''' Method to checks for Special Rule #2. Determins if any seeds are to be capture based on final positioning. '''
        
        # Two dicionarys that contain the opposite index's number of seeds.
        player_1_opposites = {
                    1: self._board[12],
                    2: self._board[11],
                    3: self._board[10],
                    4: self._board[9],
                    5: self._board[8],
                    6: self._board[7],
                    }
        player_2_opposites = {
                    1: self._board[5],
                    2: self._board[4],
                    3: self._board[3],
                    4: self._board[2],
                    5: self._board[1],
                    6: self._board[0],
                    }
        
        if player_index == 1:
            final_pit_index = pit_index + seeds_to_move_copy
            
            # If a pit has more than 13 seeds, then find the remainder of that result to figure out what the final position would be. 
            # Then set the final pit index appropriately.
            if pit_index + seeds_to_move_copy > 12:       
                final = pit_index + ((pit_index + seeds_to_move_copy) % 12)
                final_pit_index = (pit_index + final) % 7 + 1
        
            # Series of statements to check if there is only one seed in the pit (after the player has already dropped 1 into each pit) at a particular pit index.
            # If there is only one seed, that means the pit was previously empty.
            # If the capture conditions are satisfied, then all both the last pit and the opposite pit into the Player's store and set both pits to 0 seeds.
            if final_pit_index == 1 and self._board[0] == 1:
                self._board[6] = self._board[6] + self._board[0] + player_1_opposites[final_pit_index]
                self._board[0] = 0
                self._board[12] = 0
            elif final_pit_index == 2 and self._board[1] == 1:
                self._board[6] = self._board[6] + self._board[1] + player_1_opposites[final_pit_index]
                self._board[1] = 0
                self._board[11] = 0
            elif final_pit_index == 3 and self._board[2] == 1:
                self._board[6] = self._board[6] + self._board[2] + player_1_opposites[final_pit_index]
                self._board[2] = 0
                self._board[10] = 0   
            elif final_pit_index == 4 and self._board[3] == 1:
                self._board[6] = self._board[6] + self._board[3] + player_1_opposites[final_pit_index]
                self._board[3] = 0
                self._board[9] = 0    
            elif final_pit_index == 5 and self._board[4] == 1:
                self._board[6] = self._board[6] + self._board[4] + player_1_opposites[final_pit_index]
                self._board[4] = 0
                self._board[8] = 0   
            elif final_pit_index == 6 and self._board[5] == 1:
                self._board[6] = self._board[6] + self._board[5] + player_1_opposites[final_pit_index]
                self._board[5] = 0
                self._board[7] = 0    
                
        elif player_index == 2:
            final_pit_index = pit_index + seeds_to_move_copy
            
            if pit_index + seeds_to_move_copy > 12:
                final = pit_index + ((pit_index + seeds_to_move_copy) % 12)
                final_pit_index = (pit_index + final) % 7 + 1   
            
            if final_pit_index == 1 and self._board[7] == 1:
                self._board[13] = self._board[13] + self._board[7] + player_2_opposites[final_pit_index]
                self._board[7] = 0
                self._board[5] = 0 
            elif final_pit_index == 2 and self._board[8] == 1:
                self._board[13] = self._board[13] + self._board[8] + player_2_opposites[final_pit_index]
                self._board[8] = 0
                self._board[4] = 0 
            elif final_pit_index == 3 and self._board[9] == 1:
                self._board[13] = self._board[13] + self._board[9] + player_2_opposites[final_pit_index]
                self._board[9] = 0
                self._board[3] = 0 
            elif final_pit_index == 4 and self._board[10] == 1:
                self._board[13] = self._board[13] + self._board[10] + player_2_opposites[final_pit_index]
                self._board[10] = 0
                self._board[2] = 0   
            elif final_pit_index == 5 and self._board[11] == 1:
                self._board[13] = self._board[13] + self._board[11] + player_2_opposites[final_pit_index]
                self._board[11] = 0
                self._board[1] = 0               
            elif final_pit_index == 6 and self._board[12] == 1:
                self._board[13] = self._board[13] + self._board[12] + player_2_opposites[final_pit_index]
                self._board[12] = 0
                self._board[0] = 0                         
                         
    def go_again(self, player_index, pit_index, seeds_to_move_copy): 
        ''' 
        Method that checks for Special Rule #1 (if the last seed in your hand lands in your store, take another turn) 
        
        Takes as parameters the index of the pit and the total seeds in the pit will be moved.
        '''      
        if player_index == 1 and (pit_index + seeds_to_move_copy == 7):
            print("player 1 take another turn")
        elif player_index == 2 and (pit_index + seeds_to_move_copy == 7):
            print("player 2 take another turn")
     
            
# game = Mancala()
# player1 = game.create_player("Lily")
# player2 = game.create_player("Lucy")
# game.print_board()
# print(game.return_winner())

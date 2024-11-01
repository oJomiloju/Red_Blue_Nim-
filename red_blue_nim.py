'''
RED BLUE NIM GAME USING MINMAX SEARCH WITH ALPHA BETA PRUNING 
'''
import sys 
import argparse

class GameState:
    def __init__(self, red_pile, blue_pile, version):
        self.red_pile = red_pile
        self.blue_pile = blue_pile
        self.version = version  # Store the version within GameState
    
    def is_terminal(self):
        ''' CHECK IF THE GAME HAS REACHED A TERMINAL STATE '''
        if self.red_pile == 0 or self.blue_pile == 0:
            return True
    
    def get_possible_moves(self):
        ''' RETURN A LIST OF POSSIBLE MOVES (PICK 1 OR 2 MARBLES FROM A PILE) '''
        moves = []
        if self.red_pile >= 2:
            moves.append(('red', 2))
        if self.blue_pile >= 2:
            moves.append(('blue', 2))
        if self.red_pile >= 1:
            moves.append(('red', 1))
        if self.blue_pile >= 1:
            moves.append(('blue', 1))
        if self.version == 'misere':
            moves.reverse()  # Reverse the order for Misère version
        return moves
    
    def apply_move(self, move):
        ''' APPLY THE MOVE TO THE GAME STATE '''
        pile, count = move
        if pile == 'red':
            new_red_pile = self.red_pile - count
            new_blue_pile = self.blue_pile
        else:
            new_red_pile = self.red_pile
            new_blue_pile = self.blue_pile - count
        return GameState(new_red_pile, new_blue_pile, self.version)
    
    def evaluate(self, player):
        ''' EVALUATE THE CURRENT STATE FOR THE PLAYER '''
        red_value = 2
        blue_value = 3
        score = self.red_pile * red_value + self.blue_pile * blue_value
        
        if self.is_terminal():
            if self.version == 'standard':
                return -score
            elif self.version == 'misere':
                return score

        return score if player == 'human' else -score



class RedBlueNim:
    def __init__(self, red_pile, blue_pile, version, first_player):
        self.game_state = GameState(red_pile, blue_pile, version)
        self.current_player = first_player

    def play_game(self):
        while not self.game_state.is_terminal():
            self.print_game_state()

            if self.current_player == 'human':
                move = self.get_human_move()
            else:
                _, move = self.minmax(self.game_state, float('-inf'), float('inf'), maximizing=(self.current_player == 'computer'))
            print(f"Chosen move by {self.current_player}: {move}")

            if move is None:
                print("Error: No valid moves found, ending game.")
                break
            
            self.game_state = self.game_state.apply_move(move)
            self.current_player = 'computer' if self.current_player == 'human' else 'human'
        
        self.print_game_state()
        self.print_winner()

    def minmax(self, state, alpha, beta, maximizing):
        if state.is_terminal():
            return state.evaluate(self.current_player), None

        best_move = None

        if maximizing:
            max_eval = float('-inf')
            for move in state.get_possible_moves():
                new_state = state.apply_move(move)
                eval_score, _ = self.minmax(new_state, alpha, beta, False)
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in state.get_possible_moves():
                new_state = state.apply_move(move)
                eval_score, _ = self.minmax(new_state, alpha, beta, True)
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval, best_move


    def get_human_move(self):
        """Prompt human Player for a move"""
        valid_moves = self.game_state.get_possible_moves()
        print("Choose a pile and count from the following options: ")
        for i, move in enumerate(valid_moves):
            print(f"{i+1}. {move[0]} {move[1]}")
        choice = int(input("Enter the number of your choice: ")) - 1
        return valid_moves[choice]

    def print_game_state(self):
        '''DISPLAYING THE CURRENT GAME STATE'''
        print(f"Current game state: Red Pile = {self.game_state.red_pile}, Blue Pile = {self.game_state.blue_pile}")

    def print_winner(self):
        # Calculate remaining marbles as the score difference
        remaining_red = self.game_state.red_pile
        remaining_blue = self.game_state.blue_pile
        total_score = remaining_red * 2 + remaining_blue * 3  # Assuming red marbles are worth 2 points and blue 3 points

        if self.game_state.version == 'standard':
            winner = 'human' if self.current_player == 'computer' else 'computer'
        elif self.game_state.version == 'misere':
            winner = 'computer' if self.current_player == 'human' else 'human'
        
        print(f"Game Over! {winner.capitalize()} wins!")
        print(f"Winning score difference: {total_score}")




def main():
    '''MAIN FUNCTION TO RUN THE GAME'''
    parser = argparse.ArgumentParser(description="Play the Red-Blue Nim game.")
    parser.add_argument("red_pile", type=int, help="Initial number of red marbles")
    parser.add_argument("blue_pile", type=int, help="Initial number of blue marbles")
    parser.add_argument("version", choices=['standard', 'misere'], help="Game version: 'standard' or 'misere'")
    parser.add_argument("first_player", nargs='?', choices=['human', 'computer'], default='human', 
                        help="First player: 'human' or 'computer' (default: 'human')")

    args = parser.parse_args()

    # Initialize and start the game
    game = RedBlueNim(args.red_pile, args.blue_pile, args.version, args.first_player)
    game.play_game()


if __name__ == "__main__":
    main()

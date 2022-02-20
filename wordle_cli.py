from game_manager import GameState, GameStatus, LetterStatus
import signal
import sys

def handle_ctrl_c(sig, frame):
    print("\nGoodbye!")
    sys.exit(0)

def print_words(game):
    for i, word in enumerate(game.attempts):
        letters_status = game.letters_status[i]
        colored_word = ""
        for letter, status in zip(word, letters_status):
            if status == LetterStatus.ABSENT:
                colored_word += letter
            elif status == LetterStatus.RIGHT_POS:
                colored_word += '\x1b[6;30;42m' + letter + '\x1b[0m'
            else:
                colored_word += '\x1b[6;30;43m' + letter + '\x1b[0m'
        print(colored_word)
            

def print_game_state(game):        
    print_words(game)
    if game.current_status() == GameStatus.OVER_USER_WON:
        print("You won!")
    elif game.current_status() == GameStatus.OVER_MAX_ATTEMPTS:
        print("Sorry, answer was: " + game.answer)
    elif game.current_status() == GameStatus.IN_PROGRESS:
        print("Attempts left: {0}".format(game.attempts_left()))

def run_game():
    game = GameState()
    print("New Game Started!")
    while not game.is_over():
        print_game_state(game)
        attempt = input("Enter a 5-letter word or Ctrl-C to exit: ")
        if not game.accept_input(attempt):
            print("Invalid word!")
    print_game_state(game)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_ctrl_c)
    run_game()
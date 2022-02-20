import enum
from vocab import get_random_answer, is_valid_word

class LetterStatus(enum.Enum):
    ABSENT = 1
    RIGHT_POS = 2
    WRONG_POS = 3

class GameStatus(enum.Enum):
    INIT = 1
    IN_PROGRESS = 2
    OVER_MAX_ATTEMPTS = 3
    OVER_USER_WON = 4
    
def get_letters_status(word, answer):
    ret = []
    for i, letter in enumerate(word):
        if letter == answer[i]:
            ret.append(LetterStatus.RIGHT_POS)
        elif letter in answer:
            ret.append(LetterStatus.WRONG_POS)
        else:
            ret.append(LetterStatus.ABSENT)
    return ret

class GameState():
    def __init__(self, max_attempts = 5):
        self.answer = get_random_answer()
        self.attempts = []
        self.max_attempts = max_attempts
        self.letters_status = []

    def attempts_left(self):
        return self.max_attempts - len(self.attempts)

    def current_status(self):
        if len(self.attempts) > 0 and self.attempts[-1] == self.answer:
            return GameStatus.OVER_USER_WON
        if len(self.attempts) == self.max_attempts:
            return GameStatus.OVER_USER_WON
        if len(self.attempts) == 0:
            return GameStatus.INIT
        return GameStatus.IN_PROGRESS

    def is_over(self):
        return self.current_status() in {GameStatus.OVER_MAX_ATTEMPTS, GameStatus.OVER_USER_WON}

    def accept_input(self, word):
        word = word.upper()
        if not is_valid_word(word):
            return False
        if self.is_over():
            raise Exception("Game over! Can't accept any more attempts!")
        self.attempts.append(word)
        self.letters_status.append(get_letters_status(word, self.answer))
        return True


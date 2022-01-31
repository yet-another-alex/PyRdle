import random

# Constants
MIN_WIDTH = 2
MIN_HEIGHT = 1
FONT_SIZE = 64
C_GREY = '#2a2a2c'
C_YELLOW = '#ad952b'
C_GREEN = '#44813f'

# classes
class PyrdleGame:
    def __init__(self, wordlist):
        # WORDS
        self.words = []
        # "pointer" to current char
        self.current_box = None
        self.current_idx = 1
        self.current_guess = 1
        # current word
        self.current_word = ''
        self.current_try = ''
        # game solved?
        self.solved = False
        self.load_wordlist(wordlist)

    def load_wordlist(self, wordlist):
        with open(wordlist, 'r') as wordfile:
            words = wordfile.readlines()

        self.words = [w.strip() for w in words]

    def is_valid(self):
        if len(self.current_try) != 5:
            return False
        else:
            return self.current_try.lower() in self.words

    def pick_word(self):
        self.current_word = random.choice(self.words).upper()

    def reset(self):
        self.current_box = None
        self.current_idx = 1
        self.current_guess = 1
        self.current_word = ''
        self.current_try = ''
        self.solved = False
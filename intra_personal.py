# intra_personal.py: Personality generator file that is responsible for the inner workings -->
# of a potential characters mind as a result of user input combined with world input

from lib import fill_random_sub_values

# Generates the inital birth statistics of a character with optional user override on specific traits
def initialize_character(name):
    fill_random_sub_values(name)

# intra_personal.py: Personality generator file that is responsible for the inner workings -->
# of a potential characters mind as a result of user input combined with world input

from lib import fill_random_sub_values

# Generates the inital birth statistics of a character with optional user override on specific traits
def generate_birth_statistics(trait_levels=[]):
    fill_random_sub_values()
    #bwg = get_truncated_normal(mean=3.25, sd=1, low=2.5, upp=4)
    #weight = bwg.rvs()
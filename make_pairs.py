"""
Script to make pairs. Requirements:
- Excluded pairs: never match this student with anyone in this list
- Tech levels: prefer to pair students who are within 3 levels
- Historical pairs: prefer to pair students who have not worked together
- Temperament: Assertive, Passive, Chill
    Avoid:
        Assertive + Passive
    Acceptable:
        Assertive + Assertive
        Passive + Passive
        Chill + Chill
        Assertive + Chill
        Passive + Chill

Data structure: 

student_pairs = {
   student_name: {
        tech_level: int,
        temperament: string,
        excluded: set(student_name),
        past_pairs: list[student_name]
   },
   ...
}

In: file with pairs dictionary
Print: proposed pairs for today, star any repeats
    Ask for user approval for proposed pairs
    If yes, update pairs dictionary file with these new pairs (append to past_pairs)
    If no, rerun and get new pairs
        > Later: allow to fix specific pairs and reroll other pairs
Out: list of student pairs for today
        > Way Later: send students a slack message with their pair for today

"""
FILE = 't1_pairs_dict.py'

from t1_pairs_dict import STUDENT_PAIRS
from pprint import pprint
import random
# import itertools
import json

def generate_pairs():
    """Match students based on exclusion list and tech level"""

    students = set(STUDENT_PAIRS.keys())
    pairs = {}

    while students:
        
        student = students.pop()

        # The last unpaired student could be an excluded match, so this could fail
        try:
            match = (students - STUDENT_PAIRS[student]['excluded']).pop()

            while match in STUDENT_PAIRS[student]['past_pairs']:
            # try:
                allowed_students = (students - STUDENT_PAIRS[student]['excluded']).pop()
                match = allowed_students.pop()
                print(f'Trying student={student} with match={match}')
                # except:
                #     print(f'Failed: students={students} student={student} match={match}')
                #     return

            # Is the difference in levels within 3?
            if not abs(STUDENT_PAIRS[match]['tech_level'] - STUDENT_PAIRS[student]['tech_level']) <= 3:
                print(f"{student} tech level={STUDENT_PAIRS[student]['tech_level']} with {match} tech level={STUDENT_PAIRS[match]['tech_level']}")
                should_proceed = input('Okay to proceed? [Y]ES / [N]O: ')

                if should_proceed.lower() in ['no', 'n']:
                    # TODO break out matching as a function so it can be
                    # called until (1) no tech level issue, (2) user approves 
                    # match, or (3) run out of match options
                    print('Quitting: try again')
                    return
                else: 
                    while should_proceed.lower() not in ['yes', 'y']:
                        should_proceed = input('Invalid key! [Y]ES / [N]O: ')
            
            # Set math creates a new set, so remove match from original pool
            students.remove(match)
        except:
            print(f'Failed: students={students} student={student} match={match}')
            return

        pairs[student] = match

    pprint(pairs)
    should_write = input('Write to file? [Y]ES / [N]O: ')
    if should_write.lower() in ['yes', 'y']:
        update_global_var(pairs)
    else:
        while should_write.lower() not in ['no', 'n']:
            should_write = input('Invalid key! [Y]ES / [N]O: ')

    return pairs


def update_global_var(pairs):
    """Save generated pairs to global variable file"""

    with open(FILE, 'r') as f:
        x = json.load(f)
        for something in x:
            print(something)
        # for student in pairs:
        #     pair = pairs[student]
        #     STUDENT_PAIRS[student]['past_pairs'].append(pair)
        #     STUDENT_PAIRS[pair]['past_pairs'].append(student)
        #     print(f"Updated student={student}['past_pairs']: {STUDENT_PAIRS[student]['past_pairs']}")
        #     print(f"Updated pair={pair}['past_pairs']: {STUDENT_PAIRS[pair]['past_pairs']}")


pairs = generate_pairs()



# # All permutations
# def create_options():
#     """ """
#     pair_permutations = itertools.permutations(STUDENT_PAIRS.keys(), 2)





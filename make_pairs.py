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

from t1_pairs_dict import STUDENT_PAIRS
from pprint import pprint
import random
import itertools

# Get random pairs, ignoring all factors
def generate_pairs():
    """Brute force, match students randomly"""
    students = set(STUDENT_PAIRS.keys())
    pairs = {}

    while students:
        
        student = students.pop()

        # The last unpaired student could be an excluded match, so this could fail
        try:
            match = (students - STUDENT_PAIRS[student]['excluded']).pop()

            # Is the difference in levels within 3?
            if not abs(STUDENT_PAIRS[match]['tech_level'] - STUDENT_PAIRS[student]['tech_level']) <= 3:
                print(f"{student} tech level={STUDENT_PAIRS[student]['tech_level']} with {match} tech level={STUDENT_PAIRS[match]['tech_level']}")
                proceed = input('Okay to proceed? YES / NO: ')

                if proceed.lower() in ['yes', 'y']:
                    # Set math creates a new set, so remove match from original pool
                    students.remove(match)
                elif proceed.lower() in ['no', 'n']:
                    print('Quitting: try again')
                    return

            else:
                students.remove(match)
        except:
            print(f'Failed: students={students} student={student} match={match}')

        pairs[student] = match

    pprint(pairs)
    return pairs

generate_pairs()


# # All permutations
# def create_options():
#     """ """
#     pair_permutations = itertools.permutations(STUDENT_PAIRS.keys(), 2)





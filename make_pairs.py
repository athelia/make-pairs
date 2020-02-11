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
import random
import itertools

# Get random pairs, ignoring all factors
def generate_pairs():
    """Brute force, match students randomly"""
    students = set(STUDENT_PAIRS.keys())
    print(students)
    pairs = {}

    while students:
        import pdb; pdb.set_trace()
        student1 = students.pop()
        student2 = students.pop()
        pairs[student1] = student2
        pairs[student2] = student1

    return pairs

generate_pairs()
# Set math


# # All permutations
# def create_options():
#     """ """
#     pair_permutations = itertools.permutations(STUDENT_PAIRS.keys(), 2)





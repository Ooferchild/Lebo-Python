import random
import numpy as np

period = "\n|Pd |\t\tClass\t\t| Room |\tTeacher |"
teacher = ('Lebo')
_class = ('Math','Social','Science','Russian','Lunch','English','Weights','Python')



base = f"\n| {period} |\t\t{random.choice(_class)}\t\t| {room} |\t{teacher} |"

def room():
    num = random.randrange(100,540)

def p(room):
    print("\t\t\t\tProgram Card\n_____________________________________________\n|Pd |\t\tClass\t\t| Room | Teacher |" , base,  end="|\n")

if __name__ == "__main__":
    p(room)
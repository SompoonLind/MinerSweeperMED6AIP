import random, numpy

eight_tile = [2, 1, 3, 0, 8, 4, 6, 7, 5]

def genetic_algorhitm():
    initial_state = eight_tile
    return initial_state


def main():
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    if genetic_algorhitm() == goal_state:
        print("True")
    else:
        print("False")



if __name__ == '__main__':
    main()

import random
from AStar import A_star_search

initial_state = [2, 1, 3, 0, 8, 4, 6, 7, 5]

def genetic_algo():
    return initial_state


def main():
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    if genetic_algo() == goal_state:
        print("True")
    else:
        print("False")



if __name__ == '__main__':
    A_star_search(initial_state)
    main()

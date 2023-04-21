def count_matching_elements(arr1, arr2):
    num_matches = 0
    for i, j in zip(arr1, arr2):
        if i == j:
            num_matches += 1
    return num_matches

def main():
    Initial_state = [1, 2, 3, 4, 5]
    goal_state = [3, 2, 1, 4, 6]
    num_matches = count_matching_elements(Initial_state, goal_state)
    print(f"The number of matching elements is: {num_matches}")

if __name__ == '__main__':
    main()
# Using backtracking to resolve n-queues problem
import numpy as np

max_columns = 8
max_rows = max_columns

def print_chess(problem):
    head = "_" * (len(problem) + 2)
    tail = "-" * (len(problem) + 2)

    print(head)
    for row in problem:
        row_str = "|"
        for item in row:
            row_str += str(item)
        row_str += "|"
        print(row_str)
    print(tail + "\n")


def remove_diagonal(problem, occupied_coordinate, max_cols, candidates):
    row, col = occupied_coordinate
    step = max_cols - col - 1
    # remove right-down
    if (row + step) < len(problem) and (row + step) in candidates:
        candidates.remove(row + step)
    # remove right-up
    if (row - step) >= 0 and (row - step) in candidates:
        candidates.remove(row - step)


def construct_candidates(problem, k) -> int:
    if k <= 0:  # for first column
        return [0]  # return 'first row' if it is a 1x1 chess
    else:
        # find empty rows
        candidates = set(range(len(problem)))
        for col in range(k):
            for row in range(max_rows):
                if problem[row][col] > 0:
                    # remove queens in the same row or same column
                    if row in candidates:
                        candidates.remove(row)
                    # remove queens in the same diagonal
                    remove_diagonal(problem, (row, col), k, candidates)
        return list(candidates)


# check all rows to make sure they all have queues ('1')
def is_solution(problem, k):
    result = True
    for index in range(min(k, len(problem))):
        if sum(problem[index]) <= 0:
            result = False
    return result


def construct_solution(problem, candidate, k):
    new_problem = problem.copy()
    new_problem[candidate][k - 1] = 1
    return new_problem


def solve(problem, k):
    if is_solution(problem, k):
        print_chess(problem)
        return 1
    else:
        count = 0
        candidates = construct_candidates(problem, k)
        for candidate in candidates:
            new_problem = construct_solution(problem, candidate, k)
            count += solve(new_problem, k + 1)
        return count


if __name__ == "__main__":
    # try to resolve a max_rows x max_columns chess matrix
    initial_problem = np.zeros((max_rows, max_columns), dtype=int)
    count = solve(initial_problem, 1)
    print("Number of solutions: ", count)

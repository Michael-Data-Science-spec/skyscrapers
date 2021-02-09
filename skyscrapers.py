"""
Lab0 Task1 Mykhailo Kuzmyn
"""

import doctest

def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("skyscrapers1.txt")
    ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    with open(path, 'r') as f:
        game_lst = f.readlines()
    for idx, line in enumerate(game_lst):
        game_lst[idx] = line.strip('\n')
    return game_lst


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    visible_buildings = [int(input_line[1])]

    for idx in range(1, len(input_line) - 1):

        if int(input_line[idx]) > visible_buildings[-1]:
            visible_buildings.append(int(input_line[idx]))
    
    if len(visible_buildings) != pivot:
        return False

    return True


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board:

        if '?' in line:
            return False
    
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board[1: -1]:
        building_lst = [int(x) for x in line[1: -1]]
        building_set = {int(x) for x in line[1: -1]}

        if sorted(building_lst) != list(building_set):
            return False
    
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board[1: -1]:

        if line[0] != '*':
            if not left_to_right_check(line, int(line[0])):
                return False

        if line[-1] != '*':
            if not left_to_right_check(line[::-1], int(line[-1])):
                return False

    return True
doctest.testmod()

def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    transformed_board = []
    l = len(board)

    for idx1 in range(l):
        line = []

        for idx2 in range(l):
            line.append(board[idx2][idx1])

        line = ''.join(line)
        transformed_board.append(line)
    
    if not check_horizontal_visibility(transformed_board):
        return False

    return True


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("skyscrapers1.txt")
    True
    """
    board = read_input(input_path)

    if (check_not_finished_board(board) == 0
       or check_uniqueness_in_rows(board) == 0
       or check_horizontal_visibility(board) == 0
       or check_columns(board) == 0):
       return False

    return True

doctest.testmod()

# if __name__ == "__main__":
#     print(check_skyscrapers("check.txt"))

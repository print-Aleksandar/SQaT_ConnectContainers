import pytest
from game.services import filter_valid_moves, drop_disc, is_draw


PLAYER1 = "1"
PLAYER2 = "2"


def test_drop_on_empty_board():
    """
    Disc should fall at bottom of the board, on selected column.

    7 columns:
        * board[-1] = row: 5, column: 6
        * board[-2] = row: 5, column: 5
        * board[-3] = row: 5, column: 4
        * board[-4] = row: 5, column: 3
        ...
    """

    board = "0" * 42

    new_board, _ = drop_disc(board=board, player=PLAYER1, column=3)

    assert new_board[-4] == PLAYER1


def test_two_drops_on_same_column():
    """
    Second disc should fall one row above first one, in same column.
    """

    board = "0" * 42

    new_board, _ = drop_disc(board=board, player=PLAYER1, column=2)
    new_board2, _ = drop_disc(board=new_board, player=PLAYER2, column=2)

    accessor1 = -5
    accessor2 = -5 - 7

    assert new_board2[accessor1] == PLAYER1 and new_board2[accessor2] == PLAYER2


def test_drop_when_column_is_filled():
    """
    Should not allow dropping when column is filled.
    """

    board = "0" * 42
    column = 4

    for row in range(6):
        pos = row * 7 + column
        board = board[:pos] + (PLAYER2 if row % 2 == 0 else PLAYER1) + board[pos + 1:]

    with pytest.raises(RuntimeError, match=r"Column is entirely filled."):
        drop_disc(board=board, player=PLAYER1, column=column)


def test_exception_when_should_not_happen():
    """
    Only one spot left in column, exception should not be raised.
    """

    board = "0" * 42
    column = 4

    for row in range(1, 6, +1):
        pos = row * 7 + column
        board = board[:pos] + (PLAYER2 if row % 2 == 0 else PLAYER1) + board[pos + 1:]

    drop_disc(board=board, player=PLAYER2, column=column)


def test_full_placement():
    """
    Drops will be tested, goal is to fill entire board
    with valid moves (draw scenario).

    Scenario:
    1212121
    1212121
    1212121
    2121212
    2121212
    2121212
    """

    scenario = "121212112121211212121212121221212122121212"
    board = "0" * 42

    for x in range(41, -1, -1):
        column = x % 7
        if x > 20:
            board, _ = drop_disc(board=board, player=PLAYER2 if column % 2 == 0 else PLAYER1, column=column)
        else:
            board, _ = drop_disc(board=board, player=PLAYER1 if column % 2 == 0 else PLAYER2, column=column)

    assert scenario == board


def test_draw_scenario():
    """
    Board given to draw checker will be finished game where draw happened.

    Scenario:
    1212121
    1212121
    1212121
    2121212
    2121212
    2121212
    """

    scenario = "121212112121211212121212121221212122121212"
    assert is_draw(scenario) == True


def test_draw_scenario_when_is_not():
    """
    Board given to draw checker will be unfinished game where currently is not draw.

    Scenario:
    0212121
    1212121
    1212121
    2121212
    2121212
    2121212
    """

    scenario = "021212112121211212121212121221212122121212"
    assert is_draw(scenario) == False


def test_filter_of_valid_moves():
    """
    Board given to the filter will be unfinished game with
    unfilled columns: 0, 2 and 3.

    Scenario:
    0200121
    0210121
    0210121
    0121212
    2121212
    2121212
    """

    scenario = "020012102101210210121012121221212122121212"
    assert filter_valid_moves(scenario) == [0, 2, 3]

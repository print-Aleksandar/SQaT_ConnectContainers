import pytest
from game.services import drop_disc
from game.win_checker import (VerticalCheck,
                              HorizontalCheck,
                              MainDiagonalCheck,
                              AntiDiagonalCheck, WinCheckerRegistry)


PLAYER1 = "1"
PLAYER2 = "2"


"""
With following order of drops in each test scenario correctness of that test can be checked.
"""


def test_vertical_check():
    board = "0" * 42
    for i in range(6):
        column = 2 if i % 2 == 0 else 4
        player = PLAYER1 if i % 2 == 0 else PLAYER2
        board, _ = drop_disc(board=board, column=column, player=player)
    board, new_disc_pos = drop_disc(board=board, column=2, player=PLAYER1)
    row, col = divmod(new_disc_pos, 7)
    checker = VerticalCheck(row=row, col=col, pos=0)
    if not checker.supports():
        raise RuntimeError("Should not happen.")
    checker.set_accesser()
    checked_sequence = [board[pos] for pos in checker.accesser]
    checked_sequence = "".join(checked_sequence)
    assert checked_sequence == PLAYER1 * 4


@pytest.mark.parametrize("pos", range(4))
def test_horizontal_check(pos: int):
    board = "0" * 42
    for column in [x for x in range(5) if pos != x]:
        board, _ = drop_disc(board=board, column=column, player=PLAYER1)
        board, _ = drop_disc(board=board, column=column, player=PLAYER2)
    board, new_disc_pos = drop_disc(board=board, column=pos, player=PLAYER1)
    row, col = divmod(new_disc_pos, 7)
    checker = HorizontalCheck(row=row, col=col, pos=pos)
    if not checker.supports():
        raise RuntimeError("Should not happen.")
    checker.set_accesser()
    checked_sequence = [board[pos] for pos in checker.accesser]
    checked_sequence = "".join(checked_sequence)
    assert checked_sequence == PLAYER1 * 4


def test_anti_diagonal_check_pos0():
    board = "0" * 42
    board, _ = drop_disc(board=board, column=6, player=PLAYER1)
    board, _ = drop_disc(board=board, column=1, player=PLAYER2)
    board, _ = drop_disc(board=board, column=2, player=PLAYER1)
    board, _ = drop_disc(board=board, column=3, player=PLAYER2)

    board, _ = drop_disc(board=board, column=1, player=PLAYER1)
    board, _ = drop_disc(board=board, column=2, player=PLAYER2)
    board, _ = drop_disc(board=board, column=3, player=PLAYER1)

    board, _ = drop_disc(board=board, column=3, player=PLAYER2)
    board, _ = drop_disc(board=board, column=2, player=PLAYER1)

    board, _ = drop_disc(board=board, column=6, player=PLAYER2)

    board, _ = drop_disc(board=board, column=3, player=PLAYER1)

    board, _ = drop_disc(board=board, column=6, player=PLAYER2)

    board, new_disc_pos = drop_disc(board=board, column=0, player=PLAYER1)

    row, col = divmod(new_disc_pos, 7)
    checker = AntiDiagonalCheck(row=row, col=col, pos=0)
    if not checker.supports():
        raise RuntimeError("Should not happen.")
    checker.set_accesser()
    checked_sequence = [board[pos] for pos in checker.accesser]
    checked_sequence = "".join(checked_sequence)
    assert checked_sequence == PLAYER1 * 4


def test_anti_diagonal_check_pos1():
    board = "0" * 42
    board, _ = drop_disc(board=board, column=0, player=PLAYER1)
    board, _ = drop_disc(board=board, column=1, player=PLAYER2)
    board, _ = drop_disc(board=board, column=2, player=PLAYER1)
    board, _ = drop_disc(board=board, column=3, player=PLAYER2)

    board, _ = drop_disc(board=board, column=3, player=PLAYER2)
    board, _ = drop_disc(board=board, column=2, player=PLAYER1)

    board, _ = drop_disc(board=board, column=3, player=PLAYER2)
    board, _ = drop_disc(board=board, column=2, player=PLAYER1)

    board, _ = drop_disc(board=board, column=2, player=PLAYER2)
    board, _ = drop_disc(board=board, column=3, player=PLAYER1)

    board, _ = drop_disc(board=board, column=2, player=PLAYER2)

    board, new_disc_pos = drop_disc(board=board, column=1, player=PLAYER1)

    row, col = divmod(new_disc_pos, 7)
    checker = AntiDiagonalCheck(row=row, col=col, pos=1)
    if not checker.supports():
        raise RuntimeError("Should not happen.")
    checker.set_accesser()
    print(checker.accesser)
    checked_sequence = [board[pos] for pos in checker.accesser]
    checked_sequence = "".join(checked_sequence)
    assert checked_sequence == PLAYER1 * 4


def test_anti_diagonal_check_pos2():
    board = "0" * 42
    board, _ = drop_disc(board=board, column=0, player=PLAYER1)
    board, _ = drop_disc(board=board, column=1, player=PLAYER2)
    board, _ = drop_disc(board=board, column=2, player=PLAYER1)
    board, _ = drop_disc(board=board, column=3, player=PLAYER2)

    board, _ = drop_disc(board=board, column=1, player=PLAYER1)
    board, _ = drop_disc(board=board, column=2, player=PLAYER2)
    board, _ = drop_disc(board=board, column=3, player=PLAYER1)

    board, _ = drop_disc(board=board, column=3, player=PLAYER2)

    board, _ = drop_disc(board=board, column=3, player=PLAYER1)

    board, _ = drop_disc(board=board, column=6, player=PLAYER2)

    board, new_disc_pos = drop_disc(board=board, column=2, player=PLAYER1)

    row, col = divmod(new_disc_pos, 7)
    checker = AntiDiagonalCheck(row=row, col=col, pos=2)
    if not checker.supports():
        raise RuntimeError("Should not happen.")
    checker.set_accesser()
    checked_sequence = [board[pos] for pos in checker.accesser]
    checked_sequence = "".join(checked_sequence)
    assert checked_sequence == PLAYER1 * 4


def test_anti_diagonal_check_pos3():
    board = "0" * 42
    board, _ = drop_disc(board=board, column=0, player=PLAYER1)
    board, _ = drop_disc(board=board, column=1, player=PLAYER2)
    board, _ = drop_disc(board=board, column=2, player=PLAYER1)
    board, _ = drop_disc(board=board, column=3, player=PLAYER2)

    board, _ = drop_disc(board=board, column=1, player=PLAYER1)
    board, _ = drop_disc(board=board, column=2, player=PLAYER2)
    board, _ = drop_disc(board=board, column=3, player=PLAYER1)

    board, _ = drop_disc(board=board, column=3, player=PLAYER2)
    board, _ = drop_disc(board=board, column=2, player=PLAYER1)

    board, _ = drop_disc(board=board, column=6, player=PLAYER2)

    board, new_disc_pos = drop_disc(board=board, column=3, player=PLAYER1)

    row, col = divmod(new_disc_pos, 7)
    checker = AntiDiagonalCheck(row=row, col=col, pos=3)
    if not checker.supports():
        raise RuntimeError("Should not happen.")
    checker.set_accesser()
    checked_sequence = [board[pos] for pos in checker.accesser]
    checked_sequence = "".join(checked_sequence)
    assert checked_sequence == PLAYER1 * 4

def test_main_diagonal_check_pos0():
    board = "0" * 42
    board, _ = drop_disc(board=board, column=0, player=PLAYER1)
    board, _ = drop_disc(board=board, column=1, player=PLAYER2)

    board, _ = drop_disc(board=board, column=0, player=PLAYER1)
    board, _ = drop_disc(board=board, column=1, player=PLAYER2)

    board, _ = drop_disc(board=board, column=3, player=PLAYER1)

    board, _ = drop_disc(board=board, column=2, player=PLAYER2)
    board, _ = drop_disc(board=board, column=2, player=PLAYER1)

    board, _ = drop_disc(board=board, column=0, player=PLAYER2)

    board, _ = drop_disc(board=board, column=1, player=PLAYER1)

    board, _ = drop_disc(board=board, column=6, player=PLAYER2)

    board, new_disc_pos = drop_disc(board=board, column=0, player=PLAYER1)

    row, col = divmod(new_disc_pos, 7)
    checker = MainDiagonalCheck(row=row, col=col, pos=0)
    if not checker.supports():
        raise RuntimeError("Should not happen.")
    checker.set_accesser()
    checked_sequence = [board[pos] for pos in checker.accesser]
    checked_sequence = "".join(checked_sequence)
    assert checked_sequence == PLAYER1 * 4


def test_main_diagonal_check_pos1():
    board = "0" * 42
    board, _ = drop_disc(board=board, column=0, player=PLAYER1)
    board, _ = drop_disc(board=board, column=1, player=PLAYER2)

    board, _ = drop_disc(board=board, column=0, player=PLAYER1)
    board, _ = drop_disc(board=board, column=1, player=PLAYER2)

    board, _ = drop_disc(board=board, column=3, player=PLAYER1)

    board, _ = drop_disc(board=board, column=2, player=PLAYER2)
    board, _ = drop_disc(board=board, column=2, player=PLAYER1)

    board, _ = drop_disc(board=board, column=0, player=PLAYER2)
    board, _ = drop_disc(board=board, column=0, player=PLAYER1)

    board, _ = drop_disc(board=board, column=6, player=PLAYER2)
    board, new_disc_pos = drop_disc(board=board, column=1, player=PLAYER1)

    row, col = divmod(new_disc_pos, 7)
    checker = MainDiagonalCheck(row=row, col=col, pos=1)
    if not checker.supports():
        raise RuntimeError("Should not happen.")
    checker.set_accesser()
    checked_sequence = [board[pos] for pos in checker.accesser]
    checked_sequence = "".join(checked_sequence)
    assert checked_sequence == PLAYER1 * 4


def test_main_diagonal_check_pos2():
    board = "0" * 42
    board, _ = drop_disc(board=board, column=0, player=PLAYER1)
    board, _ = drop_disc(board=board, column=1, player=PLAYER2)

    board, _ = drop_disc(board=board, column=0, player=PLAYER1)
    board, _ = drop_disc(board=board, column=1, player=PLAYER2)

    board, _ = drop_disc(board=board, column=3, player=PLAYER1)

    board, _ = drop_disc(board=board, column=2, player=PLAYER2)

    board, _ = drop_disc(board=board, column=1, player=PLAYER1)
    board, _ = drop_disc(board=board, column=0, player=PLAYER2)

    board, _ = drop_disc(board=board, column=0, player=PLAYER1)

    board, _ = drop_disc(board=board, column=6, player=PLAYER2)

    board, new_disc_pos = drop_disc(board=board, column=2, player=PLAYER1)

    row, col = divmod(new_disc_pos, 7)
    checker = MainDiagonalCheck(row=row, col=col, pos=2)
    if not checker.supports():
        raise RuntimeError("Should not happen.")
    checker.set_accesser()
    checked_sequence = [board[pos] for pos in checker.accesser]
    checked_sequence = "".join(checked_sequence)
    assert checked_sequence == PLAYER1 * 4


def test_main_diagonal_check_pos2():
    board = "0" * 42
    board, _ = drop_disc(board=board, column=0, player=PLAYER1)
    board, _ = drop_disc(board=board, column=1, player=PLAYER2)

    board, _ = drop_disc(board=board, column=0, player=PLAYER1)
    board, _ = drop_disc(board=board, column=1, player=PLAYER2)

    board, _ = drop_disc(board=board, column=1, player=PLAYER1)
    board, _ = drop_disc(board=board, column=0, player=PLAYER2)

    board, _ = drop_disc(board=board, column=0, player=PLAYER1)

    board, _ = drop_disc(board=board, column=2, player=PLAYER2)

    board, _ = drop_disc(board=board, column=2, player=PLAYER1)
    board, _ = drop_disc(board=board, column=6, player=PLAYER2)

    board, new_disc_pos = drop_disc(board=board, column=3, player=PLAYER1)

    row, col = divmod(new_disc_pos, 7)
    checker = MainDiagonalCheck(row=row, col=col, pos=3)
    if not checker.supports():
        raise RuntimeError("Should not happen.")
    checker.set_accesser()
    checked_sequence = [board[pos] for pos in checker.accesser]
    checked_sequence = "".join(checked_sequence)
    assert checked_sequence == PLAYER1 * 4


def test_registry_with_more_drops():
    board = "0" * 42
    board, _ = drop_disc(board=board, column=3, player=PLAYER1)
    board, _ = drop_disc(board=board, column=3, player=PLAYER2)
    board, _ = drop_disc(board=board, column=3, player=PLAYER1)

    board, _ = drop_disc(board=board, column=4, player=PLAYER2)
    board, _ = drop_disc(board=board, column=4, player=PLAYER1)
    board, _ = drop_disc(board=board, column=4, player=PLAYER2)
    board, _ = drop_disc(board=board, column=4, player=PLAYER1)

    board, _ = drop_disc(board=board, column=5, player=PLAYER2)
    board, _ = drop_disc(board=board, column=5, player=PLAYER1)
    board, _ = drop_disc(board=board, column=5, player=PLAYER2)

    board, _ = drop_disc(board=board, column=6, player=PLAYER1)
    board, _ = drop_disc(board=board, column=6, player=PLAYER2)
    board, _ = drop_disc(board=board, column=6, player=PLAYER1)
    board, _ = drop_disc(board=board, column=6, player=PLAYER2)

    board, _ = drop_disc(board=board, column=2, player=PLAYER1)

    board, _ = drop_disc(board=board, column=5, player=PLAYER2)
    board, _ = drop_disc(board=board, column=5, player=PLAYER1)

    board, new_disc_pos = drop_disc(board=board, column=6, player=PLAYER2)
    is_win = WinCheckerRegistry(board=board, new_disc_pos=new_disc_pos, player=PLAYER2).registry()
    assert is_win == True


def test_registry_with_more_drops_when_is_not_win():
    board = "0" * 42
    board, _ = drop_disc(board=board, column=3, player=PLAYER1)
    board, _ = drop_disc(board=board, column=3, player=PLAYER2)
    board, _ = drop_disc(board=board, column=3, player=PLAYER1)

    board, _ = drop_disc(board=board, column=4, player=PLAYER2)
    board, _ = drop_disc(board=board, column=4, player=PLAYER1)
    board, _ = drop_disc(board=board, column=4, player=PLAYER2)
    board, _ = drop_disc(board=board, column=4, player=PLAYER1)

    board, _ = drop_disc(board=board, column=5, player=PLAYER2)
    board, _ = drop_disc(board=board, column=5, player=PLAYER1)
    board, _ = drop_disc(board=board, column=5, player=PLAYER2)

    board, _ = drop_disc(board=board, column=6, player=PLAYER1)
    board, _ = drop_disc(board=board, column=6, player=PLAYER2)
    board, _ = drop_disc(board=board, column=6, player=PLAYER1)
    board, _ = drop_disc(board=board, column=6, player=PLAYER2)

    board, _ = drop_disc(board=board, column=2, player=PLAYER1)

    board, _ = drop_disc(board=board, column=5, player=PLAYER2)
    board, _ = drop_disc(board=board, column=5, player=PLAYER1)

    board, new_disc_pos = drop_disc(board=board, column=2, player=PLAYER2)
    is_win = WinCheckerRegistry(board=board, new_disc_pos=new_disc_pos, player=PLAYER2).registry()
    assert is_win == False


def test_registry_with_more_drops_after_every_drop():
    board = "0" * 42
    moves = [
        (3, PLAYER1), (3, PLAYER2), (3, PLAYER1),
        (4, PLAYER2), (4, PLAYER1), (4, PLAYER2), (4, PLAYER1),
        (5, PLAYER2), (5, PLAYER1), (5, PLAYER2),
        (6, PLAYER1), (6, PLAYER2), (6, PLAYER1), (6, PLAYER2),
        (2, PLAYER1),
        (5, PLAYER2), (5, PLAYER1)
    ]

    for column, player in moves:
        board, new_disc_pos = drop_disc(board=board, column=column, player=player)
        is_win = WinCheckerRegistry(board=board, new_disc_pos=new_disc_pos, player=player).registry()
        assert is_win is False

    board, new_disc_pos = drop_disc(board=board, column=6, player=PLAYER2)
    is_win = WinCheckerRegistry(board=board, new_disc_pos=new_disc_pos, player=PLAYER2).registry()
    assert is_win is True

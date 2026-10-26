def drop_disc(board: str,
              column: int,
              player: str) -> tuple[str, int]:

    if len(board) != 42:
        raise RuntimeError("Invalid board format.")

    if 0 > column > 6:
        raise RuntimeError("Column out of range.")

    counts = dict()
    counts["1"] = 0
    counts["2"] = 0
    for val in board:
        if val in ("1", "2"):
            counts[val] += 1

    if counts["1"] + counts["2"] == 42:
        raise RuntimeError("Board is not valid")

    if player == "1":
        if counts["1"] != counts["2"]:
            raise RuntimeError("Board is not valid")
    else:
        if counts["1"] - counts["2"] != 1:
            raise RuntimeError("Board is not valid")

    for row in range(5, -1, -1):
        disc_pos = row * 7 + column
        if board[disc_pos] == "0":
            board = board[:disc_pos] + player + board[disc_pos + 1:]
            break
    else:
        raise RuntimeError("Column is entirely filled.")

    return board, disc_pos


def is_draw(board: str) -> bool:
    return "0" not in board


def filter_valid_moves(board: str) -> list[int]:
    return [idx for idx, val in enumerate(board[:7]) if val == "0"]
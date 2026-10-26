from abc import ABC, abstractmethod


class WinChecker(ABC):
    def __init__(self, row, col, pos):
        self.row = row
        self.col = col
        self.pos = pos

        self.accesser = []

    @abstractmethod
    def supports(self) -> bool:
        pass

    @abstractmethod
    def set_accesser(self) -> None:
        pass


class VerticalCheck(WinChecker):
    def __init__(self, row, col, pos):
        super().__init__(row, col, pos)

    def supports(self) -> bool:
        return self.row <= 2

    def set_accesser(self) -> None:
        self.accesser = [
            self.row * 7 + self.col,
            self.row * 7 + 7 + self.col,
            self.row * 7 + 14 + self.col,
            self.row * 7 + 21 + self.col
        ]


class HorizontalCheck(WinChecker):
    def __init__(self, row, col, pos):
        super().__init__(row, col, pos)

    def supports(self) -> bool:
        return 0 <= self.col - self.pos <= 3

    def set_accesser(self) -> None:
        self.accesser = [
            self.row * 7 + self.col
        ]

        for i_pos in [x for x in range(4) if x != self.pos]:
            d_pos = i_pos - self.pos
            self.accesser.append(self.row * 7 + self.col + d_pos)


class MainDiagonalCheck(WinChecker):
    def __init__(self, row, col, pos):
        super().__init__(row, col, pos)

    def supports(self) -> bool:
        return (0 <= self.col - self.pos <= 3
                and self.row - self.pos >= 0
                and self.row <= 2 + self.pos)

    def set_accesser(self) -> None:
        self.accesser = [
            self.row * 7 + self.col
        ]

        for i_pos in [x for x in range(4) if x != self.pos]:
            d_pos = i_pos - self.pos
            self.accesser.append(self.row * 7 + (d_pos * 7) + self.col + d_pos)


class AntiDiagonalCheck(WinChecker):
    def __init__(self, row, col, pos):
        super().__init__(row, col, pos)

    def supports(self) -> bool:
        return (0 <= self.col - self.pos <= 3
                and self.row + self.pos <= 5
                and self.row >= 3 - self.pos)

    def set_accesser(self) -> None:
        self.accesser = [
            self.row * 7 + self.col
        ]

        for i_pos in [x for x in range(4) if x != self.pos]:
            d_pos = i_pos - self.pos
            self.accesser.append(self.row * 7 - (d_pos * 7) + self.col + d_pos)


class WinCheckerRegistry:
    def __init__(self, board: str,
                 new_disc_pos: int,
                 player: str):

        self.board = board
        self.new_disc_pos = new_disc_pos
        self.player = player

    def registry(self) -> bool:
        row, col = divmod(self.new_disc_pos, 7)

        checkers_configs = [{"cls": VerticalCheck, "configs": (row, col, 0)}]

        for x in range(4):
            checkers_configs.append({"cls": HorizontalCheck, "configs" : (row, col, x)})
            
        for x in range(4):
            checkers_configs.append({"cls": MainDiagonalCheck, "configs" : (row, col, x)})

        for x in range(4):
            checkers_configs.append({"cls": AntiDiagonalCheck, "configs" : (row, col, x)})
            
        for checker_config in checkers_configs:
            cls, configs = checker_config["cls"], checker_config["configs"]
            checker = cls(*configs)
            
            if checker.supports():
                checker.set_accesser()

                checked_sequence = [self.board[pos] for pos in checker.accesser]
                checked_sequence = "".join(checked_sequence)

                if checked_sequence == self.player * 4:
                    return True

        return False

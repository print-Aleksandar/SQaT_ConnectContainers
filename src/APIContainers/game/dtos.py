from pydantic import BaseModel


class DropRequestDTO(BaseModel):
    board: str
    column: int
    player: str


class DropResponseDTO(BaseModel):
    board: str
    is_win: bool
    is_draw: bool


class ExceptionDTO(BaseModel):
    message: str


class GatherValidDropsRequestDTO(BaseModel):
    board: str


class GatherValidDropsResponseDTO(BaseModel):
    valid_drops: list[int]

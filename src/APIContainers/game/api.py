from fastapi import FastAPI
from dtos import (GatherValidDropsRequestDTO,
                  GatherValidDropsResponseDTO,
                  DropRequestDTO, DropResponseDTO,
                  ExceptionDTO)
from services import (filter_valid_moves,
                      drop_disc,
                      is_draw)
from win_checker import WinCheckerRegistry

app = FastAPI()


@app.get("/health_check")
async def health_check():
    return {"status": "ok"}


@app.post("/gather_valid_drops")
async def gather_valid_drops(request: GatherValidDropsRequestDTO) -> GatherValidDropsResponseDTO:
    valid_drops = filter_valid_moves(board=request.board)
    return GatherValidDropsResponseDTO(valid_drops=valid_drops)


@app.post("/play_turn")
async def play_turn(request: DropRequestDTO) -> DropResponseDTO | ExceptionDTO:
    try:
        new_board, new_disc_pos = drop_disc(board=request.board, column=request.column, player=request.player)
        is_win = WinCheckerRegistry(board=new_board, new_disc_pos=new_disc_pos, player=request.player).registry()
        if not is_win:
            is_draw_status = is_draw(board=new_board)
            return DropResponseDTO(board=new_board, is_win=False, is_draw=is_draw_status)
        return DropResponseDTO(board=new_board, is_win=True, is_draw=False)
    except RuntimeError as e:
        return ExceptionDTO(message=str(e))

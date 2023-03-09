import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("/path/to/engine")

board = chess.Board()
while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=2.0))
    board.push(result.move)
    print(board)

engine.quit()

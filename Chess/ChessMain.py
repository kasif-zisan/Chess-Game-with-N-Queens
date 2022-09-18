import pygame as p

from Chess import NQueensBoard

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def loadImages():
    pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bP', 'wP', 'wR', 'wN', 'wB', 'wQ', 'wK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    NQueensBoard.N_queens(8)
    loadImages()
    running = True
    sqSelected = ()
    playerClicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                sqSelected = (row, col)
                playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    if NQueensBoard.isValid(playerClicks[0], playerClicks[1]):
                        NQueensBoard.move(playerClicks[0], playerClicks[1])
                        sqSelected = ()
                        playerClicks = []
                    else:
                        print("Invalid Move, Please give correct move")
                        playerClicks[1] = playerClicks[0]
                        NQueensBoard.move(playerClicks[0], playerClicks[1])
                        sqSelected = ()
                        playerClicks = []


        drawGameState(screen)
        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen):
    drawBoard(screen)
    drawPieces(screen, NQueensBoard.board)


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()

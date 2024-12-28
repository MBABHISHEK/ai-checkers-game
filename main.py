import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60  # Frame rate for updating the screen

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('AI Minimax Checkers')

# Function to convert mouse position to row and column on the board
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# Function to display the winner's message
def display_winner(winner):
    font = pygame.font.Font(None, 64)
    winner_text = f'{winner} is the winner!'
    text = font.render(winner_text, True, (255, 255, 255))  # White color for text
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    WINDOW.blit(text, text_rect)

def main():
    pygame.font.init()  # Initialize the font system
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    while run:
        clock.tick(FPS)

        # If it's White's turn (AI), execute the Minimax algorithm for the AI move
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
            game.ai_move(new_board)

        # Check for a winner after each move
        if game.winner() is not None:
            winner = "Red" if game.winner() == (255, 0, 0) else "White"
            print(f"The {winner} is the winner")
            display_winner(winner)  # Display the winner on the screen
            pygame.display.update()  # Update the window to show the winner
            pygame.time.delay(2000)  # Wait for 2 seconds before quitting
            run = False  # End the game

        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Terminate game

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()  # Update the game board

    pygame.quit()  # Quit Pygame

main()  # Start the game loop

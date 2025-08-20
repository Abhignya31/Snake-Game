import pygame
import sys
import os

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game Login")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE  = (50, 150, 255)
GREEN = (0, 200, 100)

# Fonts
font = pygame.font.SysFont("comicsansms", 36)
small_font = pygame.font.SysFont("comicsansms", 24)

player_name = ""
difficulty = "Easy"

def draw_text(text, font, color, surface, x, y):
    label = font.render(text, True, color)
    surface.blit(label, (x, y))

def login_screen():
    global player_name, difficulty
    input_active = False
    difficulties = ["Easy", "Medium", "Hard"]
    selected = 0

    # Game logo (just text here, can replace with image)
    logo_font = pygame.font.SysFont("comicsansms", 60)

    while True:
        screen.fill(BLACK)
        draw_text("🐍 Snake Game", logo_font, GREEN, screen, WIDTH//3, 40)
        draw_text("Enter Your Name:", font, WHITE, screen, 250, 150)

        # Player name box
        pygame.draw.rect(screen, WHITE, (250, 200, 300, 40), 2)
        name_surface = font.render(player_name, True, BLUE)
        screen.blit(name_surface, (260, 205))

        # Difficulty selection
        draw_text("Select Difficulty:", font, WHITE, screen, 250, 280)
        for i, diff in enumerate(difficulties):
            color = GREEN if i == selected else WHITE
            draw_text(diff, font, color, screen, 300, 330 + i * 50)

        # Start button
        pygame.draw.rect(screen, GREEN, (300, 500, 200, 50))
        draw_text("Start Game", font, BLACK, screen, 320, 510)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 250 <= event.pos[0] <= 550 and 200 <= event.pos[1] <= 240:
                    input_active = True
                else:
                    input_active = False
                if 300 <= event.pos[0] <= 500 and 500 <= event.pos[1] <= 550 and player_name.strip() != "":
                    # Save details
                    with open("player.txt", "w") as f:
                        f.write(f"{player_name},{difficulties[selected]}")
                    os.system("python main1.py")
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        player_name += event.unicode
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(difficulties)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(difficulties)

login_screen()

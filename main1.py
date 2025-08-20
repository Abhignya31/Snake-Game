import pygame, random, os

pygame.init()

# 🖥️ Fullscreen setup
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game - Advanced")

# 🎨 Colors
WHITE = (255, 255, 255)
RED   = (200, 0, 0)
BLUE  = (0, 0, 200)
GREEN = (0, 200, 0)
BG_COLOR = (20, 20, 30)

# Snake settings
snake_block = 20
snake_speed = 10

# Fonts
score_font = pygame.font.SysFont("comicsansms", 25)
game_over_font = pygame.font.SysFont("comicsansms", 50)

# Load player details
player_name, difficulty = "Guest", "Easy"
if os.path.exists("player.txt"):
    with open("player.txt", "r") as f:
        details = f.read().split(",")
        if len(details) == 2:
            player_name, difficulty = details

# Difficulty settings
difficulty = difficulty.strip().lower()
if difficulty == "medium":
    snake_speed = 15
elif difficulty == "hard":
    snake_speed = 20
else:
    snake_speed = 10

def Your_score(score):
    value = score_font.render(f"{player_name}'s Score: {score}", True, WHITE)
    screen.blit(value, [20, 20])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])

def gameLoop():
    global snake_speed
    game_over = False
    game_close = False

    x, y = WIDTH/2, HEIGHT/2
    dx, dy = 0, 0

    snake_list = []
    Length_of_snake = 1
    score = 0

    # Foods
    blue_x = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
    blue_y = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0
    red_x = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
    red_y = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            screen.fill(BG_COLOR)
            msg = game_over_font.render(f"Game Over, {player_name}!", True, RED)
            screen.blit(msg, [WIDTH/4, HEIGHT/3])

            final_score = score_font.render(f"Final Score: {score}", True, WHITE)
            screen.blit(final_score, [WIDTH/2 - 80, HEIGHT/2])

            retry_msg = score_font.render("Press C to Play Again or Q to Quit", True, WHITE)
            screen.blit(retry_msg, [WIDTH/4, HEIGHT/1.5])

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -snake_block; dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = snake_block; dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -snake_block; dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = snake_block; dx = 0

        x += dx
        y += dy

        # Wall collision
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        screen.fill(BG_COLOR)

        # Draw food
        pygame.draw.rect(screen, BLUE, [blue_x, blue_y, snake_block, snake_block])  # Bonus
        pygame.draw.rect(screen, RED, [red_x, red_y, snake_block, snake_block])    # Poison

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        # Self collision
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        Your_score(score)
        pygame.display.update()

        # Blue food (good)
        if x == blue_x and y == blue_y:
            blue_x = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
            blue_y = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
            score += 10

        # Red food (bad)
        if x == red_x and y == red_y:
            red_x = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
            red_y = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0
            score -= 10
            if Length_of_snake > 1:
                Length_of_snake -= 1

        clock.tick(snake_speed)

    # Save high score
    with open("scores.txt", "a") as f:
        f.write(f"{player_name},{score}\n")

    pygame.quit()
    quit()

gameLoop()

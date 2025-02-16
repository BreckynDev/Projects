import pygame

pygame.init()

#Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Constants
WIDTH = 700
HEIGHT = 450
FPS = 60

delta_time = 0

frame_per_sec = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Etch-A-Sketch")

game_paused = False

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

TEXT_COL = WHITE

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    
running = True
while running:

    delta_time = frame_per_sec.tick(FPS) / 1000 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, PURPLE, (player_pos.x, player_pos.y, 10, 10))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 140 * delta_time
    if keys[pygame.K_s]:
        player_pos.y += 140 * delta_time
    if keys[pygame.K_a]:
        player_pos.x -= 140 * delta_time
    if keys[pygame.K_d]:
        player_pos.x += 140 * delta_time
    if keys[pygame.K_r]:
        screen.fill(BLACK)

    pygame.display.update()

pygame.quit()
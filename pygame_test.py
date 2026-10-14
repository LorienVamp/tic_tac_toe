import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tic Tac Toe')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.line(screen, (255, 0, 0), (100, 100),
                     (700, 500), 5)
    pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(300, 200, 200, 200))
    pygame.display.update()
pygame.quit()

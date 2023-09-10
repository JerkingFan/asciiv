import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 128)

X = 1400
Y = 800

display_surface = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Show Text')

font = pygame.font.Font('freesansbold.ttf', 12)

land = font.render('*', True, white)

textRect = land.get_rect()

textRect.center = (X // 2, Y // 2)

r1 = pygame.Rect((10, 10, 900, 700))

while True:

    display_surface.fill(black)

    display_surface.blit(land, textRect)

    pygame.draw.rect(display_surface, white, r1, 1)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

            quit()

        pygame.display.update()

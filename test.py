import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("TEST")

clock = pygame.time.Clock()

running = True

print("GAME LOOP STARTED")

while running:

    for event in pygame.event.get():

        print("EVENT:", event)

        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

print("GAME ENDED")
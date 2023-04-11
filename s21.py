import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Cool Game')
clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            print("key pressed")

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, [10,50,100,100])
    pygame.draw.line(screen, GREEN,[0,0], [200,200], width=10)
    y_offset = 0
    while y_offset < 100:
        pygame.draw.line(screen, GREEN, [0,10 + y_offset], [100,110+ y_offset], 8)
        y_offset = y_offset + 10

    for x_offset in range(30,300,30):
        pygame.draw.line(screen, BLACK, [x_offset, 100], [x_offset - 10, 90], 2)
        pygame.draw.line(screen, BLACK, [x_offset, 90], [x_offset - 10, 100], 2)

    pygame.draw.ellipse(screen, BLACK, [20,20,250, 100], 2)
    pygame.draw.polygon(screen, BLACK, [[100,100], [0,200],[200,200]], 5)
    font = pygame.font.SysFont('Arial', 25, True, False)
    text = font.render("Hello", True, BLACK)
    screen.blit(text, [250, 250])
    score = 10
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, [0, 0])

    pygame.display.flip()
    clock.tick(60)

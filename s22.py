# import pygame

# pygame.init()

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)

# screen = pygame.display.set_mode((700, 500))
# clock = pygame.time.Clock()

# done = True
# xpos = 0
# ypos = 0
# x_change = 1
# y_change = 1
# while done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = False

#     pygame.draw.rect(screen, GREEN, [xpos, ypos, 30, 30])
#     xpos += x_change
#     ypos += y_change

#     if ypos > 470 or ypos < 0:
#         y_change = -1 * y_change
#     if xpos > 670 or xpos < 0:
#         x_change = -1 * x_change

#     pygame.display.flip()
#     clock.tick(200)


# import pygame
# pygame.init()
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
# screen = pygame.display.set_mode((700, 500))
# def draw_snowman(screen, x, y):
#     # draw a circle for the head
#     pygame.draw.ellipse(screen, WHITE, [35+x, 0+y, 25, 25])
#     # draw the middle snowman circle
#     pygame.draw.ellipse(screen, WHITE, [23+x, 20+y, 50, 50])
#     # draw the bottom snowman circle
#     pygame.draw.ellipse(screen, WHITE, [0+x, 65+y, 100, 100])
# draw_snowman(screen, 10, 10)
# draw_snowman(screen, 300, 10)
# draw_snowman(screen, 10, 300)
# pygame.display.flip()
# done = True
# while done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = False


import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
CUSTOM_COLOR = (25, 15, 102)


def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1+x, y, 10, 10])
    # Legs
    pygame.draw.line(screen, BLACK, [5+x, 17+y], [10+x, 27+y])
    pygame.draw.line(screen, BLACK, [5+x, 17+y], [x, 27+y])
    # Body
    pygame.draw.line(screen, CUSTOM_COLOR, [5+x, 17+y], [5+x, 7+y])
    # Arms
    pygame.draw.line(screen, CUSTOM_COLOR, [5+x, 7+y], [9+x, 17+y])
    pygame.draw.line(screen, CUSTOM_COLOR, [5+x, 7+y], [1+x, 17+y])


screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Stick Game")
screen.fill(WHITE)
clock = pygame.time.Clock()
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    draw_stick_figure(screen, x, y)
    pygame.display.flip()
    clock.tick(10)

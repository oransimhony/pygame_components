import pygame
from pygame.locals import *
from Components import *

def print_clicked():
    print "clicked"


def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("PyGame Components")
    running = True
    button = Button(screen, 100, 100, 200, 100, (255, 255, 255), (255, 0, 255), label="Click me!", on_click=print_clicked)
    text = Text(screen, 200, 200, color=(255, 255, 255), text="Hello There", center=False)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            button.clicked()
        button.render()
        text.render()
        pygame.display.update()

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
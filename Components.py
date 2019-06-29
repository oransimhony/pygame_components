import pygame

class Button:
    def __init__(self, screen, x, y, w, h, color, hover_color=None, label="", label_color=(0, 0, 0), on_click=None):
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.hover_color = hover_color if hover_color else color
        self.label = label
        self.label_color = label_color
        if self.label.strip() != "":
            self.text = Text(self.screen, self.x + self.w / 2, self.y + self.h / 2, label_color, text=self.label)
        else:
            self.text = False
        self.on_click = on_click

    def render(self):
        if self.hover():
            pygame.draw.rect(self.screen, self.hover_color, (self.x, self.y, self.w, self.h))
        else:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))
        if self.text:
            self.text.render()


    def hover(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.x <= mouseX <= self.x + self.w:
            if self.y <= mouseY <= self.y + self.h:
                return True
        return False

    def clicked(self):
        if self.hover() and pygame.mouse.get_pressed()[0]:
            if self.on_click:
                self.on_click()


class Text:
    def __init__(self, screen, x, y, color=(0, 0, 0), font=None, text="", size=22, antialias=False, center=True):
        pygame.font.init()
        if font:
            self.font = font
        else:
            self.font = pygame.font.SysFont('Arial', size)
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.antialias = antialias
        self.screen = screen
        self.center = center

    def render(self):
        text_surface = self.font.render(self.text, self.antialias, self.color)
        text_rect = text_surface.get_rect()
        if self.center:
            text_rect.center = (self.x, self.y)
        else:
            text_rect.x = self.x
            text_rect.y = self.y
        self.screen.blit(text_surface, text_rect)
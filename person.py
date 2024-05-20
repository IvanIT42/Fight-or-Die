import pygame
from pygame.sprite import Sprite
from settingstwo import Settings
class Person(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.ai_game = ai_game
        self.image = pygame.image.load('просто камень кольт.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.person_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.person_speed
        if self.moving_up and self.rect.top > 666:
            self.y -= self.settings.person_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.person_speed
        self.rect.x = self.x
        self.rect.y = self.y
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def center_person(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    def _check_level_person_down(self):
        self.image = pygame.image.load('просто камень кольт.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y += 4
        self.y = float(self.rect.y)
    def _check_level_person_up(self):
        if self.settings.person_level == 0:
            self.image = pygame.image.load('просто камень кольт.png')
            self.rect = self.image.get_rect()
            self.rect.midbottom = self.screen_rect.midbottom
            self.rect.y += 4
            self.y = float(self.rect.y)
        if self.settings.person_level == 1:
            self.image = pygame.image.load('бандит кольт.png')
            self.rect = self.image.get_rect()
            self.rect.midbottom = self.screen_rect.midbottom
            self.rect.y -= 1 # Сдвигаем картинку "бандит кольт" на 10 пикселей вверх
            self.y = float(self.rect.y)
        if self.settings.person_level == 2:
            self.image = pygame.image.load('рок звезда кольт(2уровень).jpg')
            self.rect = self.image.get_rect()
            self.rect.midbottom = self.screen_rect.midbottom
            self.rect.y -= 2# Сдвигаем картинку "бандит кольт" на 10 пикселей вверх
            self.y = float(self.rect.y)
        if self.settings.person_level == 3:
            self.image = pygame.image.load('серебряный кольт.png')
            self.rect = self.image.get_rect()
            self.rect.midbottom = self.screen_rect.midbottom
            self.rect.y += 2
            self.y = float(self.rect.y)
        if self.settings.person_level == 4:
            self.image = pygame.image.load('акула кольт.png')
            self.rect = self.image.get_rect()
            self.rect.midbottom = self.screen_rect.midbottom
            self.rect.y += 2
            self.y = float(self.rect.y)
        if self.settings.person_level == 5:
            self.image = pygame.image.load('золотой кольт.png')
            self.rect.midbottom = self.screen_rect.midbottom
            self.rect.y += 12
            self.y = float(self.rect.y)
        if self.settings.person_level == 6:
            self.image = pygame.image.load('норм меха кольт.jpg')
            self.rect.midbottom = self.screen_rect.midbottom
            self.rect.y += 5
            self.y = float(self.rect.y)
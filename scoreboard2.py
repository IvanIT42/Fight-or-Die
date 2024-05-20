import pygame
from pygame._sprite import Group
from person import Person
class Scoreboard():
    def __init__(self,ai_game):
        super().__init__()
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.text_color = (30,30,30)
        self.text_color1 = (0,255,0)
        self.font = pygame.font.SysFont('arial', 40)
        self.font1 = pygame.font.SysFont('times new roman', 30)
        self.text_color_red = (255,0,0)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_persons()
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.persons.draw(self.screen)

    def prep_score(self):
        rounded_score = round(self.stats.score,-1)
        score_rect = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_rect,True,self.text_color,self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color_red,self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str,True,self.text_color,self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    def prep_persons(self):
        self.persons = Group()
        for person_number in range(self.stats.persons_left):
            person = Person(self.ai_game)
            person.rect.x = 10 + person_number * person.rect.width
            person.rect.y = 10
            self.persons.add(person)
    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            self.text_color_red = (0,255,0)
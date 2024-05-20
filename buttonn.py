import pygame.font
class Button():
    def __init__(self,ai_game,msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.text_button = (255,255,255)
        self.button_color = (0,255,0)
        self.width,self.height = 225,80
        self.font = pygame.font.SysFont('arial',50)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        self._p(msg)
    def _p(self,msg):
        self.msg_image = self.font.render(msg,True,self.text_button,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
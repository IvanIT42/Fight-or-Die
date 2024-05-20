from pygame.sprite import Sprite
class Settings(Sprite):
    def __init__(self):
        self.person_level = 0
        self.screen_width = 1300
        self.screen_height = 900
        self.bg_color = (0,47,85)
        self.person_speed = 10
        self.bullets_allowed = 4
        self.bullet_width = 10
        self.bullet_height = 50
        self.bullet_speed = 25
        self.bullet_color = (25,25,25)
        self.fleet_direction = 1
        self.fleet_drop_speed = 15
        self.person_limit = 3
        self.sprout_speed = 1.3
        self.speedup_scale = 1.05
        self.score_scale = 3
        self.initalize_dynamic_settings()
        self.sprout_points = 5
    def returno(self):
        self.bullet_width = 7
        self.bullet_height = 25
        self.bullet_color = (25, 25, 25)
    def initalize_dynamic_settings(self):
        self.sprout_speed = 1.3
        self.person_speed = 10
        self.bullet_speed = 25
        self.fleet_direction = 1
        self.person_level = 0
        self.sprout_points = 5
        self.persons_left = 3
    def increase_speed(self):
        self.bullet_speed *= self.speedup_scale
        self.sprout_speed *= self.speedup_scale
        self.person_speed *= self.speedup_scale
        self.sprout_points = int(self.sprout_points * self.score_scale)
        self.person_level += 1
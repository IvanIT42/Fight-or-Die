class GameStats():
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        with open('рекорд.txt') as record:
            self.high_score = int(record.read())
        self.game_active = False
        self.score = 0
        self.settings.initalize_dynamic_settings()
        self.reset_stats()
    def reset_stats(self):
        self.persons_left = self.settings.person_limit
        self.level = 1
import sys
import pygame
from time import sleep
from random import choice
from game_stats2 import GameStats
from settingstwo import Settings
from person import Person
from bullet2 import Bullet
from antiperson import Sprout
from buttonn import Button
from scoreboard2 import Scoreboard
import pygame.mixer
import json
class Fight():
    def __init__(self):
        pygame.init()
        self.pause = pygame.mixer.Sound('пауза.mp3')
        self.pause.play(-1)
        self.game = pygame.mixer.Sound('музыка для игры.mp3')
        self.win = pygame.mixer.Sound('Brawl Stars OST - Win.mp3')
        self.button_click2 = pygame.mixer.Sound('кнопка.mp3')
        self.sound_die = pygame.mixer.Sound('звук проигрыша(когда убили).mp3')
        self.sound_false = pygame.mixer.Sound('проигрыш.mp3')
        self.up_uroven = pygame.mixer.Sound('поднял уровень.mp3')
        self.pipi = pygame.mixer.Sound('пипи кольта жэс.mp3')
        self.au = pygame.mixer.Sound('ааау кольта.mp3')
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Fight!')
        self.stats = GameStats(self)
        self.person = Person(self)
        self.sb = Scoreboard(self)
        self.bullets = pygame.sprite.Group()
        self.sprouts = pygame.sprite.Group()
        self.play_button = Button(self, "Play")
        self._create_fleet()
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.person.update()
                self._update_bullets()
                self._update_sprouts()
            self._update_screen()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    def _check_play_button(self, mouse_pos):
        button_click = self.play_button.rect.collidepoint(mouse_pos)
        if button_click and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.score = 0
            self.stats.level = 1
            self.person._check_level_person_up()
            self.pause.stop()
            self.game.play()
            self.win.stop()
            self.button_click2.play()
            self.sound_false.stop()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_persons()
            self.sprouts.empty()
            self.bullets.empty()
            self.person.center_person()
            self._create_fleet()
            pygame.mouse.set_visible(False)
            self.settings.initalize_dynamic_settings()
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.person.moving_right = True
        if event.key == pygame.K_LEFT:
            self.person.moving_left = True
        if event.key == pygame.K_UP:
            self.person.moving_up = True
        if event.key == pygame.K_DOWN:
            self.person.moving_down = True
        if event.key == pygame.K_KP_PLUS:
            pygame.mixer.music.set_volume(1.5)
        if event.key == pygame.K_KP_MINUS:
            pygame.mixer.music.set_volume(0.5)
        elif event.key == pygame.K_ESCAPE:
            self.stats.game_active = False
            pygame.mixer.music.pause()
            self.pause.play(-1)
            self.button_click2.play()
        elif event.key == pygame.K_q:
            self.button_click2.play()
            with open('рекорд.txt', 'w') as record:
                json.dump(self.stats.high_score,record)
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
        if event.key == pygame.K_p:
            self.stats.reset_stats()
            self.stats.game_active = True
            pygame.mouse.set_visible(False)
            pygame.mixer.music.unpause()
            self.win.stop()
            self.game.play()
            self.pause.stop()
            self.button_click2.play()
            self.sound_false.stop()
            self.person.center_person()
            self.person._check_level_person_up()
            self.settings.initalize_dynamic_settings()
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.person.moving_right = False
        if event.key == pygame.K_LEFT:
            self.person.moving_left = False
        if event.key == pygame.K_UP:
            self.person.moving_up = False
        if event.key == pygame.K_DOWN:
            self.person.moving_down = False
    def _ship_hit(self):
        if self.stats.persons_left > 0:
            self.stats.reset_stats()
            self._check_sounds_collidiany()
            self._check_sounds_sprout_win()
            self.stats.persons_left -= 1
            self.sprouts.empty()
            self.person._check_level_person_down()
            self.sb.prep_persons()
            self.bullets.empty()
            self._create_fleet()
            self.person.center_person()
            self.settings.initalize_dynamic_settings()
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            self.game.stop()
            self.sound_false.play()
            self._check_sounds_collidiany()
            self._check_sounds_sprout_win()
    def _check_sounds_sprout_win(self):
        sprout_win = [pygame.mixer.Sound('Примо уже здесь.mp3'),pygame.mixer.Sound('шоу продолжается.mp3'),pygame.mixer.Sound('за боль и славу.mp3'),
                      pygame.mixer.Sound('удар,удар!!.mp3'),pygame.mixer.Sound('кулаки в ярости!.mp3'),pygame.mixer.Sound('примо атакует!.mp3'),
                      pygame.mixer.Sound('время шоу.mp3'),pygame.mixer.Sound('эль примо.mp3'),pygame.mixer.Sound('пойдем.mp3'),
                      pygame.mixer.Sound('добрый вечер.mp3'),pygame.mixer.Sound('ты проиграл!.mp3'), pygame.mixer.Sound('чемпион.mp3'),
                      pygame.mixer.Sound('я лучший.mp3'),pygame.mixer.Sound('ээээль прмо!.mp3'),pygame.mixer.Sound('примооо!.mp3'),
                      pygame.mixer.Sound('эль примо агрессивно дышит.mp3'),pygame.mixer.Sound('хахахахаха.mp3'),pygame.mixer.Sound('хахахахаха2.mp3'),
                      pygame.mixer.Sound('хахахахаха3.mp3'),pygame.mixer.Sound('хахахахаха4.mp3')]
        sprout_win = choice(sprout_win)
        sprout_win.play()
    def _fire_bullets(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_sprouts_collisions()
    def _check_bullet_sprouts_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.sprouts, True, True)
        if collisions:
            self.sb.text_color = (0,255,0)
            sound1 = pygame.mixer.Sound('выстрел пистолета.mp3')
            sound1.play()
        for sprout in collisions.values():
            self.stats.score += self.settings.sprout_points * len(sprout)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.sprouts:
            self.person._check_level_person_up()
            self._check_sounds_level_up()
            self.up_uroven.play()
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
            self._check_sounds_sprout_die()
            if self.settings.person_level == 10:
                self.stats.game_active = False
                self.game.stop()
                self.pause.stop()
                self.win.play()
                pygame.mouse.set_visible(True)
                self.settings.initalize_dynamic_settings()
    def _check_sounds_sprout_die(self):
        sprout_sad = [pygame.mixer.Sound('прощай,жестокий мир.mp3'),pygame.mixer.Sound('без боли нет славы.mp3'),pygame.mixer.Sound('прощайте,амиго!.mp3'),
                      pygame.mixer.Sound('я умираю!.mp3'), pygame.mixer.Sound('стон1.mp3'),pygame.mixer.Sound('стон2.mp3'),
                      pygame.mixer.Sound('стон3.mp3')]
        sprout_sad = choice(sprout_sad)
        sprout_sad.play()
    def _check_sounds_level_up(self):
        sounds_up = [pygame.mixer.Sound('сорри,нуб!.mp3'),pygame.mixer.Sound('селфи тайм.mp3'),pygame.mixer.Sound('найс хэдшот.mp3'),
                     pygame.mixer.Sound('я так хорош!.mp3'),pygame.mixer.Sound('я так хорош!.mp3'),pygame.mixer.Sound('время повеселиться бандаранайка!.mp3'),
                     pygame.mixer.Sound('берегись выстрелов!!.mp3'),pygame.mixer.Sound('смотри и учись.mp3'),pygame.mixer.Sound('номер один!.mp3'),
                     pygame.mixer.Sound('мускулы и красота!.mp3'),pygame.mixer.Sound('время проблем...mp3'), pygame.mixer.Sound('кольт слишком хорощ!.mp3'),
                     pygame.mixer.Sound('посмотри на мой хэдшот!.mp3'), pygame.mixer.Sound('берегись кольт идет.mp3'), pygame.mixer.Sound('пипи кольта жэс.mp3'),
                     pygame.mixer.Sound('град пуль!.mp3'),pygame.mixer.Sound('это легко!.mp3'), pygame.mixer.Sound('Да!.mp3')]
        sounds_up = choice(sounds_up)
        sounds_up.play()
    def _update_sprouts(self):
        self._check_fleet_edges()
        self.sprouts.update()
        if pygame.sprite.spritecollideany(self.person, self.sprouts):
            self.sound_die.play()
            self._ship_hit()
        self._check_aliens_bottom()
    def _check_sounds_collidiany(self):
        fraza_sad = [pygame.mixer.Sound('ааау кольта.mp3'), pygame.mixer.Sound('гых кольта.mp3'),
                 pygame.mixer.Sound('читер кольта.mp3'),pygame.mixer.Sound('ноу вэй! кольта.mp3'), pygame.mixer.Sound('Оу кольта.mp3'),
                 pygame.mixer.Sound('воу,это больно кольт.mp3'),pygame.mixer.Sound('хэй ватч ит.mp3'),
                 pygame.mixer.Sound('кольт хочет к маме.mp3'),pygame.mixer.Sound('я ведь очень красивый!.mp3'),
                 pygame.mixer.Sound('только не по лицу!.mp3'),pygame.mixer.Sound('только не по лицу!.mp3'),pygame.mixer.Sound('мерси!!.mp3')]
        fraza_sad = choice(fraza_sad)
        fraza_sad.play()
    def _create_fleet(self):
        sprout = Sprout(self)
        sprout_width, sprout_height = sprout.rect.size
        available_space_x = self.settings.screen_width - (2*sprout_width)
        sprout_number_x = available_space_x // (2*sprout_width)
        available_space_y = (self.settings.screen_height - (3*sprout_height) - sprout_height)
        row_number = available_space_y // (2*sprout_height)
        for number_row in range(row_number):
            for sprout_number in range(sprout_number_x):
                self._create_sprout(sprout_number, number_row)
    def _check_fleet_edges(self): # достиг ли примо края экрана и меняет направление
        for sprout in self.sprouts.sprites():
            if sprout.check_edges():
                self._change_fleet_direction()
                break
    def _check_aliens_bottom(self): # проверяет,достиг ли примо конца экрана
        screen_rect = self.screen.get_rect()
        for sprout in self.sprouts.sprites():
            if sprout.rect.bottom >= screen_rect.bottom:
                self.sound_die.play()
                self._ship_hit()
                break
    def _change_fleet_direction(self):
        for sprout in self.sprouts.sprites():
            sprout.rect.y += (self.settings.sprout_speed * self.settings.fleet_drop_speed)
        self.settings.fleet_direction *= -1
    def _create_sprout(self, sprout_number, number_row):
        sprout = Sprout(self)
        sprout_width, sprout_height = sprout.rect.size
        sprout.x = sprout_width + 2 * sprout_width * sprout_number
        sprout.rect.x = sprout.x
        sprout.rect.y = sprout.rect.height + 2 *sprout_height * number_row
        self.sprouts.add(sprout)
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.person.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.sprouts.draw(self.screen)
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
if __name__ == '__main__':
    Fight().run_game()
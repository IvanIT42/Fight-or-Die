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
from failbutton import FailButton
import pygame.mixer
import json
class Fight():
    def __init__(self):
        pygame.init()
        self.pause = pygame.mixer.Sound('пауза.mp3')
        self.chose = pygame.mixer.Sound('музыка для выбора языка.mp3')
        self.engmusic = pygame.mixer.Sound('музыка для английского.mp3')
        self.show_music = pygame.mixer.Sound('правила.mp3')
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
        self.show_rules_screen()
        self.person = Person(self)
        self.sb = Scoreboard(self)
        self.bullets = pygame.sprite.Group()
        self.sprouts = pygame.sprite.Group()
        self.play_button = Button(self, "Play")
        self.fail_button = FailButton(self, "You've lost")
        self._create_fleet()
        self.person.center_person()
        self._k_blit()
        self._languege()
        self.chose.play()
    def _show_rect(self):
        self.text_rect1 = self.text1.get_rect(center=(self.screen.get_width() // 2, 50))
        self.text_rect2 = self.text2.get_rect(center=(self.screen.get_width() // 2, 95))
        self.text_rect3 = self.text3.get_rect(center=(self.screen.get_width() // 2, 140))
        self.text_rect4 = self.text4.get_rect(center=(self.screen.get_width() // 2, 185))
        self.text_rect5 = self.text5.get_rect(center=(self.screen.get_width() // 2, 230))
        self.text_rect6 = self.text6.get_rect(center=(self.screen.get_width() // 2, 275))
        self.dop_text = self.text_dop.get_rect(center=(self.screen.get_width() // 2, 410))
        self.text_init_rect = self.text_init.get_rect(center=(self.screen.get_width() // 2,365))
        self.text_rect7 = self.text7.get_rect(center=(self.screen.get_width() // 2, 320))
        self.text_rect8 = self.text8.get_rect(center=(self.screen.get_width() // 2, 455))
    def _languege(self):
        self.screen.fill((0,47,85))
        self.textrus = self.fontdop.render('Выберите язык/Select a language.',True,(255,255,255))
        self.texteng = self.fontdop.render('Нажмите На R,если русский,E-если английский/Press R if Russian,E if English',True,(255,255,255))
        self.textmistake = self.fontdop.render('ошиблись языком?Нажмите L/Did you make a mistake in the language?Press L',True,(255,255,255))
        self.textmistake_rect = self.textmistake.get_rect(center=(self.screen.get_width() // 2,495))
        self.texteng_rect = self.texteng.get_rect(center=(self.screen.get_width() // 2,460))
        self.textrus_rect = self.textrus.get_rect(center=(self.screen.get_width() // 2,425))
        self.screen.blit(self.textrus,self.textrus_rect)
        self.screen.blit(self.texteng,self.texteng_rect)
        self.screen.blit(self.textmistake,self.textmistake_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    def show_rules_screen(self):
            self.screen.fill((0,47,85))  # Заполняем экран черным цветом
            self.font4 = pygame.font.SysFont('times new roman',10)
            self.font = pygame.font.SysFont('times new roman', 27)  # Задаем шрифт и размер текста
            self.fontdop = pygame.font.SysFont('times new roman',22)
            self.fontfalse = pygame.font.Font(None,38)
            self.text1 = self.font.render("Добро пожаловать в игру!", True, (255, 255, 255))  # Создаем текст
            self.text2 = self.font.render('Вы играете на кольте против флота эль примо,который хочет вас покалечить!',True,(255,255,255))
            self.text3 = self.font.render('Ваша цель:не дать примо добраться до вас,иначе вы теряете жизнь.', True,(255,255,255))
            self.text4 = self.font.render('У вас в общем будет 3 жизни,они помещены в верхнем левом углу.', True,(255,255,255))
            self.text5 = self.font.render('По середине экрана отображается ваш общий рекорд,справа кол-во очков и ваш текущий уровень!',True,(255,255,255))
            self.text6 = self.font.render('Когда вы убиваете флот эль примо,то уровень игры становится выше!',True,(255,255,255))
            self.text_init = self.font.render('Но когда вы умираете,то уровень игры снова переходит на 1!',True,(255,255,255))
            self.text_dop = self.font.render('На 6 уровне у кольта накопится супер,вы можете использовать его с помощью B**',True,(255,255,255))
            self.text7 = self.font.render('Соответственно,повышается скорость кольта,эль примо,пуль и вы получаете больше очков!',True,(255,255,255))
            self.text8 = self.font.render('Не будьте самоуверенными,флот эль примо взбешён и будет биться до конца,приходя в ярость!',True,(255,255,255))
            self.text_k1 = self.fontdop.render('**-Основные клавиши:',True,(255,255,255))
            self.text_k2 = self.fontdop.render('Стрелочки вправо,влево,вверх,вниз - движение', True,(255,255,255))
            self.text_k3 = self.fontdop.render('P/Кнопка мыши на Play - начало игры', True,(255,255,255))
            self.text_k4 = self.fontdop.render('Пробел-стрельба в примо',True,(255,255,255))
            self.text_k5 = self.fontdop.render('Q-выйти из игры',True,(255,255,255))
            self.text_run_game = self.fontdop.render('Чтобы продолжить,нажмите на любую цифру и вперед!',True,(255,255,255))
            self.text_k6 = self.fontdop.render('B-использовать супер(досутпно на 6 уровне)',True,(255,255,255))
            self._show_rect()
            self._show_blit()
    def _show_blit(self):
        self.screen.blit(self.text1, self.text_rect1)
        self.screen.blit(self.text2, self.text_rect2)
        self.screen.blit(self.text3, self.text_rect3)
        self.screen.blit(self.text4, self.text_rect4)
        self.screen.blit(self.text5, self.text_rect5)
        self.screen.blit(self.text6, self.text_rect6)
        self.screen.blit(self.text7, self.text_rect7)
        self.screen.blit(self.text8, self.text_rect8)
        self.screen.blit(self.text_dop, self.dop_text)
        self.screen.blit(self.text_init,self.text_init_rect)
        self.screen.blit(self.text_run_game, (760, 850))
        self._k_blit()
    def _k_blit(self):
        alpha = 70
        text_color = (255, 255, 255, alpha)
        self.screen.blit(self.text_k1, (0, 750))
        self.screen.blit(self.text_k2, (25, 775))
        self.screen.blit(self.text_k3, (25, 795))
        self.screen.blit(self.text_k4, (25, 815))
        self.screen.blit(self.text_k5, (25, 835))
        self.screen.blit(self.text_k6, (25, 855))
        self.text_k1.set_alpha(alpha)
        self.text_k2.set_alpha(alpha)
        self.text_k3.set_alpha(alpha)
        self.text_k4.set_alpha(alpha)
        self.text_k5.set_alpha(alpha)
        self.text_k6.set_alpha(alpha)
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.person.update()
                self._update_bullets()
                self._update_sprouts()
                self._update_screen()
            if not self.stats.game_active:
                pygame.display.flip()
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
            self._check_button_events()
    def _check_button_events(self):
        self.engmusic.stop()
        self.show_music.stop()
        self.settings.person_limit = 3
        self.stats.reset_stats()
        self.person.center_person()
        self.stats.score = 0
        self.stats.level = 1
        self.person._check_level_person_up()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_persons()
        self.sprouts.empty()
        self.bullets.empty()
        self._create_fleet()
        pygame.mouse.set_visible(False)
        self.settings.initalize_dynamic_settings()
        self._music_go()
    def _music_go(self):
        self.pause.stop()
        self.game.play()
        self.win.stop()
        self.button_click2.play()
        self.sound_false.stop()
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.person.moving_right = True
        if event.key == pygame.K_LEFT:
            self.person.moving_left = True
        if event.key == pygame.K_UP:
            self.person.moving_up = True
        if event.key == pygame.K_DOWN:
            self.person.moving_down = True
        if event.key == pygame.K_p:
            self._check_button_events()
        elif event.key == pygame.K_q:
            self.button_click2.play()
            with open('рекорд.txt', 'w') as record:
                json.dump(self.stats.high_score,record)
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
            self.sb.text_color = (0,255,0)
            sound1 = pygame.mixer.Sound('AudioCutter_пипи кольта жэс(2).mp3')
            sound1.play()
        elif self.settings.person_level == 5:
            if event.key == pygame.K_b:
                self.settings.bullet_width = 300
                self.settings.bullet_height = 100
                self.settings.bullet_color = (255, 140, 0)
                self._fire_bullets()
                self.settings.returno()
        elif (event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5
              or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9 or event.key == pygame.K_0 and event.key != pygame.K_p):
            self._update_screen()
            self.show_music.stop()
            self.engmusic.stop()
            self.pause.play()
            self.chose.stop()
        self._check_chose_language(event)
    def  _check_chose_language(self,event):
        if event.key == pygame.K_l:
            self._languege()
            self.show_music.stop()
            self.engmusic.stop()
            self.chose.play()
            self.pause.stop()
        if event.key == pygame.K_r:
            self.show_rules_screen()
            self.show_music.play()
            self.engmusic.stop()
            self.chose.stop()
            self.pause.stop()
            self.play_button = Button(self, "Играть")
        if event.key == pygame.K_e:
            self.show_rules_screen2()
            self.chose.stop()
            self.show_music.stop()
            self.engmusic.play()
            self.pause.stop()
            self.play_button = Button(self, 'Play')
    def show_rules_screen2(self):
        self.screen.fill((0,47,85))
        self.text1 = self.font.render("Welcome to the game!", True, (255, 255, 255))  # Создаем текст
        self.text2 = self.font.render('You are playing on a colt against the fleet of el Primo, which wants to cripple you!', True,(255, 255, 255))
        self.text3 = self.font.render("Your goal:Don't let primo get to you, otherwise you lose your life.", True,(255, 255, 255))
        self.text4 = self.font.render('You will have 3 lives in total, they are placed in the upper left corner.', True,(255, 255, 255))
        self.text5 = self.font.render('Your total record is displayed in the middle of the screen, on the right the number of points and your current level!', True,(255, 255, 255))
        self.text6 = self.font.render('When you kill the fleet of El Primo, the level of the game becomes higher!', True,(255, 255, 255))
        self.text_init = self.font.render('But when you die, the game level goes back to 1!', True,(255, 255, 255))
        self.text_dop = self.font.render('At level 6, the colt will accumulate super, you can use it with B**',True, (255, 255, 255))
        self.text7 = self.font.render('Accordingly, the speed of colt, el primo, bullets increases and you get more points!', True,(255, 255, 255))
        self.text8 = self.font.render("Don't be overconfident, the el primo fleet is furious and will fight to the end, becoming enraged!", True,(255, 255, 255))
        self.text_k1 = self.fontdop.render('**-Main keys:', True, (255, 255, 255))
        self.text_k2 = self.fontdop.render('Arrows to the right, left, up, down - movement', True, (255, 255, 255))
        self.text_k3 = self.fontdop.render('P/Mouse button on Play - start of the game', True, (255, 255, 255))
        self.text_k4 = self.fontdop.render('Space bar-shooting in primo', True, (255, 255, 255))
        self.text_k5 = self.fontdop.render('Q-exit the game', True, (255, 255, 255))
        self.text_run_game = self.fontdop.render('To continue, click on any number and go ahead!', True,(255, 255, 255))
        self.text_k6 = self.fontdop.render('B-use super(available on 6 available)', True, (255, 255, 255))
        self._show_rect()
        self._show_blit()
    def _music_start_play(self):
        pygame.mixer.music.unpause()
        self.win.stop()
        self.game.play()
        self.pause.stop()
        self.button_click2.play()
        self.sound_false.stop()
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
            self.settings.person_limit -= 1
            self.stats.persons_left -= 1
            self.person.center_person()
            self._check_sounds_collidiany()
            self._check_sounds_sprout_win()
            self.sprouts.empty()
            self.person._check_level_person_down()
            self.sb.prep_persons()
            self.bullets.empty()
            self._create_fleet()
            self.settings.initalize_dynamic_settings()
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            self.game.stop()
            self.sound_false.play()
            self._check_sounds_collidiany()
            self._check_sounds_sprout_win()
            self.fail_button.draw_button()
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
        for sprout in collisions.values():
            self.stats.score += self.settings.sprout_points * len(sprout)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.sprouts:
            self.person.center_person()
            self.person._check_level_person_up()
            self._check_sounds_level_up()
            self.up_uroven.play()
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
            self._check_sounds_sprout_die()
            self._end_play_win()
    def _end_play_win(self):
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
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.sprouts.draw(self.screen)
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
            pygame.display.update()
        self.person.blitme()
        self._k_blit()
        pygame.display.flip()
if __name__ == '__main__':
    fg = Fight()
    fg.run_game()
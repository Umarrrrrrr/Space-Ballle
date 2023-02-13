import pygame
import random

points = 0
pygame.init()
clock = pygame.time.Clock()

size = (800, 670)
bg = pygame.image.load('images/fon.jpg')  # fon
bg_x = 0
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.FULLSCREEN)

shoot_sound = pygame.mixer.Sound('sound/shoot.mp3')
expolosion_sound = pygame.mixer.Sound('sound/explosion.mp3')
expolosion = [pygame.image.load('expolision/denomit1.png').convert(),
              pygame.image.load('expolision/denomit9.png').convert(),
              pygame.image.load('expolision/denomit2.png').convert(),
              pygame.image.load('expolision/denomit10.png').convert(),
              pygame.image.load('expolision/denomit3.png').convert(),
              pygame.image.load('expolision/denomit11.png').convert(),
              pygame.image.load('expolision/denomit4.png').convert(),
              pygame.image.load('expolision/denomit12.png').convert(),
              pygame.image.load('expolision/denomit5.png').convert(),
              pygame.image.load('expolision/denomit13.png').convert(),
              pygame.image.load('expolision/denomit6.png').convert(),
              pygame.image.load('expolision/denomit14.png').convert(),
              pygame.image.load('expolision/denomit7.png').convert(),
              pygame.image.load('expolision/denomit15.png').convert(),
              pygame.image.load('expolision/denomit8.png').convert(),
              pygame.image.load('expolision/denomit16.png').convert()]  # expolosion animation
expolision_anim_count = 0

enemy_list_in_game = []

PLAYER_IMAGE = pygame.image.load('images/player.jpg').convert()
PLAYER_SPEED = 5
PLAYER_X = 350
PLAYER_Y = 470

ENEMY_IMAGE = pygame.image.load('images/enemy.jpg').convert()
ENEMY_X = 145
ENEMY_Y = 0

BULLET_IMAGE = pygame.image.load('images/bullet.png').convert_alpha()
bullets = []

shoot_enemy = False
enemy_bullet_timer = pygame.USEREVENT + 1  # таймер появления пули вражеского корабля
pygame.time.set_timer(enemy_bullet_timer, 1000)
ENEMY_BULLET_IMAGE = pygame.image.load('images/enemy_bullet.png')
enemy_bullets = []

ARIAL_50 = pygame.font.SysFont('unicephalon.ttp', 50)
label = pygame.font.Font('Intro.otf', 40)
play_label = label.render('Play', False, (255, 0, 0), (5, 9, 13))
play_label_rect = play_label.get_rect(topleft=(440, 100))

records_label = label.render('Records', False, (255, 0, 0), (5, 9, 13))
records_label_rect = records_label.get_rect(topleft=(400, 180))

restart_game_label = label.render('Restart', False, (255, 0, 0), (0, 0, 0))
restart_game_label_rect = restart_game_label.get_rect(topleft=(430, 300))

main_menu_label = label.render('Maim menu', False, (193, 196, 199))
main_menu_label_rect = restart_game_label.get_rect(topleft=(400, 450))

main_menu_label2 = label.render('Maim menu', False, (193, 196, 199))
main_menu_label_rect2 = restart_game_label.get_rect(topleft=(350, 450))

exit_label = label.render('Exit', False, (193, 196, 199))
exit_label_rect = exit_label.get_rect(topleft=(440, 260))
point_label = label.render('Points:' + str(points), False, (122, 134, 118))
# point_label_rect = point_label.get_rect(topleft=(400, 150))

returm_main_menu_from_records_label = label.render('return main menu', False, (193, 196, 199))
returm_main_menu_from_records_label_rect = returm_main_menu_from_records_label.get_rect(topleft=(330, 600))

return_game_label = label.render('retunr to game', False, (193, 196, 199))
return_game_rect = return_game_label.get_rect(topleft=(300, 600))

permission_to_shoot = False
pygame.time.set_timer(pygame.USEREVENT, 500)

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1000)
returm_main_menu = False
returm_main_menu_from_records = False
restart_game = True
gameplay = False
running = True
records = False
stop_game = False
while running:
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()
    if not restart_game:
        gameplay = False
        screen.fill((0, 0, 0))
        screen.blit(restart_game_label, restart_game_label_rect)
        screen.blit(main_menu_label, main_menu_label_rect)
        mouse = pygame.mouse.get_pos()
        if restart_game_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            enemy_list_in_game.clear()
            enemy_bullets.clear()
            bullets.clear()
            points = 0
            PLAYER_X = 350
            PLAYER_Y = 470
            restart_game = True
            gameplay = True
        if main_menu_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            enemy_list_in_game.clear()
            enemy_bullets.clear()
            bullets.clear()
            points = 0
            PLAYER_X = 350
            PLAYER_Y = 470
            restart_game = True
            gameplay = False
    if gameplay and restart_game:
        ENEMY_X = random.randint(10, 980)
        screen.blit(bg, (bg_x, 0))
        screen.blit(PLAYER_IMAGE, (PLAYER_X, PLAYER_Y))
        point_label = label.render('Points:' + str(points), False, (122, 134, 118))
        screen.blit(point_label, (440, 600))

        player_rect = PLAYER_IMAGE.get_rect(topleft=(PLAYER_X, PLAYER_Y))

        if enemy_list_in_game:
            for (i, el) in enumerate(enemy_list_in_game):
                screen.blit(ENEMY_IMAGE, el)
                el.y += 1
                if el.y > 470:
                    enemy_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    for _ in range(16):
                        screen.blit(expolosion[expolision_anim_count], (PLAYER_X - 40, PLAYER_Y - 50))

                        expolision_anim_count += 1
                        if expolision_anim_count == 15:
                            expolosion_anim_count = 0
                    restart_game = False

        if enemy_bullets:
            for (i, el) in enumerate(enemy_bullets):
                screen.blit(ENEMY_BULLET_IMAGE, (el.x + 14, el.y + 17))
                el.y += (points + 30) ** 0.5 // 5 + 1
                if el.y > 470:
                    enemy_bullets.pop(i)
                if el.colliderect(player_rect):
                    for _ in range(16):
                        screen.blit(expolosion[expolision_anim_count], (el.x - 40, el.y - 50))

                        expolision_anim_count += 1
                        if expolision_anim_count == 15:
                            expolision_anim_count = 0
                    expolosion_sound.play()
                    points1 = str(points)
                    restart_game = False

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(BULLET_IMAGE, (el.x - 20, el.y - 12))
                el.y -= 2

                if el.y < 20:
                    bullets.pop(i)

                if enemy_list_in_game:
                    for (index, enemy) in enumerate(enemy_list_in_game):
                        if el.colliderect(enemy):
                            enemy_list_in_game.pop(index)
                            bullets.pop(i)
                            points += 10
                            expolosion_sound.play()
                            for _ in range(16):
                                screen.blit(expolosion[expolision_anim_count], (el.x - 55, el.y - 70))

                                expolision_anim_count += 1
                                if expolision_anim_count == 15:
                                    expolision_anim_count = 0
        if keys[pygame.K_LEFT] and PLAYER_X > 15:
            PLAYER_X -= PLAYER_SPEED - 2
        elif keys[pygame.K_RIGHT] and PLAYER_X < 985:
            PLAYER_X += PLAYER_SPEED - 2

    elif not gameplay and not restart_game:
        gameplay = False
        restart_game = False
    else:
        screen.blit(bg, (bg_x, 0))
        screen.blit(play_label, play_label_rect)
        screen.blit(exit_label, exit_label_rect)

        if play_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
        if exit_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == enemy_timer:  # запуск вражеского корабля
            enemy_list_in_game.append(ENEMY_IMAGE.get_rect(topleft=(ENEMY_X, 0)))
            if event.type == enemy_bullet_timer:  # запуск пули вражеского корабля
                shoot_enemy = True
            if shoot_enemy:
                enemy_bullets.append(ENEMY_BULLET_IMAGE.get_rect(topleft=(ENEMY_X, ENEMY_Y + 10)))
                shoot_enemy = False
        if event.type == pygame.USEREVENT:  # ограничение количества выстрелов игрока
            permission_to_shoot = True
        if permission_to_shoot:
            if event.type == pygame.KEYUP and event.key == pygame.K_UP:  # запуск пули игрока и ограничение выстрелов
                bullets.append(BULLET_IMAGE.get_rect(topleft=(PLAYER_X + 30, PLAYER_Y + 10)))
                permission_to_shoot = False
                shoot_sound.play()

    pygame.display.update()
    clock.tick(60)
pygame.quit()
# НЕ ОЧЕНЬ, НО ЗАТО САМ.

import pygame
import sys
import time
from pygame.color import THECOLORS

zak_num = 0

pygame.init()
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Sys admin simulator🧑‍💻")

main_menu = pygame.image.load("rfqa123.jpg")
game_start = pygame.image.load("start123.png")
per = pygame.image.load("1600x900.jpg")
first_lvl = pygame.image.load('image-Photoroom.jpg')
hone = pygame.image.load('hone.jpg')
icons = pygame.image.load('icons.png')
inst_hone = pygame.image.load('instruct.jpg')
laptop = pygame.image.load('Laptop.png')
bios = pygame.image.load('i.png')

start_pos = (240, 160)
start_rect = game_start.get_rect(topleft=start_pos)
qq = 'Предыстория: Ты 18-летний студент, который уже полгода ходит в универ.'
ww = ('Ты захотел заниматься починкой ПК и купить новый ноутбук. За это время ты смог насобирать 200$.'
      ' Данная сумма неплохая, но для покупки ноута её мало.')
ee = ('Тебе нужно подработать в компаниях для заработка денег.'
      ' Но главное не косячь, за 2 предупреждения тебя уволят')

first_lvl_rect = first_lvl.get_rect(topleft=(800, 240))
history = pygame.font.Font(None, 28)
money = 200
pres = 0
z_font = pygame.font.Font(None, 58)

hat = pygame.font.Font(None, 52).render('SYS ADMIN SIMULATOR', True, (255, 0, 0))


balance = z_font.render(f'Баланс: {money}$', True, (0, 0, 0))
pres_text = z_font.render(f'Предупреждения: {pres}', True, (0, 0, 0))

rul1 = pygame.font.Font(None, 34).render('Правила: 1) За неправильное выполнение заказа тебе дают 1 предкпреждение.', True, (255, 255, 255))
rul2 = pygame.font.Font(None, 34).render('2) Игра считается пройденной если ты прошел ВСЕ тестовые задания.', True, (255, 255, 255))
rul3 = pygame.font.Font(None, 34).render('3) Чтобы открыть инструкцию нажмите TAB, чтобы закрыть CAPS.', True, (255, 255, 255))
yes_text = z_font.render('Да', True, (0, 0, 0))
no_text = z_font.render('Нет', True, (0, 0, 0))

q = len(qq)
w = len(ww)
e = len(ee)
t = 0
ipg = False
pof = False
pof1 = False
pof2 = False

first_text = pygame.font.Font(None, 80).render('Удалить вирус с ПК, 150$ (нажать 1)', True, (0, 0, 0))
second_text = pygame.font.Font(None, 80).render('Удалить пароль с биоса, 450$ (нажать 2)', True, (0, 0, 0))
third_text = pygame.font.Font(None, 80).render('Установить Windows 11, 200$ (нажать 3)', True, (0, 0, 0))

game_over = pygame.font.Font(None, 140).render('GAME OVER', True, (255, 0, 0))
ops_1 = z_font.render('Пользователь установил программу, в комплекте с которой шёл вирус.', True, (255, 255, 255))
ops_11 = z_font.render('Он закрывает любую программу при открытии', True, (255, 255, 255))

first_text_x = pygame.font.Font(None, 80).render('Удалить вирус с ПК, 100$ (ВЫПОЛНЕННО)', True, (0, 255, 0))
second_text_x = pygame.font.Font(None, 80).render('Удалить пароль с биоса, 450$ (ВЫПОЛНЕННО)', True, (0, 255, 0))
first_text_y = pygame.font.Font(None, 80).render('Удалить вирус с ПК, 100$ (НЕ ВЫПОЛНЕННО)', True, (255, 0, 0))


show_text = False
nxt = False
d = False
inst = False
jj = False
ant = False
ant1 = False


ipg1 = False
ipg2 = False
phone = False
not_zak_2 = False
hyt = False

nxt1 = False
nxt2 = False
nxt3 = False
inp = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_1:
                ipg = True
            if event.key == pygame.K_q:
                ipg1 = True
                zak_num = 2
            if event.key == pygame.K_6:
                pof = True
                zak_num = 1
            if event.key == pygame.K_o:
                ant = True
            if event.key == pygame.K_TAB:
                inst = True
            if event.key == pygame.K_CAPSLOCK:
                inst = False
            if event.key == pygame.K_q:
                jj = False
            if event.key == pygame.K_2:
                ipg1 = True
            if event.key == pygame.K_7:
                pof1 = True
            if event.key == pygame.K_b:
                phone = True
            if event.key == pygame.K_LSHIFT:
                nxt2 = True
            if event.key == pygame.K_3:
                ipg2 = True
            if event.key == pygame.K_3:
                pof2 = True
            if event.key == pygame.K_TAB:
                inst = True
            if event.key == pygame.K_CAPSLOCK:
                inst = False
            if event.key == pygame.K_e:
                time.sleep(0.5)
                jj = True
            if event.key == pygame.K_w:
                ant1 = True
            if event.key == pygame.K_RSHIFT:
                hyt = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if start_rect.collidepoint(event.pos):
                    show_text = True
                    screen = pygame.display.set_mode((1, 1))
                    time.sleep(0.2)
                    screen = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)
                if first_lvl_rect.collidepoint(event.pos):
                    nxt = True
                if zak_num == 1:
                    nxt1 = True

    if not show_text:
        screen.blit(main_menu, (0, 0))
        screen.blit(game_start, start_pos)
        screen.blit(hat, (180, 50))
    elif show_text:
        screen.blit(per, (0, 0))
        screen.blit(first_lvl, (800, 240))
        if t < q:
            t += 1
            time.sleep(0.03)
        screen.blit(history.render(qq[:t], True, (255, 255, 255)), (20, 20))
        if t < w:
            t += 1
            time.sleep(0.03)
        screen.blit(history.render(ww[:t], True, (255, 255, 255)), (40, 40))
        if t < e:
            t += 1
            time.sleep(0.03)
        screen.blit(history.render(ee[:t], True, (255, 255, 255)), (60, 60))
        screen.blit(rul1, (60, 100))
        screen.blit(rul2, (60, 130))
        screen.blit(rul3, (60, 160))
    if nxt:
        screen.blit(hone, (0, 0))
        screen.blit(first_text, (200, 200))
        screen.blit(second_text, (200, 400))
        screen.blit(third_text, (200, 600))
        screen.blit(balance, (10, 0))
        screen.blit(pres_text, (10, 40))
    if ipg:
        screen.fill(THECOLORS['blue'])
        screen.blit(ops_1, (10, 70))
        screen.blit(ops_11, (10, 120))
        screen.blit(pygame.font.Font(None, 150).render('Нажмите 6', True, (0, 0, 0)), (500, 700))

    if pof:
        screen.blit(hone, (0, 0))
        screen.blit(icons, (0, 0))
        screen.blit(pygame.font.Font(None, 60).render("Подсказка: нажми TAB", True, (0, 0, 0)), (500, 700))
    if inst:
        screen.blit(inst_hone, (0, 0))
    if jj:
        screen.fill(THECOLORS['white'])
        screen.blit(z_font.render('Флешка', True, (0, 0, 0)),(0, 0))
        screen.blit(z_font.render('Windows 11(W)', True, (0, 0, 0)),(80, 80))
        screen.blit(z_font.render('Антивирус(O)', True, (0, 0, 0)),(80, 140))
        screen.blit(z_font.render('Консоль(K)', True, (0, 0, 0)),(80, 200))
    if ant:
        screen.fill(THECOLORS['white'])
        screen.blit(pygame.font.Font(None, 140).render('Установка...', True, (0, 0, 0)),(200, 100))
        time.sleep(1)
        screen.blit(pygame.font.Font(None, 140).render('Готово :)', True, (0, 0, 0)),(200, 200))
        screen.blit(first_lvl, (800, 240))
    if nxt1:
        screen.blit(hone, (0, 0))
        screen.blit(first_text_x, (200, 200))
        screen.blit(second_text, (200, 400))
        screen.blit(third_text, (200, 600))
        screen.blit(balance, (10, 0))
        screen.blit(pres_text, (10, 40))
    if ipg1:
        screen.fill(THECOLORS['blue'])
        screen.blit(pygame.font.Font(None, 64).render('Пользователь установил пароль на биос и забыл его. ', True, (255, 255, 255)), (40, 70))
        screen.blit(pygame.font.Font(None, 64).render('Нужно открыть консоль и прописать: curl supp_pass_bios', True, (255, 255, 255)), (40, 120))
        screen.blit(pygame.font.Font(None, 150).render('Нажмите 7', True, (0, 0, 0)), (500, 700))
    if pof1:
        screen.fill(THECOLORS['black'])
        screen.blit(pygame.font.Font(None, 30).render('Microsoft Windows [Version 10.0.22000.2538]', True, (255, 255, 255)), (10, 10))
        screen.blit(pygame.font.Font(None, 30).render('(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.', True, (255, 255, 255)), (10, 30))
        screen.blit(pygame.font.Font(None, 30).render('C:/Users/User>', True, (255, 255, 255)), (10, 100))
    if phone:
        screen.blit(hone, (0, 0))
        screen.blit(icons, (0, 0))
        screen.blit(pygame.font.Font(None, 60).render("Задание выполненно!(Нажмите Л SHIFT для выхода)", True, (0, 0, 0)), (300, 700))
    if nxt2:
        screen.blit(hone, (0, 0))
        screen.blit(first_text_x, (200, 200))
        screen.blit(second_text_x, (200, 400))
        screen.blit(third_text, (200, 600))
        screen.blit(balance, (10, 0))
        screen.blit(pres_text, (10, 40))
    if ipg2:
        screen.fill(THECOLORS['blue'])
        screen.blit(pygame.font.Font(None, 64).render('Пользователю нужно установить windows. ', True, (255, 255, 255)), (40, 70))
        screen.blit(pygame.font.Font(None, 64).render('Напомню про TAB', True, (255, 255, 255)), (40, 120))
        screen.blit(pygame.font.Font(None, 150).render('Нажмите 8', True, (0, 0, 0)), (500, 700))
    if pof2:
        screen.blit(bios, (0, 0))
    if ant1:
        screen.blit(hone, (0, 0))
        screen.blit(icons, (0, 0))
        screen.blit(pygame.font.Font(None, 60).render("Задание выполненно!(Нажмите П SHIFT для выхода)", True, (0, 0, 0)), (300, 700))
    if pres >= 2:
        screen.fill(THECOLORS['black'])
        screen.blit(game_over, (500, 400))
    if hyt:
        screen.fill(THECOLORS['blue'])
        screen.blit(laptop, (190, 200))
        screen.blit(z_font.render('Поздравляю! Ты прошёл игру)', True, (255, 255, 255)),(700, 400))
    pygame.display.flip()
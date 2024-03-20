import pygame
import time
import random

pygame.init()

# Inisialisasi variabel
lebar = 800
tinggi = 600
ukuran_block = 20
kecepatan = 15

warna_putih = (255, 255, 255)
warna_merah = (255, 0, 0)
warna_hijau = (0, 255, 0)
warna_hitam = (0, 0, 0)

layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("Permainan Ular")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 35)


def ular(ukuran_block, ular_list):
    for x in ular_list:
        pygame.draw.rect(layar, warna_hijau, [x[0], x[1], ukuran_block, ukuran_block])


def pesan(pesan, warna):
    text = font.render(pesan, True, warna)
    layar.blit(text, [lebar / 6, tinggi / 2])


def gameLoop():
    game_over = False
    game_close = False

    x1 = lebar / 2
    y1 = tinggi / 2

    x1_change = 0
    y1_change = 0

    ular_List = []
    panjang_ular = 1

    foodx = round(random.randrange(0, lebar - ukuran_block) / 10.0) * 10.0
    foody = round(random.randrange(0, tinggi - ukuran_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            layar.fill(warna_putih)
            pesan("Kamu Kalah! Tekan C-Continue or Q-Keluar", warna_merah)
            ular(ukuran_block, ular_List)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -ukuran_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = ukuran_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -ukuran_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = ukuran_block
                    x1_change = 0

        if x1 >= lebar or x1 < 0 or y1 >= tinggi or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        layar.fill(warna_putih)
        pygame.draw.rect(layar, warna_merah, [foodx, foody, ukuran_block, ukuran_block])
        ular_kepala = []
        ular_kepala.append(x1)
        ular_kepala.append(y1)
        ular_List.append(ular_kepala)
        if len(ular_List) > panjang_ular:
            del ular_List[0]

        for x in ular_List[:-1]:
            if x == ular_kepala:
                game_close = True

        ular(ukuran_block, ular_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, lebar - ukuran_block) / 10.0) * 10.0
            foody = round(random.randrange(0, tinggi - ukuran_block) / 10.0) * 10.0
            panjang_ular += 1

        clock.tick(kecepatan)

    pygame.quit()
    quit()


gameLoop()

import pygame, sys  # mengimport modul pygame dan sys
from pygame import rect  # Mengimport rect
from pygame.locals import *  # Mengimpor file local pygame
import time  # Mengimport waktu

WIDTH, HEIGHT = 600, 480  # mengatur Resolusi untuk Window
pygame.display.set_caption('Smooth Movement')  # memberi judul pada window

pygame.init()  # menginisialisasi setiap submodules di pygame
win = pygame.display.set_mode((WIDTH, HEIGHT))  # mengatur ukuran lebar dan tinggi dari window
clock = pygame.time.Clock()  # membantu melacak waktu

#mengetur warna(kecerahannya)
BLACK = (10, 10, 10)
WHITE = (255, 255, 255)
RED = (199, 90, 55)
GREEN = (190, 255, 110)
BLUE = (0, 0, 255)


# membuat class player

class Player:
    def __init__(self, x, y):  # membuat fungsi constructor dengan memasukan objek self dan parameter x,y
        self.x = int(x)  # memberikan tipe data variabel integer x
        self.y = int(y)  # memberikan tipe data variabel integer y
        self.rect = pygame.Rect(self.x, self.y, 32, 32)  # membuat attribut kotak dengan ukuran 32 x 32
        self.color = (250, 120, 60)  # memberikan warna
        self.velX = 0  # menentukan kecepatan awal x bernilai 0
        self.velY = 0  # menentukan kecepatan awal y bernilai 0
        self.left_pressed = False  # ketika ditekan tombol kiri posisinya awal/default adalah false
        self.right_pressed = False  # ketika ditekan tombol kanan posisinya awal/default adalah false
        self.up_pressed = False  # ketika ditekan tombol atas posisinya awal/default adalah false
        self.down_pressed = False  # ketika ditekan tombol bawah posisinya awal/default adalah false
        self.speed = 4  #kecepatan objek

    def draw(self,
             win):  # berfungsi untuk menggambar objek
        pygame.draw.rect(win, self.color, self.rect)

    def update(
            self):  # fungsi update dari objek self, agar bisa bergerak setiap kita tekan tombol dimana pergerakannya sesuai dengan koordinat dan kecepatan yang telah kita tentukan sebelumnya
        self.velX = 0 # merupakan nilai velocity x
        self.velY = 0 # merupakan nilai velocity y
        if self.left_pressed and not self.right_pressed and self.x > 0 : #berfungsi untuk jika tombol kiri dipencet 
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed and self.x < 570 : # self.x < 570 digunakan untuk membatasi pergerakan objek agar tidak keluar dari batas
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed and self.y > 0 :
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed and self.y < 450 :
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)


player = Player(WIDTH / 2, HEIGHT / 2)

# digunakan untuk membuat kalimat nama yaitu nama saya sendiri
font_color = (WHITE)
font_obj = pygame.font.Font("C:\Windows\Fonts\RAVIE.TTF", 25)
text = "Farhanang Wahyu Aprian"
img = font_obj.render(text, True, (BLACK))

rect = img.get_rect()
rect.topleft = (20, 20)
cursor = Rect(rect.topright, (3, rect.height))

while True:  # akan menjalankan jika perulangannya True

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # jika melakukan close maka akan keluar
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # JIka keypad dipencet maka
            if event.key == pygame.K_LEFT: # menjalankan pergerakan ke kiri
                player.left_pressed = True 
            if event.key == pygame.K_RIGHT: # menjalankan pergerakan kekanan
                player.right_pressed = True
            if event.key == pygame.K_UP: # menjalankan pergerakan keatas
                player.up_pressed = True
            if event.key == pygame.K_DOWN: # menjalankan pergerakan kebawah
                player.down_pressed = True
        if event.type == pygame.KEYUP: #jika keypad dilepas maka
            if event.key == pygame.K_LEFT: #pergerakan ke kiri dihentikan
                player.left_pressed = False
            if event.key == pygame.K_RIGHT: #pergerakan ke kanan dihentikan
                player.right_pressed = False
            if event.key == pygame.K_UP: #pergerakan keatas dihentikan
                player.up_pressed = False
            if event.key == pygame.K_DOWN: # pergerakan kebawah dihentikan
                player.down_pressed = False

            if event.type == QUIT: #jika pengguna melakukan klik pada tanda x akan berhenti
                running = False

            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(text) > 0:
                        text = text[:-1]

                else:
                    text += event.unicode
                    img = font_obj.render(text, True, PINK)
                    rect.size = img.get_size()
                    cursor.topleft = rect.topright

    # memberikan warna pada backgroud
    win.fill((BLUE))
    pygame.draw.rect(win, (RED), player)

    win.blit(img, rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(win, BLUE, cursor)
    pygame.display.update()

    player.update()
    pygame.display.flip()

    clock.tick(60)  # memberi batasan frame sehingga program tidak akan pernah berjalan lebih dari 120 frame per detik.
    pygame.display.update()

pygame.quit()
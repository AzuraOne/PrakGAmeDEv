import random
import pygame
import sys
from pygame.math import Vector2
#import modul

class Snake:
    def __init__(self):
        super().__init__()
        #membuat reset posisi snake
        self.Reset()
        # menambahkan tubuh
        self.add_body_tail = False
        # gerakan
        self.move = Vector2(1, 0)

        # menambahkan head area
        self.head_up = pygame.image.load(
            'Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load(
            'Graphics/head_down.png').convert_alpha()
        self.head_left = pygame.image.load(
            'Graphics/head_left.png').convert_alpha()
        self.head_right = pygame.image.load(
            'Graphics/head_right.png').convert_alpha()

        # tmenambahkan asset tail area
        self.tail_up = pygame.image.load(
            'Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load(
            'Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load(
            'Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load(
            'Graphics/tail_left.png').convert_alpha()

        # menambahkan body 
        self.body_vertical = pygame.image.load(
            'Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(
            'Graphics/body_horizontal.png').convert_alpha()

        # menambahkan perbelokan
        self.body_tr = pygame.image.load(
            'Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load(
            'Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load(
            'Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load(
            'Graphics/body_bl.png').convert_alpha()
        
        #menambahkan suara
        self.sound_game = pygame.mixer.Sound('Sound/eat1.wav')

    def movement(self):
        # untuk menjaga agar ekor tidak selalu memanjang
        if self.add_body_tail == True:
            self.copy_body = self.body[:]
            self.copy_body.insert(0, self.copy_body[0] + self.move)
            self.body = self.copy_body[:]
            self.add_body_tail = False
            self.sound()
        else:
            #untuk ular dapat berjalan seperti biasa
            self.copy_body = self.body[:-1]
            self.copy_body.insert(0, self.copy_body[0] + self.move)
            self.body = self.copy_body[:]

    def draw_snake(self):
        #menaggambar ular dari kepala hingga ekor
        self.update_head()
        self.update_tail()

        #menambil index pada body snake dan juga blocknya
        for index, block in enumerate(self.body):
            self.pos_x = block.x * cell_size
            self.pos_y = block.y * cell_size
            rect_snake = pygame.Rect(
                self.pos_x, self.pos_y, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, rect_snake)
               
            elif index == len(self.body)-1:
          
                screen.blit(self.tail, rect_snake)
            else:
                #untuk mendeklarasikan block sebelumnya ini berfungsi untuk mengetahui posisi ular apakah horizontal atau vertikal
                previous_block = self.body[index + 1] - block
              

                next_block = self.body[index - 1] - block
                
                if previous_block.x == next_block.x:
                    #berfungsi untuk menggambar badan secara vertikal
                    screen.blit(self.body_vertical, rect_snake)
                elif previous_block.y == next_block.y:
                   #berfungsi untuk menggambar badan pada ular secara horizontal
                    screen.blit(self.body_horizontal, rect_snake)
                else:
                    #berfungsi untuk membuat gambar ke layar ketika ular berbelok
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, rect_snake)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, rect_snake)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, rect_snake)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, rect_snake)


    def update_head(self):
        # melakukan perhintungan antara kepala dan badan sebelum kepala
        head_update = self.body[1] - self.body[0]
        #jika terdapat kondisi dibawah maka bisa dipastikan bahwa kepala menghadap kemana
        if head_update == Vector2(0,-1):
            self.head = self.head_down
        elif head_update == Vector2(0, 1): self.head = self.head_up
        elif head_update == Vector2(1,0):
            self.head = self.head_left
        elif head_update == Vector2(-1, 0): self.head = self.head_right

    def update_tail(self):
        # fungsi untuk mengetahui hadap mana ekor ular
        tail_update = self.body[-2] - self.body[-1]
        if tail_update == Vector2(0,-1):
            self.tail = self.tail_down
        elif tail_update == Vector2(0, 1): self.tail = self.tail_up
        elif tail_update == Vector2(1,0):
            self.tail= self.tail_left
        elif tail_update == Vector2(-1, 0): self.tail = self.tail_right


    def Reset(self):
        #kondisi awal ketika memulai permainan
        self.body = [Vector2(5, 10), Vector2(4,10), Vector2(3,10)]

    def add_tail(self):
        #berfungsi untuk menambahkan ekor jika kondisi True
        self.add_body_tail = True
    def sound(self):
        # berfungsi untuk menjalankan suara ketika ular memakan sesuatu
        self.sound_game.play()

class Makanan:
    def __init__(self):
        #melakukan deklarasi apa saja yang dilakukan pertama kali ketika class makanan dijalankan
        super().__init__()
        self.pos_a = []
        #memanggil gambar
        self.image = pygame.image.load('Graphics/hdbi.png').convert_alpha()
        #memanggil fungsi Random untuk mengacak lokasi makanan
        self.RandomDraw()


    def draw_fruit(self):
        #berfungsi untuk membuat perulangan sesaui koordinat yang di random
        for x in range(len(self.pos_a)-1):
            fruit_rect =  pygame.Rect(int(self.pos_a[x].x * cell_size), int(self.pos_a[x].y * cell_size),cell_size,cell_size)
            screen.blit(self.image, fruit_rect)
        

    def RandomDraw(self):
        #fungsi yang berfungsi untuk merandom sebanyak apa makanan akan ditampilkan
        for x in range(20):
            self.pos_x = random.randint(0, cell_number - 1)
            self.pos_y = random.randint(0, cell_number - 1)
            self.pos = Vector2(self.pos_x, self.pos_y)
            self.pos_a.append(self.pos)

class Musuh:
    def __init__(self):
        # Seperti snake tadi sama  hanya berbedaa koordinat
        super().__init__()
        self.Reset()
        self.add_body_tail = False
        self.move = Vector2(1, 0)

        # head Area
        self.head_up = pygame.image.load(
            'Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load(
            'Graphics/head_down.png').convert_alpha()
        self.head_left = pygame.image.load(
            'Graphics/head_left.png').convert_alpha()
        self.head_right = pygame.image.load(
            'Graphics/head_right.png').convert_alpha()

        # tail Area
        self.tail_up = pygame.image.load(
            'Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load(
            'Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load(
            'Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load(
            'Graphics/tail_left.png').convert_alpha()

        # body Area
        self.body_vertical = pygame.image.load(
            'Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(
            'Graphics/body_horizontal.png').convert_alpha()

        # body turn right
        self.body_tr = pygame.image.load(
            'Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load(
            'Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load(
            'Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load(
            'Graphics/body_bl.png').convert_alpha()

    def movement(self):
        if self.add_body_tail == True:
            self.copy_body = self.body[:]
            self.copy_body.insert(0, self.copy_body[0] + self.move)
            self.body = self.copy_body[:]
            self.add_body_tail = False
        else:
            self.copy_body = self.body[:-1]
            self.copy_body.insert(0, self.copy_body[0] + self.move)
            self.body = self.copy_body[:]
        # 1,0 arah ke kanan, -1,0 arah ke kiri , 0,1 arah kebawah, 0,-1 arah keatas
        make_move = [Vector2(1,0), Vector2(0,1), Vector2(-1,0), Vector2(0,-1)]
        index = random.randrange(0,3)
        self.move = make_move[index]
        # Fungsi perandom yang mana akan melakukan pergerakan pada ular lain secara acak
     

    def draw_snake(self):
        # fungsi menggambar ular sama seperti class snake
        self.update_head()
        self.update_tail()

        for index, block in enumerate(self.body):
            self.pos_x = block.x * cell_size
            self.pos_y = block.y * cell_size
            rect_snake = pygame.Rect(
                self.pos_x, self.pos_y, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, rect_snake)
               
            elif index == len(self.body)-1:
          
                screen.blit(self.tail, rect_snake)
            else:
                previous_block = self.body[index + 1] - block
              

                next_block = self.body[index - 1] - block
                
                if previous_block.x == next_block.x:
               
                    screen.blit(self.body_vertical, rect_snake)
                elif previous_block.y == next_block.y:
                   
                    screen.blit(self.body_horizontal, rect_snake)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, rect_snake)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, rect_snake)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, rect_snake)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, rect_snake)


    def update_head(self):
        head_update = self.body[1] - self.body[0]
        if head_update == Vector2(0,-1):
            self.head = self.head_down
        elif head_update == Vector2(0, 1): self.head = self.head_up
        elif head_update == Vector2(1,0):
            self.head = self.head_left
        elif head_update == Vector2(-1, 0): self.head = self.head_right

    def update_tail(self):
        tail_update = self.body[-2] - self.body[-1]
        if tail_update == Vector2(0,-1):
            self.tail = self.tail_down
        elif tail_update == Vector2(0, 1): self.tail = self.tail_up
        elif tail_update == Vector2(1,0):
            self.tail= self.tail_left
        elif tail_update == Vector2(-1, 0): self.tail = self.tail_right


    def Reset(self):
        self.body = [Vector2(6, 11), Vector2(5,11), Vector2(4,11), Vector2(3, 11), Vector2(2,11)]

    def add_tail(self):
        self.add_body_tail = True

class Obstacle:
    #berfungsi untuk penghalang yang mengakibatkan snake dapat kalah
    def __init__(self, x, y):
        super().__init__()
        self.pos_x = x
        self.pos_y = y
        self.pos = Vector2(self.pos_x,self.pos_y)
        


    def draw_obstacle(self):
        #menggambar obstacle
            obstacle_rect =  pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size),cell_size ,cell_size )
            pygame.draw.rect(screen, (0,0,0),obstacle_rect)
        
# Senjata
class Senjata:
    # menginisialisasi senjata
    def __init__(self) :
        self.pos_x = random.randint(0, cell_number - 1)
        self.pos_y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.pos_x, self.pos_y)
        self.pos_status = False

    #fungsi movement senjata agar dapat mengikuti player
    def movement(self):
        if self.pos_status == True:
            self.pos = self.pos_move
        
 
            
        else:
            self.pos = self.pos
    # menggambar senjata
    def draw_senjata(self):
        
        if self.pos_status == True:
            self.senjata_rect = pygame.Rect(int(self.pos_move.x * cell_size ), int(self.pos_move.y * cell_size),cell_size,cell_size)
            self.senjata = pygame.draw.rect(screen, (255,123,120),self.senjata_rect)

        
        else:
            self.senjata_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size),cell_size,cell_size)
            self.senjata = pygame.draw.rect(screen, (255,123,120),self.senjata_rect)
    # Mengubah Pos secara real time
    def update_pos(self, move):
        self.pos_move = move
        self.pos_status = True
        

        
        

class main:
    def __init__(self):
        #Menginisialisasi objek objek yang terlibat seperti snake, makanan dan senjata serta musuhnya
        self.snake = Snake()
        self.makanan = Makanan()
        
        self.senjata = Senjata()
        self.status = []
        self.opponen = Musuh()
        self.opponen1 = Musuh()


        self.obstacle1 = Obstacle(4,5)
        self.obstacle2 = Obstacle(6,7)
        #melakukan update pada movement
    def update(self):
        self.snake.movement()
        self.opponen.movement()
        self.opponen1.movement()
        self.senjata.movement()

        #melakukan update pada collision yang akan dijalankan ketika if else terpenuhi
        self.collision()
        # berfungsi untuk mengetahui posisi ular apakah melebihi garis layar atau bukan
        self.check_snake_position()
        # melakukan update pergerakan pada gerakan
        self.update_move()
    def draw(self):
        # melakukan draw / penggambaran pada objek yang telah dinisialisasi
        self.makanan.draw_fruit()
        self.snake.draw_snake()
        self.opponen.draw_snake()
        self.opponen1.draw_snake()
        self.senjata.draw_senjata()
        #membuat untuk menampilkan score
        self.Score()

        #membuat obstacle
        self.obstacle1.draw_obstacle()
        self.obstacle2.draw_obstacle()
    
    #berfungsi untuk mendeteksi adanya collision / tubrukan
    def collision(self):
        for x in range(len(self.makanan.pos_a)-1):
            if self.makanan.pos_a[x] == self.snake.body[0]:
                self.refresh(x)
                self.snake.add_tail()
                if len(self.makanan.pos_a) <= 5:
                    self.makanan.RandomDraw()
        if self.senjata.pos == self.snake.body[0]:
            self.status = 1

        for x in range(len(self.opponen.body)):
            if self.opponen.body[x] == self.snake.body[0]:
                
                self.GameOver()
                
        for x in range(len(self.opponen1.body)):
            if self.opponen1.body[x] == self.snake.body[0]:
                
                self.GameOver()
                
        
        if self.snake.body[0] == self.obstacle1.pos:
            self.GameOver()
        if self.snake.body[0] == self.obstacle2.pos:
            self.GameOver()
                
    # melakukan update move
    def update_move(self):
        
        if self.status == 1:
            new_move = self.snake.body[0]
            self.senjata.update_pos(new_move)
            

    # refresh pada makanan snake
    def refresh(self, index):
        
        self.old = self.makanan.pos_a
        self.old.pop(index)
        self.makanan.pos_a = self.old
        
        
    # melakukan snake posisi
    def check_snake_position(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.GameOver()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.GameOver()
        
       

    # fungsi yang dipanggil ketika game over / player kalah
    def GameOver(self):
        pygame.quit()
        sys.exit()
    # fungsi untuk menampilkan score
    def Score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * 2)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        
        container_score = pygame.Rect(score_rect.x - 5,score_rect.y - 5, cell_size *2,cell_size *2)
        container = pygame.draw.rect(screen, (173,216,230),container_score)
        screen.blit(score_surface,score_rect)

# berfungsi untuk konfigurasi suara agar tidak delay
pygame.mixer.pre_init(44100,-16,2,512)
# inisialiasi pygame
pygame.init()
# initiate Clock untuk mengatur fps
clock = pygame.time.Clock()
# judul game
pygame.display.set_caption("Kluwer.com")
# font
font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)
# initiate Window
cell_size, cell_number = 30, 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))

start_game = main()

bg = pygame.image.load('Background/20211006_151420_0000.png').convert_alpha()
bg_big = pygame.transform.scale(bg, (600, 600))
# initiate Screen Refresh yang akan mempengaruhi pergerakan ular
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 90)
# parameter 1 untuk memanggil Screenupdate yang kedua adalah kecepetanan screenupdate

#melakukan looping
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # berfungsi untuk SCREEN_UPDATE jika terpenuhi maka akan menjalankan method update pada game
        if event.type == SCREEN_UPDATE:
            start_game.update()
            # menekan  akan melakukan pergerakan pada ular
        if event.type == pygame.KEYDOWN:
            #tombol atas dipencet akan bereaksi jika ular tidak berbalik arah
            if event.key == pygame.K_UP:
                if start_game.snake.move.y != 1:
                    start_game.snake.move = Vector2(0, -1) 
                #sama seperti diatas yaitu akan berjalan jika ular tidak berbalik arah
            if event.key == pygame.K_DOWN:
                if start_game.snake.move.y != -1:
                    start_game.snake.move = Vector2(0, 1)                
            if event.key == pygame.K_RIGHT:
                # ketika user menekan arah kanan maka akan membelokkan ular kekanan
                if start_game.snake.move.x != -1:
                    start_game.snake.move = Vector2(1, 0)      
                # berfungsi untuk membelokkan ular ke kiri   
            if event.key == pygame.K_LEFT:
                if start_game.snake.move.x != 1:
                    start_game.snake.move = Vector2(-1, 0)

    # menampilkan bg yang berukuran besar karena telah diubah ukuran
    screen.blit(bg_big, (0,0))
    #menampilkan draw() pada start_game
    start_game.draw()
    #melakukan refresh pada display 

    pygame.display.flip()
    # 60 Fps
    clock.tick(60)

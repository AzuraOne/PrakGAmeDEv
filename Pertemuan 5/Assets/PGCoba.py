#Part A Awal
import pygame, sys, random

# Pada class Block dibawah terdapat fungsi init
class Block(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
#part A Akhir

#Part E Awal
# Pada class Player dibawah terdapat fungsi init, update, screen constraint
class Player(Block):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__(path, x_pos, y_pos)
        self.speed = speed
        self.movement = 0

    def screen_constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

    def update(self, ball_group):
        self.rect.y += self.movement
        self.screen_constrain()
#part E Part E

#Awal Part C
# Pada class Ball dibawah terdapat fungsi init, update, collisions, restart counter, reset ball
class Ball(Block):
    def __init__(self, path, x_pos, y_pos, speed_x, speed_y, paddles):
        super().__init__(path, x_pos, y_pos)
        self.speed_x = speed_x * random.choice((-1, 1))
        self.speed_y = speed_y * random.choice((-1, 1))
        self.paddles = paddles
        self.active = False
        self.score_time = 0

    def update(self):
        if self.active:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.collisions()
        else:
            self.restart_counter()
#Akhir Part C

#Awal Part G
    def collisions(self):
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            pygame.mixer.Sound.play(plob_sound)
            self.speed_y *= -1

        if pygame.sprite.spritecollide(self, self.paddles, False):
            pygame.mixer.Sound.play(plob_sound)
            collision_paddle = pygame.sprite.spritecollide(self, self.paddles, False)[0].rect
            if abs(self.rect.right - collision_paddle.left) < 10 and self.speed_x > 0:
                self.speed_x *= -1
            if abs(self.rect.left - collision_paddle.right) < 10 and self.speed_x < 0:
                self.speed_x *= -1
            if abs(self.rect.top - collision_paddle.bottom) < 10 and self.speed_y < 0:
                self.rect.top = collision_paddle.bottom
                self.speed_y *= -1
            if abs(self.rect.bottom - collision_paddle.top) < 10 and self.speed_y > 0:
                self.rect.bottom = collision_paddle.top
                self.speed_y *= -1
#Akhir part G

#Awal part B
    def reset_ball(self):
        self.active = False
        self.speed_x *= random.choice((-1, 1))
        self.speed_y *= random.choice((-1, 1))
        self.score_time = pygame.time.get_ticks()
        self.rect.center = (screen_width / 2, screen_height / 2)
        pygame.mixer.Sound.play(score_sound)
#Akhir Part B

#Awal part M
    def restart_counter(self):
        current_time = pygame.time.get_ticks()
        countdown_number = 3

        if current_time - self.score_time <= 700:
            countdown_number = 3
        if 700 < current_time - self.score_time <= 1400:
            countdown_number = 2
        if 1400 < current_time - self.score_time <= 2100:
            countdown_number = 1
        if current_time - self.score_time >= 2100:
            self.active = True


        time_counter = basic_font.render(str(countdown_number), True, accent_color)
        time_counter_rect = time_counter.get_rect(center=(screen_width / 2, screen_height / 2 + 50))
        pygame.draw.rect(screen, bg_color, time_counter_rect)
#Akhir part M

#Awal part I
# Pada class Opponent dibawah terdapat fungsi init, update, constraint
class Opponent(Block):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__(path, x_pos, y_pos)
        self.speed = speed

    def update(self, ball_group):
        if self.rect.top < ball_group.sprite.rect.y:
            self.rect.y += self.speed
        if self.rect.bottom > ball_group.sprite.rect.y:
            self.rect.y -= self.speed
        self.constrain()

    def constrain(self):
        if self.rect.top <= 0: self.rect.top = 0
        if self.rect.bottom >= screen_height: self.rect.bottom = screen_height
#Akhir part I

#Awal Part H
# Pada class Game Manager dibawah terdapat fungsi init, run game, reset ball, draw score
class GameManager:
    def __init__(self, ball_group, paddle_group):
        self.player_score = 0
        self.opponent_score = 0
        self.ball_group = ball_group
        self.paddle_group = paddle_group

    def run_game(self):
        # menggambar objek game
        self.paddle_group.draw(screen)
        self.ball_group.draw(screen)

        # mengupdate objek game
        self.paddle_group.update(self.ball_group)
        self.ball_group.update()
        self.reset_ball()
        self.draw_score()
#Akhir Part  H

#Awal Part J
    def reset_ball(self):
        if self.ball_group.sprite.rect.right >= screen_width:
            self.opponent_score += 1
            self.ball_group.sprite.reset_ball()
        if self.ball_group.sprite.rect.left <= 0:
            self.player_score += 1
            self.ball_group.sprite.reset_ball()

    def draw_score(self):
        player_score = basic_font.render(str(self.player_score), True, accent_color)
        opponent_score = basic_font.render(str(self.opponent_score), True, accent_color)

        player_score_rect = player_score.get_rect(midleft=(screen_width / 2 + 40, screen_height / 2))
        opponent_score_rect = opponent_score.get_rect(midright=(screen_width / 2 - 40, screen_height / 2))

        screen.blit(player_score, player_score_rect)
        screen.blit(opponent_score, opponent_score_rect)
#Akhir part J

#Awal part D
# clock
pygame.mixer.pre_init(44100, -16, 2, 512) # mengset format audio yang digunakan
pygame.init() # memulai pygame untuk dapat dieksekusi
clock = pygame.time.Clock() # menset fps

screen_width = 720 # Menset lebar layar
screen_height = 480 # Menset panjang layar
screen = pygame.display.set_mode((screen_width, screen_height)) # Menset ukuran layar
pygame.display.set_caption('Pong') # Menset title layar

# Mengatur Tampilan dan suara Game
bg_color = pygame.Color('#2F373F')  # mengatur background layar
accent_color = (27, 35, 43) #s
basic_font = pygame.font.Font('freesansbold.ttf', 32) # jenis font yang digunakan pada font
plob_sound = pygame.mixer.Sound("pong.ogg") # menset bola ketika bergerak
score_sound = pygame.mixer.Sound("score.ogg") #menset suara bola ketika mendapatkan score
middle_strip = pygame.Rect(screen_width / 2 - 2, 0, 4, screen_height) # mengatur net
#Akhir part D

#Awal part F
# Objek Game
player = Player('Paddle.png', screen_width - 20, screen_height / 2, 5) # mengatur Objek player pada game
opponent = Opponent('Paddle.png', 20, screen_width / 2, 5) # mengatur objek opponen pada game
paddle_group = pygame.sprite.Group() # Mengatur AI
paddle_group.add(player) 
paddle_group.add(opponent)

ball = Ball('Ball.png', screen_width / 2, screen_height / 2, 4, 4, paddle_group) #mengatur bola
ball_sprite = pygame.sprite.GroupSingle()
ball_sprite.add(ball)

game_manager = GameManager(ball_sprite, paddle_group)
#Akhir part F

#AAwal part L
while True:
    for event in pygame.event.get(): # melakukan looping pada kotak
        if event.type == pygame.QUIT: # jika disilang akan close
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: #jika salah satu tombol dipencet
            if event.key == pygame.K_UP: #jika dijalankan atas maka player ke atas
                player.movement -= player.speed
            if event.key == pygame.K_DOWN: # jika dijalankan kebawah maka player kebawah
                player.movement += player.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.movement += player.speed
            if event.key == pygame.K_DOWN:
                player.movement -= player.speed
#Akhir part L

#Awal part K
    # background
    screen.fill(bg_color) #menset background color
    pygame.draw.rect(screen, accent_color, middle_strip)

    # Untuk run game
    game_manager.run_game()

    # Render game
    pygame.display.flip()
    clock.tick(120) #mengatur FPS
#Akhir part K
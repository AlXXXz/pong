import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 300

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 153)

PlayerWidth = 20
PlayerHeight = 60

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

PlayerScore = 0
Player2Score = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PlayerWidth, PlayerHeight))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 6, HEIGHT / 2)
        self.speedy = 0
        self.score = 0

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy = -2
        if keystate[pygame.K_s]:
            self.speedy = 2
        if self.rect.y > 0 or self.rect.y < (HEIGHT - 60):
            self.rect.y += self.speedy
        

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PlayerWidth, PlayerHeight))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - (WIDTH / 6), HEIGHT / 2)
        self.speedy = 0
        self.score = 0

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -2
        if keystate[pygame.K_DOWN]:
            self.speedy = 2
        if self.rect.y > 0 or self.rect.y < (HEIGHT - 60):
            self.rect.y += self.speedy

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.xFac = 1
        self.yFac = 1

    def update(self):
        self.speedx = 1
        self.speedy = 1
        # self.speedy = 5
        self.rect.x += self.speedx * self.xFac
        self.rect.y += self.speedy * self.yFac
        # if self.rect.x >= WIDTH or self.rect.x <= 0:
        #     self.xFac *= -1
        if self.rect.y >= HEIGHT or self.rect.y <= 0:
            self.yFac *= -1


all_sprites = pygame.sprite.Group()
player = Player()
player2 = Player2()
ball = Ball()
all_sprites.add(player)
all_sprites.add(player2)
all_sprites.add(ball)

# def resetBall():
#     ball.rect.center = (WIDTH / 2, HEIGHT / 2)

def resetBallPlayer():
    ball.rect.center = (player.rect.x + 30, player.rect.y + (PlayerHeight / 2)) #((WIDTH / 6) + 20, HEIGHT / 2)
    player.score += 1

def resetBallPlayer2():
    ball.rect.center = (player2.rect.x - 30, player2.rect.y + (PlayerHeight / 2))
    player2.score += 1
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.speedx = -8
            if event.key == pygame.K_DOWN:
                player.speedx = 8

    # Обновление
    all_sprites.update()
    

    if ball.rect.x == player.rect.x + PlayerWidth and (ball.rect.y >= player.rect.y - 50 and ball.rect.y <= player.rect.y + 50):
        ball.xFac *= -1
    if ball.rect.x >= player2.rect.x - PlayerWidth and (ball.rect.y >= player2.rect.y - 50 and ball.rect.y <= player2.rect.y + 50):
        ball.xFac *= -1

    if ball.rect.x >= WIDTH:
        resetBallPlayer()
    if ball.rect.x <= 0:
        resetBallPlayer2()

    print(player.score, ":", player2.score)

    #print("ball X Y", ball.rect.x, ball.rect.y, "Pos X Y:", player2.rect.x, player2.rect.y, "top:", player2.rect.y, "mid:", player2.rect.y + (PlayerHeight / 3), "bottom", player2.rect.y + (2 * (PlayerHeight / 3)))


    # Рендеринг
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT), 7)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()

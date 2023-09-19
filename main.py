import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 153)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 6, HEIGHT / 2)
        self.speedy = 0

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy = -8
        if keystate[pygame.K_s]:
            self.speedy = 8
        if self.rect.y > 0 or self.rect.y < (HEIGHT - 60):
            self.rect.y += self.speedy

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - (WIDTH / 6), HEIGHT / 2)
        self.speedy = 0

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
        if self.rect.y > 0 or self.rect.y < (HEIGHT - 60):
            self.rect.y += self.speedy
        #print(self.rect.y)

# class Ball(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((15, 15))
#         self.image.fill(RED)
#         self.rect = self.image.get_rect()
#         self.rect.center = (WIDTH / 2, HEIGHT / 2)
#     def update(self):
#         self.rect.x += 5
#         print(self.rect.x)
#         if self.rect.left >= WIDTH:
#             self.rect.x *= -1

class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1

    def display(self):
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)
 
    def update(self):
        self.posx += self.speed*self.xFac
        self.posy += self.speed*self.yFac
 
        # If the ball hits the top or bottom surfaces,
        # then the sign of yFac is changed and it
        # results in a reflection
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1
 
        # If the ball touches the left wall for the first time,
        # The firstTime is set to 0 and we return 1
        # indicating that Geek2 has scored
        # firstTime is set to 0 so that the condition is
        # met only once and we can avoid giving multiple
        # points to the player
        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= WIDTH and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0
 
    # Used to reset the position of the ball
    # to the center of the screen
    def reset(self):
        self.posx = WIDTH /2
        self.posy = HEIGHT /2
        self.xFac *= -1
        self.firstTime = 1
 
    # Used to reflect the ball along the X-axis
    def hit(self):
        self.xFac *= -1
 
    def getRect(self):
        return self.ball

all_sprites = pygame.sprite.Group()
player = Player()
player2 = Player2()
# ball = Ball()
all_sprites.add(player)
all_sprites.add(player2)
ball = Ball(WIDTH / 2, HEIGHT / 2, 7, 7, RED)
# all_sprites.add(ball)

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
    
    
    # Рендеринг
    screen.fill(BLACK)
    point = ball.update()
    if point:  
        ball.reset()
    ball.display()
    pygame.draw.line(screen, WHITE, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT), 7)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
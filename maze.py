from pygame import *
from PyQt5 import Qt


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed


class wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_width,wall_height,wall_x,wall_y):   
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width,self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


background = transform.scale(image.load('newbackground.jpg'),(700,500))


clock= time.Clock()
FPS = 60

ball = GameSprite('ball.png',350,250,5)
wallie1 = pygame.Surface(0,255,0,30,250,430,200)
wallie2 = wall(0,255,0,30,250,100,100)
window = display.set_mode((700,500))
display.set_caption('Лабиринт')
game = True
finish = False

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        ball.reset()
        window.blit(wallie1,(0,0))



    clock.tick(FPS)
    display.update()


from pygame import *
from PyQt5 import Qt

speed_x = 5
speed_y = 5

speed_x2 = 5
speed_y = 5

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(30,200))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class GameSprite2(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player2(GameSprite):
    def update2(self):
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 300:
            self.rect.y += self.speed


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




ball = GameSprite2('ball.png',350,250,5)

ball2 = GameSprite('ball.png',250,250,5)

wallie1 = Player('kitty.jpg',0,0,20)

wallie2 = Player2('kitty.jpg',670,300,20)

window = display.set_mode((700,500))

display.set_caption('пингпонг')

game = True

finish = False

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        ball.reset() 
        
        wallie1.update()
        wallie1.reset()
        wallie2.update2()
        wallie2.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        ball2.rect.x += speed_x
        ball2.rect.y += speed_y

        if sprite.collide_rect(ball,wallie1):
            speed_x *= -1.1

        if sprite.collide_rect(ball,wallie2):
            speed_x *= -1.1

        if ball.rect.y > 425:
            speed_y *= -1

        if ball.rect.y < 0 :
            speed_y *= -1
        if ball.rect.y > 600:
            window.blit(font1,(0,0))        
        

    clock.tick(FPS)
    display.update()


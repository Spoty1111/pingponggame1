from pygame import *
from PyQt5 import Qt

speed_x = 3
speed_y = 3

speed_x2 = 3
speed_y2 = 3


score = 0
score2 = 0

#####################################################классы###########################################################################

class GameSprite3(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def reset2(self):
        window.blit(self.image,(250,250))

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(20,200))
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
    def reset2(self):
        window.blit(self.image,(350,250))

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




background = transform.scale(image.load('newbackground.jpg'),(700,500))




################################обьекты классов,переменные(также на первых строчках)############################################################################

clock= time.Clock()
FPS = 60

ball = GameSprite3('ball.png',350,250,5)

ball2 = GameSprite2('ball.png',250,250,5)

wallie1 = Player('kitty.jpg',0,0,20)

wallie2 = Player2('kitty.jpg',670,300,20)

window = display.set_mode((700,500))

font.init()
font = font.SysFont('Arial',80)


display.set_caption('пингпонг')

game = True

finish = False
##################################################игровой цикл,отрисовка объектов###############################################################
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        ball2.reset()
        ball.reset() 
        
        wallie1.update()
        wallie1.reset()
        wallie2.update2()
        wallie2.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        ball2.rect.x -= speed_x2
        ball2.rect.y -= speed_y2

        text = font.render('счет:'+ str(score),1,(255,255,255))
        window.blit(text,(10,20))

        text2 = font.render('счет:'+ str(score2),1,(255,255,255))
        window.blit(text2,(450,20))

############################################столкновения#############################################################################################
        if sprite.collide_rect(ball,wallie1):
            speed_x *= -1.1

        if sprite.collide_rect(ball,wallie2):
            speed_x *= -1.1

        if sprite.collide_rect(ball2,ball):
            speed_x *= -1.1
            speed_x2 *= -1.1

        if sprite.collide_rect(ball2,wallie1):
            speed_x2 *= -1.1

        if sprite.collide_rect(ball2,wallie2):
            speed_x2 *= -1.1
#################################################края############################################################################################
        if ball.rect.y > 425:
            speed_y *= -1

        if ball.rect.y < 0 :
            speed_y *= -1
        

        if ball2.rect.y > 425:
            speed_y2 *= -1

        if ball2.rect.y < 0 :
            speed_y2 *= -1

########################################подсчет##############################################################################
        if ball.rect.x == 650:
            score += 1
            ball.reset2()
        

        if ball2.rect.x == 650:
            score2 += 1
            ball2.reset2()

        if ball.rect.x == -65:
            score += 1
            ball.reset2()
            
        if ball2.rect.x == -65:
            score2 += 1
            ball2.reset2()
      
        

    clock.tick(FPS)
    display.update()


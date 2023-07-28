from pygame import *
mixer.init()
mixer.music.load('C418 - Moog City 2.mp3')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.SysFont('Arial', 70)
win = font.render ('YOU WIN!', True,(255, 200, 0))
lose = font.render ('YOU Lose', True,(255, 0, 0))


class Gamesprite(sprite.Sprite):
    def __init__(self, play_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(play_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_d] and self.rect.x < win_width-80:
            self.rect.x += self.speed 

        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed 

        if keys[K_s] and self.rect.y < win_height-80:
            self.rect.y += self.speed

class Enemy(Gamesprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 450:
            self.direction = 'right'
        if self.rect.x >= win_width-80:
            self.direction  = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed    


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_wigth, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_wigth
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((203, 171, 39))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


win_width = 700
win_height = 500


window = display.set_mode((win_width, win_height))
display.set_caption('Лабиринт')
bg = transform.scale(image.load('1.jpg'), (1920, 1080))


player = Player('hero.png', 5, win_height-80, 4)
enemy = Enemy('cyborg.png', win_width-80, 200, 2)
treasure = Gamesprite('4.png', win_width - 120, win_height - 80, 0)

w1 = Wall(50, 52, 7, 100, 20, 450, 10)
w2 = Wall(250, 252, 107, 100, 480, 350, 10)
w3 = Wall(250, 252, 107, 100, 20, 10, 380)
w4 = Wall(250, 252, 107, 210, 190, 10, 300)
w5 = Wall(250, 252, 107, 310, 20, 10, 380)
w6 = Wall(250, 252, 107, 300, 480, 350, 10)
w7 = Wall(250, 252, 107, 300, 20, 450, 10)
w8 = Wall(250, 252, 107, 440, 190, 10, 300)





clock = time.Clock()


game = True
finish = False




while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(bg, (0,0))
        player.update()
        enemy.update()
        player.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        enemy.reset()
        treasure.reset()
        display.update()
        clock.tick(60)  

        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or \
            sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4):
            finish = True
            window.blit(lose, (200,200))
            kick.play()
        if sprite.collide_rect(player, treasure):
            finish = True
            window.blit(win, (200,200))
            money.play()







































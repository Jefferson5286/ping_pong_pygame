from random import randint
import pygame

pygame.init()

tela = pygame.display.set_mode([800, 450])


class Players:
    def __init__(self):
        self.pos = [200, 200]
        self.speed = [8, 8]
        self.cor = [75, 163, 87]
        self.life = [3, 3]

    def update(self):
        self.player_1()
        self.player_2()

        self.move()

    def events(self):
        pass

    def player_1(self):
        self.wall_collider(0)
        return pygame.draw.rect(tela, self.cor, [0, self.pos[0], 15, 90])

    def player_2(self):
        self.wall_collider(1)
        return pygame.draw.rect(tela, self.cor, [785, self.pos[1], 15, 90])

    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.pos[1] += self.speed[0]
        elif key[pygame.K_RIGHT]:
            self.pos[1] -= self.speed[0]
        if key[pygame.K_a]:
            self.pos[0] -= self.speed[1]
        elif key[pygame.K_d]:
            self.pos[0] += self.speed[1]

    def wall_collider(self, index):
        if self.pos[index] < 0:
            self.pos[index] = 0
        elif self.pos[index] > 360:
            self.pos[index] = 360


class Boll:
    def __init__(self):
        self.pos = [400, 225]
        self.cor = [196, 188, 165]
        self.speed_x = 8
        self.speed_y = 4

    def update(self):
        self.pos[0] += self.speed_x
        self.boll()

    def boll(self):
        return pygame.draw.circle(tela, self.cor, self.pos, 15)

    # noinspection SpellCheckingInspection
    def detected_wall_y_collider(self):
        centery = self.boll().centery
        return True if centery > 450 or centery < 0 else False

    # noinspection SpellCheckingInspection
    def detected_wall_x_collider(self):
        centerx = self.boll().centerx
        return True if centerx > 800 or centerx < 0 else False
    

# noinspection SpellCheckingInspection
class Cenario:
    def __init__(self):
        pass


players = Players()
boll = Boll()

player = [
    players.player_1(),
    players.player_2()
]

ramming = True
clock = pygame.time.Clock()
operator = ''

while ramming:
    tela.fill([57, 71, 227])
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            ramming = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass

    players.update()
    boll.update()

    if boll.boll().colliderect(players.player_1()) or boll.boll().colliderect(players.player_2()):
        boll.speed_x = -boll.speed_x
        value = randint(0, 3)
        if value == 0:
            operator = ''
        elif value == 1:
            operator = '+'
        else:
            operator = '-'

    if boll.detected_wall_y_collider():
        boll.speed_y = -boll.speed_y

    if boll.detected_wall_x_collider():
        boll.pos = [400, 225]

    if operator != '':
        exec(f'boll.pos[1] {operator}= -boll.speed_y')

    pygame.display.update()

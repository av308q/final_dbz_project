import pygame

pygame.init()

win = pygame.display.set_mode((1500,752))
pygame.display.set_caption("Dragon Ball Z")

walkRight = (pygame.image.load('images/dbz_img/trunksmr.png'), pygame.image.load('images/dbz_img/trunksm2r.png'), pygame.image.load('images/dbz_img/trunksm3r.png'), pygame.image.load('images/dbz_img/trunksm4r.png'), pygame.image.load('images/dbz_img/trunksm5r.png'), pygame.image.load('images/dbz_img/trunksm6r.png'), pygame.image.load('images/dbz_img/trunksm7r.png'), pygame.image.load('images/dbz_img/trunksm8r.png'), pygame.image.load('images/dbz_img/trunksm9r.png'))
walkLeft = (pygame.image.load('images/dbz_img/trunksm.png'), pygame.image.load('images/dbz_img/trunksm2.png'), pygame.image.load('images/dbz_img/trunksm3.png'), pygame.image.load('images/dbz_img/trunksm4.png'), pygame.image.load('images/dbz_img/trunksm5.png'), pygame.image.load('images/dbz_img/trunksm6.png'), pygame.image.load('images/dbz_img/trunksm7.png'), pygame.image.load('images/dbz_img/trunksm8.png'), pygame.image.load('images/dbz_img/trunksm9.png'))

#jump = (pygame.image.load('images/dbz_img/cellj1.png'), pygame.image.load('images/dbz_img/cellj2.png'), pygame.image.load('images/dbz_img/cellj3.png'), pygame.image.load('images/dbz_img/cellj4.png'), pygame.image.load('images/dbz_img/cellj5.png'), pygame.image.load('images/dbz_img/cellj6.png'), pygame.image.load('images/dbz_img/cellj7.png'), pygame.image.load('images/dbz_img/cellj8.png'), pygame.image.load('images/dbz_img/cellj8.png'))
jump = (pygame.image.load('images/dbz_img/trunksj1.png'), pygame.image.load('images/dbz_img/trunksj2.png'), pygame.image.load('images/dbz_img/trunksj3.png'), pygame.image.load('images/dbz_img/trunksj4.png'), pygame.image.load('images/dbz_img/trunksj5.png'), pygame.image.load('images/dbz_img/trunksj6.png'), pygame.image.load('images/dbz_img/trunksj7.png'), pygame.image.load('images/dbz_img/trunksj8.png'), pygame.image.load('images/dbz_img/trunksj8.png'))
bg = pygame.image.load('images/dbz_stage_tourny.png')
char = pygame.image.load("images/dbz_img/cell_stand1.png")
kameha = pygame.image.load("images/dbz_img/mis2.png")

clock = pygame.time.Clock()

# LIST OF SOUNDS 
pygame.mixer.init()
sound = pygame.mixer.Sound('sounds/cell_theme.wav')
kame_sound = pygame.mixer.Sound('kame_1.wav')

score = 0

class player_one(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 12
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walk_count = 0
        self.standing = True
        self.health = 10
        self.hitbox = (self.x + 40, self.y, 70, 160)

    def draw(self,win):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if not(self.standing) and not(self.is_jump):
            if self.left:
                win.blit(walkLeft[self.walk_count//3], (self.x,self.y))
                self.walk_count += 1
            elif self.right:
                win.blit(walkRight[self.walk_count//3], (self.x,self.y))
                self.walk_count += 1
        elif self.is_jump:
                win.blit(jump[self.jump_count//3], (self.x,self.y))   
        else:
            if self.right:
                win.blit(walkRight[0], (self.x,self.y))
            else:
                win.blit(walkLeft[0], (self.x,self.y))

        self.hitbox = (self.x + 40, self.y, 70, 160)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class projectile(object):
    def __init__(self, x, y, width, height, radius, facing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.facing = facing
        self.vel = 18 * facing
        self.radius = radius
        self.kameha_count = 0
        
    def draw(self, win):
        win.blit(kameha, (self.x,self.y))

class player_two(object):
    walk_right = (pygame.image.load('images/dbz_img/cell_walk1r.png'), pygame.image.load('images/dbz_img/cell_walk2r.png'), pygame.image.load('images/dbz_img/cell_walk3r.png'), pygame.image.load('images/dbz_img/cell_walk4r.png'), pygame.image.load('images/dbz_img/cell_walk5r.png'), pygame.image.load('images/dbz_img/cell_walk6r.png'), pygame.image.load('images/dbz_img/cell_walk7r.png'), pygame.image.load('images/dbz_img/cell_walk8r.png'), pygame.image.load('images/dbz_img/cell_walk9r.png'))
    walk_left = (pygame.image.load('images/dbz_img/cell_walk1.png'), pygame.image.load('images/dbz_img/cell_walk2.png'), pygame.image.load('images/dbz_img/cell_walk3.png'), pygame.image.load('images/dbz_img/cell_walk4.png'), pygame.image.load('images/dbz_img/cell_walk5.png'), pygame.image.load('images/dbz_img/cell_walk6.png'), pygame.image.load('images/dbz_img/cell_walk7.png'), pygame.image.load('images/dbz_img/cell_walk8.png'), pygame.image.load('images/dbz_img/cell_walk9.png'))
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walk_count = 0
        self.vel = 12
        self.hitbox = (self.x + 40, self.y, 70, 160)
        self.health = 10
        self.visible = True
        self.jump_count = 10

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walk_count + 1 >= 27:   #number is 27 because of the images in the sprite
                self.walk_count = 0
            if self.vel > 0:
                win.blit(self.walk_right[self.walk_count //3], (self.x, self.y))
                self.walk_count += 1
            else:
                win.blit(self.walk_left[self.walk_count //3], (self.x, self.y))
                self.walk_count += 1

            # win.blit(jump[self.jump_count //3], (self.x, self.y))
            # self.jump_count += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 40, self.y, 70, 160)
            #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0

    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False

def redraw_game_window():
    
    win.blit(bg, (0,0))

    #draw character to screen
    goku.draw(win)
    cell.draw(win)
    for kama in kamehameha:
        kama.draw(win)

    pygame.display.update()

#create instance of player1 object here

goku = player_one(900,520,40,160)
cell = player_two(50,470,40,160, 1150)
shoot_loop = 0
kamehameha = []
sound.play()
#main loop
run = True
while run:
    clock.tick(27)

    if shoot_loop > 0:
        shoot_loop += 1
    if shoot_loop > 3:
        shoot_loop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for kama in kamehameha:
        if kama.y - kama.radius < cell.hitbox[1] + cell.hitbox[3] and kama.y + kama.radius > cell.hitbox[1]:
            if kama.x + kama.radius > cell.hitbox[0] and kama.x - kama.radius < cell.hitbox[0] + cell.hitbox[2]:
                cell.hit()
                score += 1
                kamehameha.pop(kamehameha.index(kama))
        if kama.x < 1300 and kama.x > 0:
            kama.x += kama.vel
        else:
            kamehameha.pop(kamehameha.index(kama))

    # Set up a list
    keys = pygame.key.get_pressed()

    #track key entered by user to determine action
    if keys[pygame.K_SPACE] and shoot_loop == 0:
        if goku.left:
            facing = -1
        else:
            facing = 1
        if len(kamehameha) < 5:
            kamehameha.append(projectile(round(goku.x + goku.width //4), round(goku.y + goku.height//4), 64, 64, 1, facing))
        shoot_loop = 1

    if keys[pygame.K_LEFT] and goku.x > goku.vel:
        goku.x -= goku.vel
        goku.left = True
        goku.right = False
        goku.standing = False
    elif keys[pygame.K_RIGHT] and goku.x < 1200 - goku.width - goku.vel:
        goku.x += goku.vel
        goku.left = False
        goku.right = True
        goku.standing = False
    else:
        goku.standing = True
        goku.walk_count = 0

    if not(goku.is_jump):
        if keys[pygame.K_UP]:
            goku.is_jump = True
            goku.right = False
            goku.left = False
            goku.walk_count = 0
    else:
        if goku.jump_count >= -10:
            neg = 1
            if goku.jump_count < 0:
                neg = -1
            goku.y -= (goku.jump_count ** 2) * neg
            goku.jump_count -= 1
        else:
            goku.is_jump = False
            goku.jump_count = 10

    redraw_game_window()

pygame.quit()

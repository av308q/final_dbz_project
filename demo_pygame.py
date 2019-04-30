import pygame

pygame.init()

win = pygame.display.set_mode((1500,752))

walkRight = (pygame.image.load('images/dbz_img/cell_walk1r.png'), pygame.image.load('images/dbz_img/cell_walk2r.png'), pygame.image.load('images/dbz_img/cell_walk3r.png'), pygame.image.load('images/dbz_img/cell_walk4r.png'), pygame.image.load('images/dbz_img/cell_walk5r.png'), pygame.image.load('images/dbz_img/cell_walk6r.png'), pygame.image.load('images/dbz_img/cell_walk7r.png'), pygame.image.load('images/dbz_img/cell_walk8r.png'), pygame.image.load('images/dbz_img/cell_walk9r.png'))
walkLeft = (pygame.image.load('images/dbz_img/cell_walk1.png'), pygame.image.load('images/dbz_img/cell_walk2.png'), pygame.image.load('images/dbz_img/cell_walk3.png'), pygame.image.load('images/dbz_img/cell_walk4.png'), pygame.image.load('images/dbz_img/cell_walk5.png'), pygame.image.load('images/dbz_img/cell_walk6.png'), pygame.image.load('images/dbz_img/cell_walk7.png'), pygame.image.load('images/dbz_img/cell_walk8.png'), pygame.image.load('images/dbz_img/cell_walk9.png'))
jump = (pygame.image.load('images/cell_jump_1.png'), pygame.image.load('images/cell_jump_2.png'), pygame.image.load('images/cell_jump_3.png'), pygame.image.load('images/cell_jump_4.png'), pygame.image.load('images/cell_jump_5.png'), pygame.image.load('images/cell_jump_6.png'), pygame.image.load('images/cell_jump_6.png'), pygame.image.load('images/cell_jump_7.png'), pygame.image.load('images/cell_jump_8.png'))
bg = pygame.image.load('images/dbz_stage_tourny.png')
char = pygame.image.load("images/dbz_img/cell_stand1.png")

clock = pygame.time.Clock()

x = 900
y = 470
width = 64
height = 64
vel = 10

is_jump = False
jump_count = 10

left = False
right = False
walk_count = 0


def redraw_game_window():
    global walk_count
    # This snippet of code fills the 
    # screen with the color black so a line of squares
    # do not appear
    win.blit(bg, (0,0))

    if walk_count + 1 >= 27:
        walk_count = 0
    if left:
        win.blit(walkLeft[walk_count//3], (x,y))
        walk_count += 1
    elif right:
        win.blit(walkRight[walk_count//3], (x,y))
        walk_count += 1
    elif is_jump:
        win.blit(jump[jump_count//3], (x,y))
    else:
        win.blit(char, (x,y))
    
    # In order to show Goku, refresh the page
    pygame.display.update()
    
#main loop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # Set up a list
    keys = pygame.key.get_pressed()

    #track key entered by user to determine 
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1200 - width - vel:
        x += vel
        left = False
        right = True
    else:
        right = False
        left = False
        walk_count = 0

    if not(is_jump):
        if keys[pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
            walk_count = 0
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    redraw_game_window()

    #move Goku


pygame.quit()





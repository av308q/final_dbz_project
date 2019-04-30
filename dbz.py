import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos


class Hero(Character):
    pass

class Monster(Character):
    pass

def main():
    width = 1280
    height = 738
    blue_color = (97, 159, 182)
    
    pygame.mixer.init()
    sound = pygame.mixer.Sound('sounds/cell_theme.wav')

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('DBZ')

    background_image = pygame.image.load('images/dbz_background.png').convert_alpha()
    hero_image = pygame.image.load('images/dbz_img/cellj2.png').convert_alpha()
    monster_image = pygame.image.load('images/dbz_img/cellj1.png').convert_alpha()

    #our hero
    player = Hero(hero_image, [400,250])
    monster = Monster(monster_image, [950,250])

    player_group = pygame.sprite.Group()
    player_group.add(player)

    monster_group = pygame.sprite.Group()
    monster_group.add(monster)

    # Game initialization
    
    sound.play()
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            
                

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.blit(background_image, [0,0])

        player_group.draw(screen)
        monster_group.draw(screen)
        # Game display

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()

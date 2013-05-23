import pygame
from pygame.locals import *

from GameObject import GameObject
from Player import Player
from Bullet import Bullet
from Enemy import Enemy


FPS = 30    # frames per second
screenWidth = 1018
screenHeight = 720
clock = pygame.time.Clock()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((screenWidth,screenHeight))
    background = pygame.image.load('background.jpg')

    players = pygame.sprite.RenderUpdates()
    player = Player(screen)
    players.add(player)
    enemies = pygame.sprite.RenderUpdates()
    enemies.add(Enemy(screen))
    bullets = pygame.sprite.RenderUpdates()
    bulletTicks = 0

    Done = False

    while not Done:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            dx = player.vx
            dy = 0
            if event.type == QUIT:
                Done = True
                break;
            elif event.type == KEYDOWN:
                pressedKeys = pygame.key.get_pressed()
                if pressedKeys[K_ESCAPE]:
                    Done = True
                    break
 
                if pressedKeys[K_SPACE]:
                   dy = -20

                if pressedKeys[K_LEFT]:
                     dx = -(4 + pressedKeys[K_LSHIFT] * 8)
                elif pressedKeys[K_RIGHT]:
                     dx = 4 + pressedKeys[K_LSHIFT] * 8
                else:
                     pass

            elif event.type == KEYUP and event.key in (K_RIGHT, K_LEFT):
                dx, dy = 0, 0
            else:
                pass

        player.move(dx, dy)
        players.draw(screen)

        for enemy in enemies:
            enemy.move()
            if enemy.seesTarget(player):
                if bulletTicks > (FPS * 5):
                    #fire once per second
                    bullets.add(enemy.fire())
                    bulletTicks = 0
                else:
                    bulletTicks += 1
            else:
                bulletTicks = 0 
        enemies.draw(screen)

        for bullet in bullets:
            bullet.move()

        bullets.draw(screen)

        bulletHit = pygame.sprite.spritecollideany(player, bullets)

        if bulletHit is not None:
            player.kill()
            bulletHit.kill()
            Done = True
        
        pygame.display.flip()
        ms = clock.tick(FPS)

    pygame.quit()

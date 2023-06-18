import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("N.E.A.T.")
screen.fill((255, 255, 255))


class Player:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.width = 20
        self.height = 20

    def display(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def move(self, direction):
        if direction == "up":
            if self.y > 0:
                self.y -= 0.1
            else:
                self.y = 0
        if direction == "down":
            if self.y < 600 - self.height:
                self.y += 0.1
            else:
                self.y = 600 - self.height
        if direction == "left":
            if self.x > 0:
                self.x -= 0.1
            else:
                self.x = 0
        if direction == "right":
            if self.x < 600 - self.width:
                self.x += 0.1
            else:
                self.x = 600 - self.width


class Goal:
    def __init__(self):
        self.x = 500
        self.y = 100
        self.width = 40
        self.height = 40

    def display(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))


player1 = Player()
goal = Goal()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_DOWN]:
        player1.move("down")
    if keystate[pygame.K_UP]:
        player1.move("up")
    if keystate[pygame.K_LEFT]:
        player1.move("left")
    if keystate[pygame.K_RIGHT]:
        player1.move("right")

    screen.fill((255,255,255))
    goal.display()
    player1.display()
    pygame.display.flip()
import pygame
from pygame.math import Vector2
from random import randint

pygame.init()
display = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

class Particle:
    def __init__(self, coord: Vector2):
        self.coord = coord
        self.size = 5
        self.velocity = Vector2(0, 3)
        self.lifetime = 255
        
    def update_position(self):
        self.coord += self.velocity
        self.velocity.y *= 1.04
        self.velocity.x *= 0.94
        
        self.lifetime *= 0.95
    
    def show(self):
        R = 255
        G = 255 - self.lifetime
        B = G
        
        pygame.draw.circle(
            display,
            (R, G, B),
            self.coord,
            self.size,
        )


class ParticleSystem:
    def __init__(self):
        self.particles = []

    def add_particle(self, pos: Vector2):
        p = Particle(pos)
        p.velocity.x = randint(-6, 6)
        self.particles.append(p)
    
    def clear(self):
        for p in self.particles:
            if p.coord.y > display.get_height():
                self.particles.remove(p)
    
    def show(self):   
        for p in self.particles:
            p.update_position()
            p.show()

ps = ParticleSystem()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_SPACE]:
        # Born a new particle...
        ps.add_particle(Vector2(250, 50))
    
    ps.clear()
    display.fill((255, 255, 255))
    ps.show()
    pygame.display.update()
    clock.tick(60)
    print(len(ps.particles))
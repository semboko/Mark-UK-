import pygame
from random import randint
from pygame.math import Vector2 as V2
from datetime import datetime

pygame.init()


WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

background_image = pygame.image.load("assets/Background.png")
terrain_image = pygame.image.load("assets/Terrain.png")

game_over_sound = pygame.mixer.Sound("assets/game_over.wav")
game_over_sound.set_volume(0.15)


best_scores = []


scroll_x = 0
distance = 0

score = 0

score_font = pygame.font.SysFont("Arial", 20)

game_over = False


def game_over_screen():
    font = pygame.font.SysFont("Arial", 60)
    text_image = font.render("Game Over", True, (0, 0, 0))
    dest = text_image.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    display.blit(text_image, dest)
    
    y = dest.bottom
    
    for entry in best_scores:
        date = entry[0]
        score = entry[0]
        row = date + " - " + score
        row_image = score_font.render(row, True, (0, 0, 0))
        display.blit(row_image, (200, y))
        y += row_image.get_height()


class Pillar:
    
    interval_heigh = 200
    
    def __init__(self):
        self.x = WINDOW_WIDTH
        
        self.interval_y = randint(
            self.interval_heigh/2 + 30, 
            WINDOW_HEIGHT - terrain_image.get_height() - self.interval_heigh/2 - 30,
        )
        
        self.upper_pipe = pygame.image.load("assets/Pipe.png")
        self.lower_pipe = pygame.transform.flip(self.upper_pipe, flip_x=False, flip_y=True)
        
        self.counted = False
        
    def get_rects(self):
        upper_y = self.interval_y - self.interval_heigh / 2 - self.upper_pipe.get_height()
        lower_y = self.interval_y + self.interval_heigh / 2
        
        upper_rect = pygame.Rect((self.x, upper_y), self.upper_pipe.get_size())
        lower_rect = pygame.Rect((self.x, lower_y), self.lower_pipe.get_size())
        
        return upper_rect, lower_rect
    
    def render(self):
        upper_rect, lower_rect = self.get_rects()
        
        display.blit(self.upper_pipe, upper_rect)
        display.blit(self.lower_pipe, lower_rect)


class Bird:
    def __init__(self, pos: V2):
        self.pos = pos
        self.y_velocity = 3
         
        raw_image = pygame.image.load("assets/Bird.png")
        self.image = pygame.transform.scale(raw_image, (50, 50))
        
    def update(self):
        if self.y_velocity < 0:
            self.y_velocity *= 0.9 
        
            if self.y_velocity > -1:
                self.y_velocity = 1.1
        
        if self.y_velocity > 0:
            self.y_velocity *= 1.06
        
        if not game_over:
            self.pos.y += self.y_velocity
    
    def jump(self):
        # self.pos.y -= 100
        if not game_over:
            self.y_velocity = -7
    
    def render(self):
        dest = self.image.get_rect(center=self.pos)
        display.blit(self.image, dest)
        return dest


bird = Bird(V2(200, 320))

pillars = []

def restart_game():
    global bird
    global pillars
    global game_over
    global score
    global scroll_x
    global distance
    
    bird = Bird(V2(200, 300))
    pillars = []
    game_over = False
    score = 0
    scroll_x = 0
    distance = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()
                if game_over:
                    restart_game()
            
    display.blit(background_image, (0, 0))
    for i in range(2):
        w = terrain_image.get_width()
        display.blit(terrain_image, (scroll_x + w * i, 565))
    
    bird_rect = bird.render()
    
    for p in pillars:
        if not game_over:
            p.x -= 4
        
        p.render()
        
        if game_over:
            continue
        
        if p.x < -200:
            pillars.remove(p)
        
        if p.x < bird.pos.x and not p.counted:
            score += 1
            p.counted = True
        
        upper_rect, lower_rect = p.get_rects()
        
        if bird_rect.colliderect(upper_rect) or bird_rect.colliderect(lower_rect):
            print("Game must be stoped")
            game_over = True
            game_over_sound.play()
    
    
    score_image = score_font.render("Score: " + str(score), True, (0, 0, 0))
    display.blit(score_image, (10, 10))
    
    if game_over:
        date = datetime.now().strftime("%d/%m/%y %H:M")
        best_scores.append((date, str(score)))
        
        game_over_screen()
    
    pygame.display.update()
    clock.tick(60)
    
    if not game_over:
        scroll_x -= 5
        distance += 5

    if scroll_x < -480:
        scroll_x = 0
        
    if distance % 300 == 0:
        pillars.append(Pillar())
        
    bird.update()
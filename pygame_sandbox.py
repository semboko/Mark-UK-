import pygame

pygame.init()

size = 500, 500
display = pygame.display.set_mode(size)

circle_center = [250, 250]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
        #         circle_center[1] -= 10
        #     if event.key == pygame.K_DOWN:
        #         circle_center[1] += 10
        #     if event.key == pygame.K_LEFT:
        #         circle_center[0] -= 10
        #     if event.key == pygame.K_RIGHT:
        #         circle_center[0] += 10
    
    pressed_keys = pygame.key.get_pressed()
    
    if pressed_keys[pygame.K_LEFT]:
        circle_center[0] -= 10
    if pressed_keys[pygame.K_RIGHT]:
        circle_center[0] += 10
    if pressed_keys[pygame.K_UP]:
        circle_center[1] -= 10
    if pressed_keys[pygame.K_DOWN]:
        circle_center[1] += 10
    
    display.fill((255, 255, 255))
    pygame.draw.circle(display, (255, 255, 0), circle_center, 50)
    pygame.display.update()
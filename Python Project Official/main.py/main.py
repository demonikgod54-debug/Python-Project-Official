#basic
from os.path import join
import pygame
pygame.init()
screen_width, screen_length = 1400, 800
front_screen = pygame.display.set_mode((screen_width, screen_length))
eventrunning = True
clock = pygame.time.Clock()
scene = 1
timer = 100
reset = 100
#velocity
gravity = 10
Jump = -30
y_vel = Jump

#name
pygame.display.set_caption('Chill Game')

#Imports & rect
Magicroom = pygame.image.load('images/Background.png').convert()
background = pygame.image.load('images/realbackground.png').convert()
player_surf = pygame.image.load('images/playert.png').convert()
player_rect = player_surf.get_frect(center = (300,300),)
player_movement = pygame.math.Vector2(0,0)
player_speed = 0.5
ground = pygame.image.load('images/ground2.png').convert_alpha()
ground_rect = ground.get_frect(center = (400,1080))
wall_left = pygame.FRect(0,0,0,1080)
wall_right = pygame.FRect(1760,0,500,1080)
forestdoor = pygame.image.load('images/door.png').convert_alpha()
forestdoor_rect = forestdoor.get_frect(center = (700, 500))
forest = pygame.image.load('images/forest.jpg').convert_alpha()
tree = pygame.image.load('images/spruce.png').convert_alpha()
tree_rect = tree.get_frect(center = (1200,440))
plainsdoor_rect = forestdoor.get_frect(center = (100,530))
portal = pygame.image.load('images/portal.png').convert_alpha()
portal_rect = portal.get_frect(center=(1000,460))
backup = pygame.image.load('images/grounder.png').convert_alpha()
normal = pygame.image.load('images/playert.png').convert_alpha()
platform = pygame.image.load('images/platform.png').convert_alpha()
platform_rect = platform.get_frect(center = (128, 670))
platform2 = pygame.image.load('images/platform.png').convert_alpha()
platform3 = pygame.image.load('images/platform.png').convert_alpha()
platform4 = pygame.image.load('images/platform.png').convert_alpha()
platform5 = pygame.image.load('images/platform.png').convert_alpha()
platform6 = pygame.image.load('images/platform.png').convert_alpha()
platform7 = pygame.image.load('images/platform.png').convert_alpha()
platform_rect2 = platform.get_frect(center = (365,580))
platform_rect3 = platform.get_frect(center = (583, 495))
platform_rect4 = platform.get_frect(center = (300, 386))
platform_rect5 = platform.get_frect(center = (620,290))
platform_rect6 = platform.get_frect(center = (920, 280))
platform_rect7 = platform.get_frect(center = (1090, 228))
collide_plat2= pygame.rect.FRect.colliderect(platform_rect2,player_rect)
collide_plat3= pygame.rect.FRect.colliderect(platform_rect3,player_rect)
collide_plat4= pygame.rect.FRect.colliderect(platform_rect4,player_rect)
collide_plat5= pygame.rect.FRect.colliderect(platform_rect5,player_rect)
collide_plat6= pygame.rect.FRect.colliderect(platform_rect6,player_rect)
collide_plat7= pygame.rect.FRect.colliderect(platform_rect7,player_rect)                                   
#player_jump = pygame.image.load()
#player_left = pygame.image.load()
#player_right = pygame.image.load( )



wood = 10
rice = 10
#loop
while eventrunning:
    clock.tick(4000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            eventrunning = False
    corner = player_rect.topleft
    x_pos = player_rect.x
    y_pos = player_rect.y
    #going down
    if timer > 0:
        timer -= 1
        print(timer)
    # movement for a
    collide_ground = pygame.rect.FRect.colliderect(ground_rect, player_rect)
    if collide_ground == False:
        player_rect.y += 0.5
    keys = pygame.key.get_pressed()
    # movement for a
    # movement for d
    if keys[pygame.K_d]:
        player_movement.x = 0.339
        player_surf = backup
    elif keys[pygame.K_a]:
        player_movement.x = -0.4
        player_surf = backup
        print('left')
    else:
        player_movement.x = 0
        player_surf = normal 
    player_rect.center += player_movement * player_speed
    #Collision
    if collide_ground:
        jump = True
    if collide_ground:
        player_rect.bottom = ground_rect.top
    collide_wallleft = pygame.rect.FRect.colliderect(wall_left, player_rect)
    if collide_wallleft:
        player_rect.left = wall_left.right
    collide_wallright = pygame.rect.FRect.colliderect(wall_right, player_rect)
    if collide_wallright:
        player_rect.right = wall_right.left
    #graphic
    infdoor = pygame.rect.FRect.colliderect(forestdoor_rect, player_rect)
    inpdoor = pygame.rect.FRect.colliderect(plainsdoor_rect, player_rect)
    inmdoor = pygame.rect.FRect.colliderect(portal_rect, player_rect)
    if scene == 1:
        front_screen.blit(background,(-300,-300))
        front_screen.blit(forestdoor, forestdoor_rect)
        front_screen.blit(player_surf, player_rect)
        front_screen.blit(portal,portal_rect)
    #move to new page 1
    mouse_pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN and forestdoor_rect.collidepoint(mouse_pos) and infdoor:
        scene = 2
    if scene == 2:
        front_screen.blit(forest,(0,-300))
        front_screen.blit(forestdoor, plainsdoor_rect)
        front_screen.blit(tree,tree_rect)
    front_screen.blit(player_surf,player_rect)
    if event.type == pygame.MOUSEBUTTONDOWN and plainsdoor_rect.collidepoint(mouse_pos) and inpdoor:
        scene = 1
    if event.type == pygame.MOUSEBUTTONDOWN and portal_rect.collidepoint(mouse_pos) and inmdoor and 9 < rice and 9 < wood:
        scene = 3
    if scene == 3:
        front_screen.blit(Magicroom, (0,-300))
        front_screen.blit(player_surf,player_rect)
        ground_rect = ground.get_frect(center = (400,1250))
        front_screen.blit(platform, platform_rect)
        front_screen.blit(platform2, platform_rect2)
        front_screen.blit(platform3, platform_rect3)
        front_screen.blit(platform4, platform_rect4)
        front_screen.blit(platform5, platform_rect5)
        front_screen.blit(platform6, platform_rect6)
        front_screen.blit(platform7, platform_rect7)
        collide_plat2= pygame.rect.FRect.colliderect(platform_rect2,player_rect)
        collide_plat3= pygame.rect.FRect.colliderect(platform_rect3,player_rect)
        collide_plat4= pygame.rect.FRect.colliderect(platform_rect4,player_rect)
        collide_plat5= pygame.rect.FRect.colliderect(platform_rect5,player_rect)
        collide_plat6= pygame.rect.FRect.colliderect(platform_rect6,player_rect)
        collide_plat7= pygame.rect.FRect.colliderect(platform_rect7,player_rect)
        if collide_plat2:
            player_rect.bottom = platform_rect2.top
        if collide_plat3:
            player_rect.bottom = platform_rect3.top
        if collide_plat4:
            player_rect.bottom = platform_rect4.top      
        if collide_plat5:
            player_rect.bottom = platform_rect5.top
        if collide_plat6:
            player_rect.bottom = platform_rect6.top
        if collide_plat7:
            player_rect.bottom = platform_rect7.top
        if collide_plat2 == False or collide_plat3 == False or collide_plat4 == False or collide_plat5 == False or collide_plat6 == False or collide_plat7 == False:
            player_rect.y +=0.4
        jump = True  
    if scene != 3:     
        if collide_ground == False:
            jump = False
        if collide_ground:
            jump = True
        if keys[pygame.K_w] and jump:
            player_movement.y = -74
        elif collide_ground:
            player_surf = normal
        else:
            player_movement.y = 0
    player_rect.center += player_movement * player_speed
    if scene == 3:
        if collide_ground == False or collide_plat2 == False or collide_plat3 == False or collide_plat4 == False or collide_plat5 == False or collide_plat6 == False or collide_plat7 == False:
            jump = False
        if collide_ground or collide_plat2 or collide_plat3 or collide_plat4 or collide_plat5 or collide_plat6 or collide_plat7:
            jump = True
        if keys[pygame.K_w] and jump:
            player_movement.y = -74
        elif collide_ground:
            player_surf = normal
        else:
            player_movement.y = 0
    player_rect.center += player_movement * player_speed                 
    pygame.display.update()
pygame.quit()

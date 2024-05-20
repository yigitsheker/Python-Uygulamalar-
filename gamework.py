import sys, pygame,random

screen_width = 600
screen_height = 600

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont("arial",20)

while True:
    for even in pygame.event.get():
        pygame.quit()
        sys.exit()

    screen.fill(255,0,0)
    rect = pygame.rect(100,100,200,200)
    pygame.draw.rect(screen(255,255,255),rect)
    score_text = font.render("Score: 0",True,(0,0,0))
    screen.blit(score_text,(10,10))

    pygame.display.update()
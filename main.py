import pygame
import CONSTANS as const

def main():

    #init
    pygame.init()

    window = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
    pygame.display.set_caption(const.WINDOW_TITLE)
    is_running = True
    

    clock = pygame.time.Clock()
    #gameloop
    while is_running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

    #close
    window.close()
    print("end")

if __name__ == "__main__":
    main()

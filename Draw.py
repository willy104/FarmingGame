import pygame
import CONSTANS as const

def button(name, id, surface):
    try:
        print(f"draw {name} button")
        buttonImage = pygame.image.load(f"assets/{name}{id}.png")
        rect = buttonImage.get_rect()
        rect.topleft = (const.BUTTON_POS[f"{name}{id}"][0], const.BUTTON_POS[f"{name}{id}"][1])
        surface.blit(buttonImage, rect)
    except pygame.error as e:
        print(f"Error loading button image for {name}{id}: {e}")
        return False
    return True

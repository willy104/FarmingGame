import pygame

def Button(id, name, surface, rect):
    try:
        print(f"draw {name} button")
        buttonImage = pygame.image.load(f"assets/{name}{id}.png")
        surface.blit(buttonImage, rect)
    except pygame.error as e:
        print(f"Error loading button image for {name}{id}: {e}")
        return False
    return True

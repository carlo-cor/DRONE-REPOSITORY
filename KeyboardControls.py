import pygame

#   KEYBOARD CONTROLS   #
def keyboardInit():
    pygame.init()
    window = pygame.display.set_mode((400, 400))  # DIMENSIONS

def keyPressCheck(keyVal):
    response = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()             # CHECKS IF THE KEY IS PRESSED
    key = getattr(pygame, 'K_{}'.format(keyVal))    # KEY FORMAT EX. 'K_{LEFT}', 'K_{RIGHT}', ETC.
    if keyInput[key]:
        response = True
    pygame.display.update()

    return response

def main():
    print(keyPressCheck("TAB"))                     # USE THIS TO CHECK KEY NAME

if __name__ == "__main__":
    keyboardInit()
    while True:
        main()
import pygame
import random

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Coin-Toss')
pygame.display.set_icon(pygame.image.load("images/coin_icon.png").convert_alpha())

coin_imgs = [pygame.image.load(f'images/coin/Coin_{i}.png').convert_alpha() for i in range(1, 14)]
coin_imgs = [pygame.transform.scale(img, (300, 300)) for img in coin_imgs]

coin_flip_sound = pygame.mixer.Sound("images/sound/coin_flip.mp3")

coin_center = (screen_width // 2, screen_height // 2)

def flip_coin():
    choices = ['Head', 'Tail', 'Just do it', 'Just give up']
    probabilities = [0.4, 0.4, 0.19, 0.01]
    return random.choices(choices, weights=probabilities)[0]

coin_result = None
flip_animation = False
flip_frame = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c and not flip_animation:
                coin_result = flip_coin()
                flip_animation = True
                flip_frame = 0
                coin_flip_sound.play()

    screen.fill((223,215,175))

    if flip_animation:
        if flip_frame < len(coin_imgs):
            screen.blit(coin_imgs[flip_frame], (coin_center[0] - coin_imgs[flip_frame].get_width() // 2, coin_center[1] - coin_imgs[flip_frame].get_height() // 2))
            flip_frame += 1
        else:
            flip_animation = False

    else:
        screen.blit(coin_imgs[0], (coin_center[0] - coin_imgs[0].get_width() // 2, coin_center[1] - coin_imgs[0].get_height() // 2))

    font = pygame.font.Font('fonts/KodeMono-Bold.ttf', 30)
    text = font.render("Press C", True, (0, 0, 0))
    screen.blit(text, (screen_width // 2 - 65, screen_height - 50))

    font_ = pygame.font.Font('fonts/KodeMono.ttf', 30)
    text = font_.render("If you can't choose, just flip a coin.", True, (0, 0, 0))
    screen.blit(text, (180,50))

    if coin_result is not None and not flip_animation:
        font = pygame.font.Font('fonts/Adamina-Regular.ttf', 40)
        text = font.render(coin_result, True, (0, 0, 0))
        screen.blit(text, (screen_width // 2 - 50, screen_height // 2 + coin_imgs[0].get_height() // 2))

    pygame.display.update()

    clock.tick(15)

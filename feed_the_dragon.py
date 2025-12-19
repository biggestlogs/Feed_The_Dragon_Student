import pygame, random

# Initialize pygame
pygame.init()


def make_text(font_object, text, color, background_color):
    return font_object.render(text, True, color, background_color)


def blit(surface, item, rect):
    surface.blit(item, rect)


def fill(surface, color):
    surface.fill(color)


def update_display():
    pygame.display.update()


# Set display surface
# TODO:
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the Dragon")


# Set FPS and clock
# TODO:
FPS = 60
clock = pygame.time.Clock()


# Set game values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY


# Set colors
# TODO:
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#   - Define color constants using RGB tuples, such as:
#       * GREEN
#       * DARKGREEN:  RGB value of 10, 50, 10
#       * WHITE
#       * BLACK


# Set fonts
# TODO:
font = pygame.font.Font('assets/AttackGraffiti.ttf', 32)


# Set text
title_text=make_text(font,'feed the dragon' , GREEN, DARKGREEN)
lives_text=make_text(font, f'Lives: {player_lives}' , GREEN, DARKGREEN)
score_text=make_text(font, f'Score: {score}', GREEN, DARKGREEN)

title_rect = title_text.get_rect()
score_rect = score_text.get_rect()
lives_rect = lives_text.get_rect()

score_rect.topleft = (10,10)
title_rect.midtop = 50
lives_rect.topleft = (WINDOW_WIDTH - 10.10)

#       * score_rect at the top-left (e.g., (10, 10))
#       * title_rect centered horizontally at the top
#       * lives_rect at the top-right (e.g., (WINDOW_WIDTH - 10, 10))


# Set sounds and music
# TODO:
coin_catch_sound=pygame.mixer.Sound('assets/coin_catch.wav')
coin_miss_sound=pygame.mixer.Sound('assets/coin_miss.wav')
pygame.mixer.music.load('assets/ftd_background_music.wav')
#   - Load sound effects for:
#       * catching a coin (e.g., "assets/coin_sound.wav")
#       * missing a coin (e.g., "assets/miss_sound.wav")
#   - Optionally adjust the miss sound volume using set_volume(...)
#   - Load background music (e.g., "assets/ftd_background_music.wav") using pygame.mixer.music.load(...)


# Set images
# TODO:
dragon_sprite = pygame.image.load('assets/dragon_right.png')
dragon_sprite_rect = dragon_sprite.get_rect()
dragon_sprite_rect.left = 32
dragon_sprite_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

coin_sprite = pygame.image.load('assets/coin.png')
coin_sprite_rect = coin_sprite.get_rect()
coin_sprite_rect.right = WINDOW_WIDTH//BUFFER_DISTANCE
coin_sprite_rect.y = random.randint(64, WINDOW_HEIGHT - 32)



# The main game loop
# TODO:
pygame.mixer.music.play('assets/ftd_background_music.wav')
running = True


def tick():
    clock.tick(FPS)



def is_still_running():
    events = pygame.event.get()
    if pygame.QUIT in events:
        running = False

    # TODO:
    #   - Get the pygame event list with pygame.event.get()
    #   - If you see an event of type pygame.QUIT, set running to False
    #     so the main loop will end and the game can quit.
      # TODO: remove this when finished


def move_player():
    pygame.key.get_pressed()
    if pygame.key.get_pressed()[pygame.K_UP]:


    # TODO:
    #   - Get the current state of the keyboard using pygame.key.get_pressed()
    #   - If the up arrow is pressed and the player is not above a top limit (e.g., y > 64),
    #       move the player up by PLAYER_VELOCITY.
    #   - If the down arrow is pressed and the player is not below the bottom of the window,
    #       move the player down by PLAYER_VELOCITY.
    pass  # TODO: remove this when finished


def handle_coin():
    # TODO:
    #   - Move the coin to the left each frame by subtracting coin_velocity from coin_rect.x.
    #   - If the coin passes off the left side of the screen (coin_rect.x < 0):
    #       * Subtract 1 from player_lives.
    #       * Play the miss sound.
    #       * Reset the coin's position:
    #           - x: WINDOW_WIDTH + BUFFER_DISTANCE
    #           - y: a random integer between a top margin (e.g., 64) and near the bottom edge.
    pass  # TODO: remove this when finished


def handle_collisions():
    # TODO:
    #   - Check if the player_rect and coin_rect are colliding using colliderect(...)
    #   - If they collide:
    #       * Increase score by 1
    #       * Play the coin sound
    #       * Increase coin_velocity by COIN_ACCELERATION
    #       * Reset the coin's position:
    #           - x: WINDOW_WIDTH + BUFFER_DISTANCE
    #           - y: random integer between the same top and bottom margins
    pass  # TODO: remove this when finished


def update_hud():
    # TODO:
    #   - Re-create score_text and lives_text each frame using make_text(...),
    #     so they show the updated score and lives values.
    #   - Remember to use the same font and colors (GREEN and DARKGREEN).
    pass  # TODO: remove this when finished


def game_over_check():
    # TODO:
    #   - If player_lives reaches 0:
    #       * Draw the game over text and the "press any key to play again" text on the screen.
    #       * Update the display so the player can see the game over screen.
    #       * Stop the background music.
    #       * Create a loop (e.g., is_paused = True) that:
    #           - Waits for events:
    #               + If the player presses any key (KEYDOWN):
    #                   · Reset score to 0
    #                   · Reset player_lives to PLAYER_STARTING_LIVES
    #                   · Reset player position to center vertically
    #                   · Reset coin_velocity to COIN_STARTING_VELOCITY
    #                   · Restart the background music
    #                   · Exit the pause loop (resume game)
    #               + If the player clicks the window close button (QUIT):
    #                   · Set running to False and exit the pause loop so the game can end.
    pass  # TODO: remove this when finished


def update_screen():
    # TODO:
    #   - Fill the display_surface with a background color (e.g., BLACK) using your fill(...) helper.
    #   - Draw the HUD elements on the screen:
    #       * score_text, title_text, lives_text at their rect positions using your blit(...) helper.
    #   - Draw a horizontal line across the screen near the top to separate the HUD from the play area.
    #   - Draw the player image and the coin image at their rect positions using your blit(...) helper.
    #   - Finally, call update_display() so that everything appears on the screen.
    pass


while running:
    # Main game loop steps:
    #   1. Handle quit events.
    #   2. Move the player based on keyboard input.
    #   3. Move the coin and handle misses.
    #   4. Check for collisions between player and coin.
    #   5. Update the HUD text to match the current score and lives.
    #   6. Check if the game is over and either reset or quit.
    #   7. Draw everything on the screen.
    #   8. Tick the clock to control the frame rate.

    is_still_running()
    move_player()
    handle_coin()
    handle_collisions()
    update_hud()
    game_over_check()
    update_screen()
    tick()

# End the game
pygame.quit()

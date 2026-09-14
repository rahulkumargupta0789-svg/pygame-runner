import pygame
import asyncio
import random

# =========================================================
# INITIALIZE
# =========================================================

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

pygame.display.set_caption("Pixel Runner")

clock = pygame.time.Clock()


# =========================================================
# AUDIO
# =========================================================

jump_sound = pygame.mixer.Sound(
    "audio/jump.ogg"
)

jump_sound.set_volume(0.5)


background_music = pygame.mixer.Sound(
    "audio/music.ogg"
)

background_music.set_volume(0.3)


# =========================================================
# LOAD GRAPHICS
# =========================================================

# Background
sky_surface = pygame.image.load(
    "graphics/Sky.png"
).convert()

ground_surface = pygame.image.load(
    "graphics/ground.png"
).convert()


# =========================================================
# PLAYER GRAPHICS
# =========================================================

player_walk_1 = pygame.image.load(
    "graphics/player/player_walk_1.png"
).convert_alpha()

player_walk_2 = pygame.image.load(
    "graphics/player/player_walk_2.png"
).convert_alpha()

player_jump = pygame.image.load(
    "graphics/player/jump.png"
).convert_alpha()

player_stand = pygame.image.load(
    "graphics/player/player_stand.png"
).convert_alpha()

player_stand = pygame.transform.rotozoom(
    player_stand,
    0,
    2
)


# =========================================================
# SNAIL GRAPHICS
# =========================================================

snail_1 = pygame.image.load(
    "graphics/snail/snail1.png"
).convert_alpha()

snail_2 = pygame.image.load(
    "graphics/snail/snail2.png"
).convert_alpha()


# =========================================================
# FLY GRAPHICS
# =========================================================

fly_1 = pygame.image.load(
    "graphics/fly/Fly1.png"
).convert_alpha()

fly_2 = pygame.image.load(
    "graphics/fly/Fly2.png"
).convert_alpha()


# =========================================================
# PLAYER CLASS
# =========================================================

class Player(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.walk_frames = [
            player_walk_1,
            player_walk_2
        ]

        self.walk_index = 0

        self.image = self.walk_frames[0]

        self.rect = self.image.get_rect(
            midbottom=(80, 300)
        )

        self.gravity = 0

    # -----------------------------------------------------
    # JUMP
    # -----------------------------------------------------

    def jump(self):

        if self.rect.bottom >= 300:

            self.gravity = -20

            jump_sound.play()

    # -----------------------------------------------------
    # GRAVITY
    # -----------------------------------------------------

    def apply_gravity(self):

        self.gravity += 1

        self.rect.y += self.gravity

        if self.rect.bottom >= 300:

            self.rect.bottom = 300

            self.gravity = 0

    # -----------------------------------------------------
    # ANIMATION
    # -----------------------------------------------------

    def animation(self):

        # Jump animation
        if self.rect.bottom < 300:

            self.image = player_jump

        # Walking animation
        else:

            self.walk_index += 0.1

            if self.walk_index >= len(
                self.walk_frames
            ):

                self.walk_index = 0

            self.image = self.walk_frames[
                int(self.walk_index)
            ]

    # -----------------------------------------------------
    # UPDATE
    # -----------------------------------------------------

    def update(self):

        keys = pygame.key.get_pressed()

        # Space jump
        if keys[pygame.K_SPACE]:

            self.jump()

        self.apply_gravity()

        self.animation()


# =========================================================
# OBSTACLE CLASS
# =========================================================

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, obstacle_type):

        super().__init__()

        # -------------------------------------------------
        # SNAIL
        # -------------------------------------------------

        if obstacle_type == "snail":

            self.frames = [
                snail_1,
                snail_2
            ]

            y_position = 300

        # -------------------------------------------------
        # FLY
        # -------------------------------------------------

        else:

            self.frames = [
                fly_1,
                fly_2
            ]

            y_position = 210

        self.animation_index = 0

        self.image = self.frames[0]

        self.rect = self.image.get_rect(
            midbottom=(
                random.randint(850, 1000),
                y_position
            )
        )

    # -----------------------------------------------------
    # OBSTACLE ANIMATION
    # -----------------------------------------------------

    def animation(self):

        self.animation_index += 0.1

        if self.animation_index >= len(
            self.frames
        ):

            self.animation_index = 0

        self.image = self.frames[
            int(self.animation_index)
        ]

    # -----------------------------------------------------
    # UPDATE
    # -----------------------------------------------------

    def update(self):

        self.animation()

        # Move obstacle left
        self.rect.x -= 6

        # Delete when off screen
        if self.rect.right < 0:

            self.kill()


# =========================================================
# SPRITE GROUPS
# =========================================================

player = pygame.sprite.GroupSingle()

player.add(
    Player()
)

obstacle_group = pygame.sprite.Group()


# =========================================================
# FONT
# =========================================================

test_font = pygame.font.Font(
    "font/Pixeltype.ttf",
    50
)


# =========================================================
# GAME VARIABLES
# =========================================================

game_active = False

start_time = 0

score = 0


# =========================================================
# GAME TITLE
# =========================================================

game_name = test_font.render(
    "Pixel Runner",
    False,
    (168, 85, 247)
)

game_name_rect = game_name.get_rect(
    center=(400, 80)
)


# =========================================================
# START MESSAGE
# =========================================================

game_message = test_font.render(
    "Press SPACE to run",
    False,
    (34, 211, 238)
)

game_message_rect = game_message.get_rect(
    center=(400, 320)
)


# =========================================================
# DISPLAY SCORE
# =========================================================

def display_score():

    current_time = (
        pygame.time.get_ticks() // 1000
    ) - start_time

    score_surface = test_font.render(
        f"Score: {current_time}",
        False,
        (52, 211, 153)
    )

    score_rect = score_surface.get_rect(
        center=(400, 50)
    )

    screen.blit(
        score_surface,
        score_rect
    )

    return current_time


# =========================================================
# RESET GAME
# =========================================================

def reset_game():

    global score

    score = 0

    # Reset player position
    player.sprite.rect.midbottom = (
        80,
        300
    )

    # Reset gravity
    player.sprite.gravity = 0

    # Reset animation
    player.sprite.walk_index = 0

    player.sprite.image = player_walk_1

    # Remove all obstacles
    obstacle_group.empty()


# =========================================================
# COLLISION
# =========================================================

def check_collision():

    collision = pygame.sprite.spritecollide(
        player.sprite,
        obstacle_group,
        False
    )

    if collision:

        obstacle_group.empty()

        return False

    return True


# =========================================================
# MAIN
# =========================================================

async def main():

    global game_active
    global start_time
    global score

    obstacle_spawn_timer = 0

    running = True

    while running:

        # =================================================
        # EVENTS
        # =================================================

        for event in pygame.event.get():

            # -------------------------------------------------
            # QUIT
            # -------------------------------------------------

            if event.type == pygame.QUIT:

                running = False

            # -------------------------------------------------
            # KEYBOARD
            # -------------------------------------------------

            if event.type == pygame.KEYDOWN:

                # SPACE
                if event.key == pygame.K_SPACE:

                    # START GAME
                    if not game_active:

                        game_active = True

                        start_time = (
                            pygame.time.get_ticks()
                            // 1000
                        )

                        reset_game()

                        # Start background music
                        background_music.play(-1)

                        # Jump immediately
                        player.sprite.jump()

            # -------------------------------------------------
            # MOUSE
            # -------------------------------------------------

            if event.type == pygame.MOUSEBUTTONDOWN:

                # During game
                if game_active:

                    player.sprite.jump()

                # Start game
                else:

                    game_active = True

                    start_time = (
                        pygame.time.get_ticks()
                        // 1000
                    )

                    reset_game()

                    # Start music
                    background_music.play(-1)

                    # Jump
                    player.sprite.jump()

        # =================================================
        # GAME ACTIVE
        # =================================================

        if game_active:

            # Background
            screen.blit(
                sky_surface,
                (0, 0)
            )

            screen.blit(
                ground_surface,
                (0, 300)
            )

            # Score
            score = display_score()

            # Player
            player.update()

            player.draw(screen)

            # -------------------------------------------------
            # OBSTACLE SPAWNING
            # -------------------------------------------------

            obstacle_spawn_timer += 1

            if obstacle_spawn_timer >= 90:

                obstacle_spawn_timer = 0

                obstacle_type = random.choice(
                    [
                        "snail",
                        "snail",
                        "snail",
                        "fly"
                    ]
                )

                obstacle_group.add(
                    Obstacle(obstacle_type)
                )

            # -------------------------------------------------
            # OBSTACLES
            # -------------------------------------------------

            obstacle_group.update()

            obstacle_group.draw(screen)

            # -------------------------------------------------
            # COLLISION
            # -------------------------------------------------

            if not check_collision():

                game_active = False

                # Stop music on game over
                background_music.stop()

        # =================================================
        # START / GAME OVER SCREEN
        # =================================================

        else:

            screen.fill(
                (15, 23, 42)
            )

            # Player standing image
            screen.blit(
                player_stand,
                player_stand.get_rect(
                    center=(400, 200)
                )
            )

            # Title
            screen.blit(
                game_name,
                game_name_rect
            )

            # First screen
            if score == 0:

                screen.blit(
                    game_message,
                    game_message_rect
                )

            # Game over
            else:

                score_message = test_font.render(
                    f"Your score: {score}",
                    False,
                    (111, 196, 169)
                )

                score_message_rect = (
                    score_message.get_rect(
                        center=(400, 320)
                    )
                )

                screen.blit(
                    score_message,
                    score_message_rect
                )

        # =================================================
        # UPDATE SCREEN
        # =================================================

        pygame.display.update()

        clock.tick(60)

        # IMPORTANT FOR PYGBAG
        await asyncio.sleep(0)


# =========================================================
# START GAME
# =========================================================

asyncio.run(main())
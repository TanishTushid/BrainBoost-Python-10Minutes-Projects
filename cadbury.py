import pygame
import math
import time

# ================= INITIALIZE =================
pygame.init()

# ================= CONFIG =================
WIDTH, HEIGHT = 1000, 750
FPS = 60

# Colors
BACKGROUND = (10, 0, 25)
TEXT_COLOR = (255, 255, 255)
TEXT_SHADOW = (255, 100, 180)

# Lyrics
LYRICS = """
close your eyes, kiss me,  
i can read your lips,
on your fingertips,
i can feel your smile,
come on my lips, 
and happiness in your eyes.
kiss me
"""

all_words = LYRICS.replace("\n", " ").split()

# ================= WORD TIMING =================
# Timing for each word according to song rhythm

word_timings = [
    0.8,  # close
    0.8,  # your
    1.0,  # eyes

    0.7,  # Miss
    1.0,  # me

    0.5,  # I
    0.5,  # can
    0.7,  # read
    0.6,  # your
    1.0,  # lips

    0.5,  # On
    0.6,  # my
    1.1,  # fingertips

    0.5,  # I
    0.5,  # can
    0.7,  # feel
    0.6,  # your
    1.0,  # smile

    0.7,  # Come
    0.5,  # on
    0.6,  # my
    1.0,  # lips

    0.6,  # And
    1.0,  # happiness
    0.5,  # in
    0.5,  # our
    1.2   # eyes
]

# ================= WINDOW =================
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌈 Huge Rainbow Heart ❤️")

clock = pygame.time.Clock()

# ================= HEART POSITION =================
HEART_CX = WIDTH // 2
HEART_CY = HEIGHT // 2 + 20

# ================= FONT =================
font_word = pygame.font.SysFont(
    "times new roman",
    75,
    bold=True,
    italic=True
)

# ================= RAINBOW HEART =================
def draw_rainbow_heart(surface, cx, cy, scale):

    heart_colors = [
        (255, 120, 200),
        (255, 0, 180),
        (0, 180, 255),
        (0, 255, 255),
        (50, 255, 50),
        (255, 255, 0),
        (255, 150, 0),
        (255, 0, 120),
        (180, 0, 255),
    ]

    for i, color in enumerate(heart_colors):

        layer_scale = scale * (1 - i * 0.085)

        points = []

        for t in range(0, 360, 3):

            t_rad = math.radians(t)

            x = 16 * math.sin(t_rad) ** 3

            y = (
                13 * math.cos(t_rad)
                - 5 * math.cos(2 * t_rad)
                - 2 * math.cos(3 * t_rad)
                - math.cos(4 * t_rad)
            )

            px = cx + x * layer_scale
            py = cy - y * layer_scale

            points.append((px, py))

        pygame.draw.polygon(surface, color, points)

# ================= SPARKLES =================
class Sparkle:

    def __init__(self):
        self.reset()

    def reset(self):

        angle = math.radians(
            pygame.time.get_ticks() % 360
        )

        radius = 320 + (pygame.time.get_ticks() % 120)

        self.x = HEART_CX + math.cos(angle) * radius
        self.y = HEART_CY + math.sin(angle) * radius

        self.size = 2 + (pygame.time.get_ticks() % 4)

        self.speed = 0.5 + (pygame.time.get_ticks() % 3)

        self.vx = math.cos(angle) * self.speed
        self.vy = math.sin(angle) * self.speed

        self.alpha = 255

        self.color = [
            (255, 255, 255),
            (255, 120, 180),
            (0, 255, 255),
            (255, 255, 0)
        ][pygame.time.get_ticks() % 4]

    def update(self):

        self.x += self.vx
        self.y += self.vy

        self.alpha -= 3

        if self.alpha <= 0:
            self.reset()

    def draw(self, surface):

        glow = pygame.Surface(
            (30, 30),
            pygame.SRCALPHA
        )

        pygame.draw.circle(
            glow,
            (*self.color, self.alpha),
            (15, 15),
            self.size
        )

        surface.blit(glow, (self.x, self.y))

# Create sparkles
sparkles = [Sparkle() for _ in range(120)]

# ================= TEXT =================
def draw_glow_text(surface, text, x, y):

    # Glow effect
    glow = font_word.render(
        text,
        True,
        (255, 120, 200)
    )

    glow.set_alpha(100)

    for dx in range(-5, 6, 2):
        for dy in range(-5, 6, 2):

            rect = glow.get_rect(
                center=(x + dx, y + dy)
            )

            surface.blit(glow, rect)

    # Shadow
    shadow = font_word.render(
        text,
        True,
        TEXT_SHADOW
    )

    shadow_rect = shadow.get_rect(
        center=(x + 4, y + 4)
    )

    surface.blit(shadow, shadow_rect)

    # Main text
    main = font_word.render(
        text,
        True,
        TEXT_COLOR
    )

    main_rect = main.get_rect(
        center=(x, y)
    )

    surface.blit(main, main_rect)

# ================= VARIABLES =================
running = True

pulse_phase = 0

word_index = 0

last_word_time = time.time()

# ================= MAIN LOOP =================
while running:

    # ========== EVENTS ==========
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_r:
                word_index = 0

    # ========== UPDATE ==========
    current_time = time.time()

    pulse_phase += 0.05

    # Smooth pulse
    pulse = 1 + 0.04 * math.sin(pulse_phase)

    # ================= SONG-LIKE WORD TIMING =================
    if word_index < len(all_words):

        current_delay = word_timings[word_index]

        if current_time - last_word_time > current_delay:

            word_index += 1

            last_word_time = current_time

    # Update sparkles
    for s in sparkles:
        s.update()

    # ========== DRAW ==========
    screen.fill(BACKGROUND)

    # Sparkles
    for s in sparkles:
        s.draw(screen)

    # ================= HUGE HEART =================
    draw_rainbow_heart(
        screen,
        HEART_CX,
        HEART_CY,
        18 * pulse
    )

    # ================= SLOW SHINE =================
    shine_x = HEART_CX - 140 + math.sin(pulse_phase * 0.3) * 18
    shine_y = HEART_CY - 250 + math.cos(pulse_phase * 0.2) * 8

    shine_surface = pygame.Surface(
        (90, 50),
        pygame.SRCALPHA
    )

    pygame.draw.ellipse(
        shine_surface,
        (255, 255, 255, 120),
        (0, 0, 90, 50)
    )

    screen.blit(
        shine_surface,
        (shine_x, shine_y)
    )

    # ================= WORD =================
    if word_index > 0:

        current_word = all_words[word_index - 1]

        draw_glow_text(
            screen,
            current_word,
            HEART_CX,
            HEART_CY + 20
        )

    # ========== DISPLAY ==========
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
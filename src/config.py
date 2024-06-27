import pygame, os

from sound import Sound
from theme import Theme


class Config:

    def __init__(self):
        self.themes = []
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        self.font = pygame.font.SysFont("Arial", 18, bold=True)
        self.move_sound = pygame.mixer.Sound(os.path.join("assets/sounds/move.wav"))
        self.capture_sound = pygame.mixer.Sound(os.path.join("assets/sounds/capture.wav"))

    def change_theme(self):
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]

    def _add_themes(self):
        yellow = Theme(
            (255, 255, 191),
            (255, 255, 0),
            (255, 255, 102),
            (255, 255, 51),
            "#C86464",
            "#C84646",
        )
        pink = Theme(
            (255, 204, 229),
            (255, 102, 178),
            (255, 153, 204),
            (255, 102, 178),
            "#C86464",
            "#C84646",
        )
        blue = Theme(
            (200, 230, 255),
            (0, 102, 204),
            (102, 178, 255),
            (0, 102, 204),
            "#C86464",
            "#C84646",
        )
        gray = Theme(
            (192, 192, 192),
            (128, 128, 128),
            (169, 169, 169),
            (105, 105, 105),
            "#C86464",
            "#C84646",
        )

        self.themes = [yellow, pink, blue, gray]

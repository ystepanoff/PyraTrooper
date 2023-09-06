from typing import NoReturn
import pygame


def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

    return rotated_image, new_rect


class Pyratrooper:
    def __init__(self, width: int = 800, height: int = 600) -> None:
        self._init_pygame()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        
        self.barrel = None
        self.barrel_angle = 0
        
    def main_loop(self) -> NoReturn:
        while True:
            self._handle_input()
            self._process_logic()
            self._draw_game()

    def _init_pygame(self) -> None:
        pygame.init()
        pygame.display.set_caption("pyratrooper")

    def _handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.barrel_angle <= 90:
                self.barrel_angle += 1
                self.clock.tick(120)
        if keys[pygame.K_RIGHT]:
            if self.barrel_angle >= -90:
                self.barrel_angle -= 1
                self.clock.tick(120)

                    
    def _process_logic(self) -> None:
        pass

    def _draw_game(self):
        self.screen.fill((0, 0, 0))
        self._draw_cannon()
        pygame.display.flip()

    def _draw_cannon(self):
        # white stand
        w = self.width // 10
        h = self.height // 10
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            ((self.width - w) // 2, self.height - h, w, h),
        )

        # barrel
        barrel = pygame.Surface((w, w), pygame.SRCALPHA)

        pygame.draw.rect(
            barrel,
            (101, 247, 246),
            (w // 2 - w // 12, w // 12, w // 6, w // 3),
        )
        pygame.draw.circle(
            barrel,
            (255, 82, 242),
            (w // 2, w // 2),
            w // 6,
        )
        pygame.draw.circle(
            barrel,
            (101, 247, 246),
            (w // 2, w // 2),
            w // 24,
        )
        pygame.draw.circle(
            barrel,
            (101, 247, 246),
            (w // 2, w // 12),
            w // 12
        )
        rotated_barrel = pygame.transform.rotate(barrel, self.barrel_angle)
        barrel_rect = rotated_barrel.get_rect(
            center=barrel.get_rect(
                center=(self.width // 2, self.height - h - w // 3 - w // 24),
            ).center
        )
        self.screen.blit(rotated_barrel, barrel_rect)

        # pink base
        pygame.draw.rect(
            self.screen,
            (255, 82, 242),
            ((self.width - w // 3) // 2, self.height - h - w // 3, w // 3, w // 3),
        )

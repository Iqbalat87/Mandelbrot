import pygame
from pygame.locals import MOUSEBUTTONDOWN, KEYDOWN, K_ESCAPE, K_x, K_PLUS, K_MINUS
from Complexe import Complexe
from Mandelbrot import is_in_mandelbrot


class Animation():

    def __init__(self, CT, w, h):
        self.w = w
        self.h = h
        self.fen = pygame.display.set_mode((w, h))
        self.center = (0, 0)
        self.cur_pos = [0, 0]
        self.zoom = 0.1
        self.COLOR_TABLE = CT

    def put_pixel(self, pos, c):
        x, y = pos
        self.fen.set_at((x, y), c)

    def change_pos(self):
        self.cur_pos[0] += 1

        if self.cur_pos[0] == self.w:
            self.cur_pos[1] += 1
            self.cur_pos[0] = 0

        if self.cur_pos[1] == self.h:
            self.reset_screen()
            self.zoom *= 0.5

    def reset_screen(self):
        self.fen.fill((0, 0, 0))
        self.cur_pos = [0, 0]

    def set_direction(self, pos):
        x, y = pos
        self.center = (self.center[0] + (x - self.w / 2) * self.zoom,
                       self.center[1] + (y - self.h / 2) * self.zoom)
        print(self.center)

        self.reset_screen()

    def take_screenshot(self):
        pygame.image.save(self.fen, "Screenshot\Mandelbrot_{}_{}.png".format(self.zoom, self.center))

    def action(self, event):
        for e in event:
            if e.type == MOUSEBUTTONDOWN:
                self.set_direction(e.pos)
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    self.on = False
                elif e.key == K_x:
                    self.take_screenshot()
                elif e.key == K_PLUS:
                    self.zoom *= 0.1
                    self.reset_screen()
                elif e.key == K_MINUS:
                    self.zoom *= 2
                    self.reset_screen()

    def run(self):
        self.on = True

        while self.on:
            index = is_in_mandelbrot(
                Complexe(re=self.center[0] + (self.cur_pos[0] - self.w / 2) * self.zoom,
                         im=self.center[1] + (self.cur_pos[1] - self.h / 2) * self.zoom),
                500,
                len(self.COLOR_TABLE) - 1)

            self.put_pixel(self.cur_pos, self.COLOR_TABLE[index - 1])
            self.change_pos()
            self.action(pygame.event.get())
            pygame.display.update()


COLOR_TABLE = [(223, 247, 0), (90, 255, 0), (255, 7, 0), (250, 127, 0), (255, 247, 0), (187, 247, 0), (56, 255, 0), (89, 255, 0), (31, 0, 0), (92, 137, 0), (69, 161, 0), (208, 221, 0), (244, 92, 0), (224, 127, 0), (67, 211, 0), (234, 251, 0), (189, 100, 0), (219, 255, 0), (167, 216, 0), (255, 7, 0), (17, 0, 0), (81, 4, 0), (33, 188, 0), (85, 173, 0), (32, 3, 0), (173, 189, 0), (17, 136, 0), (69, 83, 0), (96, 252, 0), (153, 153, 0), (0, 136, 0), (175, 236, 0), (241, 141, 0), (241, 73, 0), (105, 42, 0), (122, 6, 0), (26, 144, 0), (178, 248, 0), (255, 5, 0), (77, 107, 0), (159, 28, 0), (142, 212, 0), (4, 177, 0), (222, 255, 0), (68, 36, 0), (31, 248, 0), (251, 222, 0), (223, 255, 0), (160, 254, 0), (36, 221, 0), (16, 132, 0), (0, 4, 0), (229, 175, 0), (254, 247, 0), (86, 251, 0), (235, 202, 0), (16, 72, 0), (254, 255, 0), (49, 247, 0), (63, 231, 0), (158, 255, 0), (224, 127, 0), (217, 255, 0), (220, 174, 0), (16, 244, 0), (255, 231, 0), (218, 255, 0), (154, 214, 0), (114, 151, 0), (184, 253, 0), (15, 253, 0),
               (149, 37, 0), (127, 134, 0), (159, 131, 0), (83, 116, 0), (59, 182, 0), (252, 255, 0), (224, 7, 0), (102, 54, 0), (156, 255, 0), (31, 248, 0), (0, 128, 0), (117, 102, 0), (25, 0, 0), (186, 186, 0), (155, 147, 0), (142, 61, 0), (93, 123, 0), (211, 7, 0), (153, 78, 0), (176, 192, 0), (206, 24, 0), (255, 247, 0), (60, 255, 0), (54, 255, 0), (245, 254, 0), (16, 0, 0), (188, 255, 0), (0, 132, 0), (100, 108, 0), (32, 253, 0), (32, 250, 0), (154, 219, 0), (85, 239, 0), (211, 159, 0), (125, 175, 0), (146, 219, 0), (122, 255, 0), (215, 254, 0), (39, 204, 0), (25, 254, 0), (27, 221, 0), (28, 183, 0), (16, 128, 0), (0, 248, 0), (113, 188, 0), (92, 67, 0), (34, 138, 0), (14, 252, 0), (44, 245, 0), (74, 44, 0), (189, 255, 0), (133, 162, 0), (24, 198, 0), (125, 134, 0), (217, 106, 0), (18, 116, 0), (223, 255, 0), (239, 7, 0), (22, 68, 0), (177, 213, 0), (16, 4, 0), (251, 221, 0), (8, 251, 0), (26, 71, 0), (29, 236, 0), (18, 209, 0), (246, 246, 0), (255, 255, 0), (190, 247, 0), (224, 255, 0), (102, 158, 0), (0, 0, 0)]

w = 400
h = 400

Animation(COLOR_TABLE[::-1], w, h).run()
pygame.quit()
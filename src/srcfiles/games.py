#! /usr/bin/env python
from abc import ABC, abstractmethod
from pprint import pprint
import pygame
from pygame.locals import *
import numpy as np

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def write_verbose_fn(verbose):
    if verbose:
        return lambda *args: pprint(*args)
    else:
        return lambda *args: None

class BoardGame(ABC):
    def __init__(self, parameters, verbose=False, do_visualize=False):
        super().__init__()
        self.parameters = parameters
        self.log_writer = write_verbose_fn(verbose)
        self.do_visualize = do_visualize


    @abstractmethod
    def make_action(self, action, player):
        return NotImplemented

    @abstractmethod
    def is_game_end_condition(self):
        return NotImplemented

    @abstractmethod
    def visualize(self, action, player):
        """
        a function that sets up the visualization of
        the game. Is different from visualisation of 
        a single state. 
        """
        return NotImplemented

    @abstractmethod
    def visualize_single_state(self):
        return NotImplemented

class OldGoldGame(BoardGame):
    def __init__(self, parameters, verbose=False, do_visualize=False):
        super().__init__(parameters, verbose, do_visualize)
        self.size = parameters['size']
        self.player_tracker = 0 # 0 is player 1 and 1 is player 2
        self.board = np.zeros((self.size, 2))
        

        pass ### continue

class HexGame(BoardGame):
    def __init__(self, parameters, verbose=False, do_visualize=False):
        super().__init__(parameters, verbose, do_visualize)
        self.size = parameters['size']
        self.W_HEIGHT = parameters.get('window height', 800)
        self.W_WIDTH = parameters.get('window width', 800)
        self.CAPTION = 'HexGame'
        self.node_radius = parameters.get('node radius', 5)
        self._FPS = 30
        self.board = np.zeros((self.size, self.size, 2))

        if do_visualize:
            self.visualize()


    def visualize(self):
        pygame.init()
        frame_per_sec = pygame.time.Clock()
        self.display_surface  = pygame.display.set_mode((self.W_WIDTH, self.W_HEIGHT))
        self.display_surface.fill(color=WHITE)
        pygame.display.flip()
        pygame.display.set_caption(self.CAPTION)
        self._draw_board()

            # Make Node


    def _draw_board(self):
        margins = 0.9
        distance_x = self.W_WIDTH*margins / self.size / 2
        distance_y = self.W_HEIGHT*margins / self.size /2
        dx = np.array([-distance_x, distance_y])
        dy = np.array([distance_x, distance_y])
        pos = np.array([self.W_WIDTH/2, self.W_HEIGHT*(1-margins)])
        self.nodes = {}
        for count, node in enumerate(self.board.reshape(-1, 2)):
            i = count // self.size
            j = count % self.size

            self.log_writer(pos + i*dx + j*dy)
            self.nodes[i,j] = pygame.draw.circle(
                surface = self.display_surface,
                color=self._get_color(node),
                radius=self.node_radius,
                center=pos + i*dx + j * dy 

            )
        pygame.display.flip()
        input('press Enter to exit')

    def make_action(self):
        pass

    def visualize_single_state(self):
        pass

    def is_game_end_condition(self):
        pass

    def _get_color(self, node):
        if node[0]:
            return RED
        elif node[1]:
            return BLUE
        else:
            return BLACK












    
if __name__ == '__main__':
    import time
    game_parameters = {'size': 10,  }

    game = HexGame(game_parameters, verbose=True, do_visualize=True)

    







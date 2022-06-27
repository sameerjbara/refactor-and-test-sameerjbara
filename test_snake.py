from unittest import TestCase
import pygame
import snake
from snake import Snake
from snake import snake_block


class TestSnake(TestCase):

    def test_calculate_dir(self):
        s = snake.Snake()
        s.calculate_dir(pygame.K_LEFT)
        self.assertEqual(s.get_dir(), [-snake_block, 0])
        s.calculate_dir(pygame.K_RIGHT)
        self.assertEqual(s.get_dir(), [snake_block, 0])
        s.calculate_dir(pygame.K_UP)
        self.assertEqual(s.get_dir(), [0,-snake_block])
        s.calculate_dir(pygame.K_DOWN)
        self.assertEqual(s.get_dir(), [0,snake_block])

    def test_eat_food(self):
        s = snake.Snake()
        self.assertEqual(s.eat_food([10, 10]), False)
        self.assertEqual(s.eat_food([snake.dis_width / 2, snake.dis_height / 2]), True)

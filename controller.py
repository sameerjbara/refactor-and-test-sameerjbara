import pygame
import random
import snake

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

snake_block = 10
snake_speed = 15


class Controller:
    def __init__(self):
        self.game_over = False
        self.game_close = False
        pygame.init()
        self.dis = pygame.display.set_mode((dis_width, dis_height))
        pygame.display.set_caption('Snake Game by Edureka')
        self.clock = pygame.time.Clock()
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 35)
        self.food = [round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0,
                     round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0]

    def your_score(self, score):
        value = self.score_font.render("Your Score: " + str(score), True, yellow)
        self.dis.blit(value, [0, 0])

    def check_bound(self, pos):
        return pos[0] >= dis_width or pos[0] < 0 or pos[1] >= dis_height or pos[1] < 0

    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [dis_width / 6, dis_height / 3])

    def game_loop(self):
        my_snake = snake.Snake()
        # get_snake_list(my_snake)
        snake_list = my_snake.get_snake_list()

        while not self.game_over:

            while self.game_close:
                self.dis.fill(blue)
                self.message("You Lost! Press C-Play Again or Q-Quit", red)
                self.your_score(len(snake_list) - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                            self.game_close = False
                        if event.key == pygame.K_c:
                            self.game_over = False
                            self.game_close = False
                            self.game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    my_snake.calculate_dir(event.key)

            my_snake.move_snake()

            if self.check_bound(my_snake.get_head_position()) or my_snake.collide_with_body():
                self.game_close = True
            self.dis.fill(blue)
            pygame.draw.rect(self.dis, green, [self.food[0], self.food[1], snake_block, snake_block])
            my_snake.draw_snake(self.dis)
            self.your_score(len(snake_list) - 1)
            pygame.display.update()
            if my_snake.eat_food(self.food):
                self.food[0] = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                self.food[1] = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            self.clock.tick(snake_speed)



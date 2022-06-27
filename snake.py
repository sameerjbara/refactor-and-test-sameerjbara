import pygame

dis_width = 600
dis_height = 400
snake_block = 10
black = (0, 0, 0)


class Snake:
    def __init__(self):
        self.head = [dis_width / 2, dis_height / 2]
        self.dir = [0, 0]
        self.snake_list = [self.head]
        self.snake_length = 1

    def get_head_position(self):
        return self.head

    def draw_snake(self, dis):
        for x in self.snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

    def get_snake_list(self):
        return self.snake_list

    def calculate_dir(self, key):
        if key == pygame.K_LEFT:
            self.dir[0] = -snake_block
            self.dir[1] = 0

        elif key == pygame.K_RIGHT:
            self.dir[0] = snake_block
            self.dir[1] = 0

        elif key == pygame.K_UP:
            self.dir[1] = -snake_block
            self.dir[0] = 0

        elif key == pygame.K_DOWN:
            self.dir[1] = snake_block
            self.dir[0] = 0

    def move_snake(self):
        self.head[0] += self.dir[0]
        self.head[1] += self.dir[1]
        snake_Head = []
        snake_Head.append(self.head[0])
        snake_Head.append(self.head[1])
        self.snake_list.append(snake_Head)

        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]

    def collide_with_body(self):
        for x in self.snake_list[:-1]:
            if x == self.head:
                return True
        return False

    def eat_food(self, food):
        if self.head[0] == food[0] and self.head[1] == food[1]:
            self.snake_length += 1
            return True
        else:
            return False

    def get_dir(self):
        return self.dir

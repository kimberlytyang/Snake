import pygame
from random import random

# SETTINGS
BLOCK_SIZE = 30  # Board Block Size
BLOCK_HORIZONTAL = 28  # Board Width in Blocks
BLOCK_VERTICAL = 20  # Board Height in Blocks
BORDER = 40  # Border Around Game Board
WINDOW_COLOR = [160, 173, 158]

pygame.font.init()
FONT_SIZE = int(BLOCK_SIZE * 1.5)
text = pygame.font.SysFont("Courier", FONT_SIZE)
FONT_SIZE_2 = BLOCK_SIZE
result_text = pygame.font.SysFont("Courier", FONT_SIZE_2)

BOARD_WIDTH = BLOCK_HORIZONTAL * BLOCK_SIZE
BOARD_HEIGHT = BLOCK_VERTICAL * BLOCK_SIZE

WIDTH = BOARD_WIDTH + 2 * BORDER
HEIGHT = BOARD_HEIGHT + 2 * BORDER + 2 * FONT_SIZE

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake =====(  :)~")


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def convert_to_pixels(coord):
    horizontal = coord[0] * BLOCK_SIZE + BORDER
    vertical = coord[1] * BLOCK_SIZE + BORDER + FONT_SIZE
    return [horizontal, vertical]


class Snake:
    def __init__(self, start_x, start_y):
        self.path = LinkedList()
        self.path.head = Node([start_x, start_y])
        self.path.tail = self.path.head
        self.matrix_location = [[0 for i in range(BLOCK_VERTICAL + 1)] for j in range(BLOCK_HORIZONTAL + 1)]
        self.matrix_location[start_x][start_y] = 1
        self.length = 0
        self.cherry = [-1, -1]
        self.spawn_cherry()
        self.extend = 3

    def start(self):
        convert = convert_to_pixels(self.path.tail.data)
        pygame.draw.rect(window, (0, 0, 0), (convert[0], convert[1], BLOCK_SIZE, BLOCK_SIZE))

    def move(self, direction):
        if self.extend == 0:
            self.matrix_location[self.path.head.data[0]][self.path.head.data[1]] = 0
            temp = self.path.head.next
            self.path.head = None
            self.path.head = temp
        else:
            self.extend -= 1

        coord = self.path.tail.data
        if direction == "U":
            self.path.tail.next = Node([coord[0], coord[1] - 1])
            self.path.tail = self.path.tail.next
            if self.end_game(self.path.tail.data):
                return False
            self.matrix_location[coord[0]][coord[1] - 1] = 1
        elif direction == "D":
            self.path.tail.next = Node([coord[0], coord[1] + 1])
            self.path.tail = self.path.tail.next
            if self.end_game(self.path.tail.data):
                return False
            self.matrix_location[coord[0]][coord[1] + 1] = 1
        elif direction == "L":
            self.path.tail.next = Node([coord[0] - 1, coord[1]])
            self.path.tail = self.path.tail.next
            if self.end_game(self.path.tail.data):
                return False
            self.matrix_location[coord[0] - 1][coord[1]] = 1
        elif direction == "R":
            self.path.tail.next = Node([coord[0] + 1, coord[1]])
            self.path.tail = self.path.tail.next
            if self.end_game(self.path.tail.data):
                return False
            self.matrix_location[coord[0] + 1][coord[1]] = 1
        else:
            print("Invalid Direction")

        coord = self.path.tail.data
        coord_cherry = self.cherry
        if coord[0] == coord_cherry[0] and coord[1] == coord_cherry[1]:
            self.eat()

        draw_screen(self.length * 25)

        convert = convert_to_pixels(self.cherry)
        pygame.draw.rect(window, (209, 35, 23), (convert[0], convert[1], BLOCK_SIZE, BLOCK_SIZE))

        curr = self.path.head
        while curr is not None:
            convert = convert_to_pixels(curr.data)
            pygame.draw.rect(window, (0, 0, 0), (convert[0], convert[1], BLOCK_SIZE, BLOCK_SIZE))
            curr = curr.next

        draw_grid()

        return True

    def end_game(self, coord):
        if coord[0] < 0 or coord[0] >= BLOCK_HORIZONTAL or coord[1] < 0 or coord[1] >= BLOCK_VERTICAL:
            return True
        elif self.matrix_location[coord[0]][coord[1]] == 1:
            return True
        return False

    def eat(self):
        self.extend += 4
        self.length += 4
        self.spawn_cherry()

    def spawn_cherry(self):
        rand_x = int(random() * BLOCK_HORIZONTAL)
        rand_y = int(random() * BLOCK_VERTICAL)
        while not self.is_open(rand_x, rand_y):
            rand_x = int(random() * BLOCK_HORIZONTAL)
            rand_y = int(random() * BLOCK_VERTICAL)
        self.cherry = [rand_x, rand_y]

    def is_open(self, x, y):
        if self.length >= BLOCK_HORIZONTAL * BLOCK_VERTICAL - 2:
            return True
        if self.matrix_location[x][y] == 0:
            return True
        return False


def draw_screen(score):
    window.fill(WINDOW_COLOR)
    title = text.render("Snake", 1, (0, 0, 0))
    window.blit(title, (BORDER, BORDER / 2))
    score_display = text.render("Score: " + str(score), 1, (0, 0, 0))
    window.blit(score_display, (BORDER, HEIGHT - (BORDER / 2) - FONT_SIZE))


def draw_grid():
    num_blocks_vertical = int(BOARD_HEIGHT / BLOCK_SIZE)
    num_blocks_horizontal = int(BOARD_WIDTH / BLOCK_SIZE)
    for i in range(num_blocks_vertical - 1):
        pygame.draw.line(window, (139, 150, 137), (BORDER, BORDER + FONT_SIZE + BLOCK_SIZE * (i + 1)), (BORDER + BOARD_WIDTH, BORDER + FONT_SIZE + BLOCK_SIZE * (i + 1)))
    for i in range(num_blocks_horizontal - 1):
        pygame.draw.line(window, (139, 150, 137), (BORDER + BLOCK_SIZE * (i + 1), BORDER + FONT_SIZE), (BORDER + BLOCK_SIZE * (i + 1), BORDER + FONT_SIZE + BOARD_HEIGHT))
    pygame.draw.rect(window, (0, 0, 0), (BORDER, BORDER + FONT_SIZE, BOARD_WIDTH, BOARD_HEIGHT), 1)


def draw_options():
    options = result_text.render("Restart: ENTER / Quit: ESC", 1, (0, 0, 0))
    window.blit(options, (WIDTH - BORDER - (16 * FONT_SIZE_2), (BORDER + FONT_SIZE) / 2 - (FONT_SIZE_2 / 2)))


def main():
    run = True
    fps = 60
    score = 0
    clock = pygame.time.Clock()

    board_middle_x = int(BLOCK_HORIZONTAL / 2)
    board_middle_y = int(BLOCK_VERTICAL / 2)
    snake = Snake(board_middle_x, board_middle_y)
    snake.start()

    global direction
    direction = None

    while run:
        clock.tick(fps)
        started = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    direction = "U"
                    started = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    direction = "D"
                    started = True
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    direction = "L"
                    started = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    direction = "R"
                    started = True
        if started:
            draw_screen(score)
            snake.move(direction)
            draw_grid()
            pygame.display.update()
            break
        draw_screen(score)
        snake.start()
        draw_grid()
        pygame.display.update()

    SPEED_LIMIT = 4
    speed_limiter = SPEED_LIMIT
    lock_direction = False
    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if lock_direction:
                    break
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != "D":
                    direction = "U"
                    lock_direction = True
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != "U":
                    direction = "D"
                    lock_direction = True
                elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != "R":
                    direction = "L"
                    lock_direction = True
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != "L":
                    direction = "R"
                    lock_direction = True
        if speed_limiter > 0:
            speed_limiter -= 1
        else:
            speed_limiter = SPEED_LIMIT
            lock_direction = False
            if not snake.move(direction):
                run = False
                draw_options()
            pygame.display.update()

    quit_game = False
    while not quit_game:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()
                    quit_game = True
                elif event.key == pygame.K_ESCAPE:
                    quit_game = True


main()

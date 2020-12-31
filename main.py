import pygame

BLOCK_SIZE = 18  # Board Block Size
BLOCK_HORIZONTAL = 28  # Board Width in Blocks
BLOCK_VERTICAL = 20  # Board Height in Blocks
FONT_SIZE = 40  # Score Text Size
BOARD_REF_X = 30  # Border
BOARD_REF_Y = 30  # Border

BOARD_WIDTH = BLOCK_HORIZONTAL * BLOCK_SIZE
BOARD_HEIGHT = BLOCK_VERTICAL * BLOCK_SIZE

WIDTH = BOARD_WIDTH + 2 * BOARD_REF_X
HEIGHT = BOARD_HEIGHT + 2 * BOARD_REF_Y + FONT_SIZE

WINDOW_COLOR = [160, 173, 158]

pygame.font.init()
text = pygame.font.SysFont("Courier", FONT_SIZE)
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


class Snake:
    def __init__(self, start_x, start_y):
        self.path = LinkedList()
        self.path.head = Node([start_x, start_y])
        self.path.tail = self.path.head
        self.cherry = [start_x + 100, start_y + 100]
        self.extend = 5

    def start(self):
        pygame.draw.rect(window, (0, 0, 0), (self.path.tail.data[0], self.path.tail.data[1], BLOCK_SIZE, BLOCK_SIZE))

    def move(self, direction):
        if direction == "U":
            self.path.tail.next = Node([self.path.tail.data[0], self.path.tail.data[1] - BLOCK_SIZE])
            self.path.tail = self.path.tail.next
        elif direction == "D":
            self.path.tail.next = Node([self.path.tail.data[0], self.path.tail.data[1] + BLOCK_SIZE])
            self.path.tail = self.path.tail.next
        elif direction == "L":
            self.path.tail.next = Node([self.path.tail.data[0] - BLOCK_SIZE, self.path.tail.data[1]])
            self.path.tail = self.path.tail.next
        elif direction == "R":
            self.path.tail.next = Node([self.path.tail.data[0] + BLOCK_SIZE, self.path.tail.data[1]])
            self.path.tail = self.path.tail.next
        else:
            print("Invalid Direction")

        if self.path.tail.data[0] == self.cherry[0] and self.path.tail.data[1] == self.cherry[1]:
            self.eat()

        if self.extend == 0:
            # temp = self.path.head                # Free up memory?
            self.path.head = self.path.head.next
            # temp = None
        else:
            self.extend -= 1

        curr = self.path.head
        while curr is not None:
            pygame.draw.rect(window, (0, 0, 0), (curr.data[0], curr.data[1], BLOCK_SIZE, BLOCK_SIZE))
            curr = curr.next

    def eat(self):
        self.extend += 3

    def random_spawn(self):
        x_coord
        y_coord


def draw_screen(score):
    window.fill(WINDOW_COLOR)
    score_display = text.render("Score: " + str(score), 1, (0, 0, 0))
    window.blit(score_display, (BOARD_REF_X, HEIGHT - (BOARD_REF_Y / 2) - FONT_SIZE))


def draw_grid():
    num_blocks_vertical = int(BOARD_HEIGHT / BLOCK_SIZE)
    num_blocks_horizontal = int(BOARD_WIDTH / BLOCK_SIZE)
    for i in range(num_blocks_vertical - 1):
        pygame.draw.line(window, (139, 150, 137), (BOARD_REF_X, BOARD_REF_Y + BLOCK_SIZE * (i + 1)), (BOARD_REF_X + BOARD_WIDTH, BOARD_REF_Y + BLOCK_SIZE * (i + 1)))
    for i in range(num_blocks_horizontal - 1):
        pygame.draw.line(window, (139, 150, 137), (BOARD_REF_X + BLOCK_SIZE * (i + 1), BOARD_REF_Y), (BOARD_REF_X + BLOCK_SIZE * (i + 1), BOARD_REF_Y + BOARD_HEIGHT))
    pygame.draw.rect(window, (0, 0, 0), (BOARD_REF_X, BOARD_REF_Y, BOARD_WIDTH, BOARD_HEIGHT), 1)


def main():
    run = True
    fps = 10
    score = 0
    clock = pygame.time.Clock()

    snake = Snake(BOARD_REF_X + BLOCK_SIZE, BOARD_REF_Y + BLOCK_SIZE)
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
                if event.key == pygame.K_UP:
                    direction = "U"
                    print(direction)
                    started = True
                elif event.key == pygame.K_DOWN:
                    direction = "D"
                    print(direction)
                    started = True
                elif event.key == pygame.K_LEFT:
                    direction = "L"
                    print(direction)
                    started = True
                elif event.key == pygame.K_RIGHT:
                    direction = "R"
                    print(direction)
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

    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "D":
                    direction = "U"
                    print(direction)
                elif event.key == pygame.K_DOWN and direction != "U":
                    direction = "D"
                    print(direction)
                elif event.key == pygame.K_LEFT and direction != "R":
                    direction = "L"
                    print(direction)
                elif event.key == pygame.K_RIGHT and direction != "L":
                    direction = "R"
                    print(direction)
        draw_screen(score)
        snake.move(direction)
        draw_grid()
        pygame.display.update()


main()

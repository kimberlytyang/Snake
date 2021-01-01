import pygame

# SETTINGS
BLOCK_SIZE = 18  # Board Block Size
BLOCK_HORIZONTAL = 28  # Board Width in Blocks
BLOCK_VERTICAL = 20  # Board Height in Blocks
FONT_SIZE = 40  # Score Text Size
BORDER = 30  # Border Around Game Board

BOARD_WIDTH = BLOCK_HORIZONTAL * BLOCK_SIZE
BOARD_HEIGHT = BLOCK_VERTICAL * BLOCK_SIZE

WIDTH = BOARD_WIDTH + 2 * BORDER
HEIGHT = BOARD_HEIGHT + 2 * BORDER + FONT_SIZE

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


def pixels(coord):
    horizontal = coord[0] * BLOCK_SIZE + BORDER
    vertical = coord[1] * BLOCK_SIZE + BORDER
    return [horizontal, vertical]


class Snake:
    def __init__(self, start_x, start_y):
        self.path = LinkedList()
        self.path.head = Node([start_x, start_y])
        self.path.tail = self.path.head
        self.length = 0
        self.cherry = [start_x + 5, start_y + 5]
        self.extend = 10

    def start(self):
        convert = pixels(self.path.tail.data)
        pygame.draw.rect(window, (0, 0, 0), (convert[0], convert[1], BLOCK_SIZE, BLOCK_SIZE))

    def move(self, direction):
        coord = self.path.tail.data
        if direction == "U":
            self.path.tail.next = Node([coord[0], coord[1] - 1])
            self.path.tail = self.path.tail.next
        elif direction == "D":
            self.path.tail.next = Node([coord[0], coord[1] + 1])
            self.path.tail = self.path.tail.next
        elif direction == "L":
            self.path.tail.next = Node([coord[0] - 1, coord[1]])
            self.path.tail = self.path.tail.next
        elif direction == "R":
            self.path.tail.next = Node([coord[0] + 1, coord[1]])
            self.path.tail = self.path.tail.next
        else:
            print("Invalid Direction")

        coord = self.path.tail.data
        coord_cherry = self.cherry
        if coord[0] == coord_cherry[0] and coord[1] == coord_cherry[1]:
            self.eat()

        if self.extend == 0:
            temp = self.path.head.next
            self.path.head = None
            self.path.head = temp
        else:
            self.extend -= 1

        curr = self.path.head
        while curr is not None:
            convert = pixels(curr.data)
            pygame.draw.rect(window, (0, 0, 0), (convert[0], convert[1], BLOCK_SIZE, BLOCK_SIZE))
            curr = curr.next

    def eat(self):
        self.extend += 1
        self.length += 1

    def random_spawn(self):
        x_coord
        y_coord


def draw_screen(score):
    window.fill(WINDOW_COLOR)
    score_display = text.render("Score: " + str(score), 1, (0, 0, 0))
    window.blit(score_display, (BORDER, HEIGHT - (BORDER / 2) - FONT_SIZE))


def draw_grid():
    num_blocks_vertical = int(BOARD_HEIGHT / BLOCK_SIZE)
    num_blocks_horizontal = int(BOARD_WIDTH / BLOCK_SIZE)
    for i in range(num_blocks_vertical - 1):
        pygame.draw.line(window, (139, 150, 137), (BORDER, BORDER + BLOCK_SIZE * (i + 1)), (BORDER + BOARD_WIDTH, BORDER + BLOCK_SIZE * (i + 1)))
    for i in range(num_blocks_horizontal - 1):
        pygame.draw.line(window, (139, 150, 137), (BORDER + BLOCK_SIZE * (i + 1), BORDER), (BORDER + BLOCK_SIZE * (i + 1), BORDER + BOARD_HEIGHT))
    pygame.draw.rect(window, (0, 0, 0), (BORDER, BORDER, BOARD_WIDTH, BOARD_HEIGHT), 1)


def main():
    run = True
    fps = 60
    score = 0
    clock = pygame.time.Clock()

    snake = Snake(1, 1)
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

    frame_limiter = 4
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
        if frame_limiter > 0:
            frame_limiter -= 1
        else:
            frame_limiter = 4
            draw_screen(score)
            snake.move(direction)
            draw_grid()
            pygame.display.update()


main()

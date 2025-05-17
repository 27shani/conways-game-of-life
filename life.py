
import pygame
import argparse
import time
import random
import os

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (40, 40, 40)
GREEN = (0, 255, 0)

CELL_SIZE = 20

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--width', type=int, default=40)
    parser.add_argument('--height', type=int, default=20)
    parser.add_argument('--fps', type=int, default=6)
    return parser.parse_args()

def load_pattern(filename):
    if not os.path.exists(filename):
        return set()
    with open(filename, 'r') as f:
        lines = f.readlines()
        return set(tuple(map(int, line.strip().split(','))) for line in lines if line.strip() and not line.startswith('#'))

def save_pattern(live_cells, filename):
    with open(filename, 'w') as f:
        for x, y in live_cells:
            f.write(f"{x},{y}\n")

def next_gen(board, width, height):
    new_board = set()
    neighbor_counts = {}

    for x, y in board:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    neighbor_counts[(nx, ny)] = neighbor_counts.get((nx, ny), 0) + 1

    for cell, count in neighbor_counts.items():
        if count == 3 or (count == 2 and cell in board):
            new_board.add(cell)

    return new_board

def random_fill(width, height):
    return set((random.randint(0, width - 1), random.randint(0, height - 1)) for _ in range((width * height) // 5))

def main():
    args = parse_args()
    width, height = args.width, args.height
    screen_width, screen_height = width * CELL_SIZE, height * CELL_SIZE

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()

    live_cells = set()
    paused = True
    generation = 0

    running = True
    while running:
        screen.fill(BLACK)

        # Draw grid
        for x in range(0, screen_width, CELL_SIZE):
            pygame.draw.line(screen, GREY, (x, 0), (x, screen_height))
        for y in range(0, screen_height, CELL_SIZE):
            pygame.draw.line(screen, GREY, (0, y), (screen_width, y))

        # Draw live cells
        for x, y in live_cells:
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, rect)

        # Display generation and count
        font = pygame.font.SysFont("Consolas", 18)
        info = font.render(f"Generation {generation}   Live cells: {len(live_cells)}", True, WHITE)
        screen.blit(info, (10, 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_n:
                    live_cells = next_gen(live_cells, width, height)
                    generation += 1
                elif event.key == pygame.K_c:
                    live_cells = set()
                    generation = 0
                elif event.key == pygame.K_r:
                    live_cells = random_fill(width, height)
                    generation = 0
                elif event.key == pygame.K_s:
                    save_pattern(live_cells, "patterns.txt")
                elif event.key == pygame.K_l:
                    live_cells = load_pattern("patterns.txt")
                    generation = 0

        if not paused:
            live_cells = next_gen(live_cells, width, height)
            generation += 1

        clock.tick(args.fps)

    pygame.quit()

if __name__ == "__main__":
    main()

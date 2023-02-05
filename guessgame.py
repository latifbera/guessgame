import pygame
import random

pygame.init()

width = 400
height = 400
screen = pygame.display.set_mode((width, height))

# Generate a random number
target = random.randint(1, 100)

# Loop until the user quits
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the user's guess
    guess = int(input("Enter your guess: "))

    # Check if the guess is correct
    if guess == target:
        print("You won!")
        running = False
    elif guess < target:
        print("Too low")
    else:
        print("Too high")

# Quit pygame
pygame.quit()

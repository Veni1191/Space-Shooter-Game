import pgzrun
from random import randint

WIDTH = 1200
HEIGHT = 600
TITLE = "Space Shooter"

#game variables
score = 0
lives = 3
is_game_over = False
enemies = []
bullets = []

#creating the player
spacecraft = Actor("shooter.png")

#creating the enemies
for i in range(8):
    enemy = Actor("enemy.png")
    enemy.x = randint(0,1120)
    enemy.y = randint(-100,0)
    enemies.append(enemy)

#displaying score and lives
def display_score():
    screen.draw.text(f"score:{score}",(50,30))
    screen.draw.text(f"lives:{lives}",(50,60))




























pgzrun.go()




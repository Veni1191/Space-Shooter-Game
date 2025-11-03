import pgzrun
from random import randint

WIDTH = 1200
HEIGHT = 600
TITLE = "Space Shooter"

#game variables
score = 0
lives = 3
is_game_over = False
speed = 5
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

#creating bullets
def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        bullet.x = spacecraft.x
        bullet.y = spacecraft.y - 50
        bullets.append(bullet)
        
#function to draw game state
def draw():
    if lives > 0: 
        screen.clear()
        screen.fill("#006494")
        spacecraft.draw()
        for enemy in enemies:
            enemy.draw()
        for bullet in bullets:
            bullet.draw()
        display_score()
    else:
        game_over_screen()

#function to update game state
def update():
    global score, lives
    #move ship left or right
    if keyboard.left:
        spacecraft.x -= speed
        if spacecraft.x <= 0:
            spacecraft.x = 0
    if keyboard.right:
        spacecraft.x += speed
        if spacecraft.x >= WIDTH:
            spacecraft.x = WIDTH
    
    #moving the bullets
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else: 
            bullet.y -= 10
    
    #moving enemies
    #move_down = False
    for enemy in enemies:
        enemy.y += 5
        if enemy.y > HEIGHT:
            enemy.x = randint(0,1120)
            enemy.y = randint(-100,0)

        #check for collision with bullets
        for bullet in bullets:
            if enemy.colliderect(bullet):
                sounds.eep.play()
                score += 5
                bullets.remove(bullet)
                enemies.remove(enemy)
        
        #collision with ship of enemies
        if enemy.colliderect(spacecraft):
            lives -= 1
            enemies.remove(enemy)
            if lives == 0:
                is_game_over = True
    
    #continously make enemies
    for i in range(8):
        enemy = Actor("enemy.png") 
        enemy.x = randint(0,1120)
        enemy.y = randint(-100,0)
        enemies.append(enemy)
        








            



            




























pgzrun.go()




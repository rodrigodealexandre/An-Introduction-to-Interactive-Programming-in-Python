#Rodrigo's version of RiceRocks for the Coursera Mini-project #8 - RiceRocks (Asteroids)
# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
started = False
rock_group = set([])
missile_group = set([])
explosion_group=set([])
level = 1
level2 = 1
highscore = 0
maxs = 5
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.s2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
    
    def st(self, value):
        self.thrust = value
        if self.thrust == True:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
        
    def draw(self,canvas):
        if self.thrust == False: 
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]] , self.image_size,
                              self.pos, self.image_size, self.angle)
        
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT      
        if self.thrust == True: 
            acc = angle_to_vector(self.angle)
            self.vel[0] += acc[0] * .2
            self.vel[1] += acc[1] * .2
        self.vel[0] *= .98
        self.vel[1] *= .98
        
    def shoot(self):
        global missile_group
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 6 * forward[0], self.vel[1] + 6 * forward[1]]
        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound)
        missile_group.add(a_missile)

        
    def get_position(self):
        return self.pos

    def get_radius(self):
        return self.radius
    
    def explode(self):
        global explosion_group        
        an_explosion = Sprite(self.pos, [0,0], self.angle, 0, explosion_image, explosion_info, explosion_sound)
        explosion_group.add(an_explosion) 
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        if self.animated:
           canvas.draw_image(self.image,[self.image_center[0]+self.image_size[0]*self.age,self.image_center[1]], self.image_size, self.pos,self.image_size,self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size,self.pos, self.image_size, self.angle)

    def update(self):
        # update angle
        self.angle += self.angle_vel
        self.age+=1
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        if self.age *.9 < self.lifespan:
            return True
        else:
            return False        
  
        
        
    def get_position(self):
        return self.pos

    def get_radius(self):
        return self.radius

    def explode(self):
        global explosion_group        
        an_explosion = Sprite(self.pos, [0,0], self.angle, 0, explosion_image, explosion_info, explosion_sound)
        explosion_group.add(an_explosion)
         
    def collide(self, other_object):
        other_pos = other_object.get_position()
        other_rad = other_object.get_radius()
        distance = dist(self.pos,other_pos)
        if distance < self.radius + other_rad:
            return True
        else:
            return False    
        
# key handlers to control ship   
def keydown(key):
    if simplegui.KEY_MAP.get("up") == key:
        my_ship.st(True)
    elif simplegui.KEY_MAP.get("left") == key:
        my_ship.angle_vel = -0.05
    elif simplegui.KEY_MAP.get("right") == key:
        my_ship.angle_vel = 0.05
    elif key == simplegui.KEY_MAP['space']:
        my_ship.shoot()
        
def keyup(key):
    if simplegui.KEY_MAP.get("up") == key:
        my_ship.st(False) 
    elif simplegui.KEY_MAP.get("left") == key:
        my_ship.angle_vel = 0
    elif simplegui.KEY_MAP.get("right") == key:
        my_ship.angle_vel = 0
        
def click(pos):
    global started, lives, score, level, level2, maxs
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True        
        lives = 3
        score = 0
        level = 1
        level2 = 1
        maxs = 5
        timer.start()
        rock_spawner()
        soundtrack.play()
        
# Sprite group        
def process_sprite_group(group_name, canvas_name):
    for sp in group_name:
        sp_to_remove = set([])
        sp.draw(canvas_name)
        if sp.update() == False:            
            sp_to_remove.add(sp)
        group_name.difference_update(sp_to_remove)

# Ship collision 
def group_collide(group, other_object):
    to_remove_set = set([])
    for sprite in group:
        if sprite.collide(other_object) == True:
            sprite.explode()
            to_remove_set.add(sprite)            
        group.difference_update(to_remove_set)
    if len(to_remove_set) > 0:
        return True

# Missile/rock collision    
def group_group_collide(group1, group2):
    to_remove_set = set([])
    global score, lives, level, level2, highscore, maxs
    for sp in group1:
        if group_collide(group2,sp) == True:
            #sp.explode()
            score += 10
            to_remove_set.add(sp)
            if score % 100 == 0:
                lives += 1
                level += 1.5
                level2 += 1
                maxs += 2
            if highscore < score:
                highscore = score
        group1.difference_update(to_remove_set)
        
        
    
# Draw in canvas        
def draw(canvas):
    global time, started, lives, rock_group, started
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
     
    # update ship and sprites
    my_ship.update()
    process_sprite_group(rock_group,canvas)
    process_sprite_group(missile_group,canvas)
    process_sprite_group(explosion_group,canvas)    
    
    #Score and Lives
    canvas.draw_text("Level", (WIDTH*.48, HEIGHT * .04), 22, "White", "sans-serif")
    canvas.draw_text(str(level2), (WIDTH*.52, HEIGHT * .10), 22, "White", "sans-serif")
    
    canvas.draw_text("Score", (WIDTH*.68, HEIGHT * .04), 22, "White", "sans-serif")
    canvas.draw_text("High Score", (WIDTH*.80, HEIGHT * .04), 22, "red", "sans-serif")
    canvas.draw_text(str(score), (WIDTH*.72, HEIGHT * .10), 22, "White", "sans-serif")
    canvas.draw_text(str(highscore), (WIDTH*.88, HEIGHT * .10), 22, "red", "sans-serif")
    for i in range(lives):
        canvas.draw_image(ship_image,[55, 45], [90, 90], [WIDTH*.06+30*i,45], [40,40],-1*math.pi/2)
    canvas.draw_text("Lives  " + str(lives), (WIDTH*.05, HEIGHT * .04), 22, "white")
    
    # Draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())

    if group_collide(rock_group, my_ship) > 0:
        lives -= 1
        my_ship.explode()
        

    # Game over
    if lives == 0:
        started = False
        rock_group = set([])
        timer.stop()
        soundtrack.rewind()
    
        
    # Missile/rock colision
    group_group_collide(missile_group, rock_group)
      
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    if started:
        if len(rock_group)< maxs:
            rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
            rock_vel = [random.random() * level - .3, random.random() * level - .3]
            rock_avel = random.random() * .2 - .1
            a_rock = Sprite(rock_pos, rock_vel, 0, rock_avel, asteroid_image, asteroid_info)
            rock_group.add(a_rock)
            
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)

# register handlers
frame.set_draw_handler(draw)
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(click)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()

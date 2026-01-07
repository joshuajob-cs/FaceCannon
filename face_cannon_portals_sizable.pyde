#Press play button in left hand corner
siz = 700
first = True
score = 0

def keyReleased():
    global first
    first = True

class Cannon(object):
    def __init__(self, x, angle, power):
        self.x = x
        self.angle = angle
        self.power = power
        
    def move(self):
        if keyPressed and key == CODED:
            if keyCode == LEFT:
                self.x -= 3
            if keyCode == RIGHT:
                self.x += 3
            if keyCode == UP:
                self.power += 0.1
                if self.power > 15:
                    self.power = 15
                print('power: '+str(self.power))
            if keyCode == DOWN:
                self.power -= 0.1
                if self.power < 0:
                    self.power = 0
                print('power: '+str(self.power))
        if keyPressed:
            if key == 'd':
                self.angle += 1
            if key == 'a':
                self.angle -= 1
        if self.angle > 90:
            self.angle = 90
        if self.angle < -90:
            self.angle = -90
        if self.x > siz-25:
            self.x = siz-25
        if self.x < 25:
            self.x = 25
        global first
        if keyPressed:
            if key == ' ':
                if first:
                    faces.append(Face(self.x, self.angle, self.power))
                    first = False
        
    def disp(self):
        pushMatrix()
        translate(self.x,siz-25)
        rotate(radians(self.angle + 90))
        fill(0)
        ellipse(-30,0,10,50)
        ellipse(0,0,50,50)
        popMatrix()

class Face(object):
    def __init__(self, x, angle, power):
        self.gravity = 0
        self.x = x
        self.y = siz-25
        self.angle = angle
        self.power = power
        self.col = color(random(0,255), random(0,255), random(0,255))
        self.x -= 40*(cos(radians(self.angle+90)))
        self.y -= 40*(sin(radians(self.angle+90)))
    
    def move(self):
        self.gravity += 0.1 
        self.y += self.gravity
        self.x -= self.power*(cos(radians(self.angle+90)))
        self.y -= self.power*(sin(radians(self.angle+90)))
        if self.x < -12.5 or self.x > siz+12.5 or self.y < -12.5 or self.y > siz+12.5:
            faces.remove(self)
        self.collide()
    
    def disp(self):
        fill(self.col)
        ellipse(self.x,self.y,25,25)
        fill(255)
        ellipse(self.x-5, self.y-4, 5, 5)
        ellipse(self.x+5, self.y-4, 5, 5)
        fill(0)
        arc(self.x, self.y+2.5, 12.5, 12.5, radians(0), radians(180))
        ellipse(self.x-5, self.y-4, 2, 2)
        ellipse(self.x+5, self.y-4, 2, 2)
        
    def collide(self):
        for every in bosses:
            x_dist = abs(self.x - every.x)
            y_dist = abs(self.y - every.y)
            if score > 199:
                if sqrt(x_dist**2 + y_dist**2) < 130:
                    if (self.x - every.x) > 0:
                        self.x -= self.power/2
                    if (self.x - every.x) < 0:
                        self.x += self.power/2
                    if (self.y - every.y) > 0:
                        self.y -= self.power/2 
                    if (self.y - every.y) < 0:
                        self.y += self.power*1.5
                    if sqrt(x_dist**2 + y_dist**2) < 35:
                        faces.remove(self)
            else:
                if sqrt(x_dist**2 + y_dist**2) < 80:
                    if (self.x - every.x) > 0:
                        self.x -= self.power/3
                    if (self.x - every.x) < 0:
                        self.x += self.power/3
                    if (self.y - every.y) > 0:
                        self.y -= self.power/3 
                    if (self.y - every.y) < 0:
                        self.y += self.power
                    if sqrt(x_dist**2 + y_dist**2) < 20:
                        faces.remove(self)
                
        
class Coin(object):
    def __init__(self):
        self.x = random(4,siz-4)
        self.y = random(4,siz-101)
        self.travelx = random(-1,1)
        self.travely = random(-1,1)
        
    def disp(self):
        fill(255,255,100)
        ellipse(self.x,self.y,8,8)
        if score > 49 and len(bosses) < 1:
            bosses.append(Boss(siz-200))
            
        
    def move(self):
        global score
        if score > 10:
            self.x += self.travelx * (score/10)
            self.y += self.travely * (score/10)
        if self.x > siz+4:
            self.x = -4
        if self.x < -4:
            self.x = siz+4
        if self.y > siz-100:
            self.y = siz-100
            self.travely *= -1
        if self.y < 4:
            self.y = 4
            self.travely *= -1
        if score > 25:
            for every in faces:
                if (self.x - every.x) > 0 and (self.x - every.x) < 50 and self.travelx < 0:
                    self.travelx *= -1
                    self.x += (score/50)
                if (self.x - every.x) < 0 and (self.x - every.x) > -50 and self.travelx > 0:
                    self.travelx *= -1
                    self.x -= (score/50)
                if (self.y - every.y) > 0 and (self.y - every.y) < 50 and self.travely < 0:
                    self.travely *= -1
                    self.y += (score/50)
                if (self.y - every.y) < 0 and (self.y - every.y) > -50 and self.travely > 0:
                    self.travely *= -1
                    self.y -= (score/50)
        self.collide()

            
    def collide(self):
        global score
        for every in faces:
            x_dist = abs(self.x - every.x)
            y_dist = abs(self.y - every.y)
            if sqrt(x_dist**2 + y_dist**2) < 16.5:
                coins.remove(self)
                score += 1
                coins.append(Coin())
                print('coins: ' + str(score))
                
                
class Boss(object):
    def __init__(self, y):
        self.x = random(50,siz-50)
        self.y = y
        self.travel = 1
        if self.y == siz-500:
           self.travel = 3 
        
    def disp(self):
        fill(160,0,160)
        ellipse(self.x, self.y, 100, 100)
        fill(255,0,255)
        ellipse(self.x, self.y, 80, 80)
        fill(0)
        ellipse(self.x, self.y, 60, 60)
        self.move()
    
    def move(self):
        if score > 99 and len(bosses) < 2:
            bosses.append(Boss(siz-300))
        if score > 149 and len(bosses) < 3:
            bosses.append(Boss(siz-500))
        if self.y <= siz-300:
            if self.x > siz-50:
                self.x = siz-50
                self.travel *= -1
            if self.x < 50:
                self.x = 50
                self.travel *= -1
            self.x += self.travel

cannon_1 = Cannon(siz/2,0,10)
bosses = []
faces = []
coins = []

def setup():
    size(siz,siz)
    for i in range(10):
        coins.append(Coin())
    
def draw():
    background(100,180,255)
    cannon_1.move()
    cannon_1.disp()
    for all3 in bosses:
        all3.disp()
    for all in faces:
        all.move()
        all.disp()
    for all2 in coins:
        all2.disp()
        all2.move()
    

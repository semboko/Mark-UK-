import turtle
from geometry import do_intersect

turtle.tracer(5)

# 1. Define the new classes of objects
class Room:
    def __init__(self, corners):
        self.corners = corners
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
    
    def draw_walls(self):
        self.t.penup()
        self.t.setpos(self.corners[0])
        self.t.pendown()
        for corner in self.corners:
            self.t.setpos(corner)
        self.t.setpos(self.corners[0])


class Robot:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.penup()
        self.clean_spots = set()
        self.direction = 0
    
    def clean_current_spot(self):
        self.t.dot(5, "blue")
        cur_x, cur_y = self.get_current_spot()
        self.clean_spots.add((cur_x, cur_y))
    
    def get_current_spot(self):
        x, y = self.t.pos()
        return round(x), round(y)
    
    def step_forward(self):
        self.t.forward(10)
    
    def step_back(self):
        self.t.back(10)
    
    def move_to(self, pos):
        left_angle = self.t.towards(pos)
        real_angle = (left_angle - self.direction) % 360
        if real_angle < 180:
            self.t.left(real_angle)
        else:
            self.t.right(360 - real_angle)
        self.direction = left_angle
        self.t.setpos(pos)
        
    def get_neighbors(self, pos):
        x, y = pos
        return (
            (x + 10, y),
            (x, y + 10),
            (x - 10, y),
            (x, y - 10),
        )
    
    def forward_is_possible(self, room):
        xs = [x for x, y in room.corners]
        ys = [y for x, y in room.corners]
        
        self.step_forward()
        cur_x, cur_y = self.get_current_spot()
        self.step_back()
        
        if cur_x > max(xs) or cur_x < min(xs) or cur_y > max(ys) or cur_y < min(ys):
            return False
        
        return True
    
    def rotate(self):
        self.t.left(90)
    
    def is_spot_outside(self, spot, room):
        xs = [x for x, y in room.corners]
        ys = [y for x, y in room.corners]
        
        cur_x, cur_y = spot
        
        if cur_x > max(xs) or cur_x < min(xs) or cur_y > max(ys) or cur_y < min(ys):
            return True
        
        return False
        
    def current_spot_is_clean(self):
        cur_x, cur_y = self.get_current_spot()
        return (cur_x, cur_y) in self.clean_spots
    
    def move_intersects_walls(self, from_pos, to_pos, room):
        for i in range(len(room.corners) - 1):
            corner1 = room.corners[i]
            corner2 = room.corners[i+1]
            if do_intersect(from_pos, to_pos, corner1, corner2):
                return True
        if do_intersect(from_pos, to_pos, room.corners[0], room.corners[-1]):
            return True
    
    def clean(self, room):
        while True:
            if not self.current_spot_is_clean():
                self.clean_current_spot()
            if not self.forward_is_possible(room):
                self.rotate()
            self.step_forward()
            
    def clean_recursively(self, room, depth=0):
        print(depth)
        if self.current_spot_is_clean():
            return
        
        self.clean_current_spot()
        
        for i in range(4):
            if self.forward_is_possible(room):
                self.step_forward()
                self.clean_recursively(room, depth=depth+1)
                self.step_back()
            self.rotate()
    
    def clean_iteratively(self, room):
        stack = []
        
        start = self.get_current_spot()
        stack.append(start)
        
        # "We make the next step if stack is not empty"
        while stack:
            current_position = stack.pop()
            self.move_to(current_position)
            self.clean_current_spot()
            for neighbor in self.get_neighbors(current_position):
                if neighbor in stack:
                    continue
                
                # if self.is_spot_outside(neighbor, room):
                #     continue
                if self.move_intersects_walls(current_position, neighbor, room):
                    continue
                
                if neighbor in self.clean_spots:
                    continue
                
                stack.append(neighbor)
            

# 2. Create new objects and call their methods
room = Room([
    (-178, -108),
    (-200, -108),
    (-200, 149),
    (194, 149),
    (194, -159),
    (-72, -159),
    (-72, -108),
    (-85, -108),
    (-85, -99),
    (-72, -99),
    (-72, 0),
    (-7, 0),
    (-7, -5),
    (-63, -5),
    (-63, -150),
    (61, -150),
    (61, -82),
    (33, -82),
    (33, -5),
    (29, -5),
    (29, 0),
    (70, 0),
    (70, -5),
    (38, -5),
    (38, -77),
    (66, -77),
    (66, -150),
    (185, -150),
    (185, -5),
    (106, -5), 
    (106, 0),
    (185, 0),
    (185, 35),
    (182, 35),
    (182, 38),
    (185, 38),
    (185, 141),
    (66, 141),
    (66, 38),
    (152, 38),
    (152, 35),
    (-75, 35),
    (-75, 38),
    (61, 38),
    (61, 141),
    (-66, 141),
    (-66, 116),
    (-72, 116),
    (-72, 141),
    (-192, 141),
    (-192, -99),
    (-178, -99),
    (-178, -108),
    (-85, -108),
])
robot = Robot()

room.draw_walls()
# robot.clean(room)
# robot.clean_recursively(room)
robot.clean_iteratively(room)

turtle.mainloop()
from random import choice

class RandomWalk():

    def __init__(self, dot_ammount=1000):

        self.dot_ammount = dot_ammount

        self.x_values = [0]
        self.y_values = [0]
    
    def get_step(self):

        xy_direction = choice([1,-1])
        xy_rand = choice([0,1,2,3,4,5,6,7,8,9])
        xy_step = xy_direction * xy_rand
        
        return xy_step
    
    def cords_gen(self):
        
        while len(self.x_values) < self.dot_ammount:

            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

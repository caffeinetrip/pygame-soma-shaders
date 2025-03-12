import math
import scripts.pygpen as pp
from .animation import Animation

# Main player class
class Player(pp.PhysicsEntity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #gravity 
        self.gravity = 500
        self.acceleration[1] = self.gravity
        self.y_velocity_cap = 330
        self.air_time = 0
        
        self.speed = 80
        
        self.jumps = self.max_jumps
        
        
        
        
        
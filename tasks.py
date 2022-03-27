

class Task():
    default_color = 'blue'
    
    def __init__(self, description, time_remain, color):
        self.description = description
        self.time_remain = time_remain
        self.color = color
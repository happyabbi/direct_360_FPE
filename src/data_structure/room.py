
class Room:
    def __init__(self, data_manager):
        self.dt = data_manager
        self.list_ly = []

        self.list_pl = []
        self.is_initialized = False
        

        self.list_corners = []
        self.boundary = None
        
        
        
from dataclasses import dataclass

@dataclass
class Bin:
    id: int
    current_load: int

    def __init__(self,id,current_load=0):
        self.id = id
        self.current_load = current_load
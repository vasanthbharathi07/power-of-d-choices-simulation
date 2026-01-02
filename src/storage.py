from dataclasses import dataclass
from src.model.bin import Bin
from src.model.ball import Ball

@dataclass
class Storage:
    bins: dict[int, Bin]
    balls: dict[int, Ball]
    bin_size: int
    bin_capacity: int
    ball_size: int

    def __init__(self,bin_size=10,bin_capacity=3):
        self.bins = {}
        self.balls = {}
        self.bin_size = bin_size
        self.bin_capacity = bin_capacity
        self.ball_size = self.bin_size * self.bin_capacity

    def get_bin(self,bin_id:int) -> Bin:
        if bin_id in self.bins:
            return self.bins.get(bin_id)
        return None
    
    def add_balls_to_bin(self,bin_id:int):
        if bin_id in self.bins:
            tempBin = self.bins[bin_id]
            tempBin.current_load = tempBin.current_load + 1
            self.bins[bin_id] = tempBin
        else:
            bin = Bin(bin_id,1)
            self.bins[bin_id] = bin

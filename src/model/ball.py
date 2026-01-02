from dataclasses import dataclass

@dataclass
class Ball:
    bin_id: int

    def __init__(self,bin_id):
        self.bin_id = bin_id

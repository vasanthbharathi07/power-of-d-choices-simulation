from dataclasses import dataclass

@dataclass
class SimulationResult:
    max_hit_rate: dict[int,int]
    snapshot_percent: list[int]
    d_choice: int

    def __init__(self,d_choice=1):
        self.max_hit_rate = {}
        self.snapshot_percent = []
        self.d_choice = d_choice

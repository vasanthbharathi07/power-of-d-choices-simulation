
from src.storage import Storage
from src.model.simulationResult import SimulationResult
from src.model.bin import Bin
import random

def init_bins_and_balls(bin_size: int, bin_capacity: int) -> Storage:
    return Storage(bin_size,bin_capacity)

def init_simulation_result(d_choice: int) -> SimulationResult:
    return SimulationResult(d_choice)
     

def choose_random_bin(test_bed: Storage,simulation_result: SimulationResult):
    choosen_random_bin: int = None
    choosen_random_bin_cache: Bin = None
    if simulation_result.d_choice == 1:
        choosen_random_bin = random.randint(1,test_bed.bin_size)
        choosen_random_bin_cache: Bin = test_bed.get_bin(choosen_random_bin)
    else:
         best_load: int = test_bed.bin_capacity + 1
         choosen_random_numbers: list = random.sample(range(1,test_bed.bin_size+1),simulation_result.d_choice)
         for choosen_random_number in choosen_random_numbers:
              choosen_bin: Bin = test_bed.get_bin(choosen_random_number)
              choosen_random_bin = choosen_random_number
              if choosen_bin == None:
                   return None,choosen_random_number
              if choosen_bin.current_load == 0:
                   choosen_random_bin_cache = choosen_bin
                   break
              else:
                   if choosen_bin.current_load < best_load:
                        best_load = choosen_bin.current_load
                        choosen_random_bin_cache = choosen_bin
         
    return choosen_random_bin_cache,choosen_random_bin
     

def throw_balls_in_bin(test_bed: Storage,simulation_result: SimulationResult):
    while True:
        # choosen_random_bin: int = random.randint(1,test_bed.bin_size)
        # choosen_random_bin_cache: Bin = test_bed.get_bin(choosen_random_bin)
        choosen_random_bin_cache ,choosen_random_number = choose_random_bin(test_bed,simulation_result)
        if choosen_random_bin_cache is not None and choosen_random_bin_cache.current_load == test_bed.bin_capacity:
                if choosen_random_bin_cache.id in simulation_result.max_hit_rate:
                    simulation_result.max_hit_rate[choosen_random_bin_cache.id] = simulation_result.max_hit_rate[choosen_random_bin_cache.id] + 1
                else:
                    simulation_result.max_hit_rate[choosen_random_bin_cache.id] = 1 
        else:
                test_bed.add_balls_to_bin(choosen_random_number)
                break

def fillBins(test_bed: Storage, simulation_result: SimulationResult):
    if test_bed is None:
        print(f"Error in test setup")

    for _ in range(test_bed.ball_size):
        throw_balls_in_bin(test_bed,simulation_result)
    report_simulation_result(test_bed,simulation_result,100)

def report_simulation_result(test_bed: Storage, simulation_result: SimulationResult,percent: int):
    print(f"***** Simulation Result *****")
    print(f"Filled ${percent} %")
    print(f"Total Random hit rates on filled bins ${sum(simulation_result.max_hit_rate.values())}")
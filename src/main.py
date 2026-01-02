
from src.choice_simulation import init_bins_and_balls, init_simulation_result, fillBins
import time

if __name__ == "__main__":
    storage_setup = init_bins_and_balls(1000000,3)
    simulation_result = init_simulation_result(3)
    start_perf_counter = time.perf_counter()
    fillBins(storage_setup,simulation_result)
    elapsed_perf_counter = time.perf_counter() - start_perf_counter
    print(f"Elapsed perf counter ${elapsed_perf_counter}")


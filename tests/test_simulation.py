import pytest
from plotly import graph_objects as go
from src.choice_simulation import fillBins, init_bins_and_balls, init_simulation_result

@pytest.mark.parametrize("bin_size", [100,10000,1000000])
@pytest.mark.parametrize("choice_of_d", [1,2,3,10,50])
@pytest.mark.parametrize("execution_number", range(1,4))
def test_single_choice_simulation_runs(bin_size,choice_of_d,execution_number,simulation_metrics_tracker):
    storage_setup = init_bins_and_balls(bin_size,3)
    simulation_result = init_simulation_result(choice_of_d)
    fillBins(storage_setup,simulation_result)
    score = sum(simulation_result.max_hit_rate.values())
    simulation_metrics_tracker.append({
        "run_id": execution_number,
        "score": score,
        "d": choice_of_d,
        "bin_size": bin_size
    })

    assert score >= 0

    
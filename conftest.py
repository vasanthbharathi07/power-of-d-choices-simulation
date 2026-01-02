import pytest
from plotly import graph_objects as go
from plotly.subplots import make_subplots

@pytest.fixture(scope="session")
def simulation_metrics_tracker():
    data = []
    yield data

    if data:
        bin_sizes = sorted(list(set(r['bin_size'] for r in data)))
        fig = make_subplots(
            rows=len(bin_sizes), cols=1, 
            subplot_titles=[f"Bin Size: {size}" for size in bin_sizes],
            vertical_spacing=0.1
        )

        d_values = sorted(list(set(r['d'] for r in data)))

        for i, size in enumerate(bin_sizes):
            for d in d_values:
                filtered_results = [r for r in data if r['bin_size'] == size and r['d'] == d]
                
                fig.add_trace(
                    go.Bar(
                        x=[f"Run {r['run_id']}" for r in filtered_results],
                        y=[r['score'] for r in filtered_results],
                        name=f"d = {d}",
                        showlegend=(i == 0) 
                    ),
                    row=i+1, col=1
                )

        fig.update_layout(
            title_text="Simulation Variation Across Bin Sizes and d-Choices",
            height=300 * len(bin_sizes),
            barmode='group',
            legend_title="Choice of d"
        )
        
        fig.write_html("sim_results.html")
        print("\nVisualization generated: sim_results.html")
# Power of d-Choices Simulation

[![Thesis Link](https://img.shields.io/badge/Thesis-The%20Power%20of%20Two%20Choices-blue)](https://www.eecs.harvard.edu/~michaelm/postscripts/mythesis.pdf)

This repository contains a Python based simulation of the **Power of Two Choices** in randomized load balancing. This concept was popularized by Michael Mitzenmacher in his influential doctoral thesis at UC Berkeley.

---

## 📖 The Concept

The "Power of $d$ Choices" is a solution to the classic **Balls into Bins** problem:

* **The Scenario:** We have $n$ bins, each with a capacity of $m$. We need to distribute $n \times m$ balls into these bins.
* **The Simple Random Approach ($d=1$):** If we pick one bin at random for each ball, collisions (trying to place a ball in a full bin) occur rarely at first. However, as bins fill up, the probability of hitting a full bin increases, leading to significant overhead.
* **The $d$-Choice Approach:** Instead of picking one bin, we pick $d$ bins (e.g., $d=2$) at random and place the ball in the one that is currently **least full**.



### Why it Matters
The beauty of this theory is its **scalability**. While the difference between $d=1$ and $d=2$ might seem small for 100 bins, it becomes massive at a scale of 1 million bins. Mitzenmacher proved that even a small increase in choices ($d=2$) leads to an **exponential** improvement in distribution, whereas increasing $d$ beyond 2 or 3 provides diminishing returns due to the computational overhead of additional lookups.

---

## Simulation Features

This project visualizes how different strategies perform under varying scales using Python:

* **Scalable Inputs:** Test with $100$, $10,000$, or $1,000,000$ bins.
* **Collision Tracking:** Measures "collision hits"—instances where the system attempts to place a ball into an already full bucket.
* **Parametric Testing:** Uses `pytest` to run distributed inputs for choices ($d=1, 2, 3, \dots$).
* **Statistical Accuracy:** Each run is repeated $N$ times to account for variance and provide a reliable distribution of results.
* **Data Visualization:** Results are plotted using **Plotly** to provide clear, interactive graphs of collision trends.

---

## Real-World Applications

The "Power of $d$ Choices" is a critical algorithm used in modern load balancers to ensure high availability and low latency. It is implemented in:
* **NGINX** (The `least_conn` with two choices)
* **Envoy & Istio**
* **HAProxy** (Commonly used in OpenShift)

By choosing the best of a small number of random samples, these systems achieve near-perfect load balancing without the overhead of maintaining a global state of all backend servers.

---

## Getting Started

### Prerequisites
* Python 3.x
* `pytest`
* `plotly`
* `pandas`

### Running the Simulation
To run the tests and generate the collision data:
```bash
uv sync
pytest test_simulation.py
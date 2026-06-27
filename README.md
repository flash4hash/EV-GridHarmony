# Smart EV Charging Optimization

A Python based simulation for optimizing Electric Vehicle (EV) charging in residential communities while respecting transformer constraints and user priorities.

## Overview

This project simulates a smart electric vehicle (EV) charging system for a residential community. The objective is to allocate limited charging power efficiently while respecting transformer capacity constraints and considering different user priorities.

## Objectives

* Prevent transformer overloading.
* Allocate charging power fairly among EVs.
* Prioritize urgent charging requests.
* Apply user based incentives through charging discounts.
* Generate charging statistics for analysis.

## Features

* Random EV profile generation
* 24-hour charging schedule generation
* Priority based scheduling algorithm
* Transformer capacity constraint
* Eco, Flex and Express user categories
* Incentive based charging cost calculation
* Simulation summary and charging statistics

## Project Structure

* `config.py` - Simulation parameters and system configuration
* `ev.py` - EV class definition
* `user_profiles.py` - Random EV profile generation
* `priority.py` - Priority score calculation
* `optimization.py` - Smart charging algorithm
* `results.py` - Billing and simulation statistics
* `main.py` - Program execution

## How to Run

### Requirements

* Python 3.x
* NumPy

### Installation

```bash
git clone <repository-url>
cd EV-GridHarmony
pip install numpy
```

### Run

```bash
python main.py
```

The program will:

* Generate random EV profiles.
* Simulate charging over 24 hours.
* Generate charging schedules.
* Display the simulation summary and sample EV results.


## Simulation Workflow

1. Generate random EV profiles.
2. Calculate charging priority for each EV.
3. Simulate charging over a 24-hour period.
4. Allocate power while respecting transformer limits.
5. Generate a 24-hour charging schedule for every EV.
6. Calculate charging costs and incentives.
7. Display simulation statistics and sample charging schedules.

## Future Improvements

* Integration of photovoltaic (solar) generation into charging decisions.
* Vehicle-to-Grid (V2G) support for peak load reduction.
* Dynamic electricity pricing based on real-time grid demand.
* Advanced fairness metrics for long-term charging allocation.
* Graphical dashboard for visualization and monitoring.

### Developed as part of the AI in Smart Charging Bootcamp.
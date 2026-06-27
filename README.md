# Smart EV Charging Optimization

## Overview

This project simulates a smart electric vehicle (EV) charging system for a residential community. The objective is to allocate limited charging power efficiently while respecting transformer capacity constraints and considering different user priorities.

## Objectives

* Prevent transformer overloading.
* Allocate charging power fairly among EVs.
* Prioritize urgent charging requests.
* Apply user-based incentives through charging discounts.
* Generate charging statistics for analysis.

## Features

* Random EV profile generation
* 24-hour charging simulation
* Priority-based scheduling algorithm
* Transformer capacity constraint
* Eco, Flex and Express user categories
* Incentive-based charging cost calculation
* Charging performance summary

## Project Structure

* `config.py` - Simulation parameters and system configuration
* `ev.py` - EV class definition
* `user_profiles.py` - Random EV profile generation
* `priority.py` - Priority score calculation
* `optimization.py` - Smart charging algorithm
* `results.py` - Billing and simulation statistics
* `main.py` - Program execution

## Simulation Workflow

1. Generate random EV profiles.
2. Calculate charging priority for each EV.
3. Simulate charging over a 24-hour period.
4. Allocate power while respecting transformer limits.
5. Calculate charging costs and incentives.
6. Display charging statistics.

## Future Improvements

* Integration of photovoltaic (solar) generation into charging decisions.
* Vehicle-to-Grid (V2G) support for peak load reduction.
* Dynamic electricity pricing based on real-time grid demand.
* Advanced fairness metrics for long-term charging allocation.
* Graphical dashboard for visualization and monitoring.

### Developed as part of the AI in Smart Charging Bootcamp.
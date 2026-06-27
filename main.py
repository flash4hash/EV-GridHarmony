from user_profiles import random_evs
from optimization import optimize_charging
from results import calculate_results

# Generate random EV profiles
ev_dict = random_evs()

# Optimize charging schedule
schedule = optimize_charging(ev_dict)

# Calculate costs and incentives
results = calculate_results(ev_dict, schedule)

print("\n========== SIMULATION SUMMARY ==========")

charged = sum(ev["fully_charged"] for ev in results.values())

print(f"Total EVs                : {len(results)}")
print(f"Fully Charged            : {charged}")
print(f"Partially Charged        : {len(results)-charged}")

total_energy = sum(ev["energy_delivered"] for ev in results.values())
total_cost = sum(ev["final_cost"] for ev in results.values())

print(f"Total Energy Delivered   : {total_energy:.2f} kWh")
print(f"Total Charging Cost      : ${total_cost:.2f}")

max_energy = 24 * 80
utilization = total_energy / max_energy * 100

print(f"Transformer Utilization  : {utilization:.2f}%")

print(f"Average Energy/EV        : {total_energy/len(results):.2f} kWh")
print(f"Average Charging Cost    : ${total_cost/len(results):.2f}")

print("\n============ SAMPLE RESULTS ============")

for ev_id in range(1, 6):
    ev = ev_dict[ev_id]
    res = results[ev_id]

    print(f"\nEV {ev_id}")
    print("-" * 50)
    print(f"Current SOC       : {ev.current_soc*100:.0f}%")
    print(f"Target SOC        : {ev.target_soc*100:.0f}%")
    print(f"Battery Capacity  : {ev.battery_cap} kWh")
    print(f"User Category     : {ev.user_pref}")
    print(f"Energy Delivered  : {res['energy_delivered']:.2f} kWh")
    print(f"Remaining Energy  : {res['remaining_energy']:.2f} kWh")
    print(f"Charging Cost     : ${res['final_cost']:.2f}")
    print(f"Status            : {'Fully Charged' if res['fully_charged'] else 'Partially Charged'}")
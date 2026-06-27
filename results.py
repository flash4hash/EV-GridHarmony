import config as cf

def calculate_results(evs, schedule):
    results = {}

    for ev_id, ev in evs.items():
        total_energy = 0
        total_cost = 0

        for hour, energy in schedule[ev_id].items():
            total_energy += energy

            # Cost before discount
            cost = energy * cf.e_price[hour]

            # Discount based on user tier
            discount = cf.user_tier[ev.user_pref]["discount"]

            total_cost += cost * (1 - discount)

        results[ev_id] = {
            "energy_delivered": round(total_energy, 2),
            "final_cost": round(total_cost, 2),
            "remaining_energy": round(ev.energy_req, 2),
            "fully_charged": ev.energy_req <= 0
        }

    return results
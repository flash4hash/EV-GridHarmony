import config as cf
from priority import priority_score

def optimize_charging (evs):
    schedule = {}                                                                       # Create a 24-hour charging schedule for every EV
    for ev_id in evs: 
        schedule[ev_id] = {i: 0 for i in range(24)} 

    for hour in range(24):                                                              # Simulate the charging process hour by hour
        parked=[]                                                                       # Find all EVs currently parked at this hour
        for ev_id in evs:
            ev=evs[ev_id]
            if ev.arrival > ev.departure:                                               # Overnight parking case (example: 6 PM to 7 AM)
                if hour >= ev.arrival or hour < ev.departure:
                    parked.append(ev_id) 
            else:
                if ev.arrival <= hour and hour < ev.departure:
                    parked.append(ev_id)

        remaining_power = cf.transformer_limit                                          # Reset available transformer capacity every hour

        priority_list = []                                                              # Calculate priority score of every available EV
        for ev_id in parked:
            ev = evs[ev_id]
            priority_list.append((ev_id, priority_score(ev, hour)))

        priority_list.sort(key=lambda x: x[1], reverse=True)                            # Sort EVs from highest priority to lowest

        for ev in priority_list:
            # Give charging power according to:
            # charger limit, transformer availability, and energy needed
            energy = min(cf.charger_limit, remaining_power, evs[ev[0]].energy_req)
            schedule[ev[0]][hour] = energy
            evs[ev[0]].energy_req -= energy
            remaining_power -= energy

            # Stop allocation if transformer capacity is exhausted
            if remaining_power <= 0:
                break

    return schedule

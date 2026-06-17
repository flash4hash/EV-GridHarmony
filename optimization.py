'''
Decision variables:
    Charging power of EV i at hour t
    V2G power of EV i at hour t

Objective:
    Minimize cost
    Maximize fairness
    Maximize solar usage
    Maximize V2G rewards
'''

import config as cf
from priority import priority_score

def optimize_charging (evs):
    schedule = {}
    for ev_id in evs: 
        schedule[ev_id] = {i: 0 for i in range(24)} 

    for hour in range(24):
        parked=[]
        for ev_id in evs:
            ev=evs[ev_id]
            if ev.arrival > ev.departure:
                if hour >= ev.arrival or hour < ev.departure:
                    parked.append(ev_id) 
            else:
                if ev.arrival <= hour and hour < ev.departure:
                    parked.append(ev_id)

        remaining_power = cf.transformer_limit

        priority_list = []
        for ev_id in parked:
            ev = evs[ev_id]
            priority_list.append((ev_id, priority_score(ev, hour)))

        priority_list.sort(key=lambda x: x[1], reverse=True)

        for ev in priority_list:
            energy = min(cf.charger_limit, remaining_power, evs[ev[0]].energy_req)
            schedule[ev[0]][hour] = energy
            evs[ev[0]].energy_req -= energy
            remaining_power -= energy

            if remaining_power <= 0:
                break

    return schedule

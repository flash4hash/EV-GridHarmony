'''
EV ID

Battery Capacity

Current SOC

Target SOC

Arrival Time

Departure Time

Priority Tier

V2G Permission

Fairness Credits
'''

class EV:
    def __init__(self, ev_id, current_soc, target_soc, battery_cap, arrival, departure, user_pref, v2g):
        self.ev_id = ev_id
        self.current_soc = current_soc
        self.target_soc = target_soc
        self.battery_cap = battery_cap
        self.arrival = arrival
        self.departure = departure
        self.user_pref = user_pref
        self.v2g = v2g
        self.energy_req = (target_soc - current_soc) * battery_cap
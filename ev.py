class EV:
    def __init__(self, ev_id, current_soc, target_soc, battery_cap, arrival, departure, user_pref, v2g):
        self.ev_id = ev_id
        self.current_soc = current_soc
        self.target_soc = target_soc
        self.battery_cap = battery_cap

        # Time window during which EV is available for charging
        self.arrival = arrival
        self.departure = departure

        # User's charging preference and V2G permission
        self.user_pref = user_pref
        self.v2g = v2g

        # Total energy needed to reach target SOC (kWh)
        self.energy_req = (target_soc - current_soc) * battery_cap
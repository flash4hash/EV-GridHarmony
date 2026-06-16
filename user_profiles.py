'''
EV 01:
SOC = 20%
Arrives = 18:00
Leaves = 07:00
Tier = Flex
V2G = Yes
'''

import numpy as np
from ev import EV
import config as cf

def random_evs():
    ev_dict = {}
    np.random.seed(101)

    for i in range(cf.number_of_evs):
        ev_dict[i+1] = EV(
            i+1, # id
            round(np.random.uniform(0.10, 0.80), 2), # current_soc
            round(np.random.uniform(0.80, 1.00), 2), # target_soc
            np.random.randint(8,19)*5, # battery_cap
            np.random.randint(12,24), # arrival
            np.random.randint(5,12), # departure
            np.random.choice(["Eco", "Flex", "Express"], p=(0.5,0.3,0.2)), # user_pref
            np.random.choice([False, True], p=(0.7, 0.3))) # v2g
    return ev_dict


# ev_id, current_soc, target_soc, battery_cap, arrival, departure, user_pref, v2g
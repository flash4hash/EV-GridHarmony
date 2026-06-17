'''
------The captain------

Load configuration
        ↓
Create EVs
        ↓
Generate environment
        ↓
Calculate priorities
        ↓
Run optimization
        ↓
Process results
        ↓
Generate graphs
'''

from user_profiles import random_evs
from optimization import optimize_charging

ev_dict = random_evs()
schedule = optimize_charging(ev_dict)

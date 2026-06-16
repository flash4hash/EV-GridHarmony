# 1. Simulation settings
# Number of EVs
number_of_evs = 100

# Time horizon (24 hours)
time_steps = list(range(24))

# 2. Electrical infrastructure
# Transformer maximum capacity
transformer_limit = 80

# Maximum charger power per EV
charger_limit = 11 

# 3. Grid environment
# Electricity prices ($/kWh)
# 0 = 12am, 23 = 11pm
e_price = {
    3: 0.15, 4: 0.10, 5: 0.11, 6: 0.12, 7: 0.18, 8: 0.25,
    9: 0.30, 10: 0.30, 11: 0.30, 12: 0.28, 13: 0.28, 14: 0.30, 15: 0.32,
    16: 0.35, 17: 0.35, 18: 0.38, 19: 0.42, 20: 0.45,
    21: 0.48, 22: 0.50, 23: 0.50, 0: 0.45, 1: 0.35, 2: 0.25
}

# 4. User categories
# For each user type:
# Priority level
# Discount/incentive percentage
user_tier = {
    "Eco": {
        "priority": 1,
        "discount": 0.2
    },
    "Flex": {
        "priority": 2,
        "discount": 0.1
    },
    "Express": {
        "priority": 3,
        "discount": 0.0
    }
}

# 5. Renewable energy
# Solar generation profile over 24 hours (kW)
solar_gen = {
    0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 5,
    6: 15, 7: 30, 8: 45, 9: 60, 10: 75, 11: 85,
    12: 90, 13: 85, 14: 75, 15: 60, 16: 40,
    17: 20, 18: 5, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0
}

# V2G payment rate ($/kWh)
v2g_reward = 0.30